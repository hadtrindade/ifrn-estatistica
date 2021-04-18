from typing import Union
from scipy import stats
import numpy as np


numeric = Union[int, float, complex]


class Probability:
    def __init__(
        self,
        x1: numeric = 0,
        x2: numeric = 0,
        mu: numeric = 0,
        sigma: numeric = 1,
    ):
        self.x1 = x1
        self.x2 = x2
        self.mu = mu
        self.sigma = sigma

    def normalize(self):
        """Normaliza para função para distribuição nornal."""
        z1 = (self.x1 - self.mu) / self.sigma
        z2 = (self.x2 - self.mu) / self.sigma
        return z1, z2

    def calculate_probability(self):
        """Calcula a probabilidade."""
        z1, z2 = self.normalize()
        x = np.arange(z1, z2, 0.001)
        probability = round(sum(stats.norm.pdf(x, 0, 1)) / 10, 3)
        return probability

    
