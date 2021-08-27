star=int(input("how many stars at base :"))
for row in range(star+1):
	for coloumn in range(row):
		print("*",end="")
	print("")
print("----------------------------------------")
number=int(input("enter the last number"))
for row in range(number+1):
	for coloumn in range(1,row):
		print(coloumn,end="")
	print("")
print("---------------------------------------")
a = int(input("Enter the number of rows: "))
k = 2 * a - 2  
for i in range(a, -1, -1):  
    for j in range(k, 0, -1):  
        print(end=" ")  
    k = k + 1  
    for j in range(0, i + 1):  
        print("*", end=" ")  
    print("")  

