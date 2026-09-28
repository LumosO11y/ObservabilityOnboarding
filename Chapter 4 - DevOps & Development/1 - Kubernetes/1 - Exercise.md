# Kubernetes Laboratory

Today, you will take the image you built in the [Dockerfile Exercise](../0%20-%20Docker/1%20-%20Dockerfile%20Exercise.md) and run it on a real Kubernetes cluster. Along the way you will see the isolated effects of Kubernetes components first-hand, get a more comprehensive view of how they work together, and learn Kubectl commands.

## Prerequisites

- Install Kubectl
- Get access to the test cluster from your mentor, along with the namespace you'll work in and the container registry you'll push images to
- The image you built in the Dockerfile Exercise

**Ground rules**: the test cluster is shared. Work only inside your own namespace, and write your resources as YAML manifests that you `kubectl apply`, rather than creating them with imperative commands - you'll be editing them throughout the lab.

## Step 0: The "Where Am I?" Test (Contexts & RBAC)

- **Goal**: Know exactly which cluster and namespace you're acting on, and what you're allowed to do there, before you change anything.

1. **Action**: Find out which context your Kubectl is currently using, and set your namespace as the default for that context.

2. **The Test**: Without actually trying it, check whether you're allowed to create Deployments in your namespace, list the cluster's Nodes, and delete a Namespace.

3. **The Question**: Why is what *you* can do on this cluster so much narrower than what the cluster itself can do? Who decided that, and with which Kubernetes objects?

- **Concept tested**: *Contexts, authentication, and RBAC.*

## Step 1: The "Ship It" Test (Images & Registries)

- **Goal**: Get your image somewhere the cluster can reach it.

1. **Action**: Tag the image from the Dockerfile Exercise as `v1` and push it to the registry your mentor pointed you to.

2. **The Question**: The image is already on your machine. Why can't the cluster just use it from there? Which component, on which machine, actually pulls the image?

- **Concept tested**: *Container registries and image distribution.*

## Step 2: The "Self-Healing" Test (Deployments & Pods)

- **Goal**: Prove that Kubernetes is the "Manager" that never sleeps.

1. **Action**: Write a Deployment manifest that runs 3 replicas of your `v1` image, with the right container port, and CPU/memory requests and limits. Apply it.

2. **Observation**: Run a suitable Kubectl command to see all three running, and which node each one landed on. If they don't reach `Running`, find out why from the Pod's events before moving on.

3. **The Test**: Manually "kill" one of the pods by deleting it.

4. **The Question**: Run the command to see all the pods again immediately. What happened? Why did a new pod appear with a different name?

- **Concept tested**: *Desired State vs. Current State.*

## Step 3: The "Permanent Address" Test (Services)

- **Goal**: Understand why we need a Service to talk to "Ephemeral" pods.

1. **Action**: Write a Service manifest for your Deployment and apply it.

2. **The Test**: Port-forward the Service to port 8080 on your machine, and open <http://localhost:8080>. You should see the same success message as in the Dockerfile Exercise.

3. **Observation**: Now, delete all the pods in that deployment.

4. **The Question**: Once the new pods are up, restart the port-forward and refresh the browser. Does the link still work? Why didn't you have to change anything, even though the "servers" (pods) are brand new? How does the chain from `localhost:8080` to port 5000 in the container compare to the port mapping you did in the Dockerfile Exercise?

- **Concept tested**: *Service Discovery and Stable Endpoints.*

## Step 4: The "Are You Ready?" Test (Probes)

- **Goal**: See how Kubernetes decides whether a pod should get traffic, and whether it should be restarted.

1. **Action**: Add a readiness probe and a liveness probe to your Deployment, both checking the app's `/` path.

2. **The Test**: Break the readiness probe on purpose by pointing it at a port nothing listens on, and apply.

3. **Observation**: Look at the pods and at the endpoints behind your Service. Then try the port-forward again.

4. **The Question**: The new pods are running - so why aren't they receiving traffic? What would have happened if you had broken the *liveness* probe instead? Fix the probe before moving on.

- **Concept tested**: *Readiness vs. Liveness.*

## Step 5: The "Cloud Config" Test (ConfigMaps & Rolling Updates)

- **Goal**: Learn to change app behavior without rebuilding the container, and roll out a new version safely.

1. **Action**: Change the app so it reads a `BACKGROUND_COLOR` environment variable and uses it as the page's background color. Build it, tag it `v2`, and push it.

2. **Action**: Create a ConfigMap with a `BACKGROUND_COLOR` key set to `blue`. Update the Deployment to use the `v2` image and to inject the ConfigMap key as an environment variable. Apply it, and watch the rollout as it happens.

3. **Observation**: While the rollout is in progress, watch the pods and the ReplicaSets. How many pods of each version existed at the same time?

4. **The Challenge**: Change the ConfigMap value from `blue` to `red`. Refresh the page before doing anything else. Then trigger a rollout and refresh it again.

5. **The Question**: Why didn't the running pods pick up the new value on their own? And why is this whole approach still better than hardcoding the color inside the Dockerfile?

6. **The Rollback**: Roll the Deployment back to its previous revision, then look at the rollout history. What happened to the page, and how was Kubernetes able to go back so quickly?

- **Concept tested**: *Decoupling configuration from code, and rolling updates.*

## Step 6: The "Resource Limit" Test (Scheduling)

- **Goal**: See how Kubernetes manages "Bin Packing" and what happens when a request can't be satisfied.

1. **Action**: Update the deployment to request far more CPU than any node in the cluster has (e.g., request 100 CPUs).

2. **Observation**: Run the command to get the pods.

3. **The Question**: Why is the new pod's status `Pending`? Run the command to get the description of the pod, then look at the "Events" section. What is the Scheduler telling you? (If your namespace has a ResourceQuota, you may not get a pod at all - in that case, find where the error shows up instead, and explain why it's different.)

4. **The Question**: Your old pods kept serving traffic the whole time. Why didn't the Deployment kill them to make room for the new one?

5. **Action**: Undo the change.

- **Concept tested**: *Scheduling Constraints and Resource Management.*

## Step 7: Clean Up

- **Goal**: Leave the shared cluster as you found it.

1. **Action**: Delete everything you created, using the labels you put on your resources rather than deleting each object by name.

2. **The Question**: Did that really remove everything you created? What was left behind, and why? (Don't delete the namespace itself unless your mentor tells you to.)

## Final Questions

1. What component noticed the pod was deleted in Step 2?

2. What component decided where to put the new pod?

3. Why did the IP of the Service stay the same while the Pod IPs changed?

4. What command would you use to see the "Logs" of a failing pod?

5. Which ServiceAccount do your pods run as? If someone compromised your app, what could they do against the Kubernetes API with it?
