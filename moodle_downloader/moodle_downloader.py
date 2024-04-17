import requests
from bs4 import BeautifulSoup
import json
import maskpass
import argparse
import sys
import requests
import os
from tqdm import tqdm

base_url = 'https://moodle.iitd.ac.in'
login_url = base_url + '/login/index.php'
course_url = base_url + '/course/view.php?id='  # Append course ID to this URL
file_download_url = base_url + '/pluginfile.php/'  # Append file ID to this URL

def login_to_moodle(username, password):
    session = requests.Session()
    login_data = {
        'username': username,
        'password': password
    }
    try:
        response = session.post(login_url, data=login_data, timeout=5)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("Logged in successfully")
        return session
    except requests.exceptions.Timeout:
        print("Connection timed out. Please check your internet connection.")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print("Failed to connect to Moodle:", e)
        sys.exit(1)
    except Exception as e:
        print("Failed to login:", e)
        sys.exit(1)


def download_pdfs(session, course_id,alldocument,n,b,e,folder_name=None, path='./'):
    course_page_url = course_url + str(course_id)
    response = session.get(course_page_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all links on the course page
    links = soup.find_all('li', class_='activity resource modtype_resource')
    
    pdf_links = []
    # Iterate through links to find PDFs and download them
    if alldocument is None:
        alldocument = "all"
    for link in links:
        span_text = link.find('span', class_='instancename').text.strip()
        file_name = span_text[:-5] + ".pdf"
        print
        if(alldocument!="all" and file_name!=alldocument+".pdf"):
            continue
        pdf_link = link.find('a')['href']
        pdf_links.append((pdf_link,file_name))
    if b is not None:
        pdf_links = pdf_links[:n]
    if e is not None:
        pdf_links = pdf_links[-n:]
    if folder_name is not None:
        folder_path = os.path.join(path, folder_name)
        try:
            os.makedirs(folder_path, exist_ok=True)  # Create folder if it doesn't exist
        except OSError as e:
            print(f"Error creating folder: {e}")
            exit()
    os.chdir(folder_path)
    total_size = 0
    for pdf_link, file_name in pdf_links:
        file_response = session.get(pdf_link, stream=True)
        if file_response.status_code == 200:
            total_size += int(file_response.headers.get('content-length', 0))

    # Create a tqdm progress bar with total combined file size
    with tqdm(total=total_size, unit='B', unit_scale=True, desc='Downloading', ncols=100) as pbar:
        for pdf_link, file_name in pdf_links:
            file_response = session.get(pdf_link, stream=True)
            if file_response.status_code == 200:
                with open(file_name, 'wb') as f:
                    for chunk in file_response.iter_content(chunk_size=1024):
                        if chunk:  # Filter out keep-alive new chunks
                            f.write(chunk)
                            pbar.update(len(chunk))
            else:
                print(f"Failed to download file {file_name}")


# Main function
def main():
    # Login to Moodle
    parser =  argparse.ArgumentParser(
                                prog='Downloads Course Material from Moodle')
    parser.add_argument("-a",'--alldocument',type=str,required=False,dest="alldocument",default=None)
    parser.add_argument("-n",'--numberofdocuments',type=int or str,required=False,dest="n",default=None)
    parser.add_argument("-b",'--begin', action="store_true",required=False,dest="b",default=None)
    parser.add_argument("-e",'--end', action="store_true",required=False,dest="e",default=None)
    parser.add_argument("-f",'--folder', type=str,required=False,dest="f",default=None)
    args = parser.parse_args()
    alldocument = args.alldocument
    folder_name = args.f
    n = args.n
    b = args.b
    e = args.e
    if(n=="all"):
        n = -1
    username = input("Username: ")
    password = maskpass.askpass(prompt="Password: ", mask="*")
    session = login_to_moodle(username, password)
    
    # Get course ID and name (you might need to customize this)
    course_name = input("Course Name or Id: ")
    
    with open('course_id.json', 'r') as file:
        data = json.load(file)
    try:
        # Check if the course_name is an integer
        course_id = int(course_name)
    except ValueError:
        # If course_name is not an integer, try to find it in the data dictionary
        if course_name in data:
            course_id = data[course_name]
        else:
            print("Invalid course name or ID")
            sys.exit(1)
    download_pdfs(session, course_id,alldocument,n,b,e,folder_name)

if __name__ == "__main__":
    global alldocument,username,password,n,b,e,folder_name
    main()
