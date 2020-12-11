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
        self.add_outer_ring()

    def add_outer_ring(self):
        for row in self.grid:
            row.insert(0, "E")
            row.append("E")
        blank_row = ["E" for i in range(self.width + 2)]
        self.grid.insert(0, blank_row)
        self.grid.append(blank_row)

    def run_step(self):
        new_grid = []
        for row in range(self.height):
            new_row = []
            for cell in range(self.width):
                new_row.append(self.run_step_for_seat(row + 1, cell + 1))
            new_grid.append(new_row)
        self.grid = new_grid
        self.add_outer_ring()
        return self.grid                     

    def get_visible_occupied_seats(self, row_num: int, col_num: int) -> int:
        ne_found = False
        n_found = False
        nw_found = False
        e_found = False
        w_found = False
        se_found = False
        s_found = False
        sw_found = False
        occupied_chairs_seen = 0
        scan_distance = 1
        while sum([ne_found, n_found, nw_found, e_found, w_found, se_found, s_found, sw_found]) < 8:
            if not ne_found:
                tile = self.grid[row_num - scan_distance][col_num + scan_distance]
                if tile == "#":
                    occupied_chairs_seen += 1
                    ne_found = True
                elif tile in ["L", "E"]:
                    ne_found = True
                    
            if not n_found:
                tile = self.grid[row_num - scan_distance][col_num]
                if tile == "#":
                    occupied_chairs_seen += 1
                    n_found = True
                elif tile in ["L", "E"]:
                    n_found = True
                    
            if not nw_found:
                tile = self.grid[row_num - scan_distance][col_num - scan_distance]
                if tile == "#":
                    occupied_chairs_seen += 1
                    nw_found = True
                elif tile in ["L", "E"]:
                    nw_found = True

            if not e_found:
                tile = self.grid[row_num][col_num + scan_distance]
                if tile == "#":
                    occupied_chairs_seen += 1
                    e_found = True
                elif tile in ["L", "E"]:
                    e_found = True            
                    
            if not w_found:
                tile = self.grid[row_num][col_num - scan_distance]
                if tile == "#":
                    occupied_chairs_seen += 1
                    w_found = True
                elif tile in ["L", "E"]:
                    w_found = True

            if not se_found:
                tile = self.grid[row_num + scan_distance][col_num + scan_distance]
                if tile == "#":
                    occupied_chairs_seen += 1
                    se_found = True
                elif tile in ["L", "E"]:
                    se_found = True
                    
            if not s_found:
                tile = self.grid[row_num + scan_distance][col_num]
                if tile == "#":
                    occupied_chairs_seen += 1
                    s_found = True
                elif tile in ["L", "E"]:
                    s_found = True
                    
            if not sw_found:
                tile = self.grid[row_num + scan_distance][col_num - scan_distance]
                if tile == "#":
                    occupied_chairs_seen += 1
                    sw_found = True
                elif tile in ["L", "E"]:
                    sw_found = True
            
            scan_distance += 1

        return occupied_chairs_seen

    def run_step_for_seat(self, row_num: int, col_num: int) -> bool:
        curr_value = self.grid[row_num][col_num]
        if curr_value in ["."]:
            return curr_value
        
        if curr_value == "L":
            return "#" if self.get_visible_occupied_seats(row_num, col_num) == 0 else "L"

        if curr_value == "#":
            return "L" if self.get_visible_occupied_seats(row_num, col_num) >= 5 else "#"

    def pretty_string(self) -> str:
        as_str = ""
        for row in self.grid:
            as_str += " ".join(row) + "\n"
        return as_str.replace('E', '')

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
