# Orchestration

## Overview

The next step in the evolution of containers was merging containerization with the concept of scale.
The result of which is Kubernetes, or K8S for short.

### The Move to the Cloud

The move to the Cloud wasn't just about moving code from a server in your office to a server in Amazon's data center. It was a fundamental shift in infrastructure philosophy.

#### The "Ephemeral" Reality

In a traditional data center, a server was stable. In the Cloud, instances (Virtual Machines) are **ephemeral**—they are designed to be temporary. A cloud provider might restart your instance for maintenance, or the hardware underneath might fail.

#### The Problem with "Just Containers" in the Cloud

If you run a single Docker container on a Cloud instance:

- **The "Death" Problem**: If that cloud instance goes down, your container dies. There is no one to notice it's gone and no one to turn it back on.

- **The "Networking" Problem**: Cloud instances get new IP addresses when they restart. If App A needs to talk to App B, it will lose the connection every time the cloud shifts.

- **The "Waste" Problem**: If you rent a massive 64GB Cloud instance but only run a 2GB container on it, you are throwing away money every second.

### Orchestration: The Manager of Thousands

As companies adopted **Microservices** (breaking one big app into 50+ tiny containers), manual management became impossible. You don't need a "script"; you need a **system**.

**Orchestration** is the automated coordination of container lifecycles. It answers the "Four Whos" of the Cloud:

- **Placement**: *Who* decides which of my 100 cloud servers has enough room for this new container?

- **Health**: *Who* restarts the container at 3:00 AM if it crashes?

- **Scaling**: *Who* creates 10 more copies of the app when a million people visit the site?

- **Networking**: *Who* connects the users on the internet to the right container?

### Kubernetes (K8s): The "Cloud OS"

Kubernetes was born at Google (under the name *Project Borg*) to manage their billions of weekly container starts. They realized that the world needed a standardized way to talk to any cloud.

#### The Core Architecture: A Deep Dive

Kubernetes works on a **Cluster** model. A cluster consists of two main parts:

##### A. The Control Plane (The Brain)

This is the "boss" that makes decisions about the cluster.

- **API Server**: The front door. When you want to do something, you talk to this.

- **etcd**: The "brain's memory." A high-speed database that stores the state of every single thing in the cluster.

- **Scheduler**: The "matchmaker." It looks at a new container and finds a server (Node) with enough empty CPU and RAM to hold it.

- **Controller Manager**: The "policeman." Its only job is to make sure the *current state* matches the *desired state*. (e.g., "I told you to run 3 copies, but I only see 2. I'll start a 3rd now.")

##### B. The Nodes (The Workers)

These are the actual Cloud instances (VMs) where your code runs.
- **Kubelet**: An agent that runs on every node. It's like a foreman taking orders from the Control Plane and making sure the containers are actually running.

- **Pods**: This is a key K8s concept. You don't run containers directly; you run **Pods**. A Pod is a wrapper for one or more containers. It's the smallest unit Kubernetes deals with.

#### The Magic of "Declarative" Management

This is a very important concept to understand the way K8s operates. It is the core foundational concept of its API.

- **Imperative (Old way)**: You give a list of commands: "Start a server, install Docker, run this image, open port 80." If any step fails, the whole thing breaks.

- **Declarative (Kubernetes way)**: You provide a Manifest (a YAML file). You simply say: *"I want 5 copies of this app running on Port 80."* Kubernetes handles the "how." If a server catches fire, K8s sees that you now only have 4 copies. Because your "Desired State" is 5, it automatically starts a new one on a different server. This is called **Self-Healing**.

#### Why K8s Specifically

Before 2017, there were other orchestrators (Docker Swarm, Mesos). Kubernetes won over them because:
- **Cloud Agnostic**: You can run K8s on AWS, then move it to Google Cloud or your own hardware without changing your code. It prevents "Vendor Lock-in."

- **Extensibility**: You can add "Custom Resources." If K8s doesn't do something you need, you can teach it how.

- **The Ecosystem**: Every major cloud provider now offers a **Managed Kubernetes Service** (like AWS EKS or Google GKE), meaning they manage the "Brain" for you, and you just worry about your apps.

## Goals

Under the subject of Kubernetes, we will touch upon, and you will learn, the following:
- Scale
- Cloud environment
- Cluster
- Cluster architecture
- Orchestration
- Nodes
- Infra nodes
- Master nodes
- Worker Nodes
- Pods
- Controllers
- Custom Resource
- CRD
- Ingress
- Services
- Volumes
- PVC
- Storage classes
- Configmap
- Secret
- Probes
- Deployment
- DaemonSet
- ReplicaSet
- StatefulSet
- RBAC
- K8S declarative API

## Outcome

A list of questions you should be able to answer at the end of this study block:

### Cloud and Orchestration
1. How does the "Ephemeral" nature of the Cloud change the way we approach application uptime compared to traditional on-premise servers?
2. Why is the "Cattle vs. Pets" analogy fundamental to understanding why we need orchestration in a cloud environment?
3. In your own words, describe the exact moment a company grows out of "just using Docker" and begins to actually need an orchestrator like Kubernetes.
4. How does Kubernetes solve the problem of "Vendor Lock-in" when a company wants to move from AWS to Google Cloud or Azure?
5. What are the pros and cons of developing for cloud environments?
6. When would a team be better off *not* adopting Kubernetes, and sticking with something simpler like Docker Compose or a managed PaaS instead?

### Cluster Architecture & Nodes
1. If the Control Plane (Master Nodes) is the "brain" of the cluster, what happens to the currently running applications if that brain temporarily loses power?
2. Compare and contrast the responsibilities of a Master Node versus a Worker Node. Who does the "thinking" and who does the "doing"?
3. What is the role of the Kubelet, and why is it considered the "foreman" of the individual worker node?
4. In a large-scale environment, why might an organization choose to have dedicated Infra Nodes for logging and monitoring instead of putting everything on Worker Nodes?
5. Explain the relationship between a Cluster and a Node. How does Kubernetes make multiple physical servers look like one giant pool of resources?

### Pods & Workload Controllers
1. Why does Kubernetes use Pods as the smallest unit of deployment instead of just running containers directly?
2. If you need to ensure that every single node in your cluster runs a specific logging agent, would you use a Deployment or a DaemonSet? Why?
3. How does a ReplicaSet act as the "policeman" for your application's availability?
4. What is the primary difference between a Deployment (for stateless apps like a web server) and a StatefulSet (for databases)?
5. Describe how a Controller uses a "reconciliation loop" to move the cluster from its current state to the desired state.

### Networking & Traffic (Services & Ingress)
1. Since Pods are frequently destroyed and recreated with new IP addresses, how does a Service provide a "permanent mailbox" for other apps to find them?
2. Think of a Service as an internal phone extension and an Ingress as the front door of the building. How do they work together to get a user from the internet to your code?
3. What are the risks of exposing a Pod directly to the internet without using the Kubernetes networking layer?

### Storage & Persistence (Volumes)
1. If a container is deleted, the data inside it is lost forever. How do Persistent Volume Claims (PVC) and Storage Classes break this cycle?
2. Explain the "Contract" metaphor: How is a PVC like a voucher that a developer gives to the cluster to request a specific amount of storage?
3. Why is the Storage Class important for cloud portability? (e.g., switching from Amazon EBS to Google Persistent Disk).

### Configuration, Secrets, & Security
1. Why is it considered a major security risk to hardcode database passwords inside a container image instead of using a Kubernetes Secret?
2. How does a ConfigMap allow you to change the behavior of an application without having to rebuild the entire Docker image?
3. In terms of RBAC (Role-Based Access Control), why is the principle of "Least Privilege" vital when giving developers access to a cluster?

### Health & The Declarative API
1. Compare a Liveness Probe to a Readiness Probe. What happens if you mix them up?
2. What does it mean that the Kubernetes API is Declarative rather than Imperative? (Hint: Think about "the what" vs. "the how").
3. How do Custom Resources (CRs) and Custom Resource Definitions (CRDs) allow Kubernetes to manage things it wasn't originally built for, like a specific type of database or an SSL certificate?

### Scaling & Performance
1. Describe the chain of events that occurs when the Horizontal Pod Autoscaler (HPA) notices a spike in CPU usage on your web application.
2. How does the concept of "Bin Packing" in Kubernetes help a company lower their monthly Cloud bill?

### Links

Here is a list of recommended reading materials to help you understand K8S. Also, feel free to use the Goals list above to find what you need to read in the links.

**Intro**
- <https://www.geeksforgeeks.org/devops/introduction-to-kubernetes-k8s/>
- <https://www.baeldung.com/ops/kubernetes>

**From the K8S Docs**
- <https://kubernetes.io/docs/concepts/overview/components/>
- <https://kubernetes.io/docs/concepts/architecture/>
- <https://kubernetes.io/docs/concepts/containers/>
- <https://kubernetes.io/docs/concepts/workloads/pods/>
- <https://kubernetes.io/docs/concepts/workloads/controllers/>
- <https://kubernetes.io/docs/concepts/services-networking/>
- <https://kubernetes.io/docs/concepts/storage/>
- <https://kubernetes.io/docs/concepts/configuration/>
- <https://kubernetes.io/docs/concepts/scheduling-eviction/>

**Full-On Guide**
- <https://www.baeldung.com/ops/kubernetes-series>

**Videos**

*Kubernetes Crash Course*
- <https://www.youtube.com/watch?v=X48VuDVv0do&pp=ygUDazhz>

*K8S Architecture*
- <https://www.youtube.com/watch?v=T4Z7visMM4E&t=1238s&pp=ygUDazhz>
- <https://www.youtube.com/watch?v=xj_GjnD4uyI&t=1050s&pp=ygUDazhz>
