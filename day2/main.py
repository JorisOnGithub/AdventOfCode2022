from typing import List

_SCORE_LOSS = 0
_SCORE_DRAW = 3
_SCORE_WIN = 6
_SCORE_MOVE = lambda move: move + 1


def part1(lines: List[str]):
    total_score = 0

    for line in lines:
        opponent_move = ord(line[0]) - ord('A')
        my_move = ord(line[2]) - ord('X')

        if opponent_move == my_move:
            total_score += _SCORE_DRAW + _SCORE_MOVE(my_move)
        elif (opponent_move + 1) % 3 == my_move:
            total_score += _SCORE_WIN + _SCORE_MOVE(my_move)
        else:
            total_score += _SCORE_LOSS + _SCORE_MOVE(my_move)

    print(total_score)


def part2(lines: List[str]):
    total_score = 0

    for line in lines:
        opponent_move = ord(line[0]) - ord('A')

        if line[2] == 'X':
            total_score += _SCORE_LOSS + _SCORE_MOVE((opponent_move - 1) % 3)
        elif line[2] == 'Y':
            total_score += _SCORE_DRAW + _SCORE_MOVE(opponent_move)
        elif line[2] == 'Z':
            total_score += _SCORE_WIN + _SCORE_MOVE((opponent_move + 1) % 3)

    print(total_score)

if __name__ == '__main__':
    with open('day2/in', 'r') as in_file:
        lines = in_file.read().splitlines()
        part1(lines)
        part2(lines)
