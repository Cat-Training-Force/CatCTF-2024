# 使用一个基础的Apache镜像，同时包含PHP模块
FROM php:7.4-apache


COPY src/flag.sh /flag.sh
COPY src/ /var/www/html/


RUN chmod +x /flag.sh && \
    chmod +x /var/www/html/

# 暴露Apache默认的HTTP端口
EXPOSE 80

# 启用Apache的rewrite模块
RUN a2enmod rewrite
RUN /flag.sh

CMD ["/flag.sh"]
CMD ["apache2-foreground"]