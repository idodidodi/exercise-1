def add_numbers(a,b):
  return a + b

def multiply(a,b):
  return a * b

def divide(a,b):
  return b / a
  
def run():
  first = 7
  second = 44.3
  print(add_numbers(first, second))
  print(multiply(first, second))
  print(divide(first, second))

# run()

def run_b():
  a = 8
  a = 17
  a = 9
  b = 6
  c = a + b
  b = c + a
  b = 8
  print(a)
  print(b)
  print(c)

# run_b()


def run_c():
  a = 8
  b = "17"
  print(a + int(b))

run_c()
