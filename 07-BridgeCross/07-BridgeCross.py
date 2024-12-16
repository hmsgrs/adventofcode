import os

script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir, 'input.txt')

total = 0
total_2=0

def validate(value,operators):
    if len(operators)==1: return value == operators[0]
    if value % operators[-1] == 0 and validate(value // operators[-1],operators[:-1]): return True
    if value > operators[-1] and validate(value - operators[-1],operators[:-1]): return True
    return False

def validate_2(value,operators):
    if len(operators)==1: return value == operators[0]
    if value % operators[-1] == 0 and validate_2(value // operators[-1],operators[:-1]): return True
    if value > operators[-1] and validate_2(value - operators[-1],operators[:-1]): return True
    str_value = str(value)
    str_operator = str(operators[-1])
    if len(str_value)>len(str_operator) and str_value.endswith(str_operator) and validate_2(int(str_value[:-len(str_operator)]), operators[:-1]): return True
    return False

for line in open(file_path):
    left, right = line.split(": ")
    value = int(left)
    operators = [int(x) for x in right.split()]
    if validate(value,operators):
        total += value
    if validate_2(value,operators):
        total_2 += value

print(total)
print(total_2)