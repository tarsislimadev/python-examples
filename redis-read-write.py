# docker run --name redis1 -d -p 6379:6379 redis

import redis

r = redis.Redis(host='localhost', port=6379, db=0)

r.set('username', 'tarsislimadev')

value = r.get('username')

print(value.decode('utf-8'))
