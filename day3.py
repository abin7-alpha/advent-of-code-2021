"""Calculate the count of total zeroes and ones"""
def calc_bits(number_list):
    zeroes = number_list.count(0)
    ones = number_list.count(1)

    return zeroes, ones

"""Return length of first row to calculate the number of lists needed"""
def empty_lists_needed(all_number_list):
    for row in all_number_list:
        each_row = list(row)
        return len(each_row)

"""Save the numbers by column wise to a list and save it in to a main list""" 
def convert_columns(all_number_list):
    #create a list of lists according to the length of the first row
    seperated_list = [[] for x in range(empty_lists_needed(all_number_list))]
    count = 0
    for row in all_number_list:
        each_row = list(row)
        for number in each_row:
            seperated_list[count].append(int(number))
            if count == len(each_row)-1:
                count = 0
            else:
                count += 1

    return seperated_list

"""returns a dictionary of bits with count of zeroes and ones"""
def calc_values(all_number_list):
    count = 0
    converted_data = convert_columns(all_number_list)
    metric = {}
    for item in converted_data:
        a, b = calc_bits(item)
        metric[f'bit{str(count)}'] = [a, b]
        count += 1

    return metric

"""Returns the converted binary number"""
def final_binary(all_number_list):
    binary_number = ""
    calculated_metric = calc_values(all_number_list)
    for key,value in calculated_metric.items():
        if value[0] < value[1]:
            binary_number += "0"
        else:
            binary_number += "1"

    return binary_number

"""Returns the opposite number of the binary_number"""
def least_binary(all_number_list):
    binary = final_binary(all_number_list)
    l_binary = ""
    for number in list(binary):
        if number == "1":
            l_binary += "0"
        else:
            l_binary += "1"

    return int(binary), int(l_binary)

"""Calculate binary to decimal number"""
def binary_to_decimal(n):
    decimal = 0
    power = 1
    while n>0:
        rem = n%10
        n = n//10
        decimal += rem*power
        power = power*2
        
    return decimal

files = open("day3.txt", "r")
data = []
for file in files:
    data.append(file.split("\n")[0])

binary1, binary2 = least_binary(data)

#To get the final by_product
by_product = binary_to_decimal(binary1) * binary_to_decimal(binary2)
print(by_product)

        
