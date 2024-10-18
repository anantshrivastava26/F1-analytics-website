import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to fetch lap times (same as before)
def fetch_lap_times():
    # Ergast API call to fetch lap times
    url = "http://ergast.com/api/f1/2023/3/laps.json?limit=1000"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        lap_data = []
        for lap in data['MRData']['RaceTable']['Races'][0]['Laps']:
            lap_number = lap['number']
            for timing in lap['Timings']:
                lap_data.append({
                    'Driver': timing['driverId'],
                    'Lap': lap_number,
                    'Position': timing['position'],
                    'Time': timing['time']
                })
        df_laps = pd.DataFrame(lap_data)
        df_laps['Time_in_seconds'] = df_laps['Time'].apply(lambda x: int(x.split(":")[0])*60 + float(x.split(":")[1]))
        return df_laps
    else:
        return None

# Pit stop detection (same as before)
def detect_pit_stops(df):
    df_sorted = df.sort_values(by=['Driver', 'Lap'])
    df_sorted['Lap_Time_Diff'] = df_sorted.groupby('Driver')['Time_in_seconds'].diff()
    pit_stop_threshold = 5
    df_sorted['Pit_Stop'] = df_sorted['Lap_Time_Diff'] > pit_stop_threshold
    return df_sorted[df_sorted['Pit_Stop'] == True]

# Average lap time comparison (same as before)
def compare_average_lap_times(df):
    avg_lap_times = df.groupby('Driver')['Time_in_seconds'].mean().reset_index()
    avg_lap_times = avg_lap_times.sort_values(by='Time_in_seconds')
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Driver', y='Time_in_seconds', data=avg_lap_times, palette='coolwarm')
    plt.title('Average Lap Time per Driver', fontsize=16)
    plt.xlabel('Driver', fontsize=12)
    plt.ylabel('Average Lap Time (seconds)', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

# Position progression (same as before)
def visualize_position_progression(df):
    plt.figure(figsize=(12, 8))
    sns.lineplot(x='Lap', y='Position', hue='Driver', data=df, marker='o')
    plt.title('Position Progression Over Laps', fontsize=16)
    plt.xlabel('Lap', fontsize=12)
    plt.ylabel('Position', fontsize=12)
    plt.gca().invert_yaxis()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
