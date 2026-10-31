def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	product = []

	if len(b) != len(a[0]):
		return -1
		
	for i in a:
		s = 0
		for j in range(len(i)):
			s += i[j] * b[j]
		product.append(s)
	return product
