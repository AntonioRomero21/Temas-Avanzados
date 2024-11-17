import pytest
from math_operations import MathOperations

class TestMathOperations:
    def setup_method(self):
        self.math_ops = MathOperations()

    def test_add(self):
        assert self.math_ops.add(2, 3) == 5
        assert self.math_ops.add(-1, 1) == 0
        assert self.math_ops.add(0, 0) == 0

    def test_subtract(self):
        assert self.math_ops.subtract(5, 3) == 2
        assert self.math_ops.subtract(0, 5) == -5
        assert self.math_ops.subtract(-5, -5) == 0

    def test_multiply(self):
        assert self.math_ops.multiply(3, 4) == 12
        assert self.math_ops.multiply(-1, 5) == -5
        assert self.math_ops.multiply(0, 100) == 0

    def test_divide(self):
        assert self.math_ops.divide(10, 2) == 5
        assert self.math_ops.divide(-10, 2) == -5
        with pytest.raises(ValueError, match="Cannot divide by zero."):
            self.math_ops.divide(10, 0)

    def test_divide_by_one(self):
        assert self.math_ops.divide(5, 1) == 5