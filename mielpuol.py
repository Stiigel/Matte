import cgi, cgitb, sys, math

def enc_print(string='', koodaus='utf-8'):
  sys.stdout.buffer.write(string.encode(koodaus) + b'\n')

cgitb.enable()

formi = cgi.FieldStorage()

enc_print("Content-Type: text/html\n\n")
enc_print("""
<!DOCTYPE html>
<html>
<head>
  <title>2. ast yh rat</title>
  <meta charset="utf-8">
  <style>
  body{
    background-color:#000;
    color:#BADA55;
  }
  input {
    width:50px;
    background-color:#404;
    color:#DA0;
  }
  </style>
</head>
<body> 
<h1>¡Toisen asteen yhtälön ratkaisin!</h1>
<h3>x = -b &plusmn; sqrt( b<sup>2</sup> - 4 ac ) / 2a</h3>
<form action="mielpuol.py" method="get">
  a<input type="text" name="a" autofocus="autofocus">
  b<input type="text" name="b">
  c<input type="text" name="c">
  <input type="submit" value="Laske">
</form>""")

try:
  a = int(formi["a"].value)
  b = int(formi["b"].value)
  c = int(formi["c"].value)
except:
  sys.exit()
  
enc_print('<br> a = %i, b = %i, c= %i <br><br>' % (a, b, c))

enc_print('x = -b &plusmn; sqrt( b<sup>2</sup> - 4 ac ) / 2a<br>')
enc_print('x = -%i &plusmn; sqrt( %i<sup>2</sup> - 4 * %i * %i ) / 2 * %i<br>' % (b,b,a,c,a))

diskLop = 4 * a * c
bTois = pow(b, 2)
disk = bTois - diskLop
ala = 2 * a


enc_print('x = -%i &plusmn; sqrt( %i - %i ) / %i<br>' % (b, bTois, diskLop, ala))

if ala == 0:
  enc_print('¡RR, ei voi jakaa 0:llalla!')
  sys.exit()

enc_print('x = -%i &plusmn; sqrt( %i ) / %i<br>' % (b, disk, ala))

if disk < 0:
  enc_print('¡RR, Ei reaaliluku juuri!')
  sys.exit()
  
elif disk == 0:
  enc_print('x = -%i / %i<br>' % (b, ala))
  vast = -b / ala
  if vast == int(vast):
    enc_print('x = %i' % vast)

else:
  sqrtDisk = math.sqrt(disk)
  
  if int(sqrtDisk) == sqrtDisk:
    enc_print('x = -%i &plusmn; %i / %i<br><br>' % (b, sqrtDisk, ala))
    
    enc_print('x = -%i + %i / %i<br>TAI<br>' % (b, sqrtDisk, ala))
    enc_print('x = -%i - %i / %i<br><br>' % (b, sqrtDisk, ala))
    
    yla1 = -b + sqrtDisk
    yla2 = -b - sqrtDisk
    
    enc_print('x = %i / %i<br>TAI<br>' % (yla1, ala))
    enc_print('x = %i / %i<br><br>' % (yla2, ala))
    
    vast1 = (-b + sqrtDisk) / ala
    vast2 = (-b - sqrtDisk) / ala
    
    if vast1 == int(vast1):
      enc_print('x = %i ' % vast1)
      if vast2 == int(vast2):
        enc_print('TAI x = %i' % vast2)
      else:
        enc_print('TAI x &asymp; %f' % vast2)
        
    else:
      enc_print('x &asymp; %f ' % vast1)
      
      if vast2 == int(vast2):
        enc_print('TAI x = %i' % vast2)    
      else:
        enc_print('TAI x &asymp; %f' % vast2)
    
  else:
    liki1 = (-b + sqrtDisk) / ala
    liki2 = (-b - sqrtDisk) / ala
    
    enc_print('<br>x = -%i + sqrt( %i ) / %i<br>TAI<br>' % (b, disk, ala))
    enc_print('x = -%i - sqrt( %i ) / %i<br><br>' % (b, disk, ala))
    
    enc_print('x &asymp; %f TAI x &asymp; %f' % (liki1, liki2))


enc_print("""
  </body>
</html>""")