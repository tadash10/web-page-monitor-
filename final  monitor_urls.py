import requests
import logging
import ssl
import datetime

def check_url_status(url):
    try:
        response = requests.get(url)
        return response.status_code
    except requests.exceptions.RequestException as e:
        log_error(f"Error accessing {url}: {e}")
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

def send_notification(recipient, message):
    # Implement the logic to send a notification to the recipient
    # using the preferred method (e.g., email, messaging service)
    # You can utilize appropriate libraries or APIs for this purpose
    pass

def log_error(message):
    logging.error(message)

def check_ssl_cert_expiry(url):
    try:
        cert = ssl.get_server_certificate((url, 443))
        x509 = ssl.load_certificate(ssl.PEM, cert)
        expiry_date = x509.get_notAfter()
        expiry_date = datetime.datetime.strptime(expiry_date.decode(), "%Y%m%d%H%M%SZ")
        return expiry_date
    except Exception as e:
        log_error(f"Error checking SSL certificate for {url}: {e}")
        return None

def is_ssl_cert_valid(url):
    expiry_date = check_ssl_cert_expiry(url)
    if expiry_date and expiry_date > datetime.datetime.now():
        return True
    return False

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
