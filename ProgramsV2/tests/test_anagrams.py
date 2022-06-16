import unittest
from ProgramsV2.apps import reverse_words


class TestAnagramModule(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(reverse_words("absd jkl"), "dsba lkj")

    def test_symbol(self):
        self.assertEqual(reverse_words("!&4azh8 (abcl)"), "!&4hza8 (lcba)")

    def test_empty(self):
        self.assertEqual(reverse_words(""), "")

    def test_number(self):
        with self.assertRaises(ValueError):
            reverse_words(8)


if __name__ == '__main__':
    unittest.main()
