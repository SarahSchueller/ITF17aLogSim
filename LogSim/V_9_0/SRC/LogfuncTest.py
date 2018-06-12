# -*- coding: utf8 -*-
import unittest
from Logfunc import AndGate, OrGate, XOrGate, NAndGate, NOrGate, NotGate, HalfAdder, FullAdder


class AndGateTest(unittest.TestCase):
    def testcase_00(self):
        a = AndGate(2)
        self.assertEqual(False, a.get_input(0), "Class AndGate Testcase 0 failed.")
        self.assertEqual(False, a.get_input(1), "Class AndGate Testcase 0 failed.")
        self.assertEqual(False, a.get_output(0), "Class AndGate Testcase 0 failed.")

    def testcase_01(self):
        a = AndGate(2)
        a.set_input(0, False)
        a.set_input(1, False)
        a.execute()
        self.assertEqual(False, a.get_output(0), "Class AndGate Testcase 1 failed.")

    def testcase_02(self):
        a = AndGate(2)
        a.set_input(0, False)
        a.set_input(1, True)
        a.execute()
        self.assertEqual(False, a.get_output(0), "Class AndGate Testcase 2 failed.")

    def testcase_03(self):
        a = AndGate(2)
        a.set_input(0, True)
        a.set_input(1, False)
        a.execute()
        self.assertEqual(False, a.get_output(0), "Class AndGate Testcase 3 failed.")

    def testcase_04(self):
        a = AndGate(2)
        a.set_input(0, True)
        a.set_input(1, True)
        a.execute()
        self.assertEqual(True, a.get_output(0), "Class AndGate Testcase 4 failed.")

    def testcase_05(self):
        a = AndGate(3)
        testdatas = [
            [False, False, False, False],
            [False, False, True, False],
            [False, True, False, False],
            [False, True, True, False],
            [True, False, False, False],
            [True, False, True, False],
            [True, True, False, False],
            [True, True, True, True]
        ]
        for testdata in testdatas:
            for i in range(0, 3):
                a.set_input(i, testdata[i])
            a.execute()
            self.assertEqual(testdata[3], a.get_output(0), "Class AndGate Testcase 5 failed: "+testdata.__str__())


class OrGateTest(unittest.TestCase):
    def testcase_00(self):
        a = OrGate(2)
        self.assertEqual(False, a.get_input(0), "Class OrGate Testcase 0 failed.")
        self.assertEqual(False, a.get_input(1), "Class OrGate Testcase 0 failed.")
        self.assertEqual(False, a.get_output(0), "Class OrGate Testcase 0 failed.")

    def testcase_01(self):
        a = OrGate(2)
        a.set_input(0, False)
        a.set_input(1, False)
        a.execute()
        self.assertEqual(False, a.get_output(0), "Class OrGate Testcase 1 failed.")

    def testcase_02(self):
        a = OrGate(2)
        a.set_input(0, False)
        a.set_input(1, True)
        a.execute()
        self.assertEqual(True, a.get_output(0), "Class OrGate Testcase 2 failed.")

    def testcase_03(self):
        a = OrGate(2)
        a.set_input(0, True)
        a.set_input(1, False)
        a.execute()
        self.assertEqual(True, a.get_output(0), "Class OrGate Testcase 3 failed.")

    def testcase_04(self):
        a = OrGate(2)
        a.set_input(0, True)
        a.set_input(1, True)
        a.execute()
        self.assertEqual(True, a.get_output(0), "Class OrGate Testcase 4 failed.")

    def testcase_05(self):
        a = OrGate(3)
        testdatas = [
            [False, False, False, False],
            [False, False, True, True],
            [False, True, False, True],
            [False, True, True, True],
            [True, False, False, True],
            [True, False, True, True],
            [True, True, False, True],
            [True, True, True, True]
        ]
        for testdata in testdatas:
            for i in range(0, 3):
                a.set_input(i, testdata[i])
            a.execute()
            self.assertEqual(testdata[3], a.get_output(0), "Class OrGate Testcase 5 failed: "+testdata.__str__())


class XOrGateTest(unittest.TestCase):
    def testcase_00(self):
        a = XOrGate(2)
        self.assertEqual(False, a.get_input(0), "Class XOrGate Testcase 0 failed.")
        self.assertEqual(False, a.get_input(1), "Class XOrGate Testcase 0 failed.")
        self.assertEqual(False, a.get_output(0), "Class XOrGate Testcase 0 failed.")

    def testcase_01(self):
        a = XOrGate(2)
        a.set_input(0, False)
        a.set_input(1, False)
        a.execute()
        self.assertEqual(False, a.get_output(0), "Class XOrGate Testcase 1 failed.")

    def testcase_02(self):
        a = XOrGate(2)
        a.set_input(0, False)
        a.set_input(1, True)
        a.execute()
        self.assertEqual(True, a.get_output(0), "Class XOrGate Testcase 2 failed.")

    def testcase_03(self):
        a = XOrGate(2)
        a.set_input(0, True)
        a.set_input(1, False)
        a.execute()
        self.assertEqual(True, a.get_output(0), "Class XOrGate Testcase 3 failed.")

    def testcase_04(self):
        a = XOrGate(2)
        a.set_input(0, True)
        a.set_input(1, True)
        a.execute()
        self.assertEqual(False, a.get_output(0), "Class XOrGate Testcase 4 failed.")

    def testcase_05(self):
        a = XOrGate(3)
        testdatas = [
            [False, False, False, False],
            [False, False, True, True],
            [False, True, False, True],
            [False, True, True, False],
            [True, False, False, True],
            [True, False, True, False],
            [True, True, False, False],
            [True, True, True, True]
        ]
        for testdata in testdatas:
            for i in range(0, 3):
                a.set_input(i, testdata[i])
            a.execute()
            self.assertEqual(testdata[3], a.get_output(0), "Class XOrGate Testcase 5 failed: "+testdata.__str__())


class NAndGateTest(unittest.TestCase):
    def testcase_00(self):
        a = NAndGate(2)
        self.assertEqual(False, a.get_input(0), "Class NAndGate Testcase 0 failed.")
        self.assertEqual(False, a.get_input(1), "Class NAndGate Testcase 0 failed.")
        self.assertEqual(True, a.get_output(0), "Class NAndGate Testcase 0 failed.")

    def testcase_01(self):
        a = NAndGate(2)
        a.set_input(0, False)
        a.set_input(1, False)
        a.execute()
        self.assertEqual(True, a.get_output(0), "Class NAndGate Testcase 1 failed.")

    def testcase_02(self):
        a = NAndGate(2)
        a.set_input(0, False)
        a.set_input(1, True)
        a.execute()
        self.assertEqual(True, a.get_output(0), "Class NAndGate Testcase 2 failed.")

    def testcase_03(self):
        a = NAndGate(2)
        a.set_input(0, True)
        a.set_input(1, False)
        a.execute()
        self.assertEqual(True, a.get_output(0), "Class NAndGate Testcase 3 failed.")

    def testcase_04(self):
        a = NAndGate(2)
        a.set_input(0, True)
        a.set_input(1, True)
        a.execute()
        self.assertEqual(False, a.get_output(0), "Class NAndGate Testcase 4 failed.")

    def testcase_05(self):
        a = NAndGate(3)
        testdatas = [
            [False, False, False, True],
            [False, False, True, True],
            [False, True, False, True],
            [False, True, True, True],
            [True, False, False, True],
            [True, False, True, True],
            [True, True, False, True],
            [True, True, True, False]
        ]
        for testdata in testdatas:
            for i in range(0, 3):
                a.set_input(i, testdata[i])
            a.execute()
            self.assertEqual(testdata[3], a.get_output(0), "Class NAndGate Testcase 5 failed: "+testdata.__str__())


class NOrGateTest(unittest.TestCase):
    def testcase_00(self):
        a = NOrGate(2)
        self.assertEqual(False, a.get_input(0), "Class NOrGate Testcase 0 failed.")
        self.assertEqual(False, a.get_input(1), "Class NOrGate Testcase 0 failed.")
        self.assertEqual(True, a.get_output(0), "Class NOrGate Testcase 0 failed.")

    def testcase_01(self):
        a = NOrGate(2)
        a.set_input(0, False)
        a.set_input(1, False)
        a.execute()
        self.assertEqual(True, a.get_output(0), "Class NOrGate Testcase 1 failed.")

    def testcase_02(self):
        a = NOrGate(2)
        a.set_input(0, False)
        a.set_input(1, True)
        a.execute()
        self.assertEqual(False, a.get_output(0), "Class NOrGate Testcase 2 failed.")

    def testcase_03(self):
        a = NOrGate(2)
        a.set_input(0, True)
        a.set_input(1, False)
        a.execute()
        self.assertEqual(False, a.get_output(0), "Class NOrGate Testcase 3 failed.")

    def testcase_04(self):
        a = NOrGate(2)
        a.set_input(0, True)
        a.set_input(1, True)
        a.execute()
        self.assertEqual(False, a.get_output(0), "Class NOrGate Testcase 4 failed.")

    def testcase_05(self):
        a = NOrGate(3)
        testdatas = [
            [False, False, False, True],
            [False, False, True, False],
            [False, True, False, False],
            [False, True, True, False],
            [True, False, False, False],
            [True, False, True, False],
            [True, True, False, False],
            [True, True, True, False]
        ]
        for testdata in testdatas:
            for i in range(0, 3):
                a.set_input(i, testdata[i])
            a.execute()
            self.assertEqual(testdata[3], a.get_output(0), "Class NOrGate Testcase 5 failed: "+testdata.__str__())


