require 'cgi'
cgi = CGI.new
puts cgi.header
puts "
<!DOCTYPE html>
<html>
  <head>
    <title>¡Jag harn't ont i magen!</title>
    <meta charset=\"utf-8\">
    <style>
    body {
      background-color: #000;
      color:#8FA;
      font-size:12pt;
    }
    div {
      float:left;
      margin-right:5%;
    }
    table { 
      border-collapse:collapse;
      float:left;
    }
    td {
      text-align:center;
      width:14pt;
      height:14pt;
      color:#303;
    }
    img { width: 200pt; }
    
    .s1{ background-color:#AC8;}
    .s2{ background-color:#AA6;}
    .s3{ background-color:#A84;}
    .s4{ background-color:#A62;}
    .s5{ background-color:#A20;}
    
    </style>
  </head>
  <body>
  <h1>Harpin tauluun heitto ohjelma</h1>
  <h2>Mutta ei kuitenkaan ihan</h2>
  <div>"

alat = []
sivu = 9
kokoAla = 9 * 9  

for i in 1..5
  seurSivu = sivu - 2  
  if i == 5
    seurSivu = 0
  end  
 
  alat[i] = (sivu * sivu) - (seurSivu * seurSivu)
  puts "A<sub>#{i}</sub>: #{alat[i]}<br>"
  sivu = seurSivu
end
puts "<br>"

E = 0
for i in 1..5
  tn = alat[i] / kokoAla.to_f
  E += i * tn
  
  puts "TN<sub>#{i}</sub>: #{alat[i]} / #{kokoAla} = #{tn.round(3)}<br>"
end

puts "<br> E(Pistemäärä) = #{E.round(3)}<br>"
puts "<a href=\"https://github.com/Stiigel/Matte/blob/master/taulu.rb\">sorsat</a>"
puts "</div>"

puts "<table>"
for i in 0..8
  puts "<tr>"
  for e in 0..8
    etaisyys = 5 - ([(i - 4).abs, (e - 4).abs].max)
    puts "<td class=\"s#{etaisyys}\">#{etaisyys}</td>"
  end
  puts "</tr>"
end
puts "</table>"
  
puts "
  <img src=\"harp.png\" alt=\"harp\">
  </body>
</html>"