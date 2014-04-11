<?php
// http://wedi.dy.fi/matte/bufkuv.php

$lev = 500;
$kor = 650;

if (isset($_REQUEST["maara"])) $maara = $_REQUEST["maara"];
else $maara = 25;

$kuva = imagecreate($lev, $kor);
$tausta = imagecolorallocate($kuva, 32, 99, 199);
$pun = imagecolorallocate($kuva, 100, 30, 29);
$vih = imagecolorallocate($kuva, 20, 210, 190);
$kel = imagecolorallocate($kuva, 250, 230, 19);
$mus = imagecolorallocate($kuva, 1, 2, 4);
$har = imagecolorallocate($kuva, 109, 112, 190);

$risteavat = 0;
$lautLev = 80;
$viivat = [];

for($i = 0; $i < $lev/$lautLev; $i++) {
  $y = $i * $lautLev + 10;
  array_push($viivat, $y); 
  imageline($kuva, 0, $y, $lev, $y, $pun);
}

for($i = 0; $i < $maara; $i++) {  
  $tikkuPit = $lautLev/2;
  $tikkuX = rand($tikkuPit, $lev - $tikkuPit);
  $tikkuY = rand($tikkuPit, $lev - $tikkuPit);
//   628318530
  $tikkuRad = mt_rand(0, 628318530) / 100000000;
  $tikkuX2 = $tikkuX + (cos($tikkuRad) * $tikkuPit);
  $tikkuY2 = $tikkuY + (sin($tikkuRad) * $tikkuPit);
  
  $rist = false;
  foreach( $viivat as $viiva) {
    if( $tikkuY >= $viiva && $tikkuY2 <= $viiva) {
      $risteavat++;
      $rist = true;
    }
    else if ( $tikkuY2 >= $viiva && $tikkuY <= $viiva) {
      $risteavat++;
      $rist = true;
    }
  }
    
  if($rist) imageline($kuva, $tikkuX, $tikkuY, $tikkuX2, $tikkuY2, $kel);
  else imageline($kuva, $tikkuX, $tikkuY, $tikkuX2, $tikkuY2, $vih);  
}

imagerectangle($kuva, $tikkuPit, $tikkuPit, $lev - $tikkuPit, $lev - $tikkuPit, $har);

imagefilledrectangle($kuva, 0, $lev, $lev, $kor, $vih);

$todnak = number_format($risteavat / $maara, 5);
$fontti = "Inconsolata-Bold.ttf";

imagettftext($kuva, 20, -5, 120, 530, $mus, $fontti, "Tikun heitto ohjelma");
$teksti = "Risteävät tikut: {$risteavat}";
imagettftext($kuva, 13, 0, 50, 580, $mus, $fontti, $teksti);
$teksti = "Todennäköisyys: {$risteavat} / {$maara} = {$todnak}";
imagettftext($kuva, 13, 0, 50, 600, $mus, $fontti, $teksti);


header("Content-Type:image/png");
imagepng($kuva);