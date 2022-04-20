import unittest
import shutil


class TestTowSum(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 只在开始时执行一次
        #print ("this setupclass() method only called once.\n")
        ...

    @classmethod
    def tearDownClass(cls):
        # 只在结束的时候执行一次
        # print ("this teardownclass() method only called once too.\n")
        # 清理pycache
        shutil.rmtree('./__pycache__')
        print('----------remove cache,successfully')



    def setUp(self):
        # 每个 test demo 执行一次
        # print ("do something before test : prepare environment.\n")
        ...

    def tearDown(self):
        # print ("do something after test : clean up.\n")
        ...

    def test_demo1(self):
        # self.assertEqual('foo'.upper(), 'FOO')
        ...

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()