sum = 0
v1 = 1
v2 = 1
v3 = 0

while v3 < 4000000:
	v3 = v1 + v2
	if v3 % 2 == 0:
		sum = sum + v3
	v1 = v2
	v2 = v3

print(sum)
