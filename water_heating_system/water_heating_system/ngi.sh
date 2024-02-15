#!/bin/bash

# Переменные
PROJECT_NAME="water_heating_system"
PROJECT_PATH="$HOME/Stydu/Work/water_heating_system"
NGINX_CONF_PATH="/usr/local/etc/nginx/servers"
GUNICORN_SOCK="/tmp/$PROJECT_NAME.sock"
GUNICORN_PORT=8000 # Используйте порт, на котором будет запущен Gunicorn

# Создать конфигурационный файл Nginx для проекта
NGINX_CONF_FILE="$NGINX_CONF_PATH/$PROJECT_NAME"

echo "Создание конфигурационного файла Nginx для проекта $PROJECT_NAME"

if [ ! -d "$NGINX_CONF_PATH" ]; then
  echo "Создание директории $NGINX_CONF_PATH"
  sudo mkdir -p "$NGINX_CONF_PATH"
fi

# Запись конфигурации в файл
cat << EOF | sudo tee $NGINX_CONF_FILE > /dev/null
server {
    listen 80;
    server_name localhost;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        alias $PROJECT_PATH/static/;
    }

    location / {
        proxy_pass http://127.0.0.1:$GUNICORN_PORT;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }
}
EOF

echo "Конфигурация Nginx для $PROJECT_NAME создана."

# Перезапуск Nginx
echo "Перезапуск Nginx..."
sudo nginx -s reload

# Запуск Gunicorn
echo "Запуск Gunicorn для $PROJECT_NAME..."
cd $PROJECT_PATH
gunicorn --workers 3 --bind 0.0.0.0:8000 $PROJECT_NAME.wsgi:application &

echo "Скрипт завершён."