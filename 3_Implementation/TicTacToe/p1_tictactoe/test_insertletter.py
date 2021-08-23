import insertletter


B = [' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
B1 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x']


def test_insert_letter():
    b = [' ' for x in range(10)]
    assert insertletter.insert_letter(b, 'x', 2) == B
    b = [' ' for x in range(10)]
    assert insertletter.insert_letter(b, 'x', 9) == B1
