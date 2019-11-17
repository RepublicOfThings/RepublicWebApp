FROM nginx:1.17.4-alpine

EXPOSE 80
EXPOSE 443

RUN rm /etc/nginx/conf.d/default.conf

COPY /keys /etc/nginx/keys

COPY /nginx/nginx.conf /etc/nginx/conf.d
