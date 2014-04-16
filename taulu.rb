require 'cgi'
cgi = CGI.new
puts cgi.header
puts "
<!DOCTYPE html>
<html>
  <head>
    <title>¡Jag harn't ont i magen</title>
    <meta charset=\"utf-8\">
    <style>
    div { float:left;}
    table { border-collapse:collapse}
    td {
      width:14pt;
      height:14pt;
      color:#001;
    }
    .s1{ background-color:#AAA;}
    .s2{ background-color:#4A9;}
    .s3{ background-color:#28F;}
    .s4{ background-color:#A82;}
    .s5{ background-color:#A28;}
    
    </style>
  </head>
  <body>
  <div>"

alat = []

sivu = 1
edellAlat = 0
ala = 0
kokoAla = 9 * 9
    

i = 5
while i > 0
  edellAlat += ala  
  ala = (sivu * sivu) - edellAlat 
  alat[i] = ala
  
  puts "#{i}. ala: #{ala}<br>"
  
  sivu += 2  
  i -= 1
end

puts "<br>"
tnt = []
E = 0

for i in 1..5
  tn = alat[i] / kokoAla.to_f
  E += i * tn
  
  puts "#{i}. tn: #{tn.round(3)}<br>"
end

puts "<br> E(Pistemäärä) = #{E.round(3)}"

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
  </body>
</html>"