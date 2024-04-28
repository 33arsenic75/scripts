import requests
import os
import sys

def download_files_from_github(owner, repo, folder_path, output_dir="downloaded_files"):
    # Construct the API URL to list contents of the folder
    api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{folder_path}"
    
    # Make a GET request to the GitHub API
    response = requests.get(api_url)
    
    # Check if request was successful
    if response.status_code != 200:
        print(f"Failed to list contents of folder '{folder_path}'")
        return

    # Parse the JSON response
    contents = response.json()
    
    # Iterate over the contents of the folder
    for item in contents:
        if item['type'] == 'file':
            # If it's a file, download it
            filename = item['name']
            download_url = item['download_url']
            os.makedirs(output_dir, exist_ok=True)
            download_file(download_url, os.path.join(output_dir, filename))
        elif item['type'] == 'dir':
            # If it's a directory, recursively call the function
            subdir_path = os.path.join(folder_path, item['name'])
            subdir_output_dir = os.path.join(output_dir, item['name'])
            download_files_from_github(owner, repo, subdir_path, subdir_output_dir)

def download_file(url, output_path):
    with requests.get(url, stream=True) as response:
        if response.status_code != 200:
            print(f"Failed to download file from {url}")
            return
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

# Example usage:
owner = "ChinmayMittal"
repo = "IITD-CSE"
year = int(sys.argv[1])
course = sys.argv[2]
if year == 1:
    folder_path = "1st-year/Courses"
elif year == 2:
    folder_path = "2nd-year/Courses"
elif year == 3:
    folder_path = "3rd-year/Courses"
elif year == 4:
    folder_path = "4th-year/Courses"

folder_path = f"{folder_path}/{course}/"
download_files_from_github(owner, repo, folder_path,output_dir=f"../{course}")
