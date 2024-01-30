# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:41:28 2024

@author: zmagwebu
"""

"""
Storing data in Python
1. Lists
2.Dictionaries
3.Data frames - spe
"""

import pandas

file = pandas.read_csv("country_data.csv")

print(file)
"""

    Age Gender       Country
0    39      M  South Africa
1    25      M      Botswana
2    29      F  South Africa
3    46      M  South Africa
4    22      F         Kenya
5    35      F    Mozambique
6    22      F       Lesotho
7    49      M         Kenya
8    30      M         Kenya
9    40      F         Egypt
10   30      M         Sudan
"""

age1 = 30
age2 = 25
age3 = 22
"""
[30,25,29,46,22]
"""
print(age)
"""
age = [30,25,29,46,22]
"""
30
"""
print(age[0])

"""
22
"""
print(max(age))
print(sum(age))
prin(len(age))

# print(avg(age))
avg

country list

print(age)

"""
[30,25,29,46,22]
"""

print(age)
age.insert(0,100)
"""
"""
Dictionaries - key:value pairs
cat: "a cute animal"
"""


mammals = {"cat":"a cute animal", "lion":"king of the jungle", "elephant":"a gigantic herbivore"}
print(mammals["cat"])

