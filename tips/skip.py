# _*_ coding:utf-8 _*_
import unittest

class demoSkipTest(unittest.TestCase):
    a = 50
    b = 20
    
    def test_jimmy(self):
        print('JIMMY skip test:')

    @unittest.skip('强制跳转')
    def test_add(self):
        result = self.a + self.b
        self.assertEqual(result, 40)

    #条件跳转，如果 condition 是 True 则跳转
    @unittest.skipIf(a<b, u"a>b 就跳过")
    def test_sub(self):
        result = self.a - self.b
        self.assertTrue(result == -30)

     #除非 conditioin 为 True，才进行调整
    @unittest.skipUnless(b==0, u"除数为 0，则跳转")
    def test_div(self):
        result = self.a / self.b
        self.assertTrue(result == 1)

    #标记该测试预期为失败 ，如果该测试方法运行失败，则该测试不算做失败
    @unittest.expectedFailure
    def test_mul(self):
        result = self.a * self.b
        self.assertTrue(result == 0)

if __name__ == "__main__":
    unittest.main()