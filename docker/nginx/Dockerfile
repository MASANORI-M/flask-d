# FROM nginx:latest

FROM amazonlinux:2023

RUN yum -y update

# install nginx
RUN yum -y install nginx

COPY nginx.conf /etc/nginx/conf.d/default.conf

CMD ["/usr/sbin/nginx", "-g", "daemon off;"]