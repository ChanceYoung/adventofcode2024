from adventofcode2024.utils.filereader import format_input
"""
Corrupted Program
A program that uses a mult(x,y) function is broken.
X and Y are 1-3 digits
Some inputs need to be ignored since the program is now corrupted
Valid inputs contain:
- No whitespace
- No special characters

Objective puzzle 1:
Find all valid Mults, sum their output
objective puzzle 2:
add in the do and dont commands which enable or disable the following mult
"""
import re

#regex pattern = mul(\d{1,3},\d{1,3})
def puzzle1(data):
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    results = re.findall(pattern, data)
    print('puzzle 1 mults: ', len(results))
    mult_pattern = r'\d{1,3},\d{1,3}'
    mult_sum = 0
    for equation in results:
        numbers = re.findall(mult_pattern, equation)
        operands = numbers[0].split(',')
        mult_sum = mult_sum + (int(operands[0]) * int(operands[1]))
    return mult_sum

def puzzle2(data):
    pattern = r"(don\'t|do|mul\(\d{1,3},\d{1,3}\))"
    # Find all matches
    matches = re.findall(pattern, data)
    # Initialize active state and result list
    active = True
    filtered_mults = []

    for match in matches:
        if match == "don't":
            active = False  # Disable collecting mults
        elif match == "do":
            active = True  # Re-enable collecting mults
        elif active and match.startswith("mul"):
            filtered_mults.append(match)  # Collect only when active
    
    print('puzzle 2 mults: ', len(filtered_mults))
    mult_pattern = r'\d{1,3},\d{1,3}'
    mult_sum = 0
    for equation in filtered_mults:
        numbers = re.findall(mult_pattern, equation)
        operands = numbers[0].split(',')
        mult_sum = mult_sum + (int(operands[0]) * int(operands[1]))
    return mult_sum


data = format_input('../day3/input.txt')
pz1_result = puzzle1(data)
print(pz1_result)
pz2_result = puzzle2(data)
print(pz2_result)