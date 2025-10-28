import constants as c
## Checks that all tiles within a 3 by 3 radius is buildable

def checkBorder(array, x, y):
    movement = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            else:
            
                movement.append((i,j))
    
    
    for dx, dy in movement:
        newX = x + dx
        newY = y + dy

        tileIndex = newX + c.COLS * newY 

        if tileIndex >= len(array) or array[tileIndex] != 18: # 18 is the value of buildable tiles
            return False
    return True