n = 600851475143
f = 2
while n > 1:
	if n % f == 0:
		print f
		n = n / f
	else:
		f = f + 1
