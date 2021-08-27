star=int(input("enter the stars at top:"))
for row in range(star,0,-1):
	for coloumn in range(row):
		print("*",end="")
	print("")
print("-------------------------------")
n = int(input("Enter the number of rows: "))
m = (2 * n) - 2  
for i in range(0, n):  
    for j in range(0, m):  
        print(end=" ")  
    m = m - 1  
    for j in range(0, i + 1):  
        print("* ", end=' ')  
    print(" ")  
print("-----------------------------------")
n = int(input("Enter the number of rows: "))
m = (2 * n) - 2  
for i in range(0, n):  
    for j in range(0, m):  
        print(end=" ")  
    m = m - 1  
    for j in range(1, i + 1):  
        print(j, end=' ')  
    print(" ")  