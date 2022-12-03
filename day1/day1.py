from typing import List

def run(lines: List[str]):
    calories_per_elf = []
    current_elf_calories = 0

    for line in lines:
        if line == '':
            calories_per_elf.append(current_elf_calories)
            current_elf_calories = 0
        else:
            current_elf_calories += int(line)
    calories_per_elf.append(current_elf_calories)
    
    # Part 1
    print(max(calories_per_elf))

    # Part 2
    print(sum(sorted(calories_per_elf, reverse=True)[:3]))

if __name__ == '__main__':
    with open('day1/in', 'r') as in_file:
        run(in_file.read().splitlines())
