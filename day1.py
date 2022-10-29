def cal_pre_values(array):
    total_pre_values = 0
    count = 0
    while count != len(array) - 1:
        if array[count] < array[count + 1]:
            total_pre_values += 1
        count += 1
    return total_pre_values

array = []
file = open("day1.txt", "r")
for data in file:
    number = int(float(data.split("\n")[0]))
    array.append(number)
file.close()

print(cal_pre_values(array))
