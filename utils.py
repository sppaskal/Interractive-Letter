import random
import json
import msvcrt
import time
import math


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

    def wait_for_key(timeout):
        '''
        Waits for key inputs for a certain timeout
        and also resets input buffer when finished.
        '''
        start_time = time.time()
        input_key = None
        while True:
            if msvcrt.kbhit():
                input_key = msvcrt.getch().decode('utf-8')
                while msvcrt.kbhit():
                    msvcrt.getch()  # Clear the input buffer
                break
            elif time.time() - start_time > timeout:
                break
        return input_key

    # --------------------------------------------------------------------------

    def seconds_to_read_words(words):
        '''
        Expects a string of words and determines
        time it would take average adult to read
        said words in seconds.
        '''
        avrg = 0.5    # words per second
        word_count = len(str(words).split())
        return word_count / avrg

    # --------------------------------------------------------------------------

    def insert_newline(input_string, max_chars):
        '''
        Assumes that input_string is a sentence
        separated by spaces. Will insert a new
        line every max_chars without cutting off
        any words.
        '''
        words = input_string.split()
        current_line_length = 0
        result = []

        for word in words:
            if current_line_length + len(word) <= max_chars:
                result.append(word)
                current_line_length += len(word) + 1  # +1 for the space
            else:
                result.append('\n' + word)
                current_line_length = len(word) + 1  # Reset line length for the new line

        return ' '.join(result)

    # --------------------------------------------------------------------------

    def segnmented_sleep(seconds, skip_keys=[]):
        '''
        Performs sleep in segments of 1 second.
        Will interrupt sleep if skip keys are
        pressed.
        '''
        for i in range(math.ceil(seconds)):
            # Check for user input to skip the introduction
            input_key = Utils.wait_for_key(0.1)
            if input_key and input_key.lower() in skip_keys:
                break
            time.sleep(1)

    # --------------------------------------------------------------------------
