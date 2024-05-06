from csp import CSP, backtracking_search

def queens(n):
    # Define the variables and their domains
    variables = range(n)
    domains = {variable: range(n) for variable in variables}

    # Define the function to check if a queen can attack another
    def can_attack(q1, q2):
        return q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])

    # Define the constraints
    def queen_constraint(A, a, B, b):
        return not can_attack((A, a), (B, b))

    # Create a CSP instance
    problem = CSP(variables, domains, queen_constraint)

    # Use the backtracking search function to find a solution
    solution = backtracking_search(problem)

    # Print the solution
    print(solution)

# Call the function for a 4x4 chessboard
queens(4)