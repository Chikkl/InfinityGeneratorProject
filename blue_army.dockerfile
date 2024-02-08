# Используем Alpine Linux в качестве базового образа
FROM alpine

# Обновляем пакеты в Alpine
RUN apk update && apk upgrade

# Устанавливаем необходимые пакеты для работы с SSH
RUN apk add openssh-server

# Генерируем SSH ключи
RUN ssh-keygen -A

# Настраиваем SSH
RUN mkdir /var/run/sshd
RUN echo 'root:password' | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Очищаем кеш пакетов
RUN rm -rf /var/cache/apk/*

# Открываем порт 22 для SSH
EXPOSE 22

# Запускаем SSH сервер при старте контейнера, указывая порт
CMD ["/usr/sbin/sshd", "-D", "-p", "22"]

