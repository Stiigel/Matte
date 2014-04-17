<?php

function arvo_vari() {
  global $kuva, $vari;
  $r = mt_rand(0, 255);
  $g = mt_rand(0, 255);
  $b = mt_rand(0, 255);
  $vari = imagecolorallocate($kuva, $r, $g, $b);
}

$siv = 50;
$vari;

$kuva = imagecreate($siv, $siv);

arvo_vari();
arvo_vari();
imagefilledrectangle( $kuva, 0, 0, $siv/2 - 1, $siv/2 - 1, $vari);
arvo_vari();
imagefilledrectangle( $kuva, $siv/2, 0, $siv, $siv/2 - 1, $vari);
arvo_vari();
imagefilledrectangle( $kuva, 0, $siv/2, $siv/2 - 1, $siv, $vari);
arvo_vari();
imagefilledellipse( $kuva, $siv/2, $siv/2, $siv/2, $siv/2, $vari);

header("Content-Type:image/png");
imagepng($kuva);