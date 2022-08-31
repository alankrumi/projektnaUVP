from model import Stiri_v_vrsto, SIRINA, PRAZNO

print("")
print("4 V VRSTO")
print("")
print("Zeleni: #\nRumeni: X")

svv = Stiri_v_vrsto()

while not svv.konec:
	print(svv.mreza)
	print("Na potezi je " + svv.na_potezi)
	i = -1
	while not (i >= 0 and i < SIRINA):
		i = int(input("Vnesi indeks stolpca: "))
	svv.postavi(i)

print("")
print("="*(2*SIRINA+1))
print("="*(2*SIRINA+1))

print(svv.mreza)
if svv.na_potezi == PRAZNO:
	print("Konec igre, ni zmagovalca")
else:
	print("Zmagovalec je " + svv.na_potezi + "!\n")