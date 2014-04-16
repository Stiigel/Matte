require 'cgi'
cgi = CGI.new
puts cgi.header

E = 0
todnak = 1 / 6.to_f

for i in 1..6
  E += i * todnak
end
puts "E(Nopan arvo) = #{E}<br>"

maara = cgi['maara'].to_i

if maara > 50000
  maara = 50000
end

if maara <= 0
  maara = 30
end

summa = 0

for i in 0..maara
  luku = rand(6) + 1
  summa += luku
  puts "#{luku}<br>"
end

ka = summa / maara.to_f
print "ka. = #{ka}"