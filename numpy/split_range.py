'https://newbedev.com/typescript-split-range-into-equal-parts-python-code-example'

import numpy

r = range(25)

l = numpy.array_split(numpy.array(r), 6)
print(l)