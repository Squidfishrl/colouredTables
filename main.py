class Cell:
    def __init__(self, column: int, row: int, value=" "):
        self.value = value
        self.cords = {"x": column, "y": row}
        self.border = {
            "top_left":'',
            "top":"",
            "top_right":'',
            "left":"",
            "right":"",
            "bottom_left":'',
            "bottom":"",
            "bottom_right":''
        }

    def __str__(self):

        return (
            f'{self.border["top_left"]}{self.border["top"]}{self.border["top_right"]}\n'
            f'{self.border["left"]} {self.value} {self.border["right"]}\n'
            f'{self.border["bottom_left"]}{self.border["bottom"]}{self.border["bottom_right"]}\n'
        )


class Table:
    def __init__(self, rows: int = 0, columns: int = 0, def_value=" "):
        self.columns = columns  # x
        self.rows = rows  # y

        # [row][column]
        self.cell_matrix = [
            [Cell(column, row, def_value) for column in range(0, columns)]
            for row in range(0, rows)
        ]

    def generate_borders(self):

        for cell in self:

            # top
            if cell.cords["y"] == 0:
                cell.border["top"] = "═══"

                cell.border["top_left"] = "╤"
                cell.border["top_right"] = "╤"

                # edge cell cases
                if cell.cords["x"] == 0:
                    cell.border["top_left"] = '╔'
                if cell.cords["x"] == self.columns-1:  # if and not elif incase of a single column table
                    cell.border["top_right"] = '╗'
            else:
                cell.border["top"] = self.above(cell).border["bottom"]
                cell.border["top_left"] = self.above(cell).border["bottom_left"]
                cell.border["top_right"] = self.above(cell).border["bottom_right"]

            # left
            if cell.cords["x"] == 0:

                cell.border["left"] = '║'

                # edge cell cases
                if cell.cords["y"] != 0:
                    cell.border["top_left"] = '╟'
                if cell.cords["y"] != self.rows-1:
                    cell.border["bottom_left"] = '╟'
            else:
                cell.border["top_left"] = self.left(cell).border["top_right"]
                cell.border["left"] = self.left(cell).border["right"]
                cell.border["bottom_left"] = self.left(cell).border["bottom_right"]

            # bottom
            if cell.cords["y"] == self.rows-1:
                cell.border["bottom"] = "═══"

                cell.border["bottom_left"] = "╧"
                cell.border["bottom_right"] = "╧"

                # edge cases
                if cell.cords["x"] == 0:
                    cell.border["bottom_left"] = '╚'
                if cell.cords["x"] == self.columns-1:  # if and not elif incase of a single column table
                    cell.border["bottom_right"] = '╝'
            else:
                cell.border["bottom"] = "───"
                cell.border["bottom_right"] = '┼'

            # right
            if cell.cords["x"] == self.columns-1:

                cell.border["right"] = "║"
                if cell.cords["y"] != 0:
                    cell.border["top_right"] = "╢"
                if cell.cords["y"] != self.rows-1:
                    cell.border["bottom_right"] = "╢"
            else:
                cell.border["right"] = "│"


    def above(self, cell: Cell) -> Cell:
        """Returns the cell above the passed one."""


        if cell.cords["y"] == 0:
            raise ValueError

        return self.cell_matrix[cell.cords["y"]-1][cell.cords["x"]]

    def left(self, cell: Cell) -> Cell:
        """Returns the cell left of the passed one."""

        if cell.cords["x"] == 0:
            raise ValueError

        return self.cell_matrix[cell.cords["y"]][cell.cords["x"]-1]

    def add_row(self, def_value=" ") -> None:
        """Adds a row at the end of the table."""

        self.cell_matrix.append(
            [Cell(column, self.rows, def_value) for column in range(0, self.columns)]
        )
        self.rows += 1

    def add_column(self, def_value=" ") -> None:
        """Adds a column at the end of all rows."""

        for row in range(0, self.rows):
            self.cell_matrix[row].append(Cell(self.columns, row, def_value))
        self.columns += 1

    def remove_row(self, row_index: int = -1) -> None:
        """Removes a row at a given index."""

        self.cell_matrix.pop(row_index)
        self.rows -= 1

    def remove_column(self, column_index: int = -1) -> None:
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

        if self.column == self.columns - 1:
            self.column = 0
            self.row += 1
        else:
            self.column += 1

        return self.cell_matrix[y][x]

    def __str__(self) -> str:
        table = ""

        for row in self.cell_matrix:

            for line in range(0, 3):

                for cell in row:
                    if line == 0:
                        if cell.cords["y"] == 0 and cell.cords["x"] == 0:
                            table += f'{cell.border["top_left"]}{cell.border["top"]}{cell.border["top_right"]}'
                        elif cell.cords["y"] == 0:
                            table += f'{cell.border["top"]}{cell.border["top_right"]}'
                    elif line == 1:
                        if cell.cords["x"] == 0:
                            table += f'{cell.border["left"]}'
                        table += f' {cell.value} {cell.border["right"]}'
                    elif line == 2:
                        if cell.cords["x"] == 0:
                            table += f'{cell.border["bottom_left"]}{cell.border["bottom"]}{cell.border["bottom_right"]}'
                        else:
                            table += f'{cell.border["bottom"]}{cell.border["bottom_right"]}'
                if cell.cords["y"] == 0 or line != 0:
                    table += "\n"

        return table


if __name__ == '__main__':
    table = Table(4,5, 'a')
    table.generate_borders()
    # for cell in table:
    #     print(cell)
    print(table)