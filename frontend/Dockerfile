# Используем официальный образ Nginx
FROM nginx:alpine

# Копируем содержимое директории frontend в контейнер
COPY . /usr/share/nginx/html

# Копируем конфигурацию nginx (если у вас есть кастомная конфигурация)
COPY nginx.conf /etc/nginx/conf.d/default.conf
