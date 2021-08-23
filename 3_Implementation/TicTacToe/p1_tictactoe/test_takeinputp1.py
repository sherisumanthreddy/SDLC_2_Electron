import takeinput
import mock
import builtins


def test_take_input():
    with mock.patch.object(builtins, 'input', lambda _: 'y'):
        assert takeinput.take_input() == 'y'
    with mock.patch.object(builtins, 'input', lambda _: 'n'):
        assert takeinput.take_input() == 'n'
