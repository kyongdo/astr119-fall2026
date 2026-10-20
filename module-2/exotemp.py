# exotemp.py -- equilibrium temperature of a planet around a star (Pod 3).
# Fast-rotating planet with zero albedo: T = (L / (16 pi sigma d^2))^(1/4). Everything in SI units.
from math import pi

SIGMA = 5.67e-8          # W m^-2 K^-4

def t_eq(L, d):
    """Equilibrium temperature (K) of a planet at distance d (m) from a star of luminosity L (W)."""
    return (L / (16 * pi * SIGMA * d**2)) ** 0.25

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

for i in range(len(planets)):
        name = planets[i][0]
        L_star = planets[i][1] * 3.8e26 # star's luminosity, solar luminosities -> W
        d_planet = planets[i][2] * 1.496e11 # star-planet distance, AU -> m
        
        # Calculate temperature once to use for both the check and the print
        temp = t_eq(L_star, d_planet)
        
        if temp > 1000:
            status = "hot"
        else:
            status = "temperate"
            
        print(f"{name:<14}{temp:>6.0f} K {status}")
