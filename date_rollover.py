import os
import time

import requests

API_KEY = os.getenv('API_KEY')
URL = f'https://pollen.googleapis.com/v1/forecast:lookup?key={API_KEY}&location.latitude=39.1&location.longitude=-84.5&days=1'


def main():
    current_day = 8

    while True:
        response = requests.get(URL).json()
        current_day = response['dailyInfo'][0]['date']['day']
        print(f"current_day = {current_day}")

        if current_day != 8:
            print(f'Date rollover at {time.localtime()}')
            print(response)
            break

        time.sleep(60 * 5)


if __name__ == '__main__':
    main()
