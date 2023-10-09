import re






def read_from_file(filename: str):
    with open("input.txt") as fin:
        states = set(fin.readline().strip().split())
        alphabet = set(fin.readline().strip().split())
        relations = {}
        for i in fin.readline().strip()[1:-1].split(") ("):
            relation = i
            state_from, terminal, state_towards = relation.split(',')
            if state_from not in relations:
                relations[state_from] = []
            relations[state_from].append((terminal, state_towards))
        init_state = fin.readline().strip()
        final_states = set(fin.readline().strip().split())
        return states, alphabet, relations, init_state, final_states





if __name__ == "__main__":
    states, alphabet, relations, init_state, final_states = read_from_file("input.txt")
    print(states)
    print(alphabet)
    print(relations)
    print(init_state)
    print(final_states)
