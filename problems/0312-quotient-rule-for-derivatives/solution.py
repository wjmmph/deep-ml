import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here
    n = len(g_coeffs) - 1
    g_coeffs_eqn, g_coeffs_der = 0, 0
    for i in g_coeffs:
        g_coeffs_eqn += i * (x**n)
        if n > 0:
            g_coeffs_der += i * n * (x ** (n - 1))
        n -= 1

    m = len(h_coeffs) - 1
    h_coeffs_eqn, h_coeffs_der = 0, 0
    for j in h_coeffs:
        h_coeffs_eqn += j * (x**m)
        if m > 0:
            h_coeffs_der += j * m * (x ** (m - 1))
        m -= 1

    der = ((g_coeffs_der * h_coeffs_eqn) - (g_coeffs_eqn * h_coeffs_der)) / (h_coeffs_eqn ** 2)
    return der
    


    