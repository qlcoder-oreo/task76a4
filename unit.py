# !/usr/bin/env python
# encoding: utf-8
import unittest
import source


class mytest(unittest.TestCase):
    def test(self):
        self.assertEqual(source.f_285c6b5(1,2),10,'fail')
if __name__ == '__main__':
    unittest.main()