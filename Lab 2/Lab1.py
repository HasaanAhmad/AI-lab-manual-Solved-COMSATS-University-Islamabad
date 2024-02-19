# LAB 1 (HASAAN AHMAD SP22-BSE-017 )

list1 = []
list2 = []

for i in range(5):
    n1=int(input("Enter a Number: "))
    list1.append(n1)

for i in range(5):
    n2=int(input("Enter a Number:"))
    list2.append(n2)

for i in range(5):
    list1.append(list2[i])
    
list1.sort()
print(list1)



