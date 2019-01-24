maior = 0

for n1 in range(999, 1, -1):
	for n2 in range(999, 1, -1):
		r = n1 * n2
		if str(r) == str(r)[::-1] and r > maior:
			maior = r
print maior
			

	
