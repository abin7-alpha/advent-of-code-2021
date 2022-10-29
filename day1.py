#A: 607 (N/A - no previous sum)
#B: 618 (increased)
#C: 618 (no change)
#D: 617 (decreased)
#E: 647 (increased)
#F: 716 (increased)
#G: 769 (increased)
#H: 792 (increased)
#In this example, there are 5 sums that are larger than the previous sum.
#
#Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?

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
