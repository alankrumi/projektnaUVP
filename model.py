

PRAZNO = "PRAZNO"
RUMENI = "RUMENI"
ZELENI = "ZELENI"

VISINA = 8
SIRINA = 10

class Stolpec:

	def __init__(self):
		self.polja = [PRAZNO for i in range(VISINA)]
		self.visina = 0
		self.je_poln = False	
	
	def postavi(self, barva):
		if self.je_poln: # ce je stolpec ze zapolnjen do vrha
			return False 
		else:
			self.polja[self.visina] = barva
			self.visina += 1
			self.je_poln = self.visina == VISINA
			return True


class Mreza:

	def __init__(self):
		self.stolpci = [Stolpec() for i in range(SIRINA)]
	
	def postavi(self, barva, stolpec):
		return self.stolpci[stolpec].postavi(barva)
	
	def ali_je_konec(self):
		# preveri, ali so 4 v vrsto v katerem od stolpcev
		for i in range(SIRINA):
			stolpec = self.stolpci[i]
			if stolpec.visina >= 4:
				# isce, ali se pojavi zaporedje stirih enakih v stolpcu:
				for j in range(stolpec.visina - 3):
					st_enakih = 0
					for k in range(4):
						if stolpec.polja[j] == stolpec.polja[j+k]:
							st_enakih += 1
					if st_enakih == 4:
						return stolpec.polja[j]
		
		# preveri 4 v vrsto za vrstice
		for j in range(VISINA):
			# isce, ali se pojavi zaporedje stirih enakih v vrstici:
			for i in range(SIRINA - 3):
				st_enakih = 0
				if self.stolpci[i].polja[j] == PRAZNO:
					continue
				
				for k in range(4):
					if self.stolpci[i].polja[j] == self.stolpci[i+k].polja[j]:
						st_enakih += 1
				if st_enakih == 4:
					return self.stolpci[i].polja[j]

		# preveri 4 v vrsto za narascajoce diagonale
		for j in range(VISINA-3):
			for i in range(SIRINA - 3):
				st_enakih = 0
				if self.stolpci[i].polja[j] == PRAZNO:
					continue
				
				for k in range(4):
					if self.stolpci[i].polja[j] == self.stolpci[i+k].polja[j+k]:
						st_enakih += 1
				if st_enakih == 4:
					return self.stolpci[i].polja[j]
		
		# preveri 4 v vrsto za padajoce diagonale
		for j in range(3, VISINA):
			for i in range(SIRINA - 3):
				st_enakih = 0
				if self.stolpci[i].polja[j] == PRAZNO:
					continue
				
				for k in range(4):
					if self.stolpci[i].polja[j] == self.stolpci[i+k].polja[j-k]:
						st_enakih += 1
				if st_enakih == 4:
					return self.stolpci[i].polja[j]

		# preveri, ali je celotna mreza zapolnjena -> konec igre brez zmagovalca

		f = 0
		for i in range(SIRINA):
			f += 1 if self.stolpci[i].je_poln else 0
		if f == SIRINA:
			return PRAZNO
		
		# ni zmagovalca/konca
		return None

	def __str__(self):
		# izris igralne mreze
		s = "\n "
		for j in range(SIRINA):
			s += str(j) + " "
		s += "\n\n"
		for i in range(VISINA):
			s += " "
			for j in range(SIRINA):
				x = self.stolpci[j].polja[VISINA-i-1]
				if x == RUMENI:
					s += "X "
				elif x == ZELENI:
					s += "# "
				else:
					s+= ": "
			s += "\n"
		return s
	
	def polja(self):
		polja = []
		for st in self.stolpci:
			s = []
			for i in range(VISINA):
				s.append(st.polja[VISINA-i-1])
			polja.append(s)
		return polja


class Stiri_v_vrsto:
	
	def __init__(self):
		self.mreza = Mreza()
		self.na_potezi = ZELENI
		self.konec = False
	
	def postavi(self, stolpec):
		if self.mreza.postavi(self.na_potezi, stolpec): # ce je poteza pravilna
			zmagovalec = self.mreza.ali_je_konec()
			if zmagovalec is None: # ce ni zmagal
				# zamenja igralca
				if self.na_potezi == ZELENI:
					self.na_potezi = RUMENI
				else:
					self.na_potezi = ZELENI
			else:
				self.konec = True
				self.na_potezi = zmagovalec
	
	def na_potezi_barva(self):
		if self.na_potezi == ZELENI:
			return "green"
		elif self.na_potezi == RUMENI:
			return "yellow"
		else:
			return "black"
	
	def barva(self, polje):
		if polje == ZELENI:
			return "green"
		elif polje == RUMENI:
			return "yellow"
		else:
			return "grey"