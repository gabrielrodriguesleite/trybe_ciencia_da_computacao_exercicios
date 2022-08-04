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
        if letter not in "-_" and not letter.isalpha():
            return False

    # O nome de usuário deve iniciar com uma letra;
    if not user[0].isalpha():
        return False

    # O nome do website deve conter somente letras e dígitos;
    for letter in site:
        if not letter.isalpha() and not letter.isdigit():
            return False

    # O tamanho máximo da extensão é de 3 caracteres.
    if len(exte) > 3:
        return False

    return True


def throws_at_bad_email(email):
    if not validEmail(email):
        raise ValueError


def validate_emails(email_arr):
    valid = []
    for email in email_arr:
        try:
            throws_at_bad_email(email)
            valid.append(email)
            continue
        except ValueError as e:
            print(e)

    return valid


def test_validEmail_1():
    assert validEmail("nome@dominio.com") is True
    assert validEmail("errad#@dominio.com") is False
    assert validEmail("outro@dominio.com") is True


def test_valid_email_array():
    assert validate_emails(
        ["nome@dominio.com", "errad#@dominio.com", "outro@dominio.com"]
    ) == ["nome@dominio.com", "outro@dominio.com"]


if __name__ == "__main__":
    print(
        validate_emails(
            ["nome@dominio.com", "errad#@dominio.com", "outro@dominio.com"]
        )
    )
