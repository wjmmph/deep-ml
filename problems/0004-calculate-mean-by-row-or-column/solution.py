def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []

	if mode.lower() == "row":
		for i in matrix:
			mean = sum(i)/len(i)
			means.append(mean)
	
	elif mode.lower() == "column":
		for i in range(len(matrix[0])):
			sum1 = 0
			for j in matrix:
				sum1 += j[i]
			mean = sum1 / len(matrix)
			means.append(mean)
	
	return means