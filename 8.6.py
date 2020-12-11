import unittest


def func(x, y):
    P = {}

    P[(0, 0)] = 0.5

    for a in range(1, x + 1):
        P[(a, 0)] = 0

    for b in range(1, y + 1):
        P[(0, b)] = 1

    for i in range(1, x + 1):
        for j in range(1, y + 1):
            P[(i, j)] = 0.5 * (P[(i - 1, j)] + P[(i, j - 1)])

    return P[(x, y)]


class MyTestCase(unittest.TestCase):

    def test_func(self):
        self.assertEqual(func(0, 0), 0.5)
        self.assertEqual(func(0, 1), 1)
        self.assertEqual(func(1, 2), 0.75)
        self.assertEqual(func(2, 1), 0.25)


if __name__ == '__main__':
    unittest.main()
