import unittest


class TestDemo(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        print("setupclass")

    def setUp(self) -> None:
        print("setup")

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardownclass")

    def tearDown(self) -> None:
        print("teardown")


    def test_sum(self):
        print("test_sum")
        x = 1 + 2
        print(x)
        self.assertEqual(x, 3, f'x={x} expection=3')

    def test_demo(self):
        print("test_demo")
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