class NotGateTest(unittest.TestCase):
    def testcase_00(self):
        a = NotGate(1)
        self.assertEqual(False, a.get_input(0), "Class NotGate Testcase 0 failed.")
        self.assertEqual(True, a.get_output(0), "Class NotGate Testcase 0 failed.")

    def testcase_01(self):
        a = NotGate(1)
        a.set_input(0, False)
        a.execute()
        self.assertEqual(True, a.get_output(0), "Class NotGate Testcase 1 failed.")

    def testcase_02(self):
        a = NotGate(1)
        a.set_input(0, True)
        a.execute()
        self.assertEqual(False, a.get_output(0), "Class NotGate Testcase 2 failed.")


    def testcase_05(self):
        a = NotGate(3)
        testdatas = [
            [False, False, False, True, True, True],
            [False, False, True, True, True, False],
            [False, True, False, True, False, True],
            [False, True, True, True, False, False],
            [True, False, False, False, True, True],
            [True, False, True, False, True, False],
            [True, True, False, False, False, True],
            [True, True, True, False, False, False]
        ]
        for testdata in testdatas:
            for i in range(0, 3):
                a.set_input(i, testdata[i])
            a.execute()
            self.assertEqual(testdata[3], a.get_output(0), "Class NotGate Testcase 5 failed: "+testdata.__str__())


class HalfAdderTest(unittest.TestCase):
    def testcase_00(self):
        a = HalfAdder()
        self.assertEqual(False, a.get_input(0), "Class HalfAdder Testcase 0 failed.")
        self.assertEqual(False, a.get_input(1), "Class HalfAdderTestcase 0 failed.")
        self.assertEqual(False, a.get_output(0), "Class HalfAdder Testcase 0 failed.")
        self.assertEqual(False, a.get_output(1), "Class HalfAdderTestcase 0 failed.")


    def testcase_02(self):
        a = HalfAdder()
        testdatas = [
            [False, False, False, False],
            [False, True, True, False],
            [True, False, True, False],
            [True, True, False, True]
        ]
        for testdata in testdatas:
            for i in range(0, 2):
                a.set_input(i, testdata[i])
            a.execute()
            self.assertEqual(testdata[2], a.get_output(0), "Class HalfAdder Testcase 2 failed: "+testdata.__str__())
            self.assertEqual(testdata[3], a.get_output(1), "Class HalfAdder Testcase 2 failed: "+testdata.__str__())




class FullAdderTest(unittest.TestCase):
    def testcase_00(self):
        a = FullAdder()
        self.assertEqual(False, a.get_input(0), "Class FullAdder Testcase 0 failed.")
        self.assertEqual(False, a.get_input(1), "Class FullAdder Testcase 0 failed.")
        self.assertEqual(False, a.get_input(2), "Class FullAdder Testcase 0 failed.")
        self.assertEqual(False, a.get_output(0), "Class FullAdder Testcase 0 failed.")
        self.assertEqual(False, a.get_output(1), "Class FullAdder Testcase 0 failed.")


    def testcase_02(self):
        a = FullAdder()
        testdatas = [
            [False, False, False, False, False],
            [False, False, True, True, False],
            [False, True, False, True, False],
            [False, True, True, False, True],
            [True, False, False, True, False],
            [True, False, True, False, True],
            [True, True, False, False, True],
            [True, True, True, True, True]
        ]
        for testdata in testdatas:
            for i in range(0, 3):
                a.set_input(i, testdata[i])
            a.execute()
            self.assertEqual(testdata[3], a.get_output(0), "Class FullAdder Testcase 2 failed: "+testdata.__str__())
            self.assertEqual(testdata[4], a.get_output(1), "Class FullAdder Testcase 2 failed: "+testdata.__str__())


if __name__ == "__main__":
    unittest.main()
