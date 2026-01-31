import os
import requests

base_url = "https://priyanka-golia.github.io/teaching/COL-750/lectures/lect{}.pdf"
save_dir = "lectures"

# Create folder if it doesn't exist
os.makedirs(save_dir, exist_ok=True)

for i in range(0, 23):
    url = base_url.format(i)
    file_path = os.path.join(save_dir, f"lect{i}.pdf")

    try:
        print(f"Downloading: {url}")
        r = requests.get(url, timeout=10)

        if r.status_code == 200:
            with open(file_path, "wb") as f:
                f.write(r.content)
            print(f"Saved: {file_path}")
        else:
            print(f"Failed (HTTP {r.status_code}): {url}")

    except Exception as e:
        print(f"Error downloading {url}: {e}")

print("\nDone.")
