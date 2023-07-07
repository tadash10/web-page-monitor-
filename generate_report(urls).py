def generate_report(urls):
    report = "URL Accessibility Report:\n\n"
    for url in urls:
        accessible = is_accessible(url)
        status = "Accessible" if accessible else "Inaccessible"
        report += f"{url}: {status}\n"
    return report
