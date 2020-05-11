from modules.adt import SeriesArray


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
        for i in range(self.num_rows -1, -1, -1):
            reversed_df.add_row(self.rows[i])
        return reversed_df

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
                row += str(self.rows[i][k]) + " " #+ " "*(len(str(self.rows[i][k])) + 1)
            s += row + "\n"
        return s
