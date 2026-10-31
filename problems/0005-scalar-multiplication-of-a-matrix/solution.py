def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	lst = []
	for i in matrix:
		lstel = []
		for j in i:
			lstel.append(j * scalar)
		lst.append(lstel)
	
	return lst