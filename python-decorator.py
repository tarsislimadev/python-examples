def a(fn):
  def b(*args, **kw):
    result = fn(*args, **kw)
    return result + 1
  return b

@a
def c(d, e):
  return d + e

print(f'1 + 1 = {c(1, 1)}?')
