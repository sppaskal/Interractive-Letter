from utils import Utils

compliments = {
    0: "Compliment 0",
    1: "Compliment 1",
    2: "Compliment 2",
    3: "Compliment 3"
}

used_compliments = []


# Program interraction loop
def main():

    print("        WELCOME DIANA")
    print("=============================")

    while True:
        print("(1) - Compliment")
        print("(2) - A favorite memory")
        print("(3) - A reason I love you")
        print("(0) - QUIT")

        option = int(input("Type your choice and press enter: "))

        if option == 0:
            break

        response = switch_case(option)
        print(response)

        print("")
        print("=============================")


def switch_case(case_key):
    cases = {
            1: get_compliment,
        }

    case_function = cases.get(case_key, get_default)

    return case_function()


def get_compliment():
    random_key = Utils.get_random_integer_in_range(
        min=0,
        max=len(compliments),
        exclusions=used_compliments
    )

    if random_key == -1:
        return "Looks like I'm out of compliments for now..."

    text = compliments.get(random_key)
    used_compliments.append(random_key)

    return text


def get_default():
    return "I'm not familiar with that option. Try one of the options I listed!"


main()
