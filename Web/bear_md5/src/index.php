<?php
error_reporting(0);
show_source(__FILE__);

// flag在flag.php里



// 听说你刚学了php，熊老师决定来考一考你。

$cat = $_GET['cat'];

$ctf = $_GET['ctf'];

if(!($cat != $ctf && md5($cat) == md5($ctf))){
    die("你听说过php弱类型比较吗？");
}

// 不错哦！熊老师对你表示赞许，接下来要加大难度了
$bear = $_POST['bear'];

$kangaroo = $_POST['kangaroo'];

if (!($bear !== $kangaroo && md5($bear) === md5($kangaroo))) {

die('有什么类型的值是强比较下也相同的?');

} 

// 看来你学的不错，flag给你了

$file = $_GET['file'];
include($file);
// flag.php中真的什么都没有吗？怎么拿出来呢？