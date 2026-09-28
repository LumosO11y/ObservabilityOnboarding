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
- CNI & kube-proxy
- NetworkPolicy
- Volumes
- PVC
- Storage classes
- Requests, limits & QoS classes
- Taints, tolerations & affinity
- PriorityClass & preemption
- Namespaces
- ResourceQuota
- LimitRange
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
- Cordon, drain & PodDisruptionBudget
- Finalizers, owner references & garbage collection
- Troubleshooting & Events
- K8S declarative API
- Horizontal Pod Autoscaler (HPA)
- KEDA
- Kubernetes distributions: OpenShift, Rancher/RKE2, K3s, and managed offerings (EKS, GKE, AKS)
- Security Context Constraints (SCCs)
- Hosted Control Planes

## Outcome

<details>
<summary><strong>Questions you should be able to answer by the end of this block (click to expand)</strong></summary>

### Cloud and Orchestration

1. How does the "Ephemeral" nature of the Cloud change the way we approach application uptime compared to traditional on-premise servers?
2. Why is the "Cattle vs. Pets" analogy fundamental to understanding why we need orchestration in a cloud environment?
3. In your own words, describe the exact moment a company grows out of "just using Docker" and begins to actually need an orchestrator like Kubernetes.
4. How does Kubernetes solve the problem of "Vendor Lock-in" when a company wants to move from AWS to Google Cloud or Azure?
5. What are the pros and cons of developing for cloud environments?
6. When would a team be better off *not* adopting Kubernetes, and sticking with something simpler like Docker Compose or a managed PaaS instead?

### Cluster Architecture & Nodes

1. If the Control Plane is the "brain" of the cluster, what happens to the currently running applications if that brain temporarily loses power?
2. What is the role of the Kubelet on a worker node?
3. In a large-scale environment, why might an organization choose to have dedicated Infra Nodes for logging and monitoring instead of putting everything on Worker Nodes?
4. Explain the relationship between a Cluster and a Node. How does Kubernetes make multiple physical servers look like one giant pool of resources?
5. Define, in one sentence each, what a Control Plane node (historically called a "master" node), an Infra Node, and a Worker Node are each responsible for. Why is it a Worker Node and not an Infra Node that would typically run a team's actual application?
6. What are the API server, etcd, the Scheduler, and the Controller Manager each responsible for? Which of them is the only one that reads and writes etcd directly, and why does that matter?
7. Walk through what happens between running `kubectl apply -f deployment.yaml` and a container actually starting on a node. Which components touch the request, and in what order?
8. etcd holds the entire state of the cluster. What would you lose if etcd's data were lost, and why is backing up etcd a different thing from backing up your applications' volumes?

### Pods & Workload Controllers

1. Why does Kubernetes use Pods as the smallest unit of deployment instead of just running containers directly?
2. What are labels and selectors? How do a Deployment, its ReplicaSet, and a Service each use them to find "their" Pods? What's an annotation, and how is it different from a label?
3. If you need to ensure that every single node in your cluster runs a specific logging agent, would you use a Deployment or a DaemonSet? Why?
4. What does a ReplicaSet do, and how does it relate to a Deployment?
5. What is the primary difference between a Deployment (for stateless apps like a web server) and a StatefulSet (for databases)?
6. Describe how a Controller uses a "reconciliation loop" to move the cluster from its current state to the desired state.
7. Deployments and StatefulSets are meant to keep Pods running forever. What is a Job for, and what does it mean for a Job's Pod to have "completed" rather than crashed?
8. What is a CronJob, and what does it use under the hood to decide when to run? (Hint: you've just learned the syntax it borrows from, back in the Linux part.)
9. What is an init container, and what is a sidecar container? Give a use case for each. How could you run a telemetry collector next to your app as a sidecar, and what would you gain or lose compared to running one per node as a DaemonSet?
10. When you change the image of a Deployment, how does a rolling update replace the old Pods with new ones? What do `maxSurge` and `maxUnavailable` control, and how do you roll back a rollout that turned out to be bad?

### Networking & Traffic (Services & Ingress)

1. Since Pods are frequently destroyed and recreated with new IP addresses, how does a Service let other apps reliably find them?
2. What are the different Service types (e.g. ClusterIP), and when would you use each?
3. What is a headless Service? Why does a StatefulSet running a replicated database (like the ClickHouse cluster from Chapter 3) need one?
4. How does a Pod resolve a name like `my-service.my-namespace`? Which component answers that DNS query, and what happens to the whole cluster if it goes down?
5. What is a CNI plugin, and what is kube-proxy? Which one gives a Pod its IP address, and which one makes traffic to a Service's IP actually reach a Pod?
6. What is the difference between a Service and an Ingress? How do they work together to get a user from the internet to your code?
7. What are the risks of exposing a Pod directly to the internet without using the Kubernetes networking layer?
8. By default, can any Pod in the cluster talk to any other Pod, even across namespaces? What is a NetworkPolicy, and why does creating one have no effect unless the cluster's CNI plugin supports it?
9. How would a gRPC connection be made between code running outside a k8s cluster and a Pod inside that cluster? Walk through the entire flow.
10. What are the disadvantages of gRPC in internal cluster communication?
11. What is the Gateway API, and what limitations of Ingress does it address? What is the current status of the ingress-nginx controller, and what does that mean for clusters that rely on it?

### Storage & Persistence (Volumes)

1. If a container is deleted, the data inside it is lost forever. How do Persistent Volume Claims (PVC) and Storage Classes break this cycle?
2. What is the relationship between a PersistentVolume (PV) and a PersistentVolumeClaim (PVC)? Who creates each one?
3. Why is the Storage Class important for cloud portability? (e.g., switching from Amazon EBS to Google Persistent Disk).
4. What is a volume's reclaim policy? What happens to the data behind a PVC when the PVC is deleted, and how can that bite you when you clean up a namespace?

### Scheduling & Resource Management

1. What is the difference between a container's resource request and its limit? Which one does the Scheduler look at, and which one is enforced while the container runs?
2. What happens when a container goes over its memory limit, and what happens when it goes over its CPU limit? Why are the two outcomes so different?
3. What are the Pod QoS classes, how does Kubernetes decide which class a Pod belongs to, and how does that decide which Pods get evicted first when a node runs low on memory?
4. What are taints and tolerations? How would you use them to make sure that only logging and monitoring workloads land on your Infra Nodes?
5. How is node affinity (or a `nodeSelector`) different from a toleration? Why do you often need both to pin a workload to a specific set of nodes?
6. What is pod anti-affinity, and why would you want it for the replicas of a database?
7. What are PriorityClasses and preemption? What could go wrong on a shared cluster if every team marked its workloads with the highest priority?

### Namespaces & Resource Quotas

1. What is a Namespace, and what problem does it solve for a cluster shared by multiple teams?
2. Are all Kubernetes objects namespaced? Give an example of one that isn't, and explain why it makes sense for that one to be cluster-wide instead.
3. What is a ResourceQuota, and how does it stop one team's namespace from starving another team's namespace of CPU/memory on a shared cluster?
4. How does a ResourceQuota on a namespace relate to the Requests and Limits you'd set on an individual Pod's containers?
5. What is a LimitRange, and what gap does it fill that a ResourceQuota doesn't? What happens when you create a Pod without requests in a namespace that has a CPU quota but no LimitRange?

### Configuration, Secrets, & Security

1. Why is it considered a major security risk to hardcode database passwords inside a container image instead of using a Kubernetes Secret?
2. How does a ConfigMap allow you to change the behavior of an application without having to rebuild the entire Docker image?
3. Kubernetes also has a Downward API. What is it, what kind of information does it expose to a running container, and how is that data fundamentally different from what a ConfigMap gives you?
4. Kubernetes Secrets are base64-encoded. Is that encryption? Where are Secrets actually stored, who can read them, and what does enabling encryption at rest change?

### Access Control & Cluster Security

1. What is the difference between authentication and authorization in the Kubernetes API? Is there a "User" object in Kubernetes? If not, how does the API server know who you are?
2. What is a ServiceAccount? How does a Pod use one to talk to the API server, and where does the Pod's credential come from?
3. What are a Role and a ClusterRole, and a RoleBinding and a ClusterRoleBinding? What happens when you bind a ClusterRole using a RoleBinding?
4. In terms of RBAC (Role-Based Access Control), why is the principle of "Least Privilege" vital when giving developers access to a cluster?
5. What does the `cluster-admin` ClusterRole actually allow? Why shouldn't it be your day-to-day identity, even on a cluster where you've been granted it?
6. How can you check, without actually trying it, whether a given user or ServiceAccount is allowed to perform an action? How would you use impersonation to see the cluster the way they see it?
7. Someone has permission to create Pods in a namespace, but not to read Secrets in it. Why can they still effectively read those Secrets? Which other permissions look harmless but are really privilege escalation paths?
8. What do `privileged: true`, `hostPath` volumes, `hostNetwork`, and `hostPID` each let a Pod do? Why is being able to run such a Pod roughly equivalent to being root on the node?
9. What is a Pod's `securityContext`? What does each of `runAsNonRoot`, `readOnlyRootFilesystem`, and dropping Linux capabilities protect against?
10. What is Pod Security Admission? What are its levels, and how is it turned on for a namespace?

### Health & The Declarative API

1. Compare Liveness, Readiness, and Startup Probes. What happens if you mix them up?
2. What does it mean that the Kubernetes API is Declarative rather than Imperative? (Hint: Think about "the what" vs. "the how").
3. How do Custom Resources (CRs) and Custom Resource Definitions (CRDs) allow Kubernetes to manage things it wasn't originally built for, like a specific type of database or an SSL certificate?
4. A CRD only defines a new resource type - it doesn't make anything happen on its own. What is the Operator pattern, and what role does a custom Controller play in making a CRD actually "do something"? (e.g. the OpenTelemetry Operator - what does it manage?)
5. A Controller reacts *after* a resource is already stored. How does Kubernetes let something intercept - and even modify - a resource the moment it's submitted, before it's ever persisted? Research Mutating and Validating Admission Webhooks. The OpenTelemetry Operator can add auto-instrumentation (from Chapter 2) to your Pods without you editing their manifests - what does it actually change in the Pod, and which kind of webhook makes that possible?
6. Admission webhooks sit in the path of every matching API request. What happens to the cluster when a webhook's backing service is down, and how does the webhook's `failurePolicy` change that?

### Cluster Operations & Maintenance

1. What is a kubeconfig file, and what is a context? Why is having several clusters in one kubeconfig dangerous, and what habits keep you from running a command against the wrong cluster?
2. What do `kubectl cordon` and `kubectl drain` do, and in what order would you use them before taking a node down for maintenance?
3. Why does `kubectl drain` refuse, by default, to handle Pods managed by a DaemonSet and Pods that use local storage?
4. What is a PodDisruptionBudget? How does it interact with `kubectl drain`, and how can a badly configured PDB block a drain forever?
5. What are owner references, and what is cascading deletion? If you delete a Deployment, what happens to its ReplicaSets and Pods, and how does an orphan deletion change that?
6. What is a finalizer? Why does a namespace sometimes get stuck in `Terminating`, and why is force-removing its finalizers risky?
7. What happens to every Custom Resource of a given type when you delete its CRD? Why does that make deleting a CRD (or uninstalling an operator along with its CRDs) one of the most destructive things a cluster-admin can do?
8. Kubernetes releases a new minor version several times a year. Why do clusters have to be upgraded one minor version at a time, and in what order are the control plane and the nodes upgraded?

### Troubleshooting

1. A Pod is `Pending`, in `ImagePullBackOff`, in `CrashLoopBackOff`, or was `OOMKilled`. What does each of these tell you, and what would you look at first for each one?
2. What are Kubernetes Events? Why are they often more useful than logs when a Pod never started, and how long do they stick around?
3. A container crashed and was restarted. How do you see the logs from the run that crashed, rather than the current one?
4. Your container image has no shell and no debugging tools. How can you still get a shell next to the running container to investigate?

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
- <https://kubernetes.io/docs/concepts/services-networking/network-policies/>
- <https://kubernetes.io/docs/concepts/services-networking/gateway/>
- <https://kubernetes.io/docs/concepts/storage/>
- <https://kubernetes.io/docs/concepts/configuration/>
- <https://kubernetes.io/docs/concepts/scheduling-eviction/>
- <https://kubernetes.io/docs/concepts/workloads/pods/downward-api/>
- <https://kubernetes.io/docs/concepts/extend-kubernetes/operator/>
- <https://opentelemetry.io/docs/platforms/kubernetes/operator/>
- <https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/>
- <https://kubernetes.io/docs/concepts/policy/resource-quotas/>
- <https://kubernetes.io/docs/concepts/policy/limit-range/>
- <https://kubernetes.io/docs/concepts/workloads/controllers/job/>
- <https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/>
- <https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/>

**Scheduling & Resources**

- <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>
- <https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/>
- <https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/>
- <https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/>
- <https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/>

**Access Control & Security**

- <https://kubernetes.io/docs/concepts/security/controlling-access/>
- <https://kubernetes.io/docs/reference/access-authn-authz/rbac/>
- <https://kubernetes.io/docs/concepts/security/rbac-good-practices/>
- <https://kubernetes.io/docs/concepts/security/service-accounts/>
- <https://kubernetes.io/docs/concepts/security/secrets-good-practices/>
- <https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/>
- <https://kubernetes.io/docs/concepts/security/pod-security-standards/>
- <https://kubernetes.io/docs/concepts/security/pod-security-admission/>
- <https://kubernetes.io/docs/tasks/configure-pod-container/security-context/>

**Cluster Operations**

- <https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/>
- <https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/>
- <https://kubernetes.io/docs/concepts/workloads/pods/disruptions/>
- <https://kubernetes.io/docs/concepts/architecture/garbage-collection/>
- <https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/>
- <https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/>
- <https://kubernetes.io/releases/version-skew-policy/>

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

</details>
