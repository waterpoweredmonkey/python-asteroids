import pygame
from text import Text

class Score(Text):
    def __init__(self, x, y, initial):
        super().__init__(x, y, initial)
        self.points = 0

    def add_score(self, to_add):
        self.points += to_add
        self.set_text(str(self.points))