def decodeNumber(frase):
    code = ""
    for letter in frase:
        if letter in "-":
            code += "-"
        if letter in "1":
            code += "1"
        if letter in "ABC":
            code += "2"
        if letter in "DEF":
            code += "3"
        if letter in "GHI":
            code += "4"
        if letter in "JKL":
            code += "5"
        if letter in "MNO":
            code += "6"
        if letter in "PQRS":
            code += "7"
        if letter in "TUV":
            code += "8"
        if letter in "WXYZ":
            code += "9"

    return code


def test_decodeNumber_1():
    assert decodeNumber("1-HOME-SWEET-HOME") == "1-4663-79338-4663"


def test_decodeNumber_2():
    assert decodeNumber("MY-MISERABLE-JOB") == "69-647372253-562"
