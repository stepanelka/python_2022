numbers = pd.DataFrame({'A': [13, 2, 7, 9, 0], 'B': [6, 5, 8, 11, 10]})                                                                         #19
numbers['C'] = numbers[['A', 'B']].apply(lambda x: sum([t**2 for t in x]), axis = 1)