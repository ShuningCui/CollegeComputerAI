# Initialize population
import random


def init_population(population_size=8, queen_size=8):
    population = []
    for i in range(population_size):
        individual = [random.randint(0,7) for x in range(queen_size)]
        population.append(individual)
    return population

# Fitness function
def fitness(individual):
    non_conflicts = 0
    for i in range(len(individual)):
        for j in range(i+1, len(individual)):
            if individual[i] != individual[j]:
                if abs(i-j) != abs(individual[i] - individual[j]):
                    non_conflicts += 1
    return non_conflicts

# 计算所有种群的适应度
def fitness_all(population):
    for i in range(len(population)):
        population[i].append(fitness(population[i]))

# 计算所有种群的适应度
def fitness_all(population):
    for i in range(len(population)):
        population[i].append(fitness(population[i]))

# 将适应度转换为概率

def fitness_probability(population):
    total = sum([x[-1] for x in population])
    for i in range(len(population)):
        population[i].append(population[i][-1]/total)


# 选择下一代 next generation population
import numpy as np


def select_next_generation(population, population_size):
    select_prob = [x[-1] for x in population]
    selected_index = np.random.choice(range(len(population)), 
                    population_size, replace=False, p=select_prob)
    next_generation = [population[i][:-2] for i in selected_index]
    return next_generation

def crossover(individual1, individual2):
    crossover_point = random.randint(1, len(individual1)-1)
    return (individual1[:crossover_point] + individual2[crossover_point:],
    individual2[:crossover_point] + individual1[crossover_point:])

def crossover_all(population):
    crossovered_population = []
    for i in range(0, len(population), 2):
        corssed1, crossed2 = crossover(population[i], population[i+1])
        crossovered_population.extend([corssed1,crossed2])
    return crossovered_population

# mutation function
def mutation(individual, mutation_rate=0.1):
    if random.random() < mutation_rate:
        mutate_point = random.randint(0, len(individual)-1)
        individual[mutate_point] = random.randint(0, len(individual)-1)
    return individual

# mutation all
def mutation_all(population, mutation_rate=0.1):
    mutated_population = [mutation(x, mutation_rate) for x in population]
    return mutated_population

def output_board(individual):
    for i in range(len(individual)):
        print(" ".join(["Q" if x == individual[i] else "*" 
                        for x in range(len(individual))]))
        
# main
# initialize population
population_size = 100000
queen_size = 8
population = init_population(population_size, queen_size)

num_generations = 1
target = 28
outs = []
target_lists = []
while True:
    # calculate fitness
    fitness_all(population)
    target_lists = [x for x in population if x[-1] == target]
    if len(target_lists) > 0:
        break
    # calculate probability
    fitness_probability(population)
    # select next generation
    next_generation = select_next_generation(population, population_size//2)
    # crossover
    crossovered_population = crossover_all(next_generation)
    random.shuffle(next_generation)
    crossovered_population.extend(crossover_all(next_generation))
    # mutation
    population = mutation_all(crossovered_population)
    num_generations += 1

    print(f"Find {len(target_lists)} target in {num_generations} generations")
    for target in target_lists:
    # print(target)
        output_board(target[:-1])
        print("\n\n")