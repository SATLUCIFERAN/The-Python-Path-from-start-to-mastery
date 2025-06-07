
class Score:
    def __init__(self, points):
        self.points = points

    def __add__(self, other):
        return Score(self.points + other.points)

    def __str__(self):
        return f"Score: {self.points}"

s1 = Score(50)
s2 = Score(70)
total = s1 + s2
print(total) # Score: 120