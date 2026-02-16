import unittest

from micropython_mock import Mock


class TestMock(unittest.TestCase):
    def test_return_value(self):
        mock = Mock(return_value=1)

        self.assertEqual(mock(), 1)
        self.assertEqual(mock(), 1)

        mock.send.return_value = 2

        self.assertEqual(mock.send(), 2)
        self.assertEqual(mock.send(), 2)

    def test_side_effect(self):
        mock = Mock(side_effect=[1, 2, 3])

        self.assertEqual(mock(), 1)
        self.assertEqual(mock(), 2)
        self.assertEqual(mock(), 3)

        mock.send.side_effect = [4, 5]

        self.assertEqual(mock.send(), 4)
        self.assertEqual(mock.send(), 5)

    def test_assert_called_with(self):
        mock = Mock()

        mock(1)
        mock.assert_called_with(1)

        mock(1, 2)
        mock.assert_called_with(1, 2)

        mock(1, 2, a=1)
        mock.assert_called_with(1, 2, a=1)

        mock(1, 2, a=1, b=2)
        mock.assert_called_with(1, 2, a=1, b=2)

        mock.send("x", "y")
        mock.send.assert_called_with("x", "y")

    def test_assert_called_with_assertion_error(self):
        mock = Mock()

        mock()
        with self.assertRaises(AssertionError):
            mock.assert_called_with(1)

    def test_reset(self):
        mock = Mock(side_effect=[1, 2, 3])

        self.assertEqual(mock(), 1)
        self.assertEqual(mock(), 2)

        mock.send.side_effect = [4, 5]

        self.assertEqual(mock.send(), 4)
        self.assertEqual(mock.send(), 5)

        mock.reset()

        self.assertEqual(mock(), 1)
        self.assertEqual(mock(), 2)
        self.assertEqual(mock(), 3)
        self.assertEqual(mock.send(), 4)
        self.assertEqual(mock.send(), 5)

    def test_called(self):
        mock = Mock()

        self.assertFalse(mock.called)

        mock()
        self.assertTrue(mock.called)

        mock.some_method()
        self.assertTrue(mock.some_method.called)

    def test_call_count(self):
        mock = Mock()

        self.assertEqual(mock.call_count, 0)

        mock()
        self.assertEqual(mock.call_count, 1)

        mock()
        self.assertEqual(mock.call_count, 2)

        mock.some_method("arg1", kwarg="value")
        self.assertEqual(mock.some_method.call_count, 1)

        mock.another_method()
        self.assertEqual(mock.another_method.call_count, 1)


if __name__ == "__main__":
    unittest.main()
