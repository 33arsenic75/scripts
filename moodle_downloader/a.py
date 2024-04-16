import requests
from bs4 import BeautifulSoup
import json
# Base URLs
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
def download_pdfs(session, course_id):
    course_page_url = course_url + str(course_id)
    response = session.get(course_page_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all links on the course page
    links = soup.find_all('li', class_='activity resource modtype_resource')
    
    # Iterate through links to find PDFs and download them
    for link in links:
        span_text = link.find('span', class_='instancename').text.strip()
        file_name = span_text[:-5] + ".pdf"
        pdf_link = link.find('a')['href']
        file_response = session.get(pdf_link)
        if file_response.status_code == 200:
            with open(file_name, 'wb') as f:
                f.write(file_response.content)
            # print("File downloaded successfully")
        else:
            print(f"Failed to download file {file_name}")



# Main function
def main():
    # Login to Moodle
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    session = login_to_moodle(username, password)
    
    # Get course ID and name (you might need to customize this)
    with open('course_id.json', 'r') as file:
        data = json.load(file)
    course_name = input("Enter the course name: ")
    course_id = data[course_name]
    # Download PDFs from the course page
    download_pdfs(session, course_id)

if __name__ == "__main__":
    main()
