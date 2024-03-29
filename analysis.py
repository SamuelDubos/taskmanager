import pandas as pd
import matplotlib.pyplot as plt
from src.loader import LOG_PATH
import datetime


class Analyzer:

    def __init__(self, period='today'):
        self.period = period
        self.main()

    @property
    def df(self):
        df = pd.read_csv(LOG_PATH, sep=r' \| ', engine='python', encoding='utf-8', header=None, names=['start', 'name'])
        df['start'] = pd.to_datetime(df['start'])
        df['end'] = df['start'].shift(-1)
        df['duration'] = (df['end'] - df['start']).dt.total_seconds().fillna(0) / 60
        return df

    @property
    def conditioned(self):
        daytime = self.df.name != 'Night'
        late = self.df.start.dt.hour > 6
        day = self.df.start.dt.date  # Modification ici
        now = datetime.datetime.now().date()  # Modification ici
        if self.period == 'Today':
            period = day == now
        elif self.period == 'Yesterday':
            period = day == now - datetime.timedelta(days=1)  # Modification ici
        elif self.period == 'Last week':
            period = (now - datetime.timedelta(days=7) <= day) & (day <= now)  # Modification ici
        else:
            period = True
        return self.df[period & late & daytime]
    
    @staticmethod
    def make_autopct(values):
        def my_autopct(pct):
            val = int(pct * sum(values) / 100)
            return f'{pct:.1f}% ({val:d} min)'
        return my_autopct

    def main(self):
        print(self.conditioned)
        activity_durations = self.conditioned.groupby('name')['duration'].sum()
        activity_durations.plot(kind='pie', ylabel='', autopct=self.make_autopct(activity_durations))
        # activity_durations.plot(kind='barh')
        # plt.xlabel('Duration (minutes)')
        # plt.ylabel('Activities')
        # plt.title('Repartition')
        # plt.grid(axis='x', )
        # step = 15 if self.period in ['Today', 'Yesterday'] else 60
        # plt.xticks(range(0, int(activity_durations.max()) + 1, step))
        plt.show()


if __name__ == '__main__':
    Analyzer()