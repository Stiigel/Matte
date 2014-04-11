import cgi, cgitb, sys, random

#http://wedi.dy.fi/matte/noppa.py

def enc_print(string='', koodaus='utf-8'):
  sys.stdout.buffer.write(string.encode(koodaus) + b'\n')

cgitb.enable()

enc_print('Content-Type: text/html\n\n')
enc_print("""
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Nopan heitto ohjelma</title>
    <style>
    body {
      background-color:#000;
      color:#BADA55;
      font-size:12pt;
    }
    caption { 
      font-weight:900;
      font-size:14pt;
    }
    td, th { width:12pt; }
    .loyto { background-color: #420; }
    #heitot {
      float:left;
      margin-right: 10%;
    }
    </style>
  </head>
  <body>
    <h1>Nopan heitto ohjelma</h1>""")

def tulosta_taulu(alku, loppu):
  loydot = 0  
  enc_print('<table>')
  
  for i in range(7):    
    if i == 0:
      enc_print('<th> </th>')
      continue    
    enc_print('<th>%i</th>' % i)
    
  for i in range(6):
    enc_print('<tr><th>%i</th>' % (i + 1) )
    for e in range(6):
      if e + 1 >= alku and e + 1 <= loppu:
        enc_print('<td class="loyto">X</td>')        
        loydot += 1
        
      elif i + 1 >= alku and i + 1 <= loppu:
        enc_print('<td class="loyto">X</td>')
        loydot += 1
        
      else:
        enc_print('<td>O</td>')
    enc_print('</tr>')
  
  enc_print('</table>')
  
  enc_print("Oikea TN: %i / %i = %.2f<br>" % (loydot, mahdMaara, loydot/mahdMaara))

def heita3():
  global vitoset, ylKolmet

  enc_print("""
  <table id="heitot">
    <caption>Heitot:</caption>
      <tr>
        <th>1.</th>
        <th>2.</th>
        <th>5</th>
        <th>&lt;3</th>
      </tr>""")
  for i in range(heittoMaara):
    enc_print('<tr>')
    tulos1 = random.randint(1,6)
    tulos2 = random.randint(1,6)
    
    enc_print('<td>%i</td>' % tulos1)
    enc_print('<td>%i</td>' % tulos2)
  
    if tulos1 == 5 or tulos2 == 5:
      vitoset += 1
      enc_print('<td>*</td>')
    else:
      enc_print('<td> </td>')
  
    if tulos1 >= 3 or tulos2 >= 3:
      ylKolmet += 1
      enc_print('<td>*</td>')
    else:
      enc_print('<td> </td>')

    enc_print('</tr>')
  enc_print('</table>')
  
def valehtele(luku):
  if luku >= 1 and luku <= 6:
    return 1
  else: 
    return  luku - 5
  
  #1 2 3 4 5 6 7 8 9 0 1
  #1 1 1 1 1 1 2 3 4 5 6
  
heittoMaara = 25
mahdMaara = 36
vitoset = 0
ylKolmet = 0

heita3()

enc_print('<h3>Anakin toinen vitonen: %i </h3>' % vitoset)
enc_print('Tilastoll. TN: %i / %i = %.2f<br>' % (vitoset, heittoMaara, vitoset/heittoMaara))

tulosta_taulu(5, 5)


enc_print('<h3>Anakin toinen yli kolme: %i </h3>' % ylKolmet )
enc_print('Tilastoll. TN: %i / %i = %.2f <br>' % (ylKolmet, heittoMaara, ylKolmet/heittoMaara))

tulosta_taulu(3, 6)

enc_print("""
    <br>
    <a href="noppa.py">¡Heitä uudestaan!</a>
  </body>
</html>""")
