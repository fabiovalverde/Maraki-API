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


## Demonstração

ID: 1, Name: Org1
ID: 2, Name: Org2
ID: 3, Name: Org3
Serial: Q2KX, Model: MRXX, Name: AP1
Serial: Q2KX, Model: MRXX, Name: AP2
Serial: Q2KX, Model: MRXX, Name: AP3
Serial: Q2KX, Model: MRXX, Name: AP4
Serial: Q2KX, Model: MRXX, Name: AP5
Serial: Q2KX, Model: MRXX, Name: AP6
Serial: Q2KX, Model: MRXX, Name: AP7
Serial: Q2KX, Model: MRXX, Name: AP8
Serial: Q2KX, Model: MRXX, Name: AP9
Serial: Q2KX, Model: MRXX, Name: AP10
Serial: Q2KX, Model: MRXX, Name: AP11
Serial: Q2KX, Model: MRXX, Name: AP12


## Author

- [@fabiovalverde](https://github.com/fabiovalverde)


