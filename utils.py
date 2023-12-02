import random


class Utils():

    @staticmethod
    def get_random_integer_in_range(min, max, exclusions=[]):
        '''
        Outputs a random number between the min and max
        given range (inclusive). Will also exclude any
        results in the exclusions list. The function returns
        -1 if there are no valid integers left in the range.
        '''
        # Create a population by removing exclusions from the range
        population = [x for x in range(min, max + 1) if x not in exclusions]

        # Check if there are valid choices in the population
        if not population:
            return -1

        # Use random.sample to get a unique random choice
        random_int = random.sample(population, 1)[0]

        return random_int
