import shelve

filename = 'shelve_file.db'

# write file
with shelve.open(filename) as file1:
  file1['a'] = 'a'
  file1['a1'] = 'a1'

# read file
with shelve.open(filename) as file2:
  print('a', file2['a'])
  print('a1', file2['a1'])
