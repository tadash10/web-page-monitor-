import requests

def check_url_status(url):
    try:
        response = requests.get(url)
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return None
