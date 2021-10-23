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
    def __init__(self, rows: int, columns: int):
        self.columns = columns  # x
        self.rows = rows  # y

        # [row][column]
        self.cell_matrix = [ [Cell(column, row) for column in range(0, columns)] for row in range(0, rows) ]

    def __len__(self):
        return self.rows * self.columns

    def __iter__(self):
        self.column = 0
        self.row = 0
        return self
    
    def __next__(self) -> Cell:

        if self.row == self.rows-1 and self.column == self.columns-1:
            raise StopIteration

        x = self.column
        y = self.row

        if self.column == self.columns-1:
            self.column = 0
            self.row += 1
        else:
            self.column += 1

        return self.cell_matrix[y][x]
