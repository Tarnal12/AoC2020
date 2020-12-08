import re
from typing import List, Tuple
from enum import Enum


class InfiniteLoopException(Exception):
    def __init__(self, accumulator, index, message="Application encountered an infinite loop."):
        self.accumulator = accumulator
        self.index = index
        self.message = message
        super().__init__(self.message)


class GameConsole():
    def __init__(self):
        self.accumulator = 0
        self.index = 0

    def load_commands(self, command_script: str) -> List[Tuple[str, int]]:
        """ Parses a given string into a list of commands

        Args:
            command_script (str): The script to parse into a command set (puzzle input)
        Returns:
            List[Tuple[Command, int]]: The commands broken into a list of tuples. 
                Each tuple is the command, and the value to execute that command for.
        """
        self.instructions = []
        for line in command_script.split('\n'):
            (command, value) = line.split(' ')
            self.instructions.append((command, int(value)))
        self.initial_instructions = self.instructions.copy()
        return self.instructions

    def alter_command(self, index: int) -> List[Tuple[str, int]]:
        if self.instructions[index][0] == "nop":
            self.instructions[index] = ("jmp", self.instructions[index][1])
        elif self.instructions[index][0] == "jmp":
            self.instructions[index] = ("nop", self.instructions[index][1])
        else:
            raise Exception("Only nop/jmp commands can be altered")
        return self.instructions

    def revert_alterations(self) -> None:
        self.instructions = self.initial_instructions.copy()

    def execute_instructions(self) -> int:
        """ Executes the list of instructions loaded via load_commands

        Returns:
            int: The value of the accumulator at the end of the script, or when it hits a breaking point
        """
        self.accumulator = 0
        self.index = 0
        indices_ran = []
        while self.index < len(self.instructions):
            if self.index in indices_ran:
                raise InfiniteLoopException(self.accumulator, self.index)

            indices_ran.append(self.index)
            (cmd, val) = self.instructions[self.index]
            getattr(self, cmd)(val)

        return self.accumulator

    ##### The actual commands
    def nop(self, val) -> None:
        self.index = self.index + 1

    def acc(self, val) -> None:
        self.accumulator = self.accumulator + val
        self.index = self.index + 1

    def jmp(self, val) -> None:
        self.index = self.index + val


if __name__ == "__main__":
    with open("Day8Input.txt", "r") as f:
        file_contents = f.read()
    
    console = GameConsole()
    cmd_list = console.load_commands(file_contents)
    for i in range(len(cmd_list)):
        try:
            if cmd_list[i][0] not in ['nop', 'jmp']:
                continue

            console.alter_command(i)
            res = console.execute_instructions()
            console.revert_alterations()
            print(f"Successful run! Final accumulator value is {res}")
            break
        except InfiniteLoopException as e:
            console.revert_alterations()
            print(f"Infinite Loop encountered at command {e.index} with acc={e.accumulator}")
