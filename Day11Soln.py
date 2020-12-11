from typing import Dict
from contextlib import suppress


class SeatingArea():
    def __init__(self, area: str):
        rows = area.split('\n')
        self.width = len(rows[0])
        self.height = len(rows)
        self.grid = []
        for row in rows:
            self.grid.append([i for i in row])

    def run_step(self):
        new_grid = []
        for row in range(self.height):
            new_row = []
            for cell in range(self.width):
                new_row.append(self.run_step_for_seat(row, cell))
            new_grid.append(new_row)
        self.grid = new_grid
        return self.grid                     

    def get_surrounding_seats(self, row_num: int, col_num: int) -> Dict[str, int]:
        cell_counts = {
            "#": 0,
            ".": 0,
            "L": 0
        }
        with suppress(IndexError):
            if row_num - 1 >= 0:
                cell_counts[self.grid[row_num - 1][col_num + 0]] += 1
                if col_num - 1 >= 0:
                    cell_counts[self.grid[row_num - 1][col_num - 1]] += 1
                if col_num + 1 < self.width:
                    cell_counts[self.grid[row_num - 1][col_num + 1]] += 1

            if col_num - 1 >= 0:
                cell_counts[self.grid[row_num + 0][col_num - 1]] += 1
            if col_num + 1 < self.width:
                cell_counts[self.grid[row_num + 0][col_num + 1]] += 1
            
            if row_num + 1 < self.height:            
                cell_counts[self.grid[row_num + 1][col_num + 0]] += 1
                if col_num - 1 >= 0:
                    cell_counts[self.grid[row_num + 1][col_num - 1]] += 1            
                if col_num + 1 < self.width:
                    cell_counts[self.grid[row_num + 1][col_num + 1]] += 1
        return cell_counts

    def run_step_for_seat(self, row_num: int, col_num: int) -> bool:
        curr_value = self.grid[row_num][col_num]
        if curr_value in ["."]:
            return curr_value
        
        if curr_value == "L":
            return "#" if self.get_surrounding_seats(row_num, col_num)["#"] == 0 else "L"

        if curr_value == "#":
            return "L" if self.get_surrounding_seats(row_num, col_num)["#"] >= 4 else "#"

    def pretty_string(self) -> str:
        as_str = ""
        for row in self.grid:
            as_str += " ".join(row) + "\n"
        return as_str

    def occupied_seats(self) -> int:
        total = 0
        for row in self.grid:
            total += row.count("#")
        return total


if __name__ == "__main__":
    with open("Day11Input.txt", "r") as f:
        raw_data = f.read()
    
    seats = SeatingArea(raw_data)
    #print(seats.pretty_string())
    prev_step = []
    curr_step = seats.pretty_string()
    while prev_step != curr_step:
        prev_step = curr_step
        curr_step = seats.run_step()
        #print(seats.pretty_string())
    print(seats.occupied_seats())        
