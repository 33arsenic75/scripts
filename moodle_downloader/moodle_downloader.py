import requests
from bs4 import BeautifulSoup
import json
import maskpass
import argparse
import sys


base_url = 'https://moodle.iitd.ac.in'
login_url = base_url + '/login/index.php'
course_url = base_url + '/course/view.php?id='  # Append course ID to this URL
file_download_url = base_url + '/pluginfile.php/'  # Append file ID to this URL

# Credentials
global username 
global password

# Function to login to Moodle and return session
def login_to_moodle(username, password):
    session = requests.Session()
    login_data = {
        'username': username,
        'password': password
    }
    session.post(login_url, data=login_data)
    return session

# Function to download PDFs from a course page
def download_pdfs(session, course_id):
    course_page_url = course_url + str(course_id)
    response = session.get(course_page_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print("hi")
    # Find all links on the course page
    links = soup.find_all('a', href=True)
    
    # Iterate through links to find PDFs and download them
def download_pdfs(session, course_id,alldocument,n,b,e):
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
    for pdf_link,file_name in pdf_links:
        file_response = session.get(pdf_link)
        if file_response.status_code == 200:
            with open(file_name, 'wb') as f:
                f.write(file_response.content)
            if(alldocument!="all"):
                break
            # print("File downloaded successfully")
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
    args = parser.parse_args()
    global alldocument
    global n
    global b
    global e
    alldocument = args.alldocument
    n = args.n
    b = args.b
    e = args.e
    if(n=="all"):
        n = -1
    username = input("Username: ")
    password = maskpass.askpass(prompt="Password: ", mask="*")
    session = login_to_moodle(username, password)
    
    # Get course ID and name (you might need to customize this)
    with open('course_id.json', 'r') as file:
        data = json.load(file)
    course_name = input("Course Name or Id: ")
    try:
        if course_name in data:
            course_id = data[course_name]
        else:
            course_id = int(course_name)
        # Download PDFs from the course page
        download_pdfs(session, course_id,alldocument,n,b,e)
    except:
        print("Invalid course name")

if __name__ == "__main__":
    main()
