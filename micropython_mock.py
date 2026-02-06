# MIT license; Copyright (c) 2025, Planet Innovation
# 436 Elgar Road, Box Hill, 3128, VIC, Australia
# Phone: +61 3 9945 7510
#


class call:
    """
    A very limited implementation of Python's unittest.mock.call.
    """

    def __init__(self, name: str, args, kargs) -> None:
        self.name = name
        self.args = args
        self.kwargs = kargs

    def __repr__(self) -> str:
        return f"call(name={self.name}, args={self.args}, kwargs={self.kwargs})"


class Mock:
    """
    A limited implementation of Python's unittest.mock.Mock.

    Args:
        return_value: The value to return when the mock is called.
        side_effect: The series of values to return when the mock is called.
            This has higher priority than return_value.
        kwargs: Other attributes and their values to set to the mock.

    Attributes:
        return_value: As above.
        side_effect: As above.
        mock_calls: A list of all calls made by the mock.
    """

    def __init__(self, return_value=None, side_effect=None, **kwargs) -> None:
        self.return_value = return_value
        self.side_effect = side_effect
        self.mock_calls: list[call] = []

        self._dict = {}  # __dict__ is readonly in micropython
        self._side_effect_count = 0

        for key, value in kwargs.items():
            self._dict[key] = value

    def assert_called_with(self, *args, **kwargs) -> None:
        """
        Assert the last call was called with the given arguments and keyword arguments.

        Raises:
            AssertionError: If the assertion fails.
        """
        if self.mock_calls[-1].args != args or self.mock_calls[-1].kwargs != kwargs:
            raise AssertionError

    def reset(self) -> None:
        """
        Reset the mock to its initial state.
        """
        self.mock_calls = []
        self._side_effect_count = 0
        for key, value in self._dict.items():
            if isinstance(value, Mock):
                value.reset()

    def __call__(self, *args, **kwargs):
        # TODO(pxp): Need to store the copied value of args/kwargs; otherwise,
        # values may change before asserting.
        self.mock_calls.append(call("", args, kwargs))

        if self.side_effect is not None:
            side_effect = self.side_effect[self._side_effect_count]
            self._side_effect_count += 1

            if isinstance(side_effect, Exception):
                raise side_effect

            return side_effect

        if self.return_value is not None:
            return self.return_value

        return Mock()

    def __getattr__(self, name: str):
        if name not in self._dict:
            self._dict[name] = Mock()

        return self._dict[name]
