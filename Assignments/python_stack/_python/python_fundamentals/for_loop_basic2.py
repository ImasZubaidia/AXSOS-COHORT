#1 Biggie Size 
def biggie_size(list):
    for x in range(len(list)):
        if list[x] > 0:
            list[x] = "Big"
    return list

print(biggie_size([-1,3,5,-5]))

#2 Count Positives 
def count_positives(list):
    total = 0
    for x in range(len(list)):
        if list[x] > 0:
            total += 1
    list.pop(len(list)-1)
    list.append(total)
    return list
print(count_positives([1,6,-4,-2,-7,-2]))

#3 Sum Total 
def sum_total(list):
    total = 0
    for x in range(len(list)):
        total = total + list[x]
    return total
    
print(sum_total([1,2,3,4]))

#4 Average - 
def average(list):
    total = 0
    for x in range(len(list)):
        total = total + list[x]
    return total/len(list)
    
print(average([1,2,3,4]))

#5 Length 
def length(list):
    return len(list)

print(length([37,2,1,-9]))
print(length([]))

#6 Minimum 
def minimum(list):
    min = list[0]
    for x in range(len(list)):
        if list[x] < min:
            min = list[x]
    return min

print(minimum([37,2,1,-9]))

#7 Maximum 
def maximum(list):
    max = list[0]
    for x in range(len(list)):
        if list[x] > max:
            max = list[x]
        return max
        
print(maximum([37,2,1,-9]))

#8 Ultimate Analysis 
def ultimate_analysis(list):
    sum = sum_total(list)
    avg = average(list)
    min = minimum(list)
    max = maximum(list)
    total_length = length(list)
    analysis = {
        'sumTotal': sum,
        'average': avg,
        'minimum': min,
        'maximum': max,
        'length': total_length
    }
    return analysis

print(ultimate_analysis([37,2,1,-9]))

#9 Reverse List 
def reverse_list(list):
    list_len = len(list)
    for x in range(int(len(list)/2)):
        temp = list[list_len-1-x]
        list[list_len-1-x] = list[x]
        list[x] = temp
    return list

print(reverse_list([2,6,5,7,8,9]))