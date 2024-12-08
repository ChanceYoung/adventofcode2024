
from adventofcode2024.utils.filereader import read_input_file

def format_input():
    data = read_input_file("../day1/input.txt")
    split_array = data.split()
    firstlist = []
    secondlist = []
    index = 0
    for number in split_array:
        if index % 2 == 0:
            firstlist.append(number)
        else:
            secondlist.append(number)
        index += 1
    return (firstlist, secondlist)

def puzzle1(firstlist, secondlist):
    #TODO:
    #Sort numbers
    #Pair smallest > largest
    #Calculate numerical distance e.g. 4-3 = 1
    #Add up all distances between left and right list
    firstlist.sort()
    secondlist.sort()
    index = 0
    distance_sum = 0
    for loc in firstlist:
        pair = secondlist[index]
        distance = abs(int(loc) - int(pair))
        distance_sum += distance
        index += 1
    return distance_sum


def puzzle2(firstlist,secondlist):
    #input: 2 lists
    #output: similarity score
    #TODO:
    #[] find how many times left list number appears in right list.
    #[] multiply number by frequency 
    #[] sum is the similarity score
    similarity_sum = 0
    for number1 in firstlist:
        frequency = 0
        for number2 in secondlist:
            if number2 == number1:
                frequency = frequency + 1
        similarity_sum = similarity_sum + (int(number1) * frequency)
    return similarity_sum


firstlist, secondlist = format_input()
pz1_result = puzzle1(firstlist, secondlist)
print(pz1_result)
pz2_result = puzzle2(firstlist, secondlist)
print(pz2_result)