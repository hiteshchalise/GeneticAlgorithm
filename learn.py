''' This is a basic Genetic Algorithm that attempts to generate solution that match target phrase by improving the fitness population of possible solution in each subsequent generation'''
import numpy as np
import random

POPULATION_SIZE = 500
#
PASSWORD = 'This is target phrase'
MUTATE_PROBABILITY = 1

def fitness(password, test_word):
    '''Fitness is calculated based on number of letter in test_word that matches with password.'''
    count = 0
    for i in range(len(password)):
        if password[i] == test_word[i]:
            count += 1
    return (count*100) / len(password)

def generate_word(password):
    '''Here random sentence is generated and returned.'''
    word = []
    for i in range(len(password)):
        word.append(np.random.randint(32, 126))
    return(''.join(chr(i) for i in word))

def generate_population(population_size, password):
    '''Population of random sentences are generated.'''
    population = []
    for i in range(population_size):
        population.append(generate_word(password))
    return(population)

def generate_mating_pool(population, population_size, test_word):
    '''Pool of individuals is made based on their fitness score.. if fitness of an individual is 10%, 10 such individual is added to the mating pool.'''
    fitness_score = []
    mating_pool = []
    for i in range(population_size):
        fitness_score.append(int(fitness(test_word, population[i])))
        for j in range(fitness_score[i]):
            mating_pool.append(population[i])
    return(mating_pool)

def create_child(individual1, individual2):
    '''A child individual is created by choosing randomly from individual1 or individual2.'''
    temp = []
    child = []
    for i in range(len(individual1)):
        check_random = np.random.randint(0,100)
        if (check_random > 50):
            # If random value from (0 to 100) is more than 50, choose i'th element from individual1.
            temp.append(individual1[i])
        else:
            # If random value from (0 to 100) is less than 50, choose i'th element from individual2.
            temp.append(individual2[i])
    # This converts array to a string.
    child = ''.join(item for item in temp)
    return child

def create_children(mating_pool, population_size):
    '''Two individuals are selected from mating pool randomly and a new population is generated.'''
    new_population = []
    for i in range(population_size):
        individual1 = mating_pool[np.random.randint(0, len(mating_pool))]
        individual2 = mating_pool[np.random.randint(0, len(mating_pool))]
        new_population.append(create_child(individual1, individual2))
    return new_population

def mutate_word(word, mutate_probability):
    '''A word is mutated based on mutate_probability'''
    temp = []
    new_word = []
    for each_element in word:
        if(np.random.randint(0, 100) <= mutate_probability):
            temp.append(chr(np.random.randint(32,126)))
        else:
            temp.append(each_element)
    new_word = ''.join(item for item in temp)
    return new_word

def mutate_population(population, mutate_probability):
    '''Each individuals in a population argument is subjected to mutate_word function where new mutated word is generated.'''
    mutated_population = []
    for each_individual in population:
        mutated_population.append(mutate_word(each_individual, mutate_probability))
    return mutated_population

def check_fitness(population, password):
    '''Whole population is checked if its individuals are equal to password.'''
    for each_individual in population:
        if each_individual == password:
            print(each_individual)
            return True
    return False

if __name__ == '__main__':
    # Random population generation
    population = generate_population(POPULATION_SIZE, PASSWORD)
    generation_count = 0

    while(True):
        # Loop until individuals match with password.
        generation_count += 1
        mating_pool = generate_mating_pool(population, POPULATION_SIZE, PASSWORD)
        new_population = create_children(mating_pool, POPULATION_SIZE)
        mutated_population = mutate_population(new_population, MUTATE_PROBABILITY)
        population = mutated_population

        if check_fitness(population, PASSWORD):
            break
        print(population[0])

    print(generation_count)
