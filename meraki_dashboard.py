from decouple import config
import requests

def get_meraki_organizations(api_key):
    url = 'https://api.meraki.com/api/v1/organizations'
    headers = {
        'X-Cisco-Meraki-API-Key': api_key,
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        organizations = response.json()
        for org in organizations:
            print(f"ID: {org['id']}, Name: {org['name']}")
        return organizations
    else:
        print(f"Request error: {response.status_code}, {response.text}")
        return None

def get_meraki_devices(api_key, organization_id):
    url = f'https://api.meraki.com/api/v1/organizations/{organization_id}/devices'
    headers = {
        'X-Cisco-Meraki-API-Key': api_key,
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        devices = response.json()
        for device in devices:
            print(f"Serial: {device['serial']}, Model: {device['model']}, Name: {device.get('name', 'N/A')}")
    else:
        print(f"Request error: {response.status_code}, {response.text}")

if __name__ == '__main__':
    api_key = config('API_KEY')  # Replace your API key in .env
    organizations = get_meraki_organizations(api_key)

    if organizations:
        # Select the organization you want (e.g. the first = 0)
        organization_id = organizations[0]['id']  # You can change this as needed (e.g. 0 or 1)
        get_meraki_devices(api_key, organization_id)