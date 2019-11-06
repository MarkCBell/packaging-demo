
from soln import get_way_count

for bounce in [11, 1000001, 12017639147]:
    print('There are {} rays with {} bounces'.format(get_way_count(bounce), bounce))

