import requests

# Define the list of URLs to monitor
urls = [
    "https://example.com",
    "https://google.com",
    "https://github.com",
    "https://openai.com",
    "https://stackoverflow.com"
]

def check_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{url} is accessible")
        else:
            print(f"{url} returned an error with status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"{url} is inaccessible: {e}")

# Iterate through the URLs and check their status
for url in urls:
    check_url(url)
