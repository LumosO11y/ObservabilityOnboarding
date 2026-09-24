# Orchestration

## Overview

The next step in the evolution of containers was merging containerization with the concept of scale, and doing so in a Cloud environment where compute is ephemeral. The result is Kubernetes, or K8s for short.

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
- Operators
- Admission Webhooks (Mutating & Validating)
- Ingress
- Services
- Volumes
- PVC
- Storage classes
- Namespaces
- ResourceQuota
- Configmap
- Secret
- Downward API
- Probes
- Deployment
- DaemonSet
- ReplicaSet
- StatefulSet
- Job
- CronJob
- RBAC
- K8S declarative API
- Horizontal Pod Autoscaler (HPA)
- KEDA
- Kubernetes distributions: OpenShift, Rancher/RKE2, K3s, and managed offerings (EKS, GKE, AKS)
- Security Context Constraints (SCCs)
- Hosted Control Planes

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
2. What is the role of the Kubelet on a worker node?
3. In a large-scale environment, why might an organization choose to have dedicated Infra Nodes for logging and monitoring instead of putting everything on Worker Nodes?
4. Explain the relationship between a Cluster and a Node. How does Kubernetes make multiple physical servers look like one giant pool of resources?
5. Define, in one sentence each, what a Master Node, an Infra Node, and a Worker Node are each responsible for. Why is it a Worker Node and not an Infra Node that would typically run a team's actual application?

### Pods & Workload Controllers

1. Why does Kubernetes use Pods as the smallest unit of deployment instead of just running containers directly?
2. If you need to ensure that every single node in your cluster runs a specific logging agent, would you use a Deployment or a DaemonSet? Why?
3. What does a ReplicaSet do, and how does it relate to a Deployment?
4. What is the primary difference between a Deployment (for stateless apps like a web server) and a StatefulSet (for databases)?
5. Describe how a Controller uses a "reconciliation loop" to move the cluster from its current state to the desired state.
6. Deployments and StatefulSets are meant to keep Pods running forever. What is a Job for, and what does it mean for a Job's Pod to have "completed" rather than crashed?
7. What is a CronJob, and what does it use under the hood to decide when to run? (Hint: you've just learned the syntax it borrows from, back in the Linux part.)

### Networking & Traffic (Services & Ingress)

1. Since Pods are frequently destroyed and recreated with new IP addresses, how does a Service let other apps reliably find them?
2. What is the difference between a Service and an Ingress? How do they work together to get a user from the internet to your code?
3. What are the risks of exposing a Pod directly to the internet without using the Kubernetes networking layer?
4. How would a gRPC connection be made between code running outside a k8s cluster and a Pod inside that cluster? Walk through the entire flow.
5. What are the disadvantages of gRPC in internal cluster communication?

### Storage & Persistence (Volumes)

1. If a container is deleted, the data inside it is lost forever. How do Persistent Volume Claims (PVC) and Storage Classes break this cycle?
2. What is the relationship between a PersistentVolume (PV) and a PersistentVolumeClaim (PVC)? Who creates each one?
3. Why is the Storage Class important for cloud portability? (e.g., switching from Amazon EBS to Google Persistent Disk).

### Namespaces & Resource Quotas

1. What is a Namespace, and what problem does it solve for a cluster shared by multiple teams?
2. Are all Kubernetes objects namespaced? Give an example of one that isn't, and explain why it makes sense for that one to be cluster-wide instead.
3. What is a ResourceQuota, and how does it stop one team's namespace from starving another team's namespace of CPU/memory on a shared cluster?
4. How does a ResourceQuota on a namespace relate to the Requests and Limits you'd set on an individual Pod's containers?

### Configuration, Secrets, & Security

1. Why is it considered a major security risk to hardcode database passwords inside a container image instead of using a Kubernetes Secret?
2. How does a ConfigMap allow you to change the behavior of an application without having to rebuild the entire Docker image?
3. Kubernetes also has a Downward API. What is it, what kind of information does it expose to a running container, and how is that data fundamentally different from what a ConfigMap gives you?
4. In terms of RBAC (Role-Based Access Control), why is the principle of "Least Privilege" vital when giving developers access to a cluster?

### Health & The Declarative API

1. Compare Liveness, Readiness, and Startup Probes. What happens if you mix them up?
2. What does it mean that the Kubernetes API is Declarative rather than Imperative? (Hint: Think about "the what" vs. "the how").
3. How do Custom Resources (CRs) and Custom Resource Definitions (CRDs) allow Kubernetes to manage things it wasn't originally built for, like a specific type of database or an SSL certificate?
4. A CRD only defines a new resource type - it doesn't make anything happen on its own. What is the Operator pattern, and what role does a custom Controller play in making a CRD actually "do something"? (e.g. the OpenTelemetry Operator - what does it manage?)
5. A Controller reacts *after* a resource is already stored. How does Kubernetes let something intercept - and even modify - a resource the moment it's submitted, before it's ever persisted? Research Mutating and Validating Admission Webhooks. The OpenTelemetry Operator can add auto-instrumentation (from Chapter 2) to your Pods without you editing their manifests - what does it actually change in the Pod, and which kind of webhook makes that possible?

### Scaling & Performance

1. Describe the chain of events that occurs when the Horizontal Pod Autoscaler (HPA) notices a spike in CPU usage on your web application.
2. How does the concept of "Bin Packing" in Kubernetes help a company lower their monthly Cloud bill?
3. The standard HPA scales on metrics like CPU and memory. What is KEDA, and what kind of scaling need does it cover that the standard HPA can't? How does KEDA relate to the HPA under the hood?

### Kubernetes Distributions ("Flavors")

1. Everything so far has been "vanilla" (upstream) Kubernetes. What is OpenShift, and how does it relate to vanilla Kubernetes - is it a fork, a distribution, or something else?
2. Research OpenShift's default security posture. What are Security Context Constraints (SCCs), and how do they differ from vanilla Kubernetes' Pod Security Admission? Specifically, what does OpenShift's default SCC prevent a pod from doing that vanilla K8s allows by default?
3. Beyond security, what does OpenShift give you "out of the box" that you'd have to set up yourself on vanilla Kubernetes ?
4. What is Rancher, and how is it different in kind from OpenShift?
5. What are RKE2 and K3s, and when would you reach for one over the other?
6. Compare running your own Kubernetes distribution (vanilla, OpenShift, RKE2) to using a cloud provider's managed offering (EKS, GKE, AKS). What operational responsibility does a managed control plane take off your plate, and what do you give up in exchange? Why don't we use cloud provider's managed clusters?
7. Some platforms use a "Hosted Control Plane" architecture (e.g. OpenShift's HyperShift). Where does the control plane run in that model? What does it change about how fast a new cluster can be provisioned, and about who pays for and operates the control plane?

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
- <https://kubernetes.io/docs/concepts/workloads/pods/downward-api/>
- <https://kubernetes.io/docs/concepts/extend-kubernetes/operator/>
- <https://opentelemetry.io/docs/kubernetes/operator/>
- <https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/>
- <https://kubernetes.io/docs/concepts/policy/resource-quotas/>
- <https://kubernetes.io/docs/concepts/workloads/controllers/job/>
- <https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/>
- <https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/>

**Full-On Guide**

- <https://www.baeldung.com/ops/kubernetes-series>

**KEDA**

- <https://keda.sh/docs/latest/concepts/>
- <https://keda.sh/docs/latest/concepts/scaling-deployments/>

**Kubernetes Distributions**

- <https://www.redhat.com/en/topics/containers/what-is-openshift>
- <https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/authentication_and_authorization/managing-pod-security-policies>
- <https://www.redhat.com/en/topics/containers/what-are-hosted-control-planes>
- <https://ranchermanager.docs.rancher.com/>
- <https://docs.k3s.io/>
- <https://docs.rke2.io/>

**Videos**

*Kubernetes Crash Course*

- <https://www.youtube.com/watch?v=X48VuDVv0do&pp=ygUDazhz>

*K8S Architecture*

- <https://www.youtube.com/watch?v=T4Z7visMM4E&t=1238s&pp=ygUDazhz>
- <https://www.youtube.com/watch?v=xj_GjnD4uyI&t=1050s&pp=ygUDazhz>
