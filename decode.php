<?php
    $encode = 'a1zLbgQsCESEIqRLwuQAyMwLyq2L5VwBxqGA3RQAyumZ0tmMvSGM2ZwB4tws';
    $decode = str_rot13($encode);
    echo $decode.'<br>';
    $orig = strrev($decode);
    echo $orig.'<br>';
    $decode = base64_decode($orig);
    echo $decode.'<br>';
    $orig = '';
    for ($i = 0; $i < strlen($decode); $i++) {
        $c = substr($decode, $i, 1);
        $ascii = ord($c) - 1;
        $c = chr($ascii);
        $orig = $orig.$c;
    }
    echo $orig.'<br>';
    echo strrev($orig);
?>