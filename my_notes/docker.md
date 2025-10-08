# Overview

Container = running instance of application + environment
Image = application + environment

Docker is a popular tool for creating images and running containers.

Containers are much more lightweight than VMs, making them ideal for
deployment and production.

## Commands

`docker build [-t IMAGENAME:TAGNAME --progress=plain --no-cache] .`

- Builds a Docker image given a directory with a Dockerfile.
- Can specify an image and tag name.
- `.` use Dockerfile in current directory.
- other args are useful for debugging

`docker run -p 8000:8000 -v __:__ --name CONTAINERNAME -d IMAGENAME`




