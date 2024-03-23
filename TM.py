class TuringMachine:
    def __init__(self, tape):
        self.tape = tape
        self.current_state = 0
        self.head_position = 0
        self.transitions = {
            # transition on 0 and 1
            0: {"0": (0, "0", 1), "1": (1, "x", 1), " ": (0, "Rejected", 0)},
            1: {"0": (1, "0", 1), "1": (2, "x", 1), " ": (1, "Rejected", 0)},
            2: {"0": (2, "0", 1), "1": (3, "x", 1), " ": (2, "Rejected", 0)},
            3: {"0": (3, "0", 1), "1": (3, "x", 1), " ": (3, "Accepted", 0)},
            # transition on blank symbol // accept or reject
            # ("q0", "0"): ("q0", "0", 1),
            # ("q0", "1"): ("q1", "x", 1),
            # ("q1", "0"): ("q1", "0", 1),
            # ("q1", "1"): ("q2", "x", 1),
            # ("q2", "0"): ("q2", "0", 1),
            # ("q2", "1"): ("q3", "x", 1),
            # # transition on blank symbol // accept or reject
            # ("q3", "0"): ("q_accept_TM", "0", 1),
            # ("q3", "1"): ("q_accept_TM", "x", 1),
            # ("q0", " "): ("q_reject_TM", " ", 0),
            # ("q1", " "): ("q_reject_TM", " ", 0),
            # ("q2", " "): ("q_reject_TM", " ", 0),
            # ("q3", " "): ("q_accept_TM", " ", 0),
        }

    def run(self):
        input_string = self.tape
        if input_string[len(input_string) - 1] != " ":
            input_string += " "

        if input_string[0] != "S":
            input_string = "S" + input_string

        while True:
            current_state = self.current_state
            current_symbol = input_string[self.head_position]
            if current_symbol == "S":
                current_symbol = input_string[self.head_position + 1]
                self.head_position += 1

            next_state, value, increment = self.transitions[current_state].get(
                current_symbol
            )
            print(
                f"current state: {current_state}, current symbol:{current_symbol}, next state: {next_state}, value: {value} and increment: {increment}"
            )

            if current_symbol == "1":
                self.current_state = next_state
                self.head_position += increment
            elif current_symbol == "0":
                self.current_state = next_state
                self.head_position += increment
            else:
                if value == "Accepted":
                    print("Accepted")
                    return True
                else:
                    print("Rejected")
                    return False


# initialize TuringMachine
tm = TuringMachine(input("Enter the input string: "))
tm.run()