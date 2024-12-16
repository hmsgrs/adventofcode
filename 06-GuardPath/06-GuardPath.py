import os

script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir, 'input.txt')


with open(file_path,'r') as f:
    site_map = []
    lines= [line.strip() for line in f.readlines()]
    for line in lines:
        site_map.append(list(line))

play_map = site_map
inside = True
pointers = {'<':[0,-1],'^':[-1,0],'>':[0,1],'v':[1,0]}
pointer_keys = list(pointers.keys())
current_pointer = 0

def find_pointer(grid, targets):
    coordinates = []  
    for row_index, row in enumerate(grid):
        for col_index, char in enumerate(row):
            if char in targets.keys():
                coordinates.append([row_index, col_index,char])

    return coordinates

def status(grid):
    site_map=grid
    origin_x,origin_y,char = find_pointer(site_map,pointers)[0]
    pointing=pointers.get(char)
    position=[origin_x,origin_y]
    next_row = origin_x + pointers.get(char)[0]
    next_col = origin_y + pointers.get(char)[1]
    
    return origin_x, origin_y,next_row,next_col,pointing,char
    
def walk(origin_x,origin_y,next_row,next_col,pointing,char):
    next_position = [next_row,next_col]
    new_position = []
    global current_pointer
    global pointer_keys
    global inside
    print(next_position)
    if 0 <= next_row < len(play_map) and 0 <= next_col < len(play_map[0]):
        
        if play_map[next_position[0]][next_position[1]] == '#':
            print(f'next position "{next_row},{next_col}" inside play map!')
            print('But it is a boulder! turning right!')
            current_pointer = (current_pointer + 1) % len(pointer_keys)
            play_map[origin_x][origin_y]= pointer_keys[current_pointer]
        else:
            new_position = [next_row,next_col]
            play_map[origin_x][origin_y]='X'
            play_map[new_position[0]][new_position[1]]= char
    else:
        print ('Out of bounds!')
        inside = False

    return new_position

while inside:
    walk(*status(play_map))

count = 1
for row in play_map:
    count += row.count('X')

print (count)