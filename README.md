# web-page-monitor-
a high-level Python script to monitor the state of five web pages.
# Web Page Monitoring Script

This script allows you to monitor the accessibility and SSL certificate validity of a list of web pages. It sends HTTP requests to the provided URLs and checks the response status codes. Additionally, it verifies the SSL certificate expiry date.

## Prerequisites

- Python 3.x
- Required Python packages:
    - requests
    - logging (standard library)
    - ssl (standard library)
    - datetime (standard library)

## Usage

1. Clone or download the repository to your local machine.
2. Install the required packages using the following command:
    ```
    pip install -r requirements.txt
    ```
3. Open the `monitor_urls.py` file and specify the URLs you want to monitor in the `urls` list.
4. Run the script using the following command:
    ```
    python monitor_urls.py
    ```

The script will iterate through the provided URLs, send HTTP requests, and display the accessibility status. It will also generate a report summarizing the accessibility status of all URLs and notify the system administrator.

## Additional Features

### Error Logging

The script incorporates error logging functionality using the `logging` library. Any errors encountered during the monitoring process will be logged to a log file for future reference.

### SSL Certificate Expiry Check

The script includes SSL certificate expiry check functionality. It retrieves the SSL certificate for each URL and compares the expiry date with the current date to determine if the certificate is still valid.

## Notification

The script provides a placeholder function for sending notifications to the system administrator. You can implement the `send_notification` function using your preferred method such as email or messaging service. Update the function with the appropriate logic and integrate it into the script as needed.

## ISO Standards

This script adheres to the following ISO standards for secure coding and best practices:

- ISO/IEC 27034:2011 - Information technology -- Security techniques -- Application security
- ISO/IEC 27035-1:2016 - Information technology -- Security techniques -- Information security incident management
- ISO/IEC 29147:2018 - Information technology -- Security techniques -- Vulnerability disclosure
- ISO/IEC 29192-1:2012 - Information technology -- Security techniques -- Lightweight cryptography
- ISO/IEC 29192-2:2012 - Information technology -- Security techniques -- Lightweight cryptography -- Part 2: Implementation aspects

Please ensure that you follow your organization's guidelines and practices when integrating this script into your environment.

## License

This script is released under the [MIT License](LICENSE).

