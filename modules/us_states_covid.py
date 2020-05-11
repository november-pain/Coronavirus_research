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
        column_range = [0, 1, 24, 25, 26]  # 2, 3, 11, 16, 19,
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


class USA:
    def __init__(self):
        self.df = csv_to_df(usa_file)
        self._format_df()
        self.state_names = self._state_names_arr()
        self.states = self._states_instances()

    def _state_names_arr(self):
        """
        makse an array of state 2-letter names
        :return: SeriesArray
        """
        st_names = SeriesArray()
        for el in self.df.columns[1]:
            if el not in st_names and el not in ['VI', 'PR', 'MP', 'GU', 'AS']:  # exclude non-states
                st_names.append(el)
        return st_names

    def _format_df(self):
        for row in self.df.rows:
            row[0] = date_convert(row[0])
        self.df = self.df.reverse_rows()
        for i in range(2, self.df.num_cols):
            self.df.map_column(i, lambda x: int(x) if x.isnumeric() else 0)

    def avarage_coeff(self):
        coeffs = SeriesArray()
        avg_pos = 0
        avg_neg = 0
        for i in range(len(self.states)):
            avg_pos += self.states[i].coeff_pos_total
            avg_neg += self.states[i].coeff_neg_total
        avg_neg = avg_neg / len(self.states)
        avg_pos = avg_pos / len(self.states)

        coeffs.append(avg_pos)
        coeffs.append(avg_neg)
        return coeffs

    def _states_instances(self):
        """
        makes an instance of class State for every state of US
        :return: SeriesArray
        """
        states = SeriesArray()
        for state in self.state_names:
            states.append(State(state, self.df))
        return states


class State:
    def __init__(self, state, df):
        self.state_name = state
        self.state_df = self._make_state_df(state, df)
        self.coeff_pos_total = 0
        self.coeff_neg_total = 0
        self.test_stats_plot()

    def _make_state_df(self, state, df):
        state_df = DataFrame()
        state_df.column_names = df.column_names
        for row in df.rows:
            if row[1] == state:
                state_df.add_row(row)
        return state_df

    def test_stats_plot(self):
        date_x = self.state_df.columns[0]
        pos = self.state_df.columns[3]
        neg = self.state_df.columns[2]
        total = self.state_df.columns[4]

        self.coeff_pos_total = self.state_df.avarage_ratio_of_growth_rates(3, 4)
        self.coeff_neg_total = self.state_df.avarage_ratio_of_growth_rates(2, 4)

        plt.figure(figsize=(15, 8))
        plt.title("State: " + self.state_name)
        plt.xlabel('Date')
        plt.ylabel('number of tests')

        plt.plot_date(date_x, pos, marker="v", ls='-', label='GMC')
        plt.plot_date(date_x, neg, ls='-')
        plt.plot_date(date_x, total, marker="^", ls='-')
        locx = plticker.MultipleLocator(base=5.0)
        plt.gca().xaxis.set_major_locator(locx)

        plt.grid(True)

        plt.legend(['positive increase', 'negative increase', 'total increase'], loc='upper left')
        path = "results/{}.png".format(self.state_name)
        plt.savefig(path)
        plt.close()


if __name__ == '__main__':
    # Auth
    # api = KaggleApi()
    # api.authenticate()
    #
    # api.dataset_download_files('sudalairajkumar/covid19-in-usa', unzip=True)
    #
    # usa_file = "us_states_covid19_daily.csv"

    usa = USA()
    print("list of states:")
    print(usa.state_names)
    print()
    print("number of states:")
    print(len(usa.state_names))

    with open("results/avarage_ratio_of_grow_rates.txt", "w") as res:
        res.write(str(usa.avarage_coeff()))
