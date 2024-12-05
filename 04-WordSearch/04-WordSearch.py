import os
from itertools import product

script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir, 'input.txt')

data = []
xmas = ["X","M","A","S"]
result = 0

with open(file_path,'r') as f:
    
    data = [list(line.strip()) for line in f]

succ= 0


for i in range(len(data)):
    for j in range(len(data[0])):
        if i < 3:
            if j < 4:
                condition_1= True
                condition_2= True
                condition_3= True
                for k in range(4):
                    if data[i][j+k] != xmas[k]:
                        condition_1= False
                        
                
                    if data[i+k][j] != xmas[k]:
                        condition_2= False
                        

                    if data[i+k][j+k] != xmas[k]:
                        condition_3= False
                        
                if condition_1:
                    succ += 1
                if condition_2:
                    succ += 1
                if condition_3:
                    succ += 1
            if j > 3 and j < (len(data[0])-3):
                
                condition_1= True
                condition_2= True
                condition_3= True
                condition_4= True
                condition_5= True

                for k in range(4):
                    if data[i][j+k] != xmas[k]:
                        condition_1= False
                        
                    if data[i+k][j+k] != xmas[k]:
                        condition_2= False
                        
                    if data[i+k][j] != xmas[k]:
                        condition_3= False
                        

                    if data[i+k][j-k] != xmas[k]:
                        condition_4= False
                        

                    if data[i][j-k] != xmas[k]:
                        condition_5= False
                           
                if condition_1:
                    succ += 1
                if condition_2:
                    succ += 1
                if condition_3:
                    succ += 1
                if condition_4:
                    succ += 1
                if condition_5:
                    succ += 1
            if j > (len(data[0])-4):   

                condition_1= True
                condition_2= True
                condition_3= True

                for k in range(4):
                    
                    if data[i+k][j] != xmas[k]:
                        condition_1= False

                    if data[i+k][j-k] != xmas[k]:
                        condition_2= False

                    if data[i][j-k] != xmas[k]:
                        condition_3= False   

                if condition_1:
                    succ += 1
                if condition_2:
                    succ += 1
                if condition_3:
                    succ += 1

        if i > 2 and i < len(data)-3:
            if j < 3:
                condition_1= True
                condition_2= True
                condition_3= True
                condition_4= True
                condition_5= True
                
                for k in range(4):
                    if data[i][j+k] != xmas[k]:
                        condition_1= False
                
                    if data[i+k][j] != xmas[k]:
                        condition_2= False

                    if data[i+k][j+k] != xmas[k]:
                        condition_3= False

                    if data[i-k][j] != xmas[k]:
                        condition_4= False

                    if data[i-k][j+k] != xmas[k]:
                        condition_5= False
                if condition_1:
                    succ += 1
                if condition_2:
                    succ += 1
                if condition_3:
                    succ += 1
                if condition_4:
                    succ += 1
                if condition_5:
                    succ += 1
            if j > 2 and j < (len(data[0])-3):
                condition_1= True
                condition_2= True
                condition_3= True
                condition_4= True
                condition_5= True
                condition_6= True
                condition_7= True
                condition_8= True
                for k in range(4):
                        if data[i][j+k] != xmas[k]:
                            condition_1= False
                    
                        if data[i][j-k] != xmas[k]:
                            condition_2= False

                        if data[i+k][j] != xmas[k]:
                            condition_3= False

                        if data[i+k][j+k] != xmas[k]:
                            condition_4= False

                        if data[i+k][j-k] != xmas[k]:
                            condition_5= False

                        if data[i-k][j] != xmas[k]:
                            condition_6= False

                        if data[i-k][j+k] != xmas[k]:
                            condition_7= False

                        if data[i-k][j-k] != xmas[k]:
                            condition_8= False
                if condition_1:
                    succ += 1
                if condition_2:
                    succ += 1
                if condition_3:
                    succ += 1
                if condition_4:
                    succ += 1
                if condition_5:
                    succ += 1
                if condition_6:
                    succ += 1
                if condition_7:
                    succ += 1
                if condition_8:
                    succ += 1
            if j > (len(data[0])-4):
                condition_1= True
                condition_2= True
                condition_3= True
                condition_4= True
                condition_5= True

                for k in range(4):
                    
                    if data[i+k][j] != xmas[k]:
                        condition_1= False

                    if data[i+k][j-k] != xmas[k]:
                        condition_2= False

                    if data[i][j-k] != xmas[k]:
                        condition_3= False
                    if data[i-k][j-k] != xmas[k]:
                        condition_4= False
                    if data[i-k][j] != xmas[k]:
                        condition_5= False

                if condition_1:
                    succ += 1
                if condition_2:
                    succ += 1
                if condition_3:
                    succ += 1   
                if condition_4:
                    succ += 1
                if condition_5:
                    succ += 1 

        if i > len(data)-4:
            if j < 3:
                condition_1= True
                condition_2= True
                condition_3= True
                for k in range(4):
                    if data[i][j+k] != xmas[k]:
                        condition_1= False
                
                    if data[i-k][j] != xmas[k]:
                        condition_2= False

                    if data[i-k][j+k] != xmas[k]:
                        condition_3= False

                if condition_1:
                    succ += 1
                if condition_2:
                    succ += 1
                if condition_3:
                    succ += 1
            if j > 2 and j < (len(data[0])-3):
                condition_1= True
                condition_2= True
                condition_3= True
                condition_4= True
                condition_5= True

                for k in range(4):
                    if data[i][j+k] != xmas[k]:
                        condition_1= False
                
                    if data[i-k][j] != xmas[k]:
                        condition_2= False

                    if data[i-k][j+k] != xmas[k]:
                        condition_3= False

                    if data[i-k][j-k] != xmas[k]:
                        condition_4= False

                    if data[i][j-k] != xmas[k]:
                        condition_5= False       
                if condition_1:
                    succ += 1
                if condition_2:
                    succ += 1
                if condition_3:
                    succ += 1
                if condition_4:
                    succ += 1
                if condition_5:
                    succ += 1
            if j > (len(data[0])-4):
                condition_1= True
                condition_2= True
                condition_3= True

                for k in range(4):
                    if data[i][j-k] != xmas[k]:
                        condition_1= False
                
                    if data[i-k][j] != xmas[k]:
                        condition_2= False

                    if data[i-k][j-k] != xmas[k]:
                        condition_3= False
                if condition_1:
                    succ += 1
                if condition_2:
                    succ += 1
                if condition_3:
                    succ += 1

print(succ)
