from utils import Utils


class Data():

    def __init__(self, name):

        self.databases = Utils.load_json_as_dict(
            path="data/databases.json"
        )

        self.db_path = self.set_db_path(name)

        self.used_compliments = []
        self.compliments = Utils.convert_dict_keys_to_ints(
            Utils.load_json_as_dict(
                path=self.db_path + "/compliments.json"
            )
        )

        self.used_memories = []
        self.memories = Utils.convert_dict_keys_to_ints(
            Utils.load_json_as_dict(
                path=self.db_path + "/memories.json"
            )
        )

        self.used_reasons = []
        self.reasons = Utils.convert_dict_keys_to_ints(
            Utils.load_json_as_dict(
                path=self.db_path + "/reasons.json"
            )
        )

        self.used_jokes = []
        self.jokes = Utils.convert_dict_keys_to_ints(
            Utils.load_json_as_dict(
                path=self.db_path + "/jokes.json"
            )
        )

        self.intro = Utils.load_json_as_dict(
            path=self.db_path + "/intro.json"
        )

        self.info = Utils.load_json_as_dict(
            path=self.db_path + "/info.json"
        )

        self.data_types = {
            0: "DNE",
            1: "compliments",
            2: "memories",
            3: "reasons",
            4: "jokes"
        }

    # -----------------------------------------------------

    def set_db_path(self, name):
        if name.lower() in self.databases:
            return "data/" + str(name)
        else:
            return "data/default"

    # -----------------------------------------------------

    def get_default(self):
        text = self.info.get("invalid_choice")
        return {
                "text": text,
                "found_new": True,
                "type": self.data_types.get(0)
            }

    # -----------------------------------------------------

    def get_compliment(self):
        random_key = Utils.get_random_integer_in_range(
            min=0,
            max=len(self.compliments),
            exclusions=self.used_compliments
        )

        if random_key is None:
            text = self.info.get("compliments_empty")
            return {
                "text": text,
                "found_new": False,
                "type": self.data_types.get(1)
            }

        text = self.compliments.get(random_key)
        self.used_compliments.append(random_key)

        return {
            "text": Utils.insert_newline(
                input_string=text,
                max_chars=67
            ),
            "found_new": True,
            "type": self.data_types.get(1)
        }

    # -----------------------------------------------------

    def get_memory(self):
        random_key = Utils.get_random_integer_in_range(
            min=0,
            max=len(self.memories),
            exclusions=self.used_memories
        )

        if random_key is None:
            text = self.info.get("memories_empty")
            return {
                "text": text,
                "found_new": False,
                "type": self.data_types.get(2)
            }

        text = self.memories.get(random_key)
        self.used_memories.append(random_key)

        return {
            "text": Utils.insert_newline(
                input_string=text,
                max_chars=67
            ),
            "found_new": True,
            "type": self.data_types.get(2)
        }

    # -----------------------------------------------------

    def get_reason(self):
        random_key = Utils.get_random_integer_in_range(
            min=0,
            max=len(self.reasons),
            exclusions=self.used_reasons
        )

        if random_key is None:
            text = self.info.get("reasons_empty")
            return {
                "text": text,
                "found_new": False,
                "type": self.data_types.get(3)
            }

        text = self.reasons.get(random_key)
        self.used_reasons.append(random_key)

        return {
            "text": Utils.insert_newline(
                input_string=text,
                max_chars=67
            ),
            "found_new": True,
            "type": self.data_types.get(3)
        }

    # -----------------------------------------------------

    def get_joke(self):
        random_key = Utils.get_random_integer_in_range(
            min=0,
            max=len(self.jokes),
            exclusions=self.used_jokes
        )

        if random_key is None:
            text = self.info.get("jokes_empty")
            return {
                "text": text,
                "found_new": False,
                "type": self.data_types.get(4)
            }

        text = self.jokes.get(random_key)
        self.used_jokes.append(random_key)

        return {
            "text": text,
            "found_new": True,
            "type": self.data_types.get(4)
        }

    # -------------------------------------------------------------------------------

    def reset_data(self, type):
        if type == self.data_types.get(1):
            self.used_compliments = []
        elif type == self.data_types.get(2):
            self.used_memories = []
        elif type == self.data_types.get(3):
            self.used_reasons = []
        elif type == self.data_types.get(4):
            self.used_jokes = []
