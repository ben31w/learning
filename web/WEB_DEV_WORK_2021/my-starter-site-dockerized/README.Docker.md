# Overview
This project is a copy of my-starter-site with some modifications to 
run the site in a Docker container based off an nginx image.
- Ran the command `docker init`.
- Modified some of the Dockerfile and compose.yaml to use nginx and map 
the appropriate files from project to container.
- Great tutorial: https://medium.com/@ayushjung63/hosting-web-pages-in-nginx-server-with-docker-95bd7ba0b5a1

----End my notes----

### Building and running your application

When you're ready, start your application by running:
`docker compose up --build`.

### Deploying your application to the cloud

First, build your image, e.g.: `docker build -t myapp .`.
If your cloud uses a different CPU architecture than your development
machine (e.g., you are on a Mac M1 and your cloud provider is amd64),
you'll want to build the image for that platform, e.g.:
`docker build --platform=linux/amd64 -t myapp .`.

Then, push it to your registry, e.g. `docker push myregistry.com/myapp`.

Consult Docker's [getting started](https://docs.docker.com/go/get-started-sharing/)
docs for more detail on building and pushing.