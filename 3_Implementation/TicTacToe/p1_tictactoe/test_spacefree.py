from . import spacefree

b = [' ' for x in range(10)]
B = [' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def test_space_is_free():
    assert spacefree.space_is_free(b, 2) == True
    assert spacefree.space_is_free(B, 2) == False
