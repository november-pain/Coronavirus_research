from modules.adt import SeriesArray
import csv


class DataFrame:
    def __init__(self):
        """
        initial method
        """
        self.columns = SeriesArray()
        self.rows = SeriesArray()
        self.num_cols = 0
        self.num_rows = 0
        self.column_names = SeriesArray()

    def add_column(self, arr):
        """
        adds a column to a DataFrame
        :param arr: SeriesArray
        :return: None
        """
        arr_copy = arr.copy_arr()
        self.columns.append(arr_copy)
        self.num_cols += 1
        if len(arr_copy) > self.num_rows:
            for i in range(len(arr_copy) - self.num_rows):
                self.add_row(SeriesArray())

        for k in range(len(arr_copy)):
            self.rows[k].append(arr_copy[k])

    def add_row(self, arr):
        """
        adds a row to a DataFrame
        :param arr: SeriesArray
        :return: None
        """
        arr_copy = arr.copy_arr()
        self.rows.append(arr_copy)
        self.num_rows += 1
        if len(arr_copy) > self.num_cols:
            for i in range(len(arr_copy) - self.num_cols):
                self.add_column(SeriesArray())

        for k in range(len(arr_copy)):
            self.columns[k].append(arr_copy[k])

    def reverse_rows(self):
        """
        :returns reversed DataFrame
        :return: DataFrame
        """
        reversed_df = DataFrame()
        reversed_df.column_names = self.column_names
        for i in range(self.num_rows - 1, -1, -1):
            reversed_df.add_row(self.rows[i])
        return reversed_df

    def map_column(self, index, func):
        """
        applies a function to column
        :param index: int
        :param func: function
        :return: None
        """
        self.columns[index].map(func)
        for row in self.rows:
            row[index] = func(row[index])

    def map_row(self, index, func):
        """
        applies a function to row
        :param index: int
        :param func: function
        :return: None
        """
        self.rows[index].map(func)
        for column in self.columns:
            column[index] = func(column[index])

    def average_ratio_of_growth_rates(self, clmn_indx1, clmn_indx2):
        """
        calculates the average ratio of growth rates
        between values of two specified columns in DataFrame
        :param clmn_indx1: index of first column: int
        :param clmn_indx2: index of second column: int
        :return: float
        """
        clmn1 = self.columns[clmn_indx1]
        clmn2 = self.columns[clmn_indx2]
        avg_ratio = 0
        count = 1
        for i in range(1, self.num_rows):
            if clmn1[i] != 0 and clmn1[i - 1] != 0 \
                    and clmn2[i] != 0 and clmn2[i - 1] != 0 \
                    and clmn1[i] != clmn2[i]:
                growth1 = clmn1[i] / clmn1[i - 1]
                growth2 = clmn2[i] / clmn2[i - 1]
                ratio = growth1 / growth2
                avg_ratio += ratio
                count += 1
        return avg_ratio / count

    def csv_to_df(self, path, column_range):
        """
        reads csv file and ads data to DataFrame
        :param column_range: array
        :param path: str
        """
        with open(path, "r") as csv_f:
            csv_reader = csv.reader(csv_f, delimiter=",")
            cursor = 0
            for row in csv_reader:
                if cursor == 0:
                    for i in range(len(row)):
                        if i in column_range:
                            self.column_names.append(row[i])
                else:
                    row_series = SeriesArray()
                    for i in range(len(row)):
                        if i in column_range:
                            row_series.append(row[i])
                    self.add_row(row_series)
                cursor += 1

    def __str__(self):
        """
        string representation of DataFrame
        :return: str
        """
        s = "DataFrame\n"
        s += str(self.column_names) + '\n'
        for i in range(self.num_rows):
            row = ""
            for k in range(len(self.rows[i])):
                row += str(self.rows[i][k]) + " " * 9  # + " "*(len(str(self.rows[i][k])) + 1)
            s += row + "\n"
        return s
