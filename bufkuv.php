<?php
// http://wedi.dy.fi/matte/bufkuv.php

$lev = 500;
$kor = 650;
$maara = 25;

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
  array_push($viivat, $i * $lautLev); 
  imageline($kuva, 0, $i * $lautLev, $lev, $i * $lautLev, $pun);
}

for($i = 0; $i < $maara; $i++) {  
  $tikkuPit = $lautLev/2;
  $tikkuX = rand(0 + $tikkuPit, $lev - $tikkuPit);
  $tikkuY = rand(0 + $tikkuPit, $lev - $tikkuPit);

  $tikkuRad = mt_rand(0, 314159265) / 100000000;
  $tikkuX2 = $tikkuX + (cos($tikkuRad) * $tikkuPit);
  $tikkuY2 = $tikkuY + (sin($tikkuRad) * $tikkuPit);
  
  $rist = false;
  foreach( $viivat as $viiva) {
    if( $tikkuY > $viiva && $tikkuY2 < $viiva) {
      $risteavat++;
      $rist = true;
    }
    else if ( $tikkuY2 > $viiva && $tikkuY < $viiva) {
      $risteavat++;
      $rist = true;
    }
  }
    
  if($rist) imageline($kuva, $tikkuX, $tikkuY, $tikkuX2, $tikkuY2, $kel);
  else imageline($kuva, $tikkuX, $tikkuY, $tikkuX2, $tikkuY2, $vih);  
}

imagerectangle($kuva, $tikkuPit, $tikkuPit, $lev - $tikkuPit, $lev - $tikkuPit, $har);

imagefilledrectangle($kuva, 0, $lev, $lev, $kor, $vih);

$todnak = $risteavat / $maara;
$fontti = "Inconsolata-Bold.ttf";

$teksti = "Risteävät tikut: {$risteavat}";
imagettftext($kuva, 13, 0, 30, 550, $mus, $fontti, $teksti);
$teksti = "Todennäköisyys: {$risteavat} / {$maara} = {$todnak}";
imagettftext($kuva, 13, 0, 30, 570, $mus, $fontti, $teksti);


header("Content-Type:image/png");
imagepng($kuva);