import requests

def fetch_latest_entry(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        latest_entry = data[-1]  # Assuming the latest entry is the last in the list
        return latest_entry
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

api_url = "https://example.com/api/latest"  # Replace with your API endpoint
latest_entry = fetch_latest_entry(api_url)
print(latest_entry)
