
def gradient_descent(grad_f, x0, learning_rate, num_iterations):
    """
    Perform gradient descent optimization to find the minimum of a function.
    
    Parameters:
    grad_f (function): The gradient of the function to minimize.
    x0 (array-like): Initial guess for the minimum.
    learning_rate (float): Step size for each iteration.
    num_iterations (int): Number of iterations to perform.
    
    Returns:
    array-like: The point at which the function is minimized after the specified iterations.
    """

    x = x0

    list_of_xs = [x0] # Initialize a list to store the points at each iteration, starting with the initial guess

    for i in range(num_iterations): # Loop over the specified number of iterations
        x = x - learning_rate * grad_f(x) # Update the point by moving in the direction of the negative gradient
        list_of_xs.append(x) # Append the updated point to the list

    return x, list_of_xs