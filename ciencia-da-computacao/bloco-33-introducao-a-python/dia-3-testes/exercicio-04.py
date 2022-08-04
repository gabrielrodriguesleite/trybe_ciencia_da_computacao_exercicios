from exercicio03 import throws_at_bad_email


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
