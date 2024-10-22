# 使用官方Python 3.12镜像作为基础镜像
FROM python:3.12-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录下的文件到容器中的/app目录
COPY . /app

# 删除不必要的文件
RUN rm -rf /app/Dockerfile /app/exp.py

# 安装依赖项
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 创建一个非root用户，避免以root权限运行应用
RUN useradd -m webuser

# 确保 /app 目录的权限设置：删除写权限，但保留 /app/uploads 的写权限
RUN chown -R webuser:webuser /app && chmod -R a-w /app && chmod u+w -R /app/uploads && chmod u+x start.sh

# 暴露Flask应用的默认端口
EXPOSE 5001

# 切换到非root用户
USER webuser

# 启动Flask应用
CMD ["./start.sh"]
