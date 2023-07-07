import ssl
import datetime

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
