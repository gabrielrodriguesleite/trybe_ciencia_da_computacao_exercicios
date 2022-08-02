def maiorNome(arr):
    n = ""
    for i in arr:
        if len(i) > len(n):
            n = i

    return n


print(
    f'O maior nome entre José, Lucas, Nádia, Fernanda, Cairo, Joana é: \
{maiorNome(["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"])}'
)
