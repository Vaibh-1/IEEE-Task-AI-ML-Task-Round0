N = int(input('Enter the no of elements in the list:'))
numbers = []
for i in range(N):
     item = int(input())
     numbers.append(item)
def process_list(numbers):
    list_2 = numbers.copy()
    list_3 = []
    for i in range(N):
        if list_2[i] >=0:
            list_3.append(list_2[i])
    list_3.append(0)
    list_3.sort()        
    return list_3       
numbers_2 = process_list(numbers)
print("Orignal:",numbers)
print("Result:",numbers_2)