decimal = int(input("십진수 입력:"))
result = ""
while decimal != 0:
    remainder = decimal % 2
    result = str(remainder) + result
    decimal //= 2

print(result)
