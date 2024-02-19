# LAB 2 (HASAAN AHMAD SP22-BSE-017 )
list1 = []
list2 = []

print("Enter values for List 1:")
for i in range(5):
    n1 = int(input("Enter a Number: "))
    list1.append(n1)

print("Enter values for List 2:")
for i in range(5):
    n2 = int(input("Enter a Number: "))
    list2.append(n2)

merged_list = list1 + list2

merged_list.sort()
print("Merged and sorted list:", merged_list)

smallest = min(merged_list)
largest = max(merged_list)

print("Smallest element:", smallest)
print("Largest element:", largest)
