require 'cgi'
cgi = CGI.new
puts cgi.header
puts "<meta charset=\"utf-8\">"
maat = ["hertta", "ruutu", "risti", "pata"]

maara = 10
kutoset = 0
punaiset = 0

for i in 0..maara
  noppa = rand(6) + 1
  if noppa == 6
    kutoset += 1
  end
  
  puts "#{noppa}<br>"
  maa = rand(4)
  arvo = rand(13) 
  
  if maa < 2
    punaiset += 1
  end
    
  puts "#{maat[maa]} #{arvo + 1}<br>"
end

puts "<br>"

puts "punaiset #{punaiset}<br>"
puts "kutoset #{kutoset}<br>"


kutTTN = kutoset/maara.to_f
kutOTN = 1 / 6.to_f
punTTN = punaiset/maara.to_f
punOTN = 2 / 4.to_f

yhtTTN = 1 - (kutTTN * punTTN)

yhtOTN = 1 - (kutOTN * punOTN)

puts "Kutosten tilast. TN: #{kutTTN}<br>"
puts "Kutosten oikea TN: #{kutOTN}<br>"
puts "Punaisten tilast. TN: #{punTTN}<br>"
puts "Punaisten oikea TN: #{punOTN}<br>"
puts "Punainen kortti TAI kutonen silmäluku<br>"
puts "Tilast TN: #{yhtTTN}<br>"
puts "Oikea TN: #{yhtOTN}<br>"