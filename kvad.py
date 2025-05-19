numbers = int(input())
result = 0
for i in range(numbers):
    n = int(input())
    if n % 2 == 1:
        result += n
print(result)