def fibonacci(n):
  a = 0
  b = 1
  while a <= n:
    print(a)
    tempA = a
    a = b
    b = tempA + b



if __name__ == "__main__":
  fibonacci(int(input("Please enter a int number: ")))