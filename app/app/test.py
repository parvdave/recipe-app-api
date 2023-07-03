
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):

    def test_add(self):
        x = 5
        y = 10

        self.assertEqual(calc.add(x, y), 15)
