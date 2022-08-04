def validEmail(email):
    """Valida endereço de email com o formato
    nomeusuario@nomewebsite.extensao
    """
    user = email.split("@")[0]
    site = email.split("@")[1].split(".")[0]
    exte = email.split(".")[1]

    # O nome de usuário deve conter somente letras, dígitos, traços e \
    # underscores (_)
    for letter in user:
        if letter not in "-_" or not letter.isalpha():
            return False

    # O nome de usuário deve iniciar com uma letra;
    if not user[0].isalpha():
        return False

    # O nome do website deve conter somente letras e dígitos;
    for letter in site:
        if not letter.isalpha() or not letter.isdigit():
            return False

    # O tamanho máximo da extensão é de 3 caracteres.
    if len(exte) > 3:
        return False

    return True


def test_validEmail_1():
    # email
    # try:
    #   break
    # except ValueError:
    #     print(email)
    assert 1 == 1
