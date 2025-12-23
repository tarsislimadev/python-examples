with open('./data/demofile.txt', 'w') as f:
  f.write('Inserting the content! ')

with open('./data/demofile.txt', 'w') as f:
  f.write('Woops! We have deleted the content! ')

with open('./data/demofile.txt', 'a') as f:
  f.write('But we appended this...')

with open('./data/demofile.txt') as f:
  print(f.read())
