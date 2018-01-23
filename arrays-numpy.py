# Pip is python's package manager
# sudo easy_install pip
# PC: run Command Prompt as an admin 'easy_install pip'
# password: post
# to see if pip is installed - pip
# sudo pip install _______ <- package_name
	# Installs on your computer
# pip list

import json
import numpy as np
a = np.array([1, 2.4, 'zoo', 3, 4, 5, 'other', 'another'])
print a
print a.dtype
print a.ndim # 1

b = np.array([[1, 2, 3, 4, 5, 6], [6, 7, 8, 9, 10, 11]])
print b.ndim
print b.shape
print b.size

b = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print b[1] # Nested array  #2
print b[1][2] # 0, 1, 2

#print np.datetime64('2016-10-14') - np.datetime64('2016-10-01')
#print np.datetime64('2005-02') + np.timedelta64(10, 'Y')
