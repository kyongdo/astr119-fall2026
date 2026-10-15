# exotemp.py -- equilibrium temperature of a planet around a star (Pod 3).
# Fast-rotating planet with zero albedo: T = (L / (16 pi sigma d^2))^(1/4). Everything in SI units.
from math import pi
import sys

sigma = 5.670374e-8     # Stefan-Boltzmann constant, W/(m^2 K^4)


def t_eq(L, d):
    """Equilibrium temperature in K for luminosity L (W) at distance d (m)."""
    flux = L / (16 * pi * sigma * d**2)
    return flux**0.25


planets = [   # name, luminosity (solar units), distance (AU)
    ["Earth",        1.0,     1.000],
    ["Mars",         1.0,     1.524],
    ["HD 209458 b",  1.6,     0.047],
    ["51 Peg b",     1.3,     0.052],
    ["TRAPPIST-1 e", 0.00055, 0.029],
    ["Kepler-22 b",  0.79,    0.85],
    ["55 Cnc e",     0.58,    0.0154],
    ["HD 189733 b",  0.34,    0.031],
    ["Kepler-452 b", 1.2,     1.046],
    ["Proxima b",    0.0016,  0.0485],
]


if __name__ == '__main__':
    L = float(sys.argv[1])      # stellar luminosity from the command line, W
    d = float(sys.argv[2])      # star-planet distance from the command line, m
    print(f"T_eq = {t_eq(L, d):.1f} K")
