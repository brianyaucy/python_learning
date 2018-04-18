def check_prime(check):
  for number in range(2, check):
    if check % number == 0:
      print(f"{check} is not a prime number.")
      break
  else:
    print(f"{check} is a prime number.")


def number_loop(upper):
  for number in range(1, upper+1):
    check_prime(number)


upper = int(input("Enter upper bound: "))
number_loop(upper)
