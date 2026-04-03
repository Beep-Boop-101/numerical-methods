# Students should edit this Python file (just as you would a Python cell in a Jupyter Notebook)
# this module will contain functions for numerical integration

import numpy as np

def trapezoidal_rule(f, a, b, N):
    #write the arguments, docstring, and actual code of this function
    """
    ghdyd
    """
    x = np.linspace(a, b, N + 1) # Create an array of N+1 equally spaced points from a to b
    y = f(x) # Evaluate the function f at each point in x
    h = (b - a) / N # Calculate the width of each subinterval
    
    integral = np.sum((h / 2) * (y[:-1] + y[1:])) # Apply the trapezoidal rule to compute the integral

    return integral



def simpsons_rule(f, a, b, N):
    #write the arguments, docstring, and actual code of this function
    
    if N % 2 != 0:
        raise ValueError("N must be even for Simpson's rule.")
    
    else:

        x = np.linspace(a, b, N + 1) # Create an array of N+1 equally spaced points from a to b
        y = f(x) # Evaluate the function f at each point in x
        h = (b - a) / N # Calculate the width of each subinterval

        integral = np.sum((h / 3) * (y[0:-2:2] + 4 * y[1:-1:2] + y[2::2]))

        
        return integral




#A = ((f(x) + f(x + h) - 2 * f(x + h/2)) / (2 * ((h / 2) ** 2)))[:-1] # Compute the second derivative of f at the midpoints of the subintervals
#B = ((f(x + h) - f(x)) / h)[:-1]
#C = (f(x + h/2))[:-1] # Evaluate the function at the midpoints of the subintervals

#area_in_quadratic_slice = (A/3) * (x[1:] ** (3)  - x[:-1] ** (3)) + (B/2) * (x[1:] ** (2)  - x[:-1] ** (2)) + (C) * (x[1:]  - x[:-1]) # Compute the area of the quadratic slice using Simpson's rule

#total_integral = np.sum(area_in_quadratic_slice) # Sum the areas of all the quadratic slices to get the total integral
