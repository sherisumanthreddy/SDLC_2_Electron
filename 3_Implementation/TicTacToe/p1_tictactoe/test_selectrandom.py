import selectrandom

list_exp = [1, 3, 7, 9]


def sel_rand():
    a = selectrandom.select_random(list_exp)
    if a in [1, 3, 7, 9]:
        return 1
    else:
        return 0


def test_select_random():
    assert sel_rand() == 1
