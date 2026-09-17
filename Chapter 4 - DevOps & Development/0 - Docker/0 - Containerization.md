# Containerization

## Overview

To familiarize yourself with the practical application of Docker, visit <https://www.docker.com/101-tutorial/> and go through the tutorial. It will help you get started and prepare yourself for the next exercise where you will have to run things from scratch.

### The Era of Containerization

The concept of containerization evolved from the Linux Kernel.
Containers are what developed after VMs to meet the growing need of the industry.
Before understanding what a container is, let's first understand its counterpart component.

#### The Image (The Blueprint)

Let's think of an Image as a **frozen snapshot of a computer system**.
It is a lightweight, standalone, executable package that includes everything needed to run a piece of software:
code, runtime, system tools, libraries, and settings.
**It's Immutable**: Once an image is created, it cannot be changed.
If you need to update your software that is of an older version to a newer version, you don't "patch" the image; you build a new one.
**Layered Architecture**: Images are built in layers. If you have an Ubuntu layer and a Java layer,
and you want to run two different apps, each image layer is only stored once.

#### Then, What is a Container? (the Living Instance)

If the Image is the blueprint for a house, the Container is the actual house.
A container is a **running instance of an image**.
It is an isolated process on your machine that feels like a separate computer but shares the host's resources.
The "Magic": When you stop a container, it disappears, but the image remains ready to spawn a 100% identical container whenever you need it.

##### Why is it "Good"? (The Core Benefits)

- Beyond solving the problems VMs didn't, containers provide three "Superpowers":
1. **Density**: Because containers don't have their own OS, you can run 10x to 50x more containers on a single server than you could with VMs.
2. **Portability**: The phrase "standardized unit of software" is key. A container runs exactly the same on a developer's laptop, a test server, and a massive cloud cluster.
3. **Isolation**: If an application running in one container crashes or consumes too much memory, it won't crash the other applications running on the same machine. It is "sandboxed."

- Containers use two specific features of the Linux Kernel to provide isolation without needing a full Guest OS:
1. **Chroot (1979)**: The oldest ancestor; it changed the root directory for a process, isolating it from the rest of the filesystem.
2. **Cgroups (Control Groups)**: Developed by Google in 2006. They manage and limit hardware resources (CPU, RAM, I/O) for a process.
3. **Namespaces**: These provide the "illusion" of isolation. They hide other processes, network interfaces, and user IDs from the container.

- Unlike VMs, containers share the **Host OS Kernel**. This makes them:
1. **Lightweight**: Megabytes instead of Gigabytes.
2. **Instant**: They boot in seconds (or milliseconds).
3. **Portable**: "It works on my machine" finally became "It works everywhere."

#### Why Did We Move Toward Containerization? The Problems VMs Didn't Solve

While Virtual Machines (VMs) were a massive leap forward from bare metal, they were a "heavyweight" solution to a "lightweight" problem.
Even with VMs, several critical friction points remained that eventually forced the industry toward containerization.

##### The "Resource Tax" (Hypervisor Overhead)

In a VM environment, every single application requires a full Guest Operating System (OS).
**The Problem**: If you want to run a simple Python script, you have to boot a 2GB Linux OS just to support it.
This Guest OS consumes CPU, RAM, and Storage before your application even starts.
**Why VMs didn't fix it**: The Hypervisor must emulate hardware for every VM.
If you have 10 VMs, you are running 10 kernels, 10 sets of system libraries, and 10 window managers (if applicable).
This "tax" limits how many apps you can cram onto one physical server.

##### Slow Scaling and "Cold Starts"

VMs are virtualized hardware. To start a VM, the system must go through a full BIOS boot, kernel initialization, and service startup.
**The Problem**: This process takes minutes.
**The Persistence**: In the modern world of "Auto-scaling" (where you want to scale out during a data spike), waiting 3 minutes for a VM to boot is too slow.
You lose data or experience lag while the "hardware" is "powering on."
**The Container Fix**: Containers share the Host Kernel, so starting one is just like starting a new tab in a browser—it happens in milliseconds.

##### The "Environmental Drift" (Configuration Management)

VMs solved hardware isolation but failed at software environment consistency.
**The Problem**: VMs are often treated like "pet" servers.
Over time, an admin might log into VM-Production-01 to update a security patch or change a Java setting, but forget to do it on VM-Production-02.
**Why VMs didn't fix it**: Because a VM is a persistent, stateful OS, it "drifts" away from its original configuration.
This leads to the classic: "It works in the Staging VM, why is it crashing in the Production VM?"
**The Container Fix**: Containers are immutable. You don't "update" a container;
You throw it away and start a new one from a standard Image. This ensures 100% parity across environments.

##### Poor Developer-to-Production Parity

The size of VM files makes them nearly impossible for developers to use locally.
**The Problem**: A VM image is usually 20GB to 100GB.
**The Persistence**: A developer cannot easily download a 50GB production VM to their laptop to debug a piece of code.
Consequently, developers write code on their local Mac/Windows OS and "hope" it works when moved to the Linux VM in the cloud.
**The Container Fix**: Because Docker images use a "Layered File System," they are tiny.
A developer can pull a 200MB software-specific image in seconds, ensuring they are coding in the exact environment where the code will live.

##### Dependency Conflict (Within the VM)

If you decided to save resources by running multiple apps inside a single large VM, you were right back to "Bare Metal" problems.
**The Problem**: App A needs Java 11, but App B (perhaps your Flink job) needs Java 17.
**Why VMs didn't fix it**: You either had to create a whole new heavy VM (wasteful)
or deal with the headache of managing multiple environment variables and paths within one OS (complex).
**The Container Fix**: Each container has its own isolated file system.
You can run 10 containers on one host, each with a different version of Java, and they will never "see" or interfere with each other.

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

1. What came before containerization? Compare "Bare Metal" deployments to Virtual Machines.
 What is the "Matrix of Hell" in software deployment, and how did it lead to the need for containers?
2. Is a container a mini-OS or just a fancy process? Research the role of the Linux Kernel in making containers possible.
3. Why did Docker become the industry standard over other container technologies like LXC (Linux Containers)? What was the "magic" Docker added to the existing tech?
4. Research the "Lifecycle" of a container. What is the difference between a container that is Submitted, Running, Stopped, and Paused?
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
