% rebase('base.tpl')

% if not konec:
<p class="lead">Na potezi je <strong style="color: {{na_potezi_barva}}">{{na_potezi}}</strong></p>
% elif na_potezi==PRAZNO:
<p class="h2">Konec igre, ni zmagovalca</h2>
% else:
<p class="h2">Zmagovalec je <strong style="color: {{na_potezi_barva}}">{{na_potezi}}</strong></h2>
% end

<form action="./poteza" method="post" class="mreza">
	% for (i, stolpec) in enumerate(mreza.stolpci):
		<div class="stolpec" style="width: {{SIRINA_STOLPCA}}%">
			% if not konec:
				% if not stolpec.je_poln:
					<input type="submit" name="stolpec" value="{{i+1}}" style="background-color: {{na_potezi_barva}}" class="indeks">
				% else:
					<div class="indeks">{{i+1}}</div>
				% end
			% end

			% for i in range(VISINA):
				<div class="krog" style="background-color: {{barva(stolpec.polja[VISINA-i-1])}}">
				</div>
			% end
		</div>
	% end
</form>

% if konec:
<a href="./nova-igra" class="btn btn-primary nova-igra">Nova igra</a>
% end