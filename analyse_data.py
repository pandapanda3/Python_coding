import json
from datetime import datetime, timedelta

def load_data():
    with open('AAPL_data.json', 'r') as f:
        return json.load(f)

# covert unix to date
def convert_ts(ts):
    return datetime.utcfromtimestamp(ts / 1000)

def cal_rolling_avg(data):
    result = []
    size = 4

    for i in range(size - 1, len(data)):
        window = data[i - size + 1:i + 1]
        avg_close = sum(bar['c'] for bar in window) / size
        result.append({
            'timestamp': convert_ts(data[i]['t']),
            '20_minute_avg_close': avg_close
        })


    with open('aapl_rolling_avg.csv', 'w') as f:
        f.write('timestamp,20_minute_avg_close\n')
        for row in result:
            f.write(f"{row['timestamp']},{row['20_minute_avg_close']}\n")

def resample_data(data, granularity):
    resampled_data = []
    current_time = convert_ts(data[0]['t'])
    end_time = convert_ts(data[-1]['t'])

    delta = timedelta(hours=granularity)

    while current_time < end_time:
        open = None
        high = float('-inf')
        low = float('inf')
        close = None

        for bar in data:
            timestamp = convert_timestamp(bar['t'])
            if current_time <= timestamp < current_time + delta:
                if open is None:
                    open = bar['o']
                close = bar['c']
                high = max(high, bar['h'])
                low = min(low, bar['l'])

        if open is not None:
            resampled_data.append({
                'timestamp': current_time,
                'open': open,
                'high': high,
                'low': low,
                'close': close
            })

        current_time += delta

    return resampled_data

def write_data(resampled_data, filename):
    with open(filename, 'w') as f:
        f.write('timestamp,open,high,low,close\n')
        for row in resampled_data:
            f.write(f"{row['timestamp']},{row['open']},{row['high']},{row['low']},{row['close']}\n")

if __name__ == "__main__":
    aapl_data = load_data()
    # 1. 20-minute rolling average of the close price
    cal_rolling_avg(aapl_data)
    
    # 2. Resample data at 1-hour intervals
    hourly_resampled_data = resample_data(aapl_data, 1)
    write_data(hourly_resampled_data, 'aapl_resampled_1h.csv')
    
    # 3. Resample data at 1-day intervals
    daily_resampled_data = resample_data(aapl_data, 24)
    write_data(daily_resampled_data, 'aapl_resampled_1d.csv')

