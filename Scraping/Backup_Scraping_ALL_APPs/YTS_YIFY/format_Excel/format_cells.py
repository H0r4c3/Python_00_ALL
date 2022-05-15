class FormatCells:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def get_col_widths(dataframe):
        # First we find the maximum length of the index column   
        idx_max = max([len(str(s)) for s in self.dataframe.index.values] + [len(str(self.dataframe.index.name))])
        # Then, we concatenate this to the max of the lengths of column name and its values for each column, left to right
        return [idx_max] + [max([len(str(s)) for s in dataframe[col].values] + [len(col)]) for col in dataframe.columns]

    def set_col_width():
        for i, width in enumerate(get_col_widths(self.dataframe)):
            worksheet.set_column(i, i, width)
