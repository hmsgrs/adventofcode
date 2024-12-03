import os

reports = []
safe = 0

# Get the script to execute from .py location.
script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir, 'input.txt')

# Load data into a list of lists
with open(file_path,'r') as f:
    for line in f.readlines():
        reports.append([int(i) for i in line.split()])

#Part one, for loop: checking if reports are sorted, and if they are, if each value of the report changes at most by 3
for report in reports:
    if report == sorted(report) or report == sorted(report,reverse=True):
        is_safe = True
        for i in range(len(report)-1):
            if abs(report[i] - report[i+1]) >= 4 or report[i] == report[i+1] :
                is_safe = False
                break
        if is_safe:
            safe += 1

print(safe)

#Part two, allowing one "error" in the report.
safe_2 = 0
for report in reports:
    is_safe = True
    errors=0
    dir_change = 0
    dir_asc = None
    for i in range(len(report)-1):
        diff = report[i+1]-report[i]

        if diff == 0:
            current_dir = 0
            errors +=1


        if diff > 0:
            current_dir = 1

        elif diff < 0:
            current_dir = -1
        
        if dir_asc is None:
            dir_asc = current_dir
            

        if current_dir != 0 and current_dir != dir_asc:
            dir_asc = current_dir
            dir_change += 1

        if dir_change > 0:
            errors +=1

        if abs(diff) > 3:
            errors += 1


    if errors > 0:
        found_safe_after_removal = False

        for j in range(len(report)):
            test_report = report[:j] + report[j + 1:]  # Remove one element

            # Validate the new list
            valid = True
            dir_change = 0
            dir_asc = None

            for k in range(len(test_report) - 1):
                diff = test_report[k + 1] - test_report[k]
                if diff == 0:
                    valid = False  # No 2 equal values
                    break
                
                if abs(diff) > 3:  # Growth constraint check
                    valid = False
                    break

                # Ensure no direction change in the new list
                if k == 0:
                    dir_asc = 1 if diff > 0 else -1 if diff < 0 else 0
                elif (diff > 0 and dir_asc == -1) or (diff < 0 and dir_asc == 1):
                    valid = False  # Direction change is not allowed
                    break

            if valid:  # If the test_report is valid, it's safe after removal
                found_safe_after_removal = True
                break

        is_safe = found_safe_after_removal  # Mark as safe if valid after removal
    if is_safe:
            safe_2 += 1
    
 

print(safe_2)