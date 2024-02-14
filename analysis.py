import pandas as pd
import matplotlib.pyplot as plt
from src.loader import LOG_PATH
import datetime


class Analyzer:

    def __init__(self):

        df = pd.read_csv(LOG_PATH, sep=r' \| ', engine='python', encoding='utf-8', header=None, names=['start', 'name'])
        df['start'] = pd.to_datetime(df['start'])
        df['end'] = df['start'].shift(-1)
        df['duration'] = (df['end'] - df['start']).dt.total_seconds().fillna(0) / 60

        daytime = df.name != 'Night'
        late = df.start.dt.hour > 6
        today = df.start.dt.day == datetime.datetime.now().day - 1

        tasks = df[today & late & daytime]

        activity_durations = tasks.groupby('name')['duration'].sum()
        plt.figure(figsize=(10, 6))
        activity_durations.plot(kind='barh', color='skyblue')
        plt.xlabel('Duration (minutes)')
        plt.ylabel('Activities')
        plt.title('Activities repartition')
        plt.grid(axis='x')
        plt.tight_layout()
        plt.show()
