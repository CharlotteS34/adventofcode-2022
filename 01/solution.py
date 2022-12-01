"""
Author : Charlotte Skidmore
Purpose: Count elves calories
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Calorie counter for elves',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read()

    return args


# --------------------------------------------------
def get_max_calorie_count_top3(text):
    calorie_counts = [0]
    elf_counter = 0

    for line in text.split('\n'):
        if len(line) == 0:
            elf_counter = elf_counter + 1
            calorie_counts.append(0)
        else:
            calorie_counts[elf_counter] += int(line)

    calorie_counts.sort(reverse=True)
    return sum(calorie_counts[0:3])


# --------------------------------------------------
def get_max_calorie_count(text):
    current_calorie_count = 0
    max_calorie_count = 0

    for line in text.split('\n'):
        if len(line) == 0:
            if current_calorie_count > max_calorie_count:
                max_calorie_count = current_calorie_count
            current_calorie_count = 0
        else:
            current_calorie_count += int(line)
    return max_calorie_count


# --------------------------------------------------
def main():
    args = get_args()
    text = args.text

    max_calorie_count = get_max_calorie_count(text)
    print(f'Max calorie count: {max_calorie_count}')
    max_calorie_count_top3 = get_max_calorie_count_top3(text)
    print(f'Max calorie count top 3 elves: {max_calorie_count_top3}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
