# Doing this locally
If you have a project with a Dockerfile, you can create an image
- `docker build -t IMAGENAME:TAGNAME .`
- Inside curr dir, build a docker image and give it a helpful IMAGENAME/TAGNAME.

If you have an image, you can run the image as a container and start/stop the container.
- `docker run -p 8080:8080 -p 5000:5000 -v /var/jenkins_home:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock --name jenkins -d jenkins-docker`
- Run the image on the given ports, with the given volumes mapped, with a helpful CONTAINERNAME

You can run Jenkins as a Docker container. (here's the project: `~/projects/learning/jenkins/jenkins-docker`)


# Doing this in DigitalOcean
For this demo, Jenkins runs as a Docker container on a Digital Ocean Droplet (162.243.40.233:8080)

ssh into the droplet

The Jenkins container has been created already, but you can start/stop it.

Inside Jenkins, we have a project for MY nodejsapp example app. This project may be running as a Docker container, but local to this computer (localhost:3000).


## Tips, commands, etc.
Don't be cheap, use a decent droplet (about $24/month)!!!!!!

Logging into DigitalOcean droplet
`ssh 162.243.40.233 -lroot`

DO THE FOLLOWING COMMANDS IN THE DROPLET...

You installed Jenkins in the Droplet using the script from Udemy: 
`wget https://raw.githubusercontent.com/wardviaene/jenkins-course/master/scripts/install_jenkins.sh`

Accessing Jenkins
http://162.243.40.233:8080/
admin password

Initialize and run container (use image jenkins/jenkins!!!!!!!!!!!)
- `docker run -d --name jenkins -p 8080:8080 -p 5000:5000 -v /var/jenkins_home jenkins/jenkins`
- `docker run -p 8080:8080 -p 5000:5000 -v /var/jenkins_home:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock --name jenkins -d jenkins-docker`

Stopping container
`docker stop CONTAINERNAME`

Starting exsiting container
`docker start CONTAINERNAME`

Deleting stopped containers
`docker system prune`

Deleting images
`docker rmi IMAGE`

Getting all containers
`docker ps -a`

Getting logs for a container
`docker logs -f CONTAINERID/NAME`

In case you need the default password
`cat /var/jenkins_home/secrets/initialAdminPassword`

After building and publishing a Docker image (ex: through buildAndPublish task in Jenkins), you can run the image as a container:
- `docker pull MY-IMAGE`
- `docker run --name MY_CONTAINER_NAME -p 3000:3000 -d MY-IMAGE`

Open terminal inside a container
`docker exec -it CONTAINERID bash`


## Tools
Jenkins has tools that can be configured. Manage Jenkins > Tools. 
You can install Maven, JDK, Gradle, Ant, Git, NodeJS.

## Jobs
Jenkins jobs are collections of build, test, and release steps.

You can create jobs through the Jenkins web UI (manual, no history, not preferred)
or you can create jobs programatically with Job DSL (automatic, version control, preferred)

Need Job DSL plugin. This lets you run DSL scripts as a build step. https://jenkinsci.github.io/job-dsl-plugin/

You would create a 'seed project' that when built, creates other jobs in Jenkins.

Give the seed project a Git repo with DSL scripts. Then provide the paths to the DSL scripts in your build steps.

The first build of the seed project should fail, because the DSL scripts need to be approved in Jenkins (go to Manage Jenkins -> In-Process Script Approval -> approve).

Depending on the steps in your DSL script, you may need to add credentials in Jenkins (go to Manage Jenkins) (e.g., you'd need Docker Hub credentials if you try to build and publish to Docker Hub).


## Pipelines
Allow you to write Jenkins build steps in code.

Automates Build-Test-Release

Similar to Jenkins Jobs DSL: both let you write CI/CD in code

Jenkins Jobs DSLs creates new jobs

Jenkins Pipelines is a job type that handles the build/test/deployment of one project.

Can be written in Jenkins DSL or Groovy

