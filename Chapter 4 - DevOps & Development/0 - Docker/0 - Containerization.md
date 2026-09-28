# Containerization

## Overview

To familiarize yourself with the practical application of Docker, visit <https://www.docker.com/101-tutorial/> and go through the tutorial. It will help you get started and prepare yourself for the next exercise where you will have to run things from scratch.

Containers are the next step after the Virtual Machines you met in Chapter 0.

## Goals

Here is a list of concepts that you will have to learn about and research that fall under the banner of Docker. It is important to understand these, as they will become your foundation to learning more subjects that will build and expand upon this.

- What came before containerization
- Containerization
- Docker
- Container
- Image
- Image layers
- The process of building an image
- Adding layers to an image
- Using an image
- Dockerfile
- Docker Compose
- Network
- Common Docker commands
- Debugging a container
- Docker best practices
- Noisy Neighbors and multi-tenant environments

## Outcome

Questions that you should know the answer to at the end of the study block:

1. What came before containerization? Compare "Bare Metal" deployments to Virtual Machines. What is the "Matrix of Hell" in software deployment, and how did it lead to the need for containers?
2. Is a container a mini-OS or just a fancy process? Research the role of the Linux Kernel in making containers possible.
3. Why did Docker become the industry standard over other container technologies like LXC (Linux Containers)? What was the "magic" Docker added to the existing tech?
4. Research the "Lifecycle" of a container. What states can a container be in, and what moves it from one state to another?
5. If an image is a "blueprint," where is it actually stored when you aren't using it? Research Docker Hub and the concept of a "Registry."
6. How does Docker use "Copy-on-Write" (CoW) strategy? If you delete a file in a top layer that existed in a bottom layer, does the image actually get smaller?
7. What happens behind the scenes when you run docker build? Research the role of the "Docker Daemon" (the engine) during this process.
8. What is the process/processes to create an image and run a container from it?
9. What is a Dockerfile?
10. Which Dockerfile instructions add a new layer to the image? Why is it a common practice to combine commands (like apt-get update && apt-get install) into a single `RUN` instruction?
11. What is the difference between Linux PID 1 and a container's PID 1? How does that affect the way your app handles the signals sent by `docker stop`?
12. What is the difference between `docker run` and `docker start`?
13. Research the ENTRYPOINT vs. CMD instructions. Both seem to start the application, but how do they behave differently when you pass arguments to the container?
14. When managing a "Microservices" architecture, why is manual container management considered "anti-pattern"? How does Compose handle the "Order of Execution" (e.g., making sure the Database starts before the App)?
15. What is a bridge?
16. What is "Isolation" in a Docker network? Research how a container on a Bridge network communicates with the outside internet vs. how it communicates with another container on the same host.
17. Beyond run and stop, research `docker system prune`. What does it clean up, and what are the risks of running it?
18. If a container is running but the app inside is crashing, how do you "remote in" to see what's happening? Research the `docker exec` command and how it differs from `docker logs`. What else would you check when debugging a container?
19. Look up the "Principle of Least Privilege." What are the risks of running your application inside a container as the root user?
20. In a cloud environment where many users share one physical server, how does Docker make sure one user's container can't steal all the CPU from another, or even see its processes? Which of the kernel features from Chapter 0 make this possible?

### Links

Here you will find useful links that can help you base yourself onto the subjects:

**Containerization**

- <https://learn.microsoft.com/en-us/virtualization/windowscontainers/about/containers-vs-vm>

**Image**

- <https://kubernetes.io/docs/concepts/containers/images/>
- <https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-an-image/>
- <https://docs.docker.com/get-started/docker-concepts/building-images/>
- <https://aws.amazon.com/compare/the-difference-between-docker-images-and-containers/>

**Container**

- <https://www.docker.com/resources/what-container/>
- <https://www.redhat.com/en/topics/containers>
- <https://kubernetes.io/docs/concepts/containers/>

**Docker**

- <https://www.baeldung.com/ops/docker-guide>
- <https://www.geeksforgeeks.org/devops/introduction-to-docker/>
- <https://docs.docker.com/get-started/>
- <https://www.geeksforgeeks.org/devops/what-is-dockerfile-syntax/>
- <https://docs.docker.com/build/building/best-practices/>
- <https://www.digitalocean.com/community/tutorials/how-to-debug-and-fix-common-docker-issues>
- <https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-registry/>
- <https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-docker-compose/>

**Docker commands**

- <https://docs.docker.com/get-started/docker_cheatsheet.pdf>
- <https://www.geeksforgeeks.org/devops/docker-instruction-commands/>
- <https://www.bmc.com/blogs/docker-commands/>

**Videos**

- <https://www.youtube.com/watch?v=DQdB7wFEygo&t=384s>
- <https://www.youtube.com/watch?v=3c-iBn73dDE&t=5532s>
- <https://www.youtube.com/watch?v=gAkwW2tuIqE&t=293s>
