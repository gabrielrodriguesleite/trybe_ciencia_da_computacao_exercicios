def latasEpreco(metrosQ):
    litros = metrosQ / 3
    latas = litros / 18
    preco = latas * 80
    return (latas, preco)


print("%d lata(s) ao valor total de R$%d pra pintar 54m²" % latasEpreco(108))
