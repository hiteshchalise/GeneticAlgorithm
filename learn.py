''' This is a basic Genetic Algorithm that attempts to generate solution that match target phrase by improving the fitness population of possible solution in each subsequent generation'''
import numpy as np
import random

POPULATION_SIZE = 500
#
PASSWORD = 'hitesh is the best'
MUTATE_PROBABILITY = 1

def fitness(password, test_word):
    '''Here fitness is calculated based on number of letter that matches with password.'''
    count = 0
    for i in range(len(password)):
        if password[i] == test_word[i]:
            count += 1
    return (count*100) / len(password)

def generate_word(password):
    word = []
    for i in range(len(password)):
        word.append(np.random.randint(32, 126))
    return(''.join(chr(i) for i in word))

def generate_population(population_size, password):
    population = []
    for i in range(population_size):
        population.append(generate_word(password))
    return(population)

def generate_mating_pool(population, population_size, test_word):
    fitness_score = []
    mating_pool = []
    for i in range(population_size):
        fitness_score.append(int(fitness(test_word, population[i])))
        for j in range(fitness_score[i]):
            mating_pool.append(population[i])
    return(mating_pool)

def create_child(individual1, individual2):
    temp = []
    child = []
    for i in range(len(individual1)):
        check_random = np.random.randint(0,100)
        if (check_random > 50):
            temp.append(individual1[i])
        else:
            temp.append(individual2[i])
    child = ''.join(item for item in temp)
    return child

def create_children(mating_pool, population_size):
    new_population = []
    for i in range(population_size):
        individual1 = mating_pool[np.random.randint(0, len(mating_pool))]
        individual2 = mating_pool[np.random.randint(0, len(mating_pool))]
        new_population.append(create_child(individual1, individual2))
    return new_population

def mutate_word(word, mutate_probability):
    temp = []
    new_word = []
    for each_element in word:
        if(np.random.randint(0, 100//mutate_probability) == 1):
            temp.append(chr(np.random.randint(32,126)))
        else:
            temp.append(each_element)
    new_word = ''.join(item for item in temp)
    return new_word

def mutate_population(population, mutate_probability):
    mutated_population = []
    for each_individual in population:
        mutated_population.append(mutate_word(each_individual, mutate_probability))
    return mutated_population

def check_fitness(population, password):
    for each_individual in population:
        if each_individual == password:
            print(each_individual)
            return True
    return False

population = generate_population(POPULATION_SIZE, PASSWORD)
generation_count = 0

while(True):
    generation_count += 1
    mating_pool = generate_mating_pool(population, POPULATION_SIZE, PASSWORD)
    new_population = create_children(mating_pool, POPULATION_SIZE)
    mutated_population = mutate_population(new_population, MUTATE_PROBABILITY)
    population = mutated_population

    if check_fitness(population, PASSWORD):
        break
    print(population[0])

print(generation_count)
