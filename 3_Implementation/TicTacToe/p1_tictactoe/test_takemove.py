import takemove
import mock
import builtins


def test_take_move():
    with mock.patch.object(builtins, 'input', lambda _: 2):
        assert takemove.take_move() == 2
