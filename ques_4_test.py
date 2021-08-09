from unittest import TestCase
from ques_4 import Total_compensation


class ProblemTest(TestCase):
    def setUp(self) -> None:
        self.employees = Total_compensation("cur")

    def tearDown(self) -> None:
        self.employees = None

    def test_get_result(self):
        self.assertEqual(self.employees.compensation, False)