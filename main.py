from data import Data
import time


# Program interraction loop
def main():
    print("        WELCOME DIANA")
    print("=============================")

    data = Data()

    while True:
        print("(1) - Compliment")
        print("(2) - Treasured memory")
        print("(3) - A reason I love you")
        print("(4) - Dad joke")
        print("(0) - QUIT")

        choice = int(input("Type your choice and press enter: "))

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

        transition(
            seconds=3,
            separator=".",
            sep_count=3
        )


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
    sec_per_sep = seconds/sep_count
    for i in range(sep_count):
        time.sleep(sec_per_sep)
        print(separator)

    print("")

# -------------------------------------------------------------------------------


main()
