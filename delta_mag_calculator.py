import math

#input log of luminosity in solar luminosities
logL=float(raw_input('What is the luminosity of your object? (i.e. abs(logL/Lo)): '))

#define variables
Mo=3.846*10**26
L=(Mo)*10**-(logL)
Lk=2.3287*10**24

#calculate delta_mag
d_mag=-2.5*math.log10(L/(Lk))
print d_mag

