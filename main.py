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

        self.rows += 1
        self.cell_matrix.append([Cell(column, self.rows-1, def_value) for column in range(0, self.columns)])

    def add_column(self, def_value = ' '):
        """Adds a column at the end of all rows."""

        self.columns += 1

        for row in range(0, self.rows):
            self.cell_matrix[row].append(Cell(self.columns-1, row, def_value))

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


if __name__ == '__main__':
    table = Table(2,3, "hello")
    for cell in table:
        print(cell)

    table.add_column("World")

    print("\n")
    for cell in table:
        print(cell)
