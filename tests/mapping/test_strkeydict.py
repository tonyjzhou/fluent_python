import unittest

from fluent_python.mapping.StrKeyDict import StrKeyDict


class StrKeyDictTest(unittest.TestCase):
    def test_get(self):
        skd = StrKeyDict({"a": 1, "b": 2})
        self.assertEqual(1, skd["a"])

    def test_get2(self):
        skd = StrKeyDict({"1": "a"})
        self.assertEqual("a", skd[1])

    def test_get_default(self):
        skd = StrKeyDict({"1": "a"})
        self.assertEqual("b", skd.get("2", "b"))


if __name__ == '__main__':
    unittest.main()
