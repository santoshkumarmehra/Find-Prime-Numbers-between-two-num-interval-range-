a=int(input("enter the 1st no = "))
b=int(input("enter the 2nd no = "))

for i in range(a,b+1):
	if i>0:
		factor=0
		for j in range(1,i+1):
			if i%j==0:
				factor=factor+1
		if factor==2:
			print(j,end=" ",sep=" ")
		factor=0
print()

		
				