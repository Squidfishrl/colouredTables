class Cell:
    def __init__(self, column: int, row: int, value=' '):
        self.value = value
        self.cords = {
            "x":column,
            "y":row
        }

    def __str__(self):
        return f"{self.value}"


class Table:
    def __init__(self, rows: int=0, columns: int=0, def_value = ' '):
        self.columns = columns  # x
        self.rows = rows  # y

        # [row][column]
        self.cell_matrix = [ [Cell(column, row, def_value) for column in range(0, columns)] for row in range(0, rows) ]

    def add_row(self, def_value = ' '):
        """Adds a row at the end of the table."""

        self.cell_matrix.append([Cell(column, self.rows, def_value) for column in range(0, self.columns)])
        self.rows += 1

    def add_column(self, def_value = ' '):
        """Adds a column at the end of all rows."""

        for row in range(0, self.rows):
            self.cell_matrix[row].append(Cell(self.columns, row, def_value))
        self.columns += 1

    def remove_row(self, row_index: int=-1):
        """Removes a row at a given index."""

        self.cell_matrix.pop(row_index)
        self.rows -= 1

    def remove_column(self, column_index: int=-1):
        """Removes a column from all rows at a given index"""

        for row in range(0, self.rows):
            self.cell_matrix[row].pop(column_index)
        self.columns -= 1

    def __len__(self):
        return self.rows * self.columns

    def __iter__(self):
        self.column = 0
        self.row = 0
        return self
    
    def __next__(self) -> Cell:

        if self.row == self.rows:
            raise StopIteration

        x = self.column
        y = self.row

        if self.column == self.columns-1:
            self.column = 0
            self.row += 1
        else:
            self.column += 1

        return self.cell_matrix[y][x]
