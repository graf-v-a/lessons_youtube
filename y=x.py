# # y = 25 + x
# y = int(input("Enter a number: "))
# for x in range(-100, 100):
#     if y == 25 + x:
#         print(f"y = {y} and x = {x}")
#         break
# else:
#     print("No solution found")

# x**x + 2*x + 3*x*y + 5 = N
result = False
N = int(input("Enter a number: "))
for x in range(-100, 100):
    for y in range(-100, 100):
        if x**x + 2*x + 3*x*y + 5 == N:
            print(f"{x} ** {x} + 2 * {x} + 3 * {x} * {y} + 5 = {N}")
            break
print(f"{x} ** {N}")
