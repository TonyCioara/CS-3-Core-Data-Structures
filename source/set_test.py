#!python

from set import Set
import unittest
# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class SetTest(unittest.TestCase):

    def test_init(self):
        s = Set()
        assert len(s.buckets) == 4
        assert s.length() == 0
        assert s.size == 0

    def test_length(self):
        s = Set()
        assert s.length() == 0
        s.add('I')
        assert s.length() == 1
        s.add('V')
        assert s.length() == 2
        s.add('X')
        assert s.length() == 3

    def test_items(self):
        s = Set()
        assert s.items() == []
        s.add('I')
        assert s.items() == [('I')]
        s.add('V')
        self.assertCountEqual(s.items(), [('I'), ('V')])
        s.add('X')
        self.assertCountEqual(s.items(), [('I'), ('V'), ('X')])

    def test_contains(self):
        s = Set()
        s.add('I', 1)
        s.add('V', 5)
        s.add('X', 10)
        assert s.contains('I') is True
        assert s.contains('V') is True
        assert s.contains('X') is True
        assert s.contains('A') is False

    def test_resize(self):
        s = Set()  # Set init_size to 2
        assert s.size == 0
        assert len(s.buckets) == 4
        assert s.load_factor() == 0
        s.add('I')
        assert s.size == 1
        assert len(s.buckets) == 4
        assert s.load_factor() == 0.25
        s.add('V')
        assert s.size == 2
        assert len(s.buckets) == 4
        assert s.load_factor() == 0.5
        s.add('X')
        assert s.size == 3
        assert len(s.buckets) == 4
        assert s.load_factor() == 0.75
        s.add('L')  # Should trigger resize
        assert s.size == 4
        assert len(s.buckets) == 8
        assert s.load_factor() == 0.5


if __name__ == '__main__':
    unittest.main()
