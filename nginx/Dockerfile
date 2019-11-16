FROM nginx:1.17.4-alpine

EXPOSE 80
EXPOSE 443

COPY keys /etc/nginx/keys

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d