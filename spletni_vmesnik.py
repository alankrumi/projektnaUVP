import bottle
import model

igra = model.Stiri_v_vrsto()

@bottle.get('/')
def zacetna_stran():
    return bottle.template('index.tpl')

@bottle.get('/nova-igra')
def zacni_igro():
    global igra
    igra = model.Stiri_v_vrsto()
    bottle.redirect('/igra')

@bottle.get('/igra')
def pokazi_igro():
    return bottle.template('igra.tpl',
                            polja=igra.mreza.polja(),
                            na_potezi=igra.na_potezi,
                            konec=igra.konec,
                            na_potezi_barva=igra.na_potezi_barva(),
                            PRAZNO=model.PRAZNO,
                            VISINA=model.VISINA,
                            SIRINA_STOLPCA=80/model.SIRINA,
                            mreza=igra.mreza,
                            barva=igra.barva)

@bottle.post('/poteza')
def poteza():
    stolpec = int(bottle.request.forms.getunicode('stolpec'))-1
    igra.postavi(stolpec)
    print(igra.mreza)
    bottle.redirect('/igra')

bottle.run()