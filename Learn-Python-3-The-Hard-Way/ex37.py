assert 1 == 1, "This is error"

for i in range(1, 5):
    if i == 3:
        print("Continue here, default message that i == 3 won't be printed")
        continue
    print(f"End of the loop, i = {i}")

try:
    1 / 0
except:
    print("You cannot divide by zero!")

print_name = lambda name: print(f"Hello, {name}")

print_name("Geralt")


b = 1
# if b == 1:
    # raise ValueError("No")
