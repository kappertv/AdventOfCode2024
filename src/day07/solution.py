def readEquations(file_path):
    with open(file_path, "r") as file:
        data = file.read().strip()
    return data.splitlines()

def part1(file_path):
    equations = readEquations(file_path)
    return sum([getEquationValue(e) for e in equations])

def getEquationValue(equation):
    assertion, values = getAssertionAndValues(equation)
    possibleResults = getPossibleResults(values)
    # print(f"Target: {assertion}")
    # print(f"numbers: {possibleResults}")
    if int(assertion) in possibleResults:
        return int(assertion)
    return 0

def getPossibleResults(values):
    optionAdd = values[0] + values[1]
    optionMul = values[0] * values[1]
    optionConcat = int(str(values[0]) + str(values[1]))
    if len(values) == 2:
        return [optionAdd, optionMul, optionConcat]
    else:
        results = []
        addList = [optionAdd] + values[2:]
        mulList = [optionMul] + values[2:]
        conList = [optionConcat] + values[2:]
        results.extend(getPossibleResults(addList))
        results.extend(getPossibleResults(mulList))
        results.extend(getPossibleResults(conList))
        return results


def getAssertionAndValues(equation):
    assertion, values = equation.split(":")
    values = [int(v) for v in values.strip().split(" ")]
    return assertion,values