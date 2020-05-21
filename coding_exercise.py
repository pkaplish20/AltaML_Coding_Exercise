def get_coordinates(data):
    coordinates = []
    x, y = 0, 0
    orientation = "North"
    inputList = list(data)
    for i in inputList:   
        if i == 'L':
            if orientation == 'North':
                orientation = 'West'
            elif orientation == 'West':
                orientation = 'South'
            elif orientation == 'South':
                orientation = 'East'
            elif orientation == 'East':
                orientation = 'North'
        elif i == 'R':
            if orientation == 'North':
                orientation = 'East'
            elif orientation == 'East':
                orientation = 'South'
            elif orientation == 'South':
                orientation = 'West'
            elif orientation == 'West':
                orientation = 'North'
        elif i == 'F':
            if orientation == 'North':
                y = y+1
                coordinates.append((x, y))
            elif orientation == 'East':
                x = x+1
                coordinates.append((x, y))
            elif orientation == 'South':
                y = y-1
                coordinates.append((x, y))
            elif orientation == 'West':
                x = x-1
                coordinates.append((x, y))
    return coordinates, orientation
