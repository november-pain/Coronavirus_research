import csv
from kaggle.api.kaggle_api_extended import KaggleApi
from modules.adt import SeriesArray
from modules.data_frame import DataFrame
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker


def csv_to_df(path):
    """
    reads csv file and ads data to DataFrame
    :param path: str
    :return:
    """
    with open(path, "r") as csv_f:
        csv_reader = csv.reader(csv_f, delimiter=",")
        df = DataFrame()
        column_range = [0, 1, 2, 3, 11, 16, 19, 24, 25, 26]
        currsor = 0
        for row in csv_reader:
            if currsor == 0:
                for i in range(len(row)):
                    if i in column_range:
                        df.column_names.append(row[i])
            else:
                row_series = SeriesArray()
                for i in range(len(row)):
                    if i in column_range:
                        row_series.append(row[i])
                df.add_row(row_series)
            currsor += 1
        return df


def date_convert(num):
    date_str = str(num)
    year = date_str[:4]
    month = date_str[4:6]
    day = date_str[6:]
    date = datetime.strptime("/".join([day, month, year]), "%d/%m/%Y")
    return date


class State:
    def __init__(self, state):
        self.state = state
        self.state_df = self.make_state_df(state)

    def make_state_df(self, state):
        state_df = DataFrame()
        state_df.column_names = usa_df.column_names
        for row in usa_df.rows:
            if row[1] == state:
                state_df.add_row(row)
        return state_df

    def test_stats_plot(self):
        date_x = self.state_df.columns[0]

        pos = self.state_df.columns[8]

        neg = self.state_df.columns[7]
        total = self.state_df.columns[9]

        pos.map(lambda x: int(x) if x.isnumeric() else 0)

        plt.figure(figsize=(15, 8))
        plt.title("State: " + self.state)
        plt.xlabel('Date')
        plt.ylabel('number of tests')

        plt.plot_date(date_x, pos, marker="v", ls='-', label='GMC')
        plt.plot_date(date_x, neg, ls='-')
        plt.plot_date(date_x, total, marker="^", ls='-')
        locx = plticker.MultipleLocator(base=5.0)
        plt.gca().xaxis.set_major_locator(locx)

        plt.grid(True)

        plt.legend(['positive','negative', 'total'], loc='upper left')
        plt.show()


if __name__ == '__main__':
    api = KaggleApi()
    api.authenticate()

    api.dataset_download_files('sudalairajkumar/covid19-in-usa', unzip=True)

    usa_file = "us_states_covid19_daily.csv"

    usa_df = csv_to_df(usa_file)
    for row in usa_df.rows:
        row[0] = date_convert(row[0])
    usa_df = usa_df.reverse_rows()


    # AL = State('AL')
    # AL.test_stats_plot()
    # print(AL.state_df)
