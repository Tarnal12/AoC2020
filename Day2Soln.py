from typing import Tuple

import re


PRINT_DEBUG = True
USE_NEW_STYLE = True


class PasswordValidator():
    def __init__(self, lower_limit, upper_limit, character, use_new_style = False):
        self.lower_limit = int(lower_limit)
        self.upper_limit = int(upper_limit)
        self.character = character
        self.use_new_style = use_new_style

    def validate_string(self, password):
        if self.use_new_style:
            return self.validate_string_new(password)
        else:
            return self.validate_string_old(password)

    def validate_string_old(self, password):
        count = password.count(self.character)
        satisfies_critera = (count >= self.lower_limit and count <= self.upper_limit)
        if PRINT_DEBUG:
            print(f"  Validating {password} has {self.lower_limit}-{self.upper_limit} {self.character}'s: {satisfies_critera}")
        return satisfies_critera

    def validate_string_new(self, password):
        matches = (
            password[self.lower_limit - 1] == self.character,
            password[self.upper_limit - 1] == self.character
        )
        satisfies_critera = sum(matches) == 1
        if PRINT_DEBUG:
            print(f"  Validating {password} has {self.character} at {self.lower_limit} OR {self.upper_limit}: {satisfies_critera}")
        return satisfies_critera


def create_validator_from_string(input_string: str) -> Tuple[PasswordValidator, str]:
    # Converts a string of the form "1-3 a: abc" into a validator and the password
    splitter = re.match(r"(\d+)-(\d+) ([a-z]): ([a-z]*)", input_string)
    split_string = splitter.groups()
    return (PasswordValidator(split_string[0], split_string[1], split_string[2], USE_NEW_STYLE),
            split_string[3])


if __name__ == "__main__":
    with open("Day2Inputs.txt", "r") as f:
        contents = f.read()
        all_inputs = [block for block in contents.split('\n\n')]

    for puzzle_input in all_inputs:
        print("   >>> NEW PUZZLE INPUT")

        valid_pw_count = 0
        input_lines = puzzle_input.split('\n')
        for line in input_lines:
            if len(line) == 0:
                continue

            (validator, password) = create_validator_from_string(line)
            if validator.validate_string(password):
                valid_pw_count = valid_pw_count + 1
        print(f"{valid_pw_count} valid passwords (out of {len(input_lines)})")
