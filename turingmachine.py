import time

class TuringMachine:
    def __init__(self, config_file):
        self.load_machine(config_file)

    def load_machine(self, filename):
        self.transitions = {}
        with open(filename) as f:
            lines = f.readlines()

        reading_transitions = False
        for line in lines:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            if line.startswith("states:"):
                self.states = line.split(":")[1].strip().split(",")
            elif line.startswith("input_symbols:"):
                self.input_symbols = line.split(":")[1].strip().split(",")
            elif line.startswith("tape_symbols:"):
                self.tape_symbols = line.split(":")[1].strip().split(",")
            elif line.startswith("start_state:"):
                self.start_state = line.split(":")[1].strip()
            elif line.startswith("blank_symbol:"):
                self.blank = line.split(":")[1].strip()
            elif line.startswith("accept_states:"):
                self.accept_states = line.split(":")[1].strip().split(",")
            elif line.startswith("transitions:"):
                reading_transitions = True
            elif reading_transitions:
                left, right = line.split("->")
                state, symbol = left.strip().split(",")
                new_state, write, move = right.strip().split(",")
                self.transitions[(state.strip(), symbol.strip())] = (
                    new_state.strip(),
                    write.strip(),
                    move.strip()
                )

    def run(self, input_string, show_steps=True):
        tape = list(input_string)
        head = 0
        state = self.start_state
        steps = 0

        while state not in self.accept_states:
            if head < 0:
                tape.insert(0, self.blank)
                head = 0
            elif head >= len(tape):
                tape.append(self.blank)

            symbol = tape[head]

            if (state, symbol) not in self.transitions:
                break

            new_state, write, move = self.transitions[(state, symbol)]
            tape[head] = write

            if move == "R":
                head += 1
            elif move == "L":
                head -= 1

            state = new_state
            steps += 1

            if show_steps:
                print(f"Estado: {state}")
                print("".join(tape))
                print(" " * head + "^")
                print("-" * 40)

        return steps
