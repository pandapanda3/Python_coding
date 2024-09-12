import configparser

import requests
import json
import os

# get data from platform
def get_data(stocksTicker, multiplier, timespan, date_from, date_to):
    url = basic_url.format(stocksTicker=stocksTicker, multiplier=multiplier, timespan=timespan, date_from=date_from, date_to=date_to, API_KEY=API_KEY)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f'The data for {stocksTicker}: {data}')
        if "results" in data:
            return data["results"]
        else:
            print(f"No results for {stocksTicker} in the given period.")
            return None
    else:
        print(f"There is some issues for gettign the data: {stocksTicker}: {response.status_code}")
        return None
   
# save the data, download the json
# def save_data(stocksTicker, data):
#     filename = f"{stocksTicker}_data.json"
#     with open(filename, 'w') as f:
#         json.dump(data, f)
#     print(f"Data saved to {filename}")

def save_data(stocksTicker, data):
    # define folder
    folder_name = "temp_result"
    
    # if does not exist, create a new one
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    # create new file path
    filename = f"{stocksTicker}_data.json"
    filepath = os.path.join(folder_name, filename)
    
    # save the data
    with open(filepath, 'w') as f:
        json.dump(data, f)
    
    print(f"Data saved to {filepath}")
    
if __name__ == '__main__':
    basic_url = "https://api.polygon.io/v2/aggs/ticker/{stocksTicker}/range/{multiplier}/{timespan}/{date_from}/{date_to}?apiKey={API_KEY}"
    config = configparser.ConfigParser()
    config.read('config.ini')

    API_KEY = config['polygon']['api_key']

    # keep it secret, not pose the key. before running, setting : export API_KEY="your_actual_api_key"
    # API_KEY = os.getenv("API_KEY")
    # get the data and save the data
    MSFT_data = get_data("MSFT", 1, "day", "2024-01-01", "2024-01-31")
    save_data("MSFT", MSFT_data)
    AAPL_data = get_data("AAPL", 5, "minute", "2024-01-20", "2024-01-30")
    save_data("AAPL", AAPL_data)
    IBM_data = get_data("IBM", 2, "hour", "2024-02-05", "2024-02-10")
    save_data("IBM", IBM_data)