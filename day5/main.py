from typing import List
import re


def part2(lines: List[str]):
    stack_numer_line_index = lines.index('') - 1
    stack_numer_line = lines[stack_numer_line_index]
    number_of_stacks = int(stack_numer_line.split()[-1])
    stacks = [[] for _ in range(number_of_stacks)]

    for stack_line in lines[stack_numer_line_index - 1::-1]:
        for i in range(number_of_stacks):
            crate_index = 1 + i * 4
            if stack_line[crate_index] != ' ':
                stacks[i].append(stack_line[crate_index])

    move_regex = re.compile(r'move (\d+) from (\d+) to (\d+)')
    for move_line in lines[stack_numer_line_index + 2:]:
        num_boxes, from_stack, to_stack = map(int, move_regex.search(move_line).groups())
        stacks[to_stack - 1].extend(stacks[from_stack - 1][-num_boxes:])
        stacks[from_stack - 1] = stacks[from_stack - 1][:-num_boxes]

    print(''.join((stack[-1] for stack in stacks)))


def part1(lines: List[str]):
    stack_numer_line_index = lines.index('') - 1
    stack_numer_line = lines[stack_numer_line_index]
    number_of_stacks = int(stack_numer_line.split()[-1])
    stacks = [[] for _ in range(number_of_stacks)]

    for stack_line in lines[stack_numer_line_index - 1::-1]:
        for i in range(number_of_stacks):
            crate_index = 1 + i * 4
            if stack_line[crate_index] != ' ':
                stacks[i].append(stack_line[crate_index])

    move_regex = re.compile(r'move (\d+) from (\d+) to (\d+)')
    for move_line in lines[stack_numer_line_index + 2:]:
        num_boxes, from_stack, to_stack = map(int, move_regex.search(move_line).groups())
        for _ in range(num_boxes):
            stacks[to_stack - 1].append(stacks[from_stack - 1].pop())

    print(''.join((stack[-1] for stack in stacks)))

if __name__ == '__main__':
    with open('day5/in', 'r') as in_file:
        lines = in_file.read().splitlines()
        part1(lines)
        part2(lines)
