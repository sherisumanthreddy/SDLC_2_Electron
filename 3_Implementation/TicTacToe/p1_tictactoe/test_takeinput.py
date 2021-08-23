from . import takeinput
from . import mock
from . import builtins


def test_take_input():
    with mock.patch.object(builtins, 'input', lambda _: 'y'):
        assert takeinput.take_input() == 'y'
    with mock.patch.object(builtins, 'input', lambda _: 'n'):
        assert takeinput.take_input() == 'n'
