<?php

error_reporting(0);
$flag = file_get_contents("/flag");

if(!session_id())
    session_start();

if(!isset($_SESSION['count']))
    $_SESSION['count']=0;

if(isset($_SESSION['answer']) && isset($_POST['answer'])){
    if(($_SESSION['answer'])!==$_POST['answer']){
        session_destroy();
        die('答案错误');
    }
    else{
        if(intval(time())-$_SESSION['time']<1){
            session_destroy();
            die('心急吃不了热豆腐');
        }
        if(intval(time())-$_SESSION['time']>3){
            session_destroy();
            die('来不及了...');
        }
        $_SESSION['count']++;
    }
}
if($_SESSION['count']>=10){
    session_destroy();
    echo $flag;
    die();
}


$num1 = mt_rand(1000,99999);
$num2 = mt_rand(100,99999);
$mode=rand(0,3);
$ans = 0;
switch($mode){
    case 0:
        $ans=$num1 + $num2;
        break;
    case 1:
        $ans=$num1 - $num2;
        break;
    case 2:
        $ans=$num1 * $num2;
        break;
    case 3:
        $ans=round($num1 / $num2);
        break;
}
$_SESSION['answer']=(string)$ans;
$_SESSION['time']=intval(time());
?>
<h1>听说你的数学水平极高，熊老师决定考考你</h1>
<p>在1~3秒内提交你的答案，答对10次可以获得flag</p>
<p>除法的结果四舍五入保留整数哦！</p>
<p> 你已经回答了 <?php echo $_SESSION['count'];?>个问题</p>

<form action="" method="post">
<?php
$sentence="";
switch($mode) {
    case 0:
        $sentence = "$num1 + $num2 = ";
        break;
    case 1:
        $sentence = "$num1 - $num2 = ";
        break;
    case 2:
        $sentence = "$num1 x $num2 = ";
        break;
    case 3:
        $sentence = "$num1 ÷ $num2 = ";
        break;
}
echo "<div"." class='question'>".$sentence."</div>";
?>
    <input type="text" name="answer">
    <input type="submit" value="提交">
</form>