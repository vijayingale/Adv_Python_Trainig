import unittest

# python -m unittest test_module test_upper
# python -m unittest testmodule.Testcase
# python -m unittest testmodule.Testclass.test
class Testexample(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('ander'.upper(),"ANDER")

    def test_isupper(self):
        self.assertTrue('ANDRE'.isupper())
        self.assertFalse('ander'.isupper())

    def test_spit(self):
        s= "hello world"
        self.assertEqual(s.split(),['hello' , 'world'])


if __name__ == "__main__":
    unittest.main()
