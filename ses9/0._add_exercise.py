import datetime


def decorator(func):
  def inner(*args, **kwargs):
    f = open('log.txt', 'a')
    f.write(datetime.datetime.now().strftime("%c")) #lille %c er et valg. kan finde alle valgmuligheder på bl.a. w3schools
    f.write(' : ')
    f.write(str(func(*args)))
    f.write('\n')
    f.close
    return func(*args, **kwargs)
  return inner

@decorator
def add(*args):
  sum = 0

  for i in args:
    sum += i
  return sum

print(add(1, 2, 3))
