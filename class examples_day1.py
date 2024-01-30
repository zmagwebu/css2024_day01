# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 15:55:17 2024

@author: zmagwebu
"""
import pandas as pd
mammals = {"cat":"a cute animal", "lion":"king of the jungle", "elephant":"a gigantic herbivore"}
print(mammals["cat"])

fruits = ["apple", "banana", "orange", "grape", "kiwi"]

size_nm = [9.8, 10.1, 13.2, 8.7, 20.5]

fruit_sizes = {'fruits':fruits,'sizes':size_nm}

df= pd.DataFrame(fruit_sizes)

print(df['fruits'])

prices = [10.00, 12.50, 16.00, 23.00, 7.00]

df['prices'] = prices