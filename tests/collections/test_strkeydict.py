import unittest

from fluent_python.collections.str_key_dict import StrKeyDict01, StrKeyDict


class StrKeyDictTest(unittest.TestCase):
    def test_get_01(self):
        skd = StrKeyDict01({"a": 1, "b": 2})
        self.assertEqual(1, skd["a"])

    def test_get2_01(self):
        skd = StrKeyDict01({"1": "a"})
        self.assertEqual("a", skd[1])

    def test_get_default_01(self):
        skd = StrKeyDict01({"1": "a"})
        self.assertEqual("b", skd.get("2", "b"))

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
