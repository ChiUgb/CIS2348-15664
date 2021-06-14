# Chiamaka Ugbaja
# hw 3.19

import math
wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input('Enter wall width (feet):\n'))
wall_area = wall_height * wall_width # calculating area
print('Wall area:', wall_area, 'square feet')
print('Paint needed:', '{:.2f}'.format(wall_area/350), 'gallons') # format answer to 2 decimal places (conversion)
print('Cans needed:', math.ceil(wall_area/350), 'can(s)\n') # rounding up for can needed


paint = {'red': 35, 'blue': 25, 'green': 23}
pick_paint = input('Choose a color to paint the wall:\n')
chosen = math.ceil(wall_area/350) * paint[pick_paint] # choosing color and price, accounting for quantity as well
print('Cost of purchasing', pick_paint, 'paint: $' + str(chosen))
