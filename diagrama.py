from graphviz import Digraph

def parse_machine(filename):
    transitions = []
    with open(filename) as f:
        lines = f.readlines()

    reading = False
    for line in lines:
        line = line.strip()
        if not line:
            continue

        if line.startswith("transitions:"):
            reading = True
            continue

        if reading and "->" in line:
            left, right = line.split("->")
            state, symbol = left.strip().split(",")
            new_state, write, move = right.strip().split(",")
            transitions.append(
                (state.strip(), symbol.strip(),
                 new_state.strip(), write.strip(), move.strip())
            )

    return transitions


def generate_diagram(machine_file, output_name="turing_machine"):
    transitions = parse_machine(machine_file)

    dot = Digraph()
    dot.attr(rankdir="LR")

    states = set()

    for (s, sym, ns, w, m) in transitions:
        states.add(s)
        states.add(ns)

    for state in states:
        dot.node(state)

    for (s, sym, ns, w, m) in transitions:
        label = f"{sym} → {w}, {m}"
        dot.edge(s, ns, label=label)

    dot.render(output_name, format="png", cleanup=True)
    print("Diagrama generado:", output_name + ".png")


if __name__ == "__main__":
    generate_diagram("maquina.txt")
