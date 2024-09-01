# test_fibonacci.py

import unittest
from questao2 import fibonacci, check_num


class TestFibonacci(unittest.TestCase):

    def test_fibonacci(self):
        # Testes de casos conhecidos da sequência Fibonacci
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 2)
        self.assertEqual(fibonacci(3), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(8), 8)
        self.assertEqual(fibonacci(13), 13)

        # Testes de números que não estão na sequência
        self.assertEqual(fibonacci(4), 5)  # O menor Fibonacci >= 4 é 5
        self.assertEqual(fibonacci(6), 8)  # O menor Fibonacci >= 6 é 8
        self.assertEqual(fibonacci(7), 8)  # O menor Fibonacci >= 7 é 8
        self.assertEqual(fibonacci(14), 21)  # O menor Fibonacci >= 14 é 21

    def test_check_num(self):
        # Testes para verificar se os números estão na sequência
        self.assertTrue(check_num(0))
        self.assertTrue(check_num(1))
        self.assertTrue(check_num(2))
        self.assertTrue(check_num(3))
        self.assertTrue(check_num(5))
        self.assertTrue(check_num(8))
        self.assertTrue(check_num(13))

        # Testes para verificar se os números não estão na sequência
        self.assertFalse(check_num(4))
        self.assertFalse(check_num(6))
        self.assertFalse(check_num(7))
        self.assertFalse(check_num(14))

    def test_negative_numbers(self):
        # Teste para números negativos (deve levantar um ValueError)
        with self.assertRaises(ValueError):
            fibonacci(-1)


if __name__ == "__main__":
    unittest.main()
