# 使用一个基础的Apache镜像，同时包含PHP模块
FROM php:7.2.2-apache

# 将当前目录中的所有文件复制到Apache的默认网站目录

COPY src/flag.sh /flag.sh
COPY src/ /var/www/html/

RUN chmod +x /flag.sh && \
    chmod +x /var/www/html/ && \
    chmod 777 uploads/

# 暴露Apache默认的HTTP端口
EXPOSE 80

# 启用Apache的rewrite模块
RUN a2enmod rewrite
RUN /flag.sh

# 运行Apache
CMD ["apache2-foreground","/flag.sh"]