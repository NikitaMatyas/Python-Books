def test(j, n):
    i = 0
    while i < j:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += n
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


numbers = []
test(20, 2)
print("The numbers: ")
for num in numbers:
    print(num)
