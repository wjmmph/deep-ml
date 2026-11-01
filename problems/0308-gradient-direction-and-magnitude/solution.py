import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
	import math
	magnitude = 0
	for i in gradient:
		magnitude += i ** 2
	magnitude = magnitude ** 0.5
	direction = []
	descent_direction = []
	for i in gradient:
		if i != 0:
			direction.append(i/magnitude)
			descent_direction.append(-1 * i/magnitude)
		else:
			direction.append(0.0)
			descent_direction.append(0.0)

	return {'direction': direction, 'descent_direction': descent_direction, 'magnitude': magnitude} 
	

