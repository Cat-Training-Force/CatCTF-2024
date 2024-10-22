# 使用官方Python 3.12镜像作为基础镜像
FROM python:3.12-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录下的文件到容器中的/app目录
COPY . /app

# 删除不必要的文件
RUN rm -rf /app/Dockerfile

# 安装依赖项
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

RUN useradd -m webuser

RUN chown -R webuser:webuser /app && chmod -R a-w /app && chmod u+w /app/uploads && chmod u+x start.sh

# 暴露Flask应用的默认端口
EXPOSE 5001

# 切换到非root用户
USER webuser

# 启动Flask应用
CMD ["./start.sh"]
