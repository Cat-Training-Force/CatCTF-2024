FROM python:3.11-alpine

ENV PYTHONUNBUFFERED=0

RUN echo "http://mirrors.ustc.edu.cn/alpine/v3.5/main" > /etc/apk/repositories
RUN echo "http://mirrors.ustc.edu.cn/alpine/v3.5/community" >> /etc/apk/repositories

COPY src/requirements.txt /tmp
RUN pip install --no-cache-dir -r /tmp/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
# Creating working directory
RUN mkdir /app
COPY src/ /app

RUN adduser -S appuser
RUN chmod -R 755 /app/
RUN chmod +x /app/start.sh
USER appuser

EXPOSE 5000

WORKDIR /app
CMD ["sh","/app/start.sh"]