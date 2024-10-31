<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>bear的图床</title>
    <style>
        body {
            background-image: url('1.jpg');
            background-size: cover;
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }

        .header {
            background-color: #888;
            padding: 10px;
            text-align: center;
        }

        .container {
            background-color: rgba(255, 255, 255, 0.7);
            padding: 20px;
            margin: 20px auto;
            max-width: 400px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
            text-align: center;
            position: relative; /* Added for positioning */
        }

        #inputArea {
            width: 100%;
            margin-top: 10px; /* Added for spacing */
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-sizing: border-box;
            background-color: #f5f5f5;
            text-align: left;
            overflow: auto; /* Added for scrolling if necessary */
        }

        #selectButton {
            background-color: #2196F3;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin-right: 10px;
            cursor: pointer;
            border-radius: 5px;
        }

        #uploadButton {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin-left: 10px;
            cursor: pointer;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>bear的图床</h1>
    </div>
    <div class="container">
        <input type="file" name="file" id="fileInput" style="display: none;" accept="*">
        <button type="button" id="selectButton">选择图片</button>
        <button type="submit" id="uploadButton">上传图片</button>
        <div id="inputArea">来给熊老师上传一点素材吧</div>
    </div>
    <script>
        const selectButton = document.getElementById('selectButton');
        const fileInput = document.getElementById('fileInput');
        const uploadForm = document.createElement('form'); // Create a form element dynamically
        uploadForm.enctype = 'multipart/form-data';
        uploadForm.action = 'upload.php';
        uploadForm.method = 'post';

        selectButton.addEventListener('click', () => {
            fileInput.click();
        });

        fileInput.addEventListener('change', () => {
            document.getElementById('inputArea').textContent = `已选择文件：${fileInput.files[0].name}`;
        });

        uploadForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            const formData = new FormData(uploadForm);

            // Remove file extension validation for now
            try {
                const response = await fetch('upload.php', {
                    method: 'POST',
                    body: formData
                });

                const data = await response.text();
                document.getElementById('inputArea').textContent = data;
            } catch (error) {
                document.getElementById('inputArea').textContent = '上传过程中出现错误。';
            }
        });

        // Append buttons to the dynamically created form
        uploadForm.appendChild(fileInput);
        uploadForm.appendChild(selectButton);
        uploadForm.appendChild(document.getElementById('uploadButton'));

        // Append the dynamically created form to the container
        document.querySelector('.container').appendChild(uploadForm);
    </script>
</body>
</html>
