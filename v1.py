import requests

def check_url_status(url):
    try:
        response = requests.get(url)
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return None

def is_accessible(url):
    status_code = check_url_status(url)
    if status_code == 200:
        return True
    return False

def monitor_urls(urls):
    for url in urls:
        accessible = is_accessible(url)
        if accessible:
            print(f"{url} is accessible")
        else:
            print(f"{url} is inaccessible")

def generate_report(urls):
    report = "URL Accessibility Report:\n\n"
    for url in urls:
        accessible = is_accessible(url)
        status = "Accessible" if accessible else "Inaccessible"
        report += f"{url}: {status}\n"
    return report

def notify_admin(report):
    print("Sending notification to system administrator:")
    print(report)

# Define the list of URLs to monitor
urls = [
    "https://example.com",
    "https://google.com",
    "https://github.com",
    "https://openai.com",
    "https://stackoverflow.com"
]

# Monitor URLs and generate a report
monitor_urls(urls)
report = generate_report(urls)

# Notify the system administrator with the report
notify_admin(report)
