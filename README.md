# micropython-mock

A limited implementation of Python's `unittest.mock.Mock` for MicroPython.

## Installation

Install using mip:

```python
import mip
mip.install("github:planetinnovation/micropython-mock")
```

## Quick Start

```python
from micropython_mock import Mock

# Create a mock object
mock_obj = Mock()

# Use the mock
mock_obj.some_method("arg1", kwarg="value")
mock_obj.another_method()

# Check calls
assert mock_obj.some_method.called
assert mock_obj.some_method.call_count == 1
assert mock_obj.another_method.call_count == 1
```

## Features

This implementation provides a subset of Python's `unittest.mock.Mock` functionality suitable for MicroPython:

- `Mock()` - Create mock objects
- `.called` - Check if mock was called
- `.call_count` - Number of times mock was called
- `.call_args` - Arguments from the last call
- `.call_args_list` - List of all call arguments
- Method and attribute access creates new mocks automatically

## Examples

For more usage examples, see:
- [examples/example.py](examples/example.py)
- [test/test_micropython_mock.py](test/test_micropython_mock.py)

## License

MIT License - Copyright (c) 2025, Planet Innovation

## Contributing

Contributions are welcome! Please open an issue or pull request on GitHub.
