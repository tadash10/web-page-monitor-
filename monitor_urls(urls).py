def monitor_urls(urls):
    for url in urls:
        accessible = is_accessible(url)
        if accessible:
            print(f"{url} is accessible")
        else:
            print(f"{url} is inaccessible")
