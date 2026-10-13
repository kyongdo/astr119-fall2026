# cometlife.py -- calculates how much a comet shrinks per orbit
# and estimates its remaining lifetime.
# Run with: python cometlife.py

from math import sqrt, pi

L = 3.8e26          # solar luminosity, J/s
GM = 1.3271e20      # G times the Sun's mass, m^3/s^2
h_ice = 2.5e6       # energy to sublimate ice, J/kg
AU = 1.49e11        # meters per AU

R = float(input("Radius [km]: ")) * 1000
rho = float(input("Density [kg/m^3]: "))
A = float(input("Albedo: "))
a_au = float(input("Semi-major axis [AU]: "))
e = float(input("Eccentricity: "))

a = a_au * AU

H_sol = (pi / 2) * (1 - A) * R**2 * L / sqrt(GM) / sqrt(a * (1 - e**2))
dM = H_sol / h_ice
dr = dM / (4 * pi * rho * R**2)

orbits = R / dr
years = orbits * a_au**1.5

print(f"The comet shrinks {dr:.2f} meters per orbit, has about {orbits:.0f} orbits left, and will last about {years:.0f} years.")