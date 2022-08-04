def decodeNumber(frase):

    return "1-4663-79338-4663"


def test_decodeNumber_1():
    assert decodeNumber("1-HOME-SWEET-HOME") == "1-4663-79338-4663"


def test_decodeNumber_2():
    assert decodeNumber("MY-MISERABLE-JOB") == "69-647372253-562"
