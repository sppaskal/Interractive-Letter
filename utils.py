import random
import json


class Utils():

    @staticmethod
    def get_random_integer_in_range(min, max, exclusions=[]):
        '''
        Outputs a random number between the min and max
        given range (min is inclusive, but max is not).
        Will also exclude any results in the exclusions list.
        The function returns None if there are no valid integers
        left in the range.
        '''
        # Create a population by removing exclusions from the range
        population = [x for x in range(min, max) if x not in exclusions]

        # Check if there are valid choices in the population
        if not population:
            return None

        # Use random.sample to get a unique random choice
        return random.sample(population, 1)[0]

    # --------------------------------------------------------------------------

    @staticmethod
    def load_json_as_dict(path):
        with open(path, 'r') as file:
            data_dict = json.load(file)
        return data_dict

    # --------------------------------------------------------------------------

    @staticmethod
    def convert_dict_keys_to_ints(data_dict):
        data_dict = {int(key): value for key, value in data_dict.items()}
        return data_dict

    # --------------------------------------------------------------------------
