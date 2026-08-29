N = int(input('Enter the no of elements in the list:'))
list_ = []
for i in range(N):
    item = int(input())
    list_.append(item)
print ("Reversed:",list_[::-1])    
sum_list = int()
for i in range(N):
    sum_list = sum_list + list_[i]
print("Sum:",sum_list) 
largest_tillnow = list_[1]
for i in range(N):
    if list_[i]>largest_tillnow :
        largest_tillnow = list_[i]
print("Largest:",largest_tillnow)
smallest_tillnow = list_[1]
for i in range(N):
    if list_[i]<smallest_tillnow :
        smallest_tillnow = list_[i]
print("Smallest:",smallest_tillnow)
even_count = int()
odd_count = int()
for i in range(N):
    if list_[i]%2 == 0:
        even_count +=1
    else:
        odd_count +=1
print("Even count",even_count) 
print("Odd count",odd_count)       

