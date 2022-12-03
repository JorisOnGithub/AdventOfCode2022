from typing import List, Dict
from collections import defaultdict


def _item_priority(item: str):
    if item.isupper():
        return ord(item) - ord('A') + 27
    else:
        return ord(item) - ord('a') + 1


def part1(lines: List[str]):
    total_priority = 0

    for rucksack in lines:
        left_compartment = set(rucksack[:len(rucksack) // 2])
        right_compartment = set(rucksack[len(rucksack) // 2:])
        item_both_compartments = left_compartment.intersection(right_compartment)

        assert len(item_both_compartments) == 1, 'There should only be one duplicate item per rucksack'

        total_priority += _item_priority(list(item_both_compartments)[0])

    print(total_priority)


def part2(lines: List[str]):
    total_priority = 0

    for group_start in range(0, len(lines), 3):
        item_type_to_occurances: Dict[str, int] = defaultdict(int)
        for rucksack in lines[group_start:group_start+3]:
            for item_type in set(rucksack):
                item_type_to_occurances[item_type] += 1

        badge_item = [item for item in item_type_to_occurances if item_type_to_occurances[item] == 3]
        assert len(badge_item) == 1, 'There should only be one badge item per group'
        total_priority += _item_priority(badge_item[0])

    print(total_priority)


if __name__ == '__main__':
    with open('day3/in', 'r') as in_file:
        lines = in_file.read().splitlines()
        part1(lines)
        part2(lines)
