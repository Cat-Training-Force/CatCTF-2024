<?php

error_reporting(0);

highlight_file(__FILE__);

if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/fl|a|c|system|php|sort|shell|exec|\.| |\'/i", $c)){
        eval($c);
    }
}