from utils import Utils

used_compliments = []
compliments = Utils.convert_dict_keys_to_ints(
    Utils.load_json_as_dict(
        path="data/compliments.json"
    )
)

used_memories = []
memories = Utils.convert_dict_keys_to_ints(
    Utils.load_json_as_dict(
        path="data/memories.json"
    )
)

used_reasons = []
reasons = Utils.convert_dict_keys_to_ints(
    Utils.load_json_as_dict(
        path="data/reasons.json"
    )
)

used_jokes = []
jokes = Utils.convert_dict_keys_to_ints(
    Utils.load_json_as_dict(
        path="data/jokes.json"
    )
)

data_types = {
    0: "DNE",
    1: "compliments",
    2: "memories",
    3: "reasons",
    4: "jokes"
}

# -------------------------------------------------------------------------------


# Program interraction loop
def main():
    print("        WELCOME DIANA")
    print("=============================")

    while True:
        print("(1) - Compliment")
        print("(2) - Treasured memory")
        print("(3) - A reason I love you")
        print("(4) - Dad joke")
        print("(0) - QUIT")

        choice = int(input("Type your choice and press enter: "))

        if choice == 0:
            break

        response = switch_case(choice)
        text_resp = response.get("text")
        found_new = response.get("found_new")
        type = response.get("type")

        print("")
        print(text_resp)
        if not found_new:
            reset = input("Would you like to reset " + str(type) + "? (Y/N): ")
            if reset.lower() == "y":
                reset_data(type)

        print("")
        print("=============================")


# -------------------------------------------------------------------------------


def switch_case(case_key):
    cases = {
            1: get_compliment,
            2: get_memory,
            3: get_reason,
            4: get_joke,
        }

    case_function = cases.get(case_key, get_default)

    return case_function()


def get_default():
    text = "I'm not familiar with that option. Try one of the options I listed!"
    return {
            "text": text,
            "found_new": True,
            "type": data_types.get(0)
        }


def get_compliment():
    random_key = Utils.get_random_integer_in_range(
        min=0,
        max=len(compliments),
        exclusions=used_compliments
    )

    if random_key is None:
        text = "Looks like I'm out of compliments for now..."
        return {
            "text": text,
            "found_new": False,
            "type": data_types.get(1)
        }

    text = compliments.get(random_key)
    used_compliments.append(random_key)

    return {
        "text": text,
        "found_new": True,
        "type": data_types.get(1)
    }


def get_memory():
    random_key = Utils.get_random_integer_in_range(
        min=0,
        max=len(memories),
        exclusions=used_memories
    )

    if random_key is None:
        text = "Looks like I'm out of memories for now..."
        return {
            "text": text,
            "found_new": False,
            "type": data_types.get(2)
        }

    text = memories.get(random_key)
    used_memories.append(random_key)

    return {
        "text": text,
        "found_new": True,
        "type": data_types.get(2)
    }


def get_reason():
    random_key = Utils.get_random_integer_in_range(
        min=0,
        max=len(reasons),
        exclusions=used_reasons
    )

    if random_key is None:
        text = "Looks like I'm out of reasons for now..."
        return {
            "text": text,
            "found_new": False,
            "type": data_types.get(3)
        }

    text = reasons.get(random_key)
    used_reasons.append(random_key)

    return {
        "text": text,
        "found_new": True,
        "type": data_types.get(3)
    }


def get_joke():
    random_key = Utils.get_random_integer_in_range(
        min=0,
        max=len(jokes),
        exclusions=used_jokes
    )

    if random_key is None:
        text = "Looks like I'm out of jokes for now..."
        return {
            "text": text,
            "found_new": False,
            "type": data_types.get(4)
        }

    text = jokes.get(random_key)
    used_jokes.append(random_key)

    return {
        "text": text,
        "found_new": True,
        "type": data_types.get(4)
    }

# -------------------------------------------------------------------------------

def reset_data(type):
    if type == data_types.get(1):
        used_compliments = []
    elif type == data_types.get(2):
        used_memories = []
    elif type == data_types.get(3):
        used_reasons = []
    elif type == data_types.get(4):
        used_jokes = []

# -------------------------------------------------------------------------------


main()
