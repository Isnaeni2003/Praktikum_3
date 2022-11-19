import random
a = float(input('masukkan nilai n =  '))
i = 0
m = 0.5
while i < 6:
	print(random.uniform(0.1,a))
	if (i == 5):
		break
	i += 1

