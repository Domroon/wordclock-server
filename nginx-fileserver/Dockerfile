FROM nginx:latest

COPY ./index.html /usr/share/nginx/html/index.html
COPY ./nginx.conf /etc/nginx/conf.d/nginx.conf
COPY ./requests_test-v010.py /usr/share/nginx/html/wordclock/v010/requests_test-v010.py
COPY ./requests_test-v020.py /usr/share/nginx/html/wordclock/v020/requests_test-v020.py