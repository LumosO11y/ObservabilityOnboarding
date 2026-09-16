# Overview
A list of questions you should be able to answer at the end of this study block:

## Cloud and Orchestration
1. How does the "Ephemeral" nature of the Cloud change the way we approach application uptime compared to traditional on-premise servers?
2. Why is the "Cattle vs. Pets" analogy fundamental to understanding why we need orchestration in a cloud environment?
3. In your own words, describe the exact moment a company grows out of "just using Docker" and begins to actually need an orchestrator like Kubernetes.
4. How does Kubernetes solve the problem of "Vendor Lock-in" when a company wants to move from AWS to Google Cloud or Azure?
5. What are the pros and cons of developing for cloud environments?
6. 

## Cluster Architecture & Nodes
1. If the Control Plane (Master Nodes) is the "brain" of the cluster, what happens to the currently running applications if that brain temporarily loses power?
2. Compare and contrast the responsibilities of a Master Node versus a Worker Node. Who does the "thinking" and who does the "doing"?
3. What is the role of the Kubelet, and why is it considered the "foreman" of the individual worker node?
4. In a large-scale environment, why might an organization choose to have dedicated Infra Nodes for logging and monitoring instead of putting everything on Worker Nodes?
5. Explain the relationship between a Cluster and a Node. How does Kubernetes make multiple physical servers look like one giant pool of resources?

## Pods & Workload Controllers
1. Why does Kubernetes use Pods as the smallest unit of deployment instead of just running containers directly?
2. If you need to ensure that every single node in your cluster runs a specific logging agent, would you use a Deployment or a DaemonSet? Why?
3. How does a ReplicaSet act as the "policeman" for your application's availability?
4. What is the primary difference between a Deployment (for stateless apps like a web server) and a StatefulSet (for databases)?
5. Describe how a Controller uses a "reconciliation loop" to move the cluster from its current state to the desired state.

## Networking & Traffic (Services & Ingress)
1. Since Pods are frequently destroyed and recreated with new IP addresses, how does a Service provide a "permanent mailbox" for other apps to find them?
2. Think of a Service as an internal phone extension and an Ingress as the front door of the building. How do they work together to get a user from the internet to your code?
3. What are the risks of exposing a Pod directly to the internet without using the Kubernetes networking layer?

## Storage & Persistence (Volumes)
1. If a container is deleted, the data inside it is lost forever. How do Persistent Volume Claims (PVC) and Storage Classes break this cycle?
2. Explain the "Contract" metaphor: How is a PVC like a voucher that a developer gives to the cluster to request a specific amount of storage?
3. Why is the Storage Class important for cloud portability? (e.g., switching from Amazon EBS to Google Persistent Disk).

## Configuration, Secrets, & Security
1. Why is it considered a major security risk to hardcode database passwords inside a container image instead of using a Kubernetes Secret?
2. How does a ConfigMap allow you to change the behavior of an application without having to rebuild the entire Docker image?
3. In terms of RBAC (Role-Based Access Control), why is the principle of "Least Privilege" vital when giving developers access to a cluster?

## Health & The Declarative API
1. Compare a Liveness Probe to a Readiness Probe. What happens if you mix them up?
2. What does it mean that the Kubernetes API is Declarative rather than Imperative? (Hint: Think about "the what" vs. "the how").
3. How do Custom Resources (CRs) and Custom Resource Definitions (CRDs) allow Kubernetes to manage things it wasn't originally built for, like a specific type of database or an SSL certificate?

## Scaling & Performance
1. Describe the chain of events that occurs when the Horizontal Pod Autoscaler (HPA) notices a spike in CPU usage on your web application.
2. How does the concept of "Bin Packing" in Kubernetes help a company lower their monthly Cloud bill?
