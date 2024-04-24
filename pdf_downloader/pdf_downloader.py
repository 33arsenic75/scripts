import requests
from tqdm import tqdm

def download_pdf(url, filename):
    # Open the URL
    with requests.get(url, stream=True) as response:
        # Check if request was successful
        if response.status_code != 200:
            print("Failed to download PDF")
            return

        # Get the total file size in bytes
        file_size = int(response.headers.get('content-length', 0))
        
        # Create a progress bar
        progress_bar = tqdm(total=file_size, unit='B', unit_scale=True, desc=filename)
        
        # Open a file to write the content to
        with open(filename, 'wb') as f:
            # Iterate over the response content in chunks
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    # Write chunk to file
                    f.write(chunk)
                    # Update progress bar
                    progress_bar.update(len(chunk))
        
        # Close the progress bar
        progress_bar.close()

# Example usage:
url = "https://books-library.net/files/books-library.net-02190127Xu1L6.pdf"
filename = "downloaded_pdf.pdf"
download_pdf(url, filename)
