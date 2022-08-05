def posto(litros, combustivel):
    if combustivel == 'gasolina':
        if litros > 20:
            return litros * 2.5 - (litros * 2.5 * 0.05)
        else:
            return litros * 2.5 - (litros * 2.5 * 0.03)

    if combustivel == 'álcool':
        if litros > 20:
            return litros * 1.9 - (litros * 1.9 * 0.04)
        else:
            return litros * 1.9 - (litros * 1.9 * 0.06)