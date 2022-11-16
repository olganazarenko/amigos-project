from types import FunctionType

from constants import COMMANDS_DICT


def reaction_func(reaction: str) -> FunctionType:
    return COMMANDS_DICT.get(reaction, lambda: 'Wrong enter.')


def change_input(user_input):
    new_input = user_input
    data = None

    for command in COMMANDS_DICT.keys():
        if user_input.strip().lower().startswith(command):
            new_input = command
            data = user_input[len(new_input) + 1:]
            break

    if data:
        data = data.split(' ')
        return reaction_func(new_input)(*data)

    return reaction_func(new_input)()
