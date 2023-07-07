def is_accessible(url):
    status_code = check_url_status(url)
    if status_code == 200:
        return True
    return False
