import requests

class TeslaAPI:
    def __init__(self, client_id, client_secret):
        self.base_url = 'https://owner-api.teslamotors.com'
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None

    def authenticate(self, email, password):
        url = f'{self.base_url}/oauth/token'
        headers = {'Content-Type': 'application/json'}
        payload = {
            'grant_type': 'password',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'email': email,
            'password': password
        }

        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            self.access_token = response.json()['access_token']
        else:
            raise Exception('Authentication Failed')

    def get_vehicles(self):
        if not self.access_token:
            raise Exception('Not authenticated')

        url = f'{self.base_url}/api/1/vehicles'
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()['response']
        else:
            raise Exception('Failed to retrieve vehicles')

# Usage example
client_id = 'your-client-id'
client_secret = 'your-client-secret'
email = 'your-email'
password = 'your-password'

tesla_api = TeslaAPI(client_id, client_secret)
tesla_api.authenticate(email, password)
vehicles = tesla_api.get_vehicles()
print(vehicles)
