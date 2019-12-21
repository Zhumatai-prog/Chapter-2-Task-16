w = int(input("Enter your weight: "))
i = 1


for i in range(15):
	print(f"{i} - year your weight will be {w * 0.165}kg")
	w = w + 1