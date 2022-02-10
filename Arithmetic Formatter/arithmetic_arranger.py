def arithmetic_arranger(problems, val=False):
    arranged_problems = ''
    if len(problems) > 5:
        arranged_problems = "Error: Too many problems."
        return arranged_problems

    
    operations = list(map(lambda x: x.split()[1], problems))
    if set(operations) != {'+', '-'} and len(set(operations)) != 2:
        arranged_problems = "Error: Operator must be '+' or '-'."
        return arranged_problems

    numbers = []  
    for problem in problems:
        p = problem.split()
        numbers.extend([p[0], p[2]])

    if not all(map(lambda x: x.isdigit(), numbers)):
        arranged_problems = "Error: Numbers must only contain digits."
        return arranged_problems

    if not all(map(lambda x: len(x) < 5, numbers)):
        arranged_problems = "Error: Numbers cannot be more than four digits."
        return arranged_problems

    top_row = ''
    dashes = ''
    values = list(map(lambda x: eval(x), problems))
    solutions = ''
    for problem in range(0, len(numbers), 2):
        space_width = max(len(numbers[problem]), len(numbers[problem+1])) + 2
        top_row += numbers[problem].rjust(space_width)
        dashes += '-' * space_width
        solutions += str(values[problem // 2]).rjust(space_width)
        if problem != len(numbers) - 2:
            top_row += ' ' * 4
            dashes += ' ' * 4
            solutions += ' ' * 4

    bottom_row = ''
    for problem in range(1, len(numbers), 2):
        space_width = max(len(numbers[problem - 1]), len(numbers[problem])) + 1
        bottom_row += operations[problem // 2]
        bottom_row += numbers[problem].rjust(space_width)
        if problem != len(numbers) - 1:
            bottom_row += ' ' * 4

    if val:
        arranged_problems = '\n'.join((top_row, bottom_row, dashes, solutions))
    else:
        arranged_problems = '\n'.join((top_row, bottom_row, dashes))
    return arranged_problems