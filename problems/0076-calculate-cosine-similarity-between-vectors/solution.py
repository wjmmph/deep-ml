import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	import math
	mv1 = sum(v1 * v2) / (math.sqrt(sum(v1 * v1)) * math.sqrt(sum(v2 * v2))) 
	return mv1