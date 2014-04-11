<?php
// http://wedi.dy.fi/matte/bufkuv.php
function kirjoita($kuva, $rivi, $teksti, $vari) {  

  for( $i = 0; $i < strlen("{$teksti}"); $i++) {
    imagechar($kuva, 5, $i * 10 + 30, $rivi, "{$teksti[$i]}", $vari);
  }
}

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

$lautLev = 80;

$risteavat = 0;
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
// imagerectangle($kuva, 50, 50, 400, 400, $mus);

$todnak = $risteavat / $maara;

imagefilledrectangle($kuva, 0, $lev, $lev, $kor, $vih);

$kissa = "Olen kissojen kauhu";

kirjoita($kuva, 550, "Risteavat tikut: {$risteavat}", $mus);
kirjoita($kuva, 570, "Todennakoisyys: {$risteavat} / {$maara} =  {$todnak}", $mus);

header("Content-Type:image/png");
imagepng($kuva);