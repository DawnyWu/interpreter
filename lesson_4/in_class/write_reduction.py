# Writing Reductions

# We are looking at chart[i] and we see x => ab . cd from j.

# Hint: Reductions are tricky, so as a hint, remember that you only want to do
# reductions if cd == []

# Hint: You'll have to look back previously in the chart.

def reductions(chart, i, x, ab, cd, j):
    pass


# Insert code here!



chart = {0: [('exp', ['exp'], ['+', 'exp'], 0), ('exp', [], ['num'], 0), ('exp', [], ['(', 'exp', ')'], 0),
             ('exp', [], ['exp', '-', 'exp'], 0), ('exp', [], ['exp', '+', 'exp'], 0)],
         1: [('exp', ['exp', '+'], ['exp'], 0)], 2: [('exp', ['exp', '+', 'exp'], [], 0)]}

print reductions(chart, 2, 'exp', ['exp', '+', 'exp'], [], 0) == [('exp', ['exp'], ['-', 'exp'], 0),
                                                                  ('exp', ['exp'], ['+', 'exp'], 0)]