from __future__ import annotations
from typing import List, Tuple
from collections import Counter
import re


bag_list = {}

class Bag():
    def __init__(self, colour: str):
        self.colour = colour
        bag_list[colour] = self
        self.contents = []
        self.containers = []

    def add_content(self, content: Tuple[int, Bag]):
        self.contents.append(content)
        content[1].add_container(self)

    def add_container(self, container: Bag):
        self.containers.append(container)

    def get_all_containers(self):
        all_containers = self.containers
        for container in all_containers:
            all_containers = all_containers + container.get_all_containers()

        return all_containers

    def get_all_contents(self):
        all_contents = []
        for (num, bag) in self.contents:
            for i in range(num):
                all_contents.append(bag)
                all_contents = all_contents + bag.get_all_contents()
        return all_contents

    def __str__(self):
        return f"{self.colour} bag"

    def __repr__(self):
        return f"Bag <{self.colour}>"


if __name__ == "__main__":
    with open("Day7Input.txt", "r") as f:
        file_contents = f.read()
        first_bag_re = re.compile("\w+ \w+")
        contents_re = re.compile("\d+ \w+ \w+")
        bag_contents_map = {}
        for line in file_contents.split('\n'):
            primary_bag = first_bag_re.match(line).group(0)
            secondary_bags = contents_re.findall(line)
            bag_contents_map[primary_bag] = secondary_bags
            bag_list[primary_bag] = Bag(primary_bag)
    
    # Give all the bags their contents
    for bag_as_str in bag_contents_map.keys():
        contents = bag_contents_map[bag_as_str]
        for item in contents:
            count = int(item.split(' ', 1)[0])
            contained_bag = bag_list[item.split(' ', 1)[1]]
            bag_list[bag_as_str].add_content((count, contained_bag))

    # Part 1
    possible_containers = bag_list["shiny gold"].get_all_containers()
    unique_possible_containers = Counter(possible_containers).keys()
    print(len(unique_possible_containers))

    # Part 2
    print(len(bag_list["shiny gold"].get_all_contents()))
