def arithmetic_formatter(problems, show_answers=False):
    first_line = ''
    second_line = ''
    dash_line = ''
    answer_line = ''

    if len(problems) > 5:
        return 'Error: Too many problems.'
        
    for problem in problems: 
        parts = problem.split() # -> parts[0] +/- parts[2]
        if parts[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        elif not parts[0].isdigit() or not parts[2].isdigit():
            return 'Error: Numbers must only contain digits.'
        elif len(parts[0]) > 4 or len(parts[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        length = max(len(parts[0]), len(parts[2])) + 2
        first_line += parts[0].rjust(length) + '    ' # -> 4 spaces
        second_line += parts[1] + parts[2].rjust(length-1) + '    ' # -> 4 spaces
        dash_line += '-' * length + '    ' # -> 4 spaces

        #calculate the answer
        if parts[1] == '+':
            result = str(int(parts[0]) + int(parts[2]))
        else:
            result = str(int(parts[0]) - int(parts[2]))
        answer_line += result.rjust(length) + '    '

    #combine
    arranged_problems = first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + dash_line.rstrip()
    
    #check result (optional argument)
    if show_answers == True:
        arranged_problems += '\n' + answer_line.rstrip()
    return arranged_problems

N = input("Insert your problems here (comma-separated): ")
# convert the input string into a list of problem strings
problems = [p.strip() for p in N.split(',') if p.strip()]
print(arithmetic_formatter(problems, True))