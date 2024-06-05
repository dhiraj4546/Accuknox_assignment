import requests

def check_application_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return "UP"
        else:
            return f"DOWN - Status Code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"DOWN - Error: {e}"

if __name__ == "__main__":
    application_url = "http://facebook.com"  # Replace with your application URL
    status = check_application_status(application_url)
    print(f"Application Status: {status}")
