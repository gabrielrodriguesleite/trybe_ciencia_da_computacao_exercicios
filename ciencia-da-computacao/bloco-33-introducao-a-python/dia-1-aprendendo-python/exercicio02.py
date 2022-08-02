def media(arr):
    n = 0
    for i in arr:
        n += i / len(arr)

    return n


print(
    f"""A média entre os números 5, 10, 15, 20, 50 é: \
{media([5, 10, 15, 20, 50])}"""
)
