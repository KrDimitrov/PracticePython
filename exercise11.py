_input = int(input("Enter a number: "))

_range = range(2, _input)

isprime = 1
for i in _range:
    if _input%i == 0:
        isprime = 0
        break
print("The number is Prime!") if isprime==1 else print("The number is not Prime!")



