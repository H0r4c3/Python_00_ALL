'https://www.delftstack.com/howto/python/python-max-value-in-list/'

nst = [ [1001, 0.0009], [1005, 0.07682], [1201, 0.57894], [1677, 0.0977] ]

idx, max_value = max(nst, key=lambda item: item[1])

print('Maximum value:', max_value, "At index:", idx)