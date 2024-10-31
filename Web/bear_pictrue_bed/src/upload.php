<?php
if ($_FILES['file']['error'] === UPLOAD_ERR_OK) {
    $uploadDir = 'uploads/';
    $uploadedFile = $uploadDir . basename($_FILES['file']['name']);
    
    $fileExtension = strtolower(pathinfo($_FILES['file']['name'], PATHINFO_EXTENSION));

    $BlackList = array('php');

    if (in_array($fileExtension, $BlackList)) {
        echo "你想对熊老师做什么！";
    } elseif (move_uploaded_file($_FILES['file']['tmp_name'], $uploadedFile)) {
        echo "文件上传成功！\n";
        echo "文件路径：" . $uploadedFile;
    } else {
        echo "文件上传失败。";
    }
} else {
    echo "文件上传错误：" . $_FILES['file']['error'];
}

?>
