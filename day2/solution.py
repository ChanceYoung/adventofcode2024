from adventofcode2024.utils.filereader import read_input_file
"""
Which reports are safe?
Rules:
1. all increasing or all decreasing
2. levels differ only by 1 to 3

input: list of reports
output: sum of how many reports are safe
"""
def format_input():
    data = read_input_file("../day2/input.txt")
    split_data = data.split('\n')
    return split_data

def check_array(arr):
    if len(arr) < 2:
        return False  # A single element or empty report is not valid by default
    
    increasing = all(1 <= int(arr[i]) - int(arr[i - 1]) <= 3 for i in range(1, len(arr)))
    decreasing = all(-3 <= int(arr[i]) - int(arr[i - 1]) <= -1 for i in range(1, len(arr)))

    return increasing or decreasing

def is_safe_with_one_removal(arr):
    if check_array(arr):
        return True  # The array is already safe

    for i in range(len(arr)):
        # Create a new array with the current element removed
        temp_arr = arr[:i] + arr[i + 1:]
        if check_array(temp_arr):
            return True  # Found a safe configuration by removing one element

    return False  # No single removal makes the array safe

def puzzle1(reports):
    safereports = 0
    unsafereports = 0
    for report in reports:
        report_numbers = report.split()
        issafe = check_array(report_numbers)
        if issafe:
            safereports += 1
        else:
            unsafereports += 1
                        
    return safereports

def puzzle2(reports):
    safereports = 0
    unsafereports = 0
    for report in reports:
        report_numbers = report.split()
        if is_safe_with_one_removal(report_numbers):
            safereports += 1
        else:
            unsafereports += 1
                        
    return safereports

reports_array = format_input()
pz1_result = puzzle1(reports_array)
pz2_result = puzzle2(reports_array)
print(pz1_result)
print(pz2_result)

