from string import ascii_uppercase
import operator


def run(program: list) -> list:
    output = []
    i = 0
    variables = {letter: 0 for letter in ascii_uppercase}
    operators = {"ADD": operator.add, "SUB": operator.sub, "MUL": operator.mul}
    comparisons = {
        "==": operator.eq,
        "!=": operator.ne,
        "<": operator.lt,
        ">": operator.gt,
        "<=": operator.le,
        ">=": operator.ge,
    }

    exit_loop = True
    while True:
        for item in program[i:]:
            i += 1
            exit_loop = False
            command = item.split(" ")

            if command[0] == "MOV":
                variables[command[1]] = (
                    int(command[2])
                    if command[2] not in variables
                    else variables[command[2]]
                )

            elif command[0] in operators:
                if command[2] not in variables:
                    variables[command[1]] = operators[command[0]](
                        variables[command[1]], int(command[2])
                    )
                else:
                    variables[command[1]] = operators[command[0]](
                        variables[command[1]], variables[command[2]]
                    )

            elif command[0] == "IF":
                if command[3] not in variables:
                    result = comparisons[command[2]](
                        variables[command[1]], int(command[3])
                    )
                else:
                    result = comparisons[command[2]](
                        variables[command[1]], variables[command[3]]
                    )

                if result:
                    i = program.index(command[5] + ":")
                    break
                elif i == len(program):
                    exit_loop = True
                    break
                else:
                    continue

            elif command[0] == "PRINT":
                output.append(int(command[1])) if command[
                    1
                ] not in variables else output.append(variables[command[1]])

            elif command[0] == "JUMP":
                i = program.index(command[1] + ":")
                break

            if command[0] == "END" or i == len(program):
                exit_loop = True
                break

        if exit_loop:
            break

    return output
