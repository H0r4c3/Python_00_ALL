import pandas as pd
import numpy as np

s1 = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
print(s1)

s2 = pd.Series([22, 35, 58], name="Age")
print(s2)

# df = pd.DataFrame(np.random.randn(5, 3), index=["a", "b", "c", "d", "e"], columns=["A", "B", "C"])
# print(np.random.randn(5, 3))
# print(df)

my_list = [[11, 12, 13], [21, 22, 23], [31, 32, 33], [41, 42, 43], [51, 52, 53]]
print(my_list)
df = pd.DataFrame(my_list, index=["a", "b", "c", "d", "e"], columns=["A", "B", "C"])
print(df)

