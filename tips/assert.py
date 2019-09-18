# _*_ coding:utf-8 _*_
import unittest
import math

class demoTest(unittest.TestCase):
    #1.基本断言
    def test1(self):
        self.assertEqual(4 + 5,9)

    def test2(self):
        self.assertNotEqual(5 * 2,10)

    def test3(self):
        self.assertTrue(4 + 5 == 9,"The result is False")

    def test4(self):
        self.assertTrue(4 + 5 == 10,"assertion fails")

    def test5(self):
        self.assertIn(3,[1,2,3])

    def test6(self):
        self.assertNotIn(3, range(5))
    #2.比较断言
    def test7(self):
        self.assertAlmostEqual(22.0 / 7, 3.14)

    def test8(self):
        self.assertNotAlmostEqual(10.0 / 3, 3)

    def test9(self):
        self.assertGreater(math.pi, 3)

    def test10(self):
        self.assertRegex("Tutorials Point (I) Private Limited","Point")
    #3.复杂断言
    def test11(self):
        self.assertListEqual([2, 3, 4], [1, 2, 3, 4, 5])

    def test12(self):
        self.assertTupleEqual((1 * 2, 2 * 2, 3 * 2), (2, 4, 6))

    def test13(self):
        self.assertDictEqual({1: 11, 2: 22}, {3: 33, 2: 22, 1: 11})

if __name__ == '__main__':
    #unittest.main()
	suite = unittest.TestSuite()
	suite.addTest(demoTest("test1"))
	suite.addTest(demoTest("test2"))
	suite.addTest(demoTest("test3"))
	suite.addTest(demoTest("test4"))
	suite.addTest(demoTest("test5"))
	suite.addTest(demoTest("test6"))
	suite.addTest(demoTest("test7"))
	suite.addTest(demoTest("test8"))
	suite.addTest(demoTest("test9"))
	suite.addTest(demoTest("test10"))
	suite.addTest(demoTest("test11"))
	suite.addTest(demoTest("test12"))
	suite.addTest(demoTest("test13"))
	unittest.TextTestRunner(verbosity=2).run(suite)

'''
verbosity
0 (静默模式): 你只能获得总的测试用例数和总的结果 比如 总共100个 失败20 成功80
1 (默认模式): 非常类似静默模式 只是在每个成功的用例前面有个“.” 每个失败的用例前面有个 “F”
2 (详细模式):测试结果会显示每个测试用例的所有相关的信息
'''