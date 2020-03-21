from numpy.polynomial.polynomial import polyfit


class Rots:
    def __init__(self):
        self.score = 0

    def get_score(self, total_reacts, coefficient_x, coefficient_y):
        expected = coefficient_x + coefficient_y
        actual = total_reacts
        self.score = ((actual - expected) / expected) * 100
        return self.score

