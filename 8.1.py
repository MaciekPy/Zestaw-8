
import unittest


def solve1(a, b, c):
    if a == 0 and b == 0 and c == 0:
        return "równanie ma nieskonczenie wiele rozwiązań"
    elif a == 0 and b == 0:
        return "równanie jest sprzeczne"
    elif a == 0:
        y = -c/b
        return "x - dowolne , y = " + str(y)
    elif b == 0:
        x = -c/a
        return "y - dowolne, x = " + str(x)
    else:
        return "y = -(" + str(a) + " * x + " + str(c) + ") / " + str(b)


class MyTestCase(unittest.TestCase):

    def test_solve1(self):
        self.assertEqual(
            solve1(0, 0, 0), "równanie ma nieskonczenie wiele rozwiązań")
        self.assertEqual(solve1(0, 0, 3), "równanie jest sprzeczne")
        self.assertEqual(solve1(0, 4, 8), "x - dowolne , y = -2.0")
        self.assertEqual(solve1(3, 4, 3), "y = -(3 * x + 3) / 4")


if __name__ == '__main__':
    unittest.main()
