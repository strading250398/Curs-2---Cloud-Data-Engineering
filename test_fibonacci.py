import unittest
from fibonacci import fibonacci

class TestFibonacii(unittest.TestCase):

    def test_fibonacci_zero(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)

    def test_valori_corecte(self):
        self.assertEqual(fibonacci(2). 1)
        self.assertEqual(fibonacci(3). 2)
        self.assertEqual(fibonacci(4). 3)
        self.assertEqual(fibonacci(5). 5)
        self.assertEqual(fibonacci(6). 6)

    class TestVitezaFibonaaci(unittest.TestCase):
        def test_viteza(self):
            start_time = time.time()
            rezultat = fibonacci(40)
            stop_time = time.time()
            print(''Executat in'', stop_time - start_time)


if __name__ == "__main__":
    unittest.main()
