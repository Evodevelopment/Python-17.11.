#example

import numpy as np

numpy1 = np.array([17.2, 20.0, 8.25, 9.50])
numpy2 = np.array([13.0, 24.0, 8.25, 9.0])

output = np.logical_and(numpy1 > 10, numpy2 < 20)
print(output)

#example1
import pandas as pd

datacamp = pd.DataFrame({
    'course': ['python', 'r', 'sql'],
    'level': ['advanced', 'intermediate', 'beginner'],
    'chapter': [1, 2, 3]
})

is_less = datacamp["chapter"] < 3
output = datacamp[is_less]

print(output)

#example2

datacamp = {
    'course': 'python',
    'level': 'intermediate',
    'lesson': {
        'dictionaries': 'python',
        'lists': 'r'
    }
}

print(datacamp.keys())
#output:
dict_keys(['course', 'level', 'lesson'])


