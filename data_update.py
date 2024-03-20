import hashlib
import os
import time

import requests

API_KEY = os.getenv('API_KEY')
URL = f'https://pollen.googleapis.com/v1/forecast:lookup?key={API_KEY}&location.latitude=39.1&location.longitude=-84.5&days=1'


def main():
    previous_data = requests.get(URL).content
    # previous_hash = hashlib.sha256(previous_data).hexdigest()

    print(f'Script started at {time.localtime()}')
    print(f'Initial data: {previous_data.decode()}')

    while True:
        data = requests.get(URL).content
        # hash = hashlib.sha256(previous_data).hexdigest()

        if previous_data != data:
            print(f'Data has been updated at {time.localtime()}')
            print(data.decode())
            previous_data = data

        time.sleep(60 * 5)


if __name__ == '__main__':
    main()
