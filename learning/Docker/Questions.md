Questions that you should know the answer to at the end of the study block:
1. What came before containerization? Compare "Bare Metal" deployments to Virtual Machines.    
 What is the "Matrix of Hell" in software deployment, and how did it lead to the need for containers?
2. Is a container a mini-OS or just a fancy process? Research the role of the Linux Kernel in making containers possible.
3. Why did Docker become the industry standard over other container technologies like LXC (Linux Containers)? What was the "magic" Docker added to the existing tech?
4. Research the "Lifecycle" of a container. What is the difference between a container that is Sumbitted, Running, Stopped, and Paused?
5. If an image is a "blueprint," where is it actually stored when you aren't using it? Research Docker Hub and the concept of a "Registry."
6. How does Docker use "Copy-on-Write" (CoW) strategy? If you delete a file in a top layer that existed in a bottom layer, does the image actually get smaller?
7. What happens behind the scenes when you run docker build? Research the role of the "Docker Daemon" (the engine) during this process.
8. What is the process/processes to create an image and run a container from it?
9. What is a Dockerfile?
10. Every command in a Dockerfile creates a layer. Why is it a common practice to combine commands (like apt-get update && apt-get install) into a single line?
11. What is the difference between Linux PID1 and a container PID1?
12. What is the difference between docker run and docker start? Why does one create a new container while the other resumes an old one?
13. Research the ENTRYPOINT vs. CMD instructions. Both seem to start the application, but how do they behave differently when you pass arguments to the container?
14. When managing a "Microservices" architecture, why is manual container management considered "anti-pattern"? How does Compose handle the "Order of Execution" (e.g., making sure the Database starts before the App)?
15. What is a bridge?
16. What is "Isolation" in a Docker network? Research how a container on a Bridge network communicates with the outside internet vs. how it communicates with another container on the same host.
17. Beyond run and stop, research docker system prune. Why is this command considered the "janitor" of the Docker world, and what are the risks of running it?
18. If a container is running but the app inside is crashing, how do you "remote in" to see what's happening? Research the docker exec command and how it differs from docker logs.
19. How do you debug a container?
20. Look up the "Principle of Least Privilege." Why should you never run your application inside a container as the root user?
21. In a cloud environment where many users share one physical server, how does Docker use Control Groups (cgroups) and Namespaces to ensure one user's container doesn't steal all the CPU from another?
