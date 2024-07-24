# Meraki Dashboard API

Search for dashboard Organizations IDs and Devices with your API

### Tutorial
pip install -r requirements.txt

edit the edit_env file to .env and enter your api key

### Informations

The `get_meraki_organizations` function returns a list of organizations.

The `get_meraki_devices` function makes a request to the Devices API, using the provided organization ID.

In the `if __name__ == '__main__'` block, the script gets the list of organizations and, if there are organizations available, takes the devices from the first organization in the list (you can adjust this as needed).

This script displays information for each device, including the serial number, model and name (if available). Make sure to replace your Meraki API key.


## Demonstration

ID: 1, Name: Org 0 (organizations[0] block)

ID: 2, Name: Org 1

ID: 3, Name: Org 2

Serial: Q2KX, Model: MRXX, Name: AP1

Serial: Q2KX, Model: MRXX, Name: AP2

Serial: Q2KX, Model: MRXX, Name: AP3

Serial: Q2KX, Model: MRXX, Name: AP4

Serial: Q2KX, Model: MRXX, Name: AP5


## Author

- [@fabiovalverde](https://github.com/fabiovalverde)


