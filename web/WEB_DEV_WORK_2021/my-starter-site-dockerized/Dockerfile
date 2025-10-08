# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/go/dockerfile-reference/

# Want to help us make this template better? Share your feedback here: https://forms.gle/ybq9Krt8jtBL3iCk7

################################################################################
# Pick a base image to serve as the foundation for the other build stages in
# this file.
# nginx is defacto image. nginx:alpine is a lighter image.
# https://hub.docker.com/_/nginx

# TODO only index page is loading.
# https://stackoverflow.com/questions/66594111/why-does-nginx-think-my-root-directory-is-usr-share-nginx-and-not-var-www-html

FROM nginx AS base

# Copy all files in the project root to the container
COPY . /usr/share/nginx/html

