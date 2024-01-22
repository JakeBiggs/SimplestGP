import random

#Parameters
target_number = 100
mutation_percentage = 2

def test_function(x,y,z):
    return 5*x**4 + 4*y**3 + 45*z - target_number


def fitness(x,y,z):
    ans = test_function(x,y,z)

    if ans == 0:
        return 1000
    else:
        return abs(1/ans)

def generate_mutation(percentage):
    lower_bound = 1 -(percentage/100) /2
    upper_bound = 1 +(percentage/100)/2
    return random.uniform(lower_bound,upper_bound)

#generating soltuions
solutions = []
for s in range(1000):
    solutions.append( (random.uniform(0,10000),
                       random.uniform(0,10000),
                       random.uniform(0,10000)))

for i in range(10000):
    ranked_solutions = []

    for s in solutions:
        ranked_solutions.append( (fitness(s[0],s[1],s[2]),s))
    ranked_solutions.sort()
    ranked_solutions.reverse()

    print(f"=== Generation {i} best solutions ===")
    print(ranked_solutions[0]) #Prints fitness then elements to achieve that

    if ranked_solutions[0][0] > 999:
        final_x = ranked_solutions[0][1][0]
        final_y = ranked_solutions[0][1][1]
        final_z = ranked_solutions[0][1][2]
        print("Solution Approximated")
        print("X =", final_x,
              "Y =", final_y,
              "Z =", final_z)
        print("Target Number:",target_number,
              "\nApproximate Solution:",5*final_x**4 + 4*final_y**3 + 45*final_z)
        break
    best_solutions = ranked_solutions[:100]

    elements = []
    for s in best_solutions:
        elements.append(s[1][0]) #X choice
        elements.append(s[1][1]) #Y choice
        elements.append(s[1][2]) #Z choice

    newGeneration = []
    for e in range(1000):
        new_X = random.choice(elements) * generate_mutation(mutation_percentage)
        new_Y = random.choice(elements) * generate_mutation(mutation_percentage)
        new_Z = random.choice(elements) * generate_mutation(mutation_percentage)

        newGeneration.append((new_X,new_Y,new_Z))

    solutions = newGeneration

