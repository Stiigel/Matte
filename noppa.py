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
    
    input {
      background-color:#010;
      color: #ADA;
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
    <h1>Nopan heitto ohjelma</h1>
    
    <form action="noppa.py" method="get">
      Määrä: <input type="text" name="maara">
      <input type="submit" value="lähetä">
    </form><br>   
    """)

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
  global vitoset, ylKolmet, summa

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
    
    summa += tulos1 + tulos2
  
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

formi = cgi.FieldStorage()

try:
  heittoMaara = int(formi["maara"].value)
  
  if heittoMaara > 50000:
    heittoMaara = 50000
    
  if heittoMaara <= 0:
    heittoMaara = 25
except:
  heittoMaara = 25
  
mahdMaara = 36
vitoset = 0
ylKolmet = 0

summa = 0
E = 0

todnak = 1 / 6

for i in range(1, 7):
  E += i * todnak

heita3()

ka = summa / (heittoMaara * 2)

enc_print('E(Nopan arvo) = %.2f<br>' % E)
enc_print('Ka. = %i / %i =  %.2f' % (summa, heittoMaara * 2, ka))
enc_print('<h3>Anakin toinen vitonen: %i </h3>' % vitoset)
enc_print('Tilastoll. TN: %i / %i = %.2f<br>' % (vitoset, heittoMaara, vitoset/heittoMaara))

tulosta_taulu(5, 5)

enc_print('<h3>Anakin toinen yli kolme: %i </h3>' % ylKolmet )
enc_print('Tilastoll. TN: %i / %i = %.2f <br>' % (ylKolmet, heittoMaara, ylKolmet/heittoMaara))

tulosta_taulu(3, 6)

enc_print("""
    <br>
    <a href="noppa.py">¡Heitä uudestaan!</a><br>
    <a href="https://github.com/Stiigel/Matte/blob/master/noppa.py">Sorsat</a>
  </body>
</html>""")
