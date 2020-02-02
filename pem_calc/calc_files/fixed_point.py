class FixedPoint:
    def __init__(self, a_float):
        self.value = float(a_float)
        self.PRECISION = 100
    def __str__(self):
        return '{0:.{1}%}'.format(self.value, self.PRECISION)

inp = FixedPoint(0.00000000000000000000000032)
print(float(str(inp)))
