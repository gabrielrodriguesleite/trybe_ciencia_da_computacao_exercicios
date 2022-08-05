

def triang(num):
    for i in range(num):
        print('*'*(i+1))


def test_triang(capsys):
    triang(5)
    captured = capsys.readouterr()
    assert captured.out == """\
*
**
***
****
*****
"""
        
        