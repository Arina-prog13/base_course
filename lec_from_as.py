from modul_N_biblioteka import earth_mass as em
from modul_N_biblioteka import gravity_constant as G
from modul_N_biblioteka import sigma_steff_bolc as sigm

g = 500 * G / 10*2
print(g)

x = em * G * sigm
print(x)