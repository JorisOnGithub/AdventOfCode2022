from typing import List, Tuple

def _parse_section(section: str) -> Tuple[int, int]:
    start, end = section.split('-')
    return int(start), int(end)


def _fully_contained(small_range: Tuple[int, int], large_range: Tuple[int, int]) -> bool:
    return small_range[0] >= large_range[0] and small_range[1] <= large_range[1]


def _has_overlap(range_a: Tuple[int, int], range_b: Tuple[int, int]) -> bool:
    return any([
        _fully_contained(range_a, range_b),
        _fully_contained(range_b, range_a),
        range_a[0] <= range_b[0] and range_a[1] >= range_b[0],
        range_b[0] <= range_a[0] and range_b[1] >= range_a[0]
    ])

def part1(lines: List[str]) -> None:
    fully_contained_pairs = 0

    for pairs in lines:
        first_elf, second_elf = [_parse_section(section) for section in pairs.split(',')]
        if _fully_contained(first_elf, second_elf) or _fully_contained(second_elf, first_elf):
            fully_contained_pairs += 1

    print(fully_contained_pairs)


def part2(lines: List[str]) -> None:
    overlapping_ranges = 0

    for pairs in lines:
        first_elf, second_elf = [_parse_section(section) for section in pairs.split(',')]
        if _has_overlap(first_elf, second_elf):
            overlapping_ranges += 1

    print(overlapping_ranges)


if __name__ == '__main__':
    with open('day4/in', 'r') as in_file:
        lines = in_file.read().splitlines()
        part1(lines)
        part2(lines)
