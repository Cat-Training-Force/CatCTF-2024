# 使用官方Python 3.12镜像作为基础镜像
FROM python:3.12-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录下的文件到容器中的/app目录
COPY . /app

RUN rm -rf /app/Dockerfile /app/instance

# 安装依赖项
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 暴露Flask应用的默认端口
EXPOSE 5000

# 启动Flask应用
CMD ["python", "app.py"]
