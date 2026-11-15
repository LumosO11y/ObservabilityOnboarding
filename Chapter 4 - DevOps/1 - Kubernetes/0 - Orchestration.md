# Orchestration

## Overview

The next step in the evolution of containers was merging containerization with the concept of scale, and doing so in a Cloud environment where compute is ephemeral. The result is Kubernetes, or K8s for short.

## Goals

Under the subject of Kubernetes, we will touch upon, and you will learn, the following:

- Scale
- Cloud environment
- Cluster
- Cluster architecture
- Control plane components: API server, etcd, Scheduler, Controller Manager
- Orchestration
- Nodes
- Control plane nodes (historically "master" nodes)
- Infra nodes
- Worker Nodes
- Pods
- Labels, selectors & annotations
- Init containers & sidecar containers
- Controllers
- Custom Resource
- CRD
- Operators
- Admission Webhooks (Mutating & Validating)
- Services and Service types
- Ingress and the Gateway API
- Cluster DNS
- Volumes
- PVC
- Access modes
- Storage classes
- Requests & limits
- Taints, tolerations & affinity
- Namespaces
- ResourceQuota
- Configmap
- Secret
- Downward API
- Probes
- Deployment
- Rolling updates & rollbacks
- DaemonSet
- ReplicaSet
- StatefulSet
- Job
- CronJob
- Authentication & authorization
- ServiceAccounts
- RBAC
- Pod Security Admission & securityContext
- Kubeconfig & contexts
- Finalizers, owner references & garbage collection
- Troubleshooting & Events
- K8S declarative API
- Horizontal Pod Autoscaler (HPA)
- KEDA
- Kubernetes distributions: OpenShift and managed offerings (EKS, GKE, AKS)
- Security Context Constraints (SCCs)
- OpenShift Routes

## Outcome

<details>
<summary><strong>Questions you should be able to answer by the end of this block (click to expand)</strong></summary>

### Cloud and Orchestration

1. Why is the "Cattle vs. Pets" analogy fundamental to understanding why we need orchestration in a cloud environment?
2. In your own words, describe the exact moment a company grows out of "just using Docker" and begins to actually need an orchestrator like Kubernetes. When would a team be better off staying with something simpler, like Docker Compose or a managed PaaS?

### Cluster Architecture & Nodes

1. If the Control Plane is the "brain" of the cluster, what happens to the currently running applications if that brain temporarily loses power?
2. Define, in one sentence each, what a Control Plane node (historically called a "master" node), an Infra Node, and a Worker Node are each responsible for. Why is it a Worker Node and not an Infra Node that would typically run a team's actual application?
3. What are the API server, etcd, the Scheduler, and the Controller Manager each responsible for? Which of them is the only one that reads and writes etcd directly, and why does that matter?
4. Walk through what happens between running `kubectl apply -f deployment.yaml` and a container actually starting on a node. Which components touch the request, and in what order?

### Pods & Workload Controllers

1. Why does Kubernetes use Pods as the smallest unit of deployment instead of just running containers directly?
2. What are labels and selectors? How do a Deployment, its ReplicaSet, and a Service each use them to find "their" Pods? What's an annotation, and how is it different from a label?
3. What is the primary difference between a Deployment (for stateless apps like a web server) and a StatefulSet (for databases)?
4. Describe how a Controller uses a "reconciliation loop" to move the cluster from its current state to the desired state. What does it mean that the Kubernetes API is declarative rather than imperative, and how does the loop make that work?
5. Deployments and StatefulSets are meant to keep Pods running forever. What are a Job and a CronJob for, and what does it mean for a Job's Pod to have "completed" rather than crashed? (Hint: think back to the Linux part of Chapter 0.)
6. What is an init container, and what is a sidecar container? Give a use case for each. How could you run a telemetry collector next to your app as a sidecar, and what would you gain or lose compared to running one per node as a DaemonSet?
7. When you change the image of a Deployment, how does a rolling update replace the old Pods with new ones? How do you roll back a rollout that turned out to be bad?

### Networking & Traffic (Services & Ingress)

1. Since Pods are frequently destroyed and recreated with new IP addresses, how does a Service let other apps reliably find them?
2. What are the different Service types (e.g. ClusterIP), and when would you use each?
3. What is a headless Service? Why does a StatefulSet running a replicated database (like the ClickHouse cluster from Chapter 3) need one?
4. How does a Pod resolve a name like `my-service.my-namespace`? Which component answers that DNS query, and what happens to the whole cluster if it goes down?
5. What is the difference between a Service and an Ingress? How do they work together to get a user from the internet to your code?
6. What is the Gateway API, and which Kubernetes SIG maintains it? What limitations of Ingress was it designed to address?
7. OpenShift (covered under Distributions below) has its own object for exposing apps: the Route. What is a Route, and how does it compare to Ingress and the Gateway API? What happens on OpenShift when you create an Ingress object?
8. How would a gRPC connection be made between code running outside a k8s cluster and a Pod inside that cluster? Walk through the entire flow.
9. What are the disadvantages of gRPC in internal cluster communication?

### Storage & Persistence (Volumes)

1. If a container is deleted, the data inside it is lost forever. How do PersistentVolumes (PV), PersistentVolumeClaims (PVC), and Storage Classes break this cycle? Who creates each one?
2. What are a PersistentVolume's access modes? Relate them to the storage types and architectures from the Storage part of Chapter 0: which kind of storage can back a volume that Pods on several nodes write to at the same time, and why?

### Scheduling & Resource Management

1. What is the difference between a container's resource request and its limit? Which one does the Scheduler look at, and which one is enforced while the container runs?
2. What happens when a container goes over its memory limit, and what happens when it goes over its CPU limit? Why are the two outcomes so different?
3. What are taints and tolerations? How would you use them to make sure that only logging and monitoring workloads land on your Infra Nodes?
4. How is node affinity (or a `nodeSelector`) different from a toleration? Why do you often need both to pin a workload to a specific set of nodes?

### Namespaces & Resource Quotas

1. What is a Namespace, and what problem does it solve for a cluster shared by multiple teams?
2. What is a ResourceQuota, and how does it stop one team's namespace from starving another's on a shared cluster? How does it relate to the requests and limits you'd set on an individual Pod's containers?

### Configuration & Secrets

1. How does a ConfigMap allow you to change the behavior of an application without having to rebuild the entire Docker image?
2. Why is it a security risk to hardcode database passwords inside a container image instead of using a Kubernetes Secret? Secrets are base64-encoded: is that encryption, and who can read them?
3. Kubernetes also has a Downward API. What is it, what kind of information does it expose to a running container, and how is that data fundamentally different from what a ConfigMap gives you?

### Access Control & Pod Security

1. What is the difference between authentication and authorization in the Kubernetes API? Is there a "User" object in Kubernetes? If not, how does the API server know who you are?
2. What is a ServiceAccount? How does a Pod use one to talk to the API server, and where does the Pod's credential come from?
3. What are a Role and a ClusterRole, and a RoleBinding and a ClusterRoleBinding? What happens when you bind a ClusterRole using a RoleBinding?
4. What is a Pod's `securityContext`? What does each of `runAsNonRoot`, `readOnlyRootFilesystem`, and dropping Linux capabilities protect against?
5. What is Pod Security Admission? What are its levels, and how is it turned on for a namespace?

### Health & Extending the API

1. Compare Liveness, Readiness, and Startup Probes. What happens if you mix them up?
2. How do Custom Resources (CRs) and Custom Resource Definitions (CRDs) allow Kubernetes to manage things it wasn't originally built for, like a specific type of database or an SSL certificate?
3. A CRD only defines a new resource type - it doesn't make anything happen on its own. What is the Operator pattern, and what role does a custom Controller play in making a CRD actually "do something"? (e.g. the OpenTelemetry Operator - what does it manage?)
4. A Controller reacts *after* a resource is already stored. How does Kubernetes let something intercept - and even modify - a resource the moment it's submitted, before it's ever persisted? Research Mutating and Validating Admission Webhooks. The OpenTelemetry Operator can add auto-instrumentation (from Chapter 2) to your Pods without you editing their manifests - what does it actually change in the Pod, and which kind of webhook makes that possible?

### Cluster Operations

1. What is a kubeconfig file, and what is a context? Why is having several clusters in one kubeconfig dangerous, and what habits keep you from running a command against the wrong cluster?
2. What are owner references, and what is cascading deletion? Starting from a Deployment, trace the chain of owners down to its Pods. What happens to them when you delete the Deployment, and how does an orphan deletion change that?
3. When an operator (like the OpenTelemetry Operator from the Health & Extending the API questions) creates Kubernetes objects for a custom resource, how does it use owner references? What happens to those objects when you delete the custom resource, and what does the operator do if you delete or edit one of them by hand?
4. What is a finalizer? Why do operators often add their own finalizers to the resources they manage? Why does a namespace sometimes get stuck in `Terminating`, and why is force-removing its finalizers risky?

### Troubleshooting

1. A Pod is `Pending`, in `ImagePullBackOff`, in `CrashLoopBackOff`, or was `OOMKilled`. What does each of these tell you, and what would you look at first for each one?
2. What are Kubernetes Events? Why are they often more useful than logs when a Pod never started, and how long do they stick around?
3. A container crashed and was restarted. How do you see the logs from the run that crashed, rather than the current one?
4. Your container image has no shell and no debugging tools. How can you still get a shell next to the running container to investigate?

### Scaling

1. Describe the chain of events that occurs when the Horizontal Pod Autoscaler (HPA) notices a spike in CPU usage on your web application.
2. The standard HPA scales on metrics like CPU and memory. What is KEDA, and what kind of scaling need does it cover that the standard HPA can't? How does KEDA relate to the HPA under the hood?

### Kubernetes Distributions ("Flavors")

1. Everything so far has been "vanilla" (upstream) Kubernetes. What is OpenShift, and how does it relate to vanilla Kubernetes - is it a fork, a distribution, or something else?
2. What are OpenShift's Security Context Constraints (SCCs), and how do they differ from Pod Security Admission? What does OpenShift's default SCC prevent a Pod from doing that vanilla Kubernetes allows by default?
3. Compare running your own Kubernetes distribution (vanilla or OpenShift) to using a cloud provider's managed offering (EKS, GKE, AKS). What operational responsibility does a managed control plane take off your plate, and what do you give up in exchange? Why don't we use cloud provider's managed clusters?

</details>

### Links

Here is a list of recommended reading materials to help you understand K8S. Also, feel free to use the Goals list above to find what you need to read in the links.

<details>
<summary><strong>Curated reading, grouped by topic (click to expand)</strong></summary>

**Intro**

- <https://www.geeksforgeeks.org/devops/introduction-to-kubernetes-k8s/>
- <https://www.baeldung.com/ops/kubernetes>

**From the K8S Docs**

- <https://kubernetes.io/docs/concepts/overview/components/>
- <https://kubernetes.io/docs/concepts/architecture/>
- <https://kubernetes.io/docs/concepts/containers/>
- <https://kubernetes.io/docs/concepts/workloads/pods/>
- <https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/>
- <https://kubernetes.io/docs/concepts/workloads/pods/init-containers/>
- <https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/>
- <https://kubernetes.io/docs/concepts/workloads/controllers/>
- <https://kubernetes.io/docs/concepts/services-networking/>
- <https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/>
- <https://kubernetes.io/docs/concepts/services-networking/gateway/>
- <https://gateway-api.sigs.k8s.io/>
- <https://kubernetes.io/docs/concepts/storage/>
- <https://kubernetes.io/docs/concepts/configuration/>
- <https://kubernetes.io/docs/concepts/scheduling-eviction/>
- <https://kubernetes.io/docs/concepts/workloads/pods/downward-api/>
- <https://kubernetes.io/docs/concepts/extend-kubernetes/operator/>
- <https://opentelemetry.io/docs/platforms/kubernetes/operator/>
- <https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/>
- <https://kubernetes.io/docs/concepts/policy/resource-quotas/>
- <https://kubernetes.io/docs/concepts/workloads/controllers/job/>
- <https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/>
- <https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/>

**Scheduling & Resources**

- <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>
- <https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/>
- <https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/>

**Access Control & Security**

- <https://kubernetes.io/docs/concepts/security/controlling-access/>
- <https://kubernetes.io/docs/reference/access-authn-authz/rbac/>
- <https://kubernetes.io/docs/concepts/security/rbac-good-practices/>
- <https://kubernetes.io/docs/concepts/security/service-accounts/>
- <https://kubernetes.io/docs/concepts/security/secrets-good-practices/>
- <https://kubernetes.io/docs/concepts/security/pod-security-standards/>
- <https://kubernetes.io/docs/concepts/security/pod-security-admission/>
- <https://kubernetes.io/docs/tasks/configure-pod-container/security-context/>

**Cluster Operations**

- <https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/>
- <https://kubernetes.io/docs/concepts/architecture/garbage-collection/>
- <https://kubernetes.io/docs/concepts/overview/working-with-objects/owners-dependents/>
- <https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/>

**Troubleshooting**

- <https://kubernetes.io/docs/tasks/debug/debug-application/debug-pods/>
- <https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/>

**Full-On Guide**

- <https://www.baeldung.com/ops/kubernetes-series>

**KEDA**

- <https://keda.sh/docs/latest/concepts/>
- <https://keda.sh/docs/latest/concepts/scaling-deployments/>

**Kubernetes Distributions**

- <https://www.redhat.com/en/technologies/cloud-computing/openshift>
- <https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/authentication_and_authorization/managing-pod-security-policies>

**Videos**

*Kubernetes Crash Course*

- <https://www.youtube.com/watch?v=X48VuDVv0do&pp=ygUDazhz>

*K8S Architecture*

- <https://www.youtube.com/watch?v=T4Z7visMM4E&t=1238s&pp=ygUDazhz>
- <https://www.youtube.com/watch?v=xj_GjnD4uyI&t=1050s&pp=ygUDazhz>

</details>
