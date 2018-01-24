# Pip is python's package manager
# sudo easy_install pip
# PC: run Command Prompt as an admin 'easy_install pip'
# password: post
# to see if pip is installed - pip
# sudo pip install _______ <- package_name
	# Installs on your computer
# pip list

# pg 75
# numpy is fondation for many other packages like pandas
# ndaray = N dim array

import json
import numpy as np
a = np.array([1, 2.4, 'zoo', 3, 4, 5, 'other', 'another'])
print(a)
print(a.dtype)
print(a.ndim) # 1

print ("-" * 10)
b = np.array([[1, 2, 3, 4, 5, 6], [6, 7, 8, 9, 10, 11]])
print(b.ndim)
print(b.shape)
print(b.size)

# similar to lists arrays can be indexed and sliced
print ("-" * 10)
b = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(b[1]) # Nested array  #2
print(b[1][2]) # 0, 1, 2 position 2 of dim 1
print(b[1,2]) # same as above


# operations between equal-size arrays applies elementwise
# pg 92 list of functions 
print(b * b)

# numpy also handles date calcs
print(np.datetime64('2016-10-14') - np.datetime64('2016-10-01'))
print(np.datetime64('2005-02') + np.timedelta64(10, 'Y'))
