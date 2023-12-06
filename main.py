from utils import Utils
from data import Data
import time
import math


# Program interraction loop
def main():

    data = Data()

    introduction(intro=data.intro)

    while True:
        print("(1) - Compliment")
        print("(2) - Treasured memory")
        print("(3) - A reason I love you")
        print("(4) - Dad joke")
        print("(0) - QUIT")

        choice = check_choice_empty(
            input("Type your choice and press enter: ")
        )

        if choice == 0:
            break

        response = switch_case(data, choice)
        text_resp = response.get("text")
        found_new = response.get("found_new")
        type = response.get("type")

        print("")
        print(text_resp)
        if not found_new:
            reset = input("Would you like to reset " + str(type) + "? (Y/N): ")
            if reset.lower() == "y":
                data.reset_data(type)

        print("")
        print("=============================")

        # NOTE: Uncomment for transition between interractions
        # transition(
        #     seconds=3,
        #     separator=".",
        #     sep_count=3
        # )

# -------------------------------------------------------------------------------


def switch_case(data, case_key):
    cases = {
            1: data.get_compliment,
            2: data.get_memory,
            3: data.get_reason,
            4: data.get_joke,
        }

    case_function = cases.get(case_key, data.get_default)

    return case_function()


# -------------------------------------------------------------------------------


def transition(seconds=1, separator=".", sep_count=3):
    sec_per_sep = seconds/(sep_count + 1)
    for i in range(sep_count):
        time.sleep(sec_per_sep)
        print(separator)

    time.sleep(sec_per_sep)
    print("")

# -------------------------------------------------------------------------------


def introduction(intro):
    '''
    intro is expected to be a dictionary with a title
    and a list of paragraphs for the body.
    '''

    print(intro.get("title"))
    print("")
    time.sleep(2)
    print("Press 'space' if you want to skip forward")
    print("")
    time.sleep(2)

    # Check for user input to skip the introduction
    input_key = Utils.wait_for_key(0.1)
    skip_keys = ['', ' ', 'space']
    if input_key not in skip_keys:
        body = intro.get("body")
        for paragraph in body:
            print(paragraph)
            print("")

            # segment sleep so that user can cancel it without
            # having to wait the full duration
            seconds = Utils.seconds_to_read_words(paragraph)
            for i in range(math.ceil(seconds)):
                # Check for user input to skip the introduction
                input_key = Utils.wait_for_key(0.1)
                skip_keys = ['', ' ', 'space']
                if input_key and input_key.lower() in skip_keys:
                    break
                time.sleep(1)

    print("=============================")

# -------------------------------------------------------------------------------


def check_choice_empty(choice):
    '''
    Checks if user input is not empty after strip
    and if it's not returns it as int. If user input
    is empty return -1.
    '''
    if choice.strip():
        return int(choice)
    else:
        return -1

# -------------------------------------------------------------------------------


main()
