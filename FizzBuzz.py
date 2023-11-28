# function
def fizzbuzz(n):
  list = []
  for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
      list.append("FizzBuzz")
    elif i % 3 == 0:
      list.append("Fizz")
    elif i % 5 == 0:
      list.append("Buzz")
    else:
      list.append(i)
  return list
  


print(fizzbuzz(24))
# [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz', 'Fizz', 22, 23, 'Fizz']
