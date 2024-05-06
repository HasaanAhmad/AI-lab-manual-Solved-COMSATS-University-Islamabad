from constraint import Problem, AllDifferentConstraint


problem = Problem()

problem.addVariables(range(4), range(4))

problem.addConstraint(AllDifferentConstraint())

problem.addConstraint(lambda q1, q2, q3, q4: abs(q1 - q2) != 1 and abs(q1 - q3) != 2 and abs(q1 - q4) != 3 and 
                                          abs(q2 - q3) != 1 and abs(q2 - q4) != 2 and abs(q3 - q4) != 1, 
                                          (0, 1, 2, 3))

solutions = problem.getSolutions()
for solution in solutions:
    print(solution)