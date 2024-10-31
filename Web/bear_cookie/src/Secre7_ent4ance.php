<?php 
    if(!isset($_COOKIE['school'])){
        setcookie("school", "huangduligong", 0, "/Secre7_ent4ance.php");
}
?>
<!DOCTYPE html>
<html>
<head>
<style>
    body {
        margin: 0;
        padding: 0;
        background-image: url('1.jpg');
        background-size: cover;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }
    .output {
        font-size: 24px;
        color: white;
        text-align: center;
    }
</style>
</head>
<body>
<div class="output">
<?php

    if($_SERVER['HTTP_X_FORWARDED_FOR'] == '127.0.0.1' || $_SERVER['HTTP_X_FORWARDED_FOR'] == '0.0.0.0')
    {
        if($_COOKIE['school'] === 'tongji')
        {
            if($_SERVER['HTTP_USER_AGENT'] === 'Tongji Academic Browser')
            {
                echo getenv("GZCTF_FLAG");
            }
            else
            {
                echo "熊老师说，高贵的同济人用的浏览器当然必须是同济学术浏览器(Tongji Academic Browser)";
            }
        }
        else
        {
            echo "熊老师看了看你的Cookie，果然是黄渡理工的，你不是tongji人，你不配获得flag！";
    }
    }
    else{
        echo "什么，你居然找到入口了！但是请求不是从本地发出来的，你肯定不是tongji人！";
    }
?>
</div>
</body>
</html>
