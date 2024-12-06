import os

script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir, 'input.txt')


with open(file_path,'r') as f:
    
    rules = [[int(rule) for rule in line.strip().split("|")] for line in f if "|" in line]
    f.seek(0)
    updates = [[int(update) for update in line.split(",")] for line in f if "," in line]

#print(rules[:5])
#print(updates[:5])

correct_updates = []

for update in updates:
    in_order = True
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                in_order = False
    if in_order:
        correct_updates.append(update)
print(correct_updates[:5])
#print(len(correct_updates))

result = 0

for update in correct_updates:
    result+= update[len(update)//2]

print(result)
            
