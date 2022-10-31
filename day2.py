"""Calculate the values according to the position of the submarine"""
def final_depth(array):
    value1 = 0
    value2 = 0
    for data in array:
        if data[0] == "forward":
            value1 += int(data[1])
        if data[0] == "up":
            value2 -= int(data[1])
        if data[0] == "down":       
            value2 += int(data[1])

    return value1, value2

file = open("day2.txt", "r")
final_data = []
for data in file:
    line = data.split()
    final_data.append(line)

a, b = final_depth(final_data)
print(a*b)
