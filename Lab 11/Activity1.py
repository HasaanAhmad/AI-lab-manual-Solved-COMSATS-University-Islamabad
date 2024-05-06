from constraint import Problem, AllDifferentConstraint

regions = ["Western Australia", "Northern Territory", "South Australia", "Queensland", "New South Wales", "Victoria", "Tasmania"]
colors = ["red", "green", "blue"]
neighbors = [("Western Australia", "Northern Territory"), ("Western Australia", "South Australia"), ("South Australia", "Northern Territory"), 
             ("Queensland", "Northern Territory"), ("Queensland", "South Australia"), ("Queensland", "New South Wales"), 
             ("New South Wales", "South Australia"), ("Victoria", "South Australia"), ("Victoria", "New South Wales"), 
             ("Victoria", "Tasmania")]
problem = Problem()
problem.addVariables(regions, colors)
for neighbor in neighbors:
    problem.addConstraint(AllDifferentConstraint(), neighbor)
solutions = problem.getSolutions()
for solution in solutions:
    print(solution)