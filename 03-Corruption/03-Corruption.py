import re
import os


script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir, 'input.txt')





pattern = r'\bmul\((\d{1,3}),\s*(\d{1,3})\)'


with open(file_path,'r') as f:
    content = f.read()

    
    matches = re.findall(pattern, content)

    
    total_sum = sum(map(lambda match: int(match[0]) * int(match[1]), matches))

print(total_sum)



total_sum2 = 0
multy = True

with open(file_path, 'r') as f:
    content = f.read()

    for match in re.findall(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", content):
    
        if match == "do()":
            multy = True
    
        elif match == "don't()":
            multy = False
    
        elif multy : 
            x, y = map(int, match[4:-1].split(","))
            total_sum2 += x * y

        
print(total_sum2)
