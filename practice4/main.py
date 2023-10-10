import re
from collections import defaultdict


def transform_NKA2DKA(states, alphabet, relations, init_state, final_states):
    i = 0
    result = []
    stack = [(init_state,)]
    while i < len(stack):
        state = stack[i]
        from_state_to_state = defaultdict(set)
        for s in state:
            for relation in relations[s]:
                from_state_to_state[relation[0]].add(relation[1])
        # print(state, from_state_to_state)
        for key, val in from_state_to_state.items():
            new_node = tuple(sorted(list(val)))
            if new_node not in stack:
                stack.append(new_node)
            result.append([''.join(state), key, ''.join(new_node)])
        i += 1
    new_final_states = [''.join(item) for item in stack if any([under_item in final_states for under_item in item])]
    new_states = [''.join(item) for item in stack]
    new_alphabet = sorted(set(i[1] for i in result))
    return new_states, new_alphabet, result, init_state, new_final_states


def print_result(states, alphabet, result, init_state, final_states):
    print("DFA:")
    print(f"Set of states: {', '.join(states)}\n")
    print(f"Input alphabet: {', '.join(alphabet)}\n")
    print("State-transitions function:")
    for item in result:
        print(f"D({item[0]}, {item[1]}) = {item[2]}")

    print()
    print(f"Initial states: {init_state}\n")
    print(f"Final states: {', '.join(final_states)}\n")


def read_from_file(filename: str):
    with open("input.txt") as fin:
        states = set(fin.readline().strip().split())
        alphabet = set(fin.readline().strip().split())
        relations = {}
        for i in fin.readline().strip()[1:-1].split(") ("):
            relation = i
            state_from, terminal, state_towards = relation.split(',')
            state_from, terminal, state_towards = state_from.strip(), terminal.strip(), state_towards.strip()
            if state_from not in relations:
                relations[state_from] = []
            relations[state_from].append((terminal, state_towards))
        init_state = fin.readline().strip()
        final_states = set(fin.readline().strip().split())
        return states, alphabet, relations, init_state, final_states


def read_from_console():
    print("Enter set of states:")
    states = set(input().strip().split())
    print("Enter the input alphabet:")
    alphabet = set(input().strip().split())
    relations = {}
    print("Enter state-transitions function (current state, input character, next state):")
    for i in input().strip()[1:-1].split(") ("):
        relation = i
        state_from, terminal, state_towards = relation.split(',')
        state_from, terminal, state_towards = state_from.strip(), terminal.strip(), state_towards.strip()
        if state_from not in relations:
            relations[state_from] = []
        relations[state_from].append((terminal, state_towards))
    print("Enter a set of initial states:")
    init_state = input().strip()
    print("Enter a set of final states:")
    final_states = set(input().strip().split())
    return states, alphabet, relations, init_state, final_states


if __name__ == "__main__":
    # print_result(*transform_NKA2DKA(*read_from_file("input.txt")))
    print_result(*transform_NKA2DKA(*read_from_console()))
