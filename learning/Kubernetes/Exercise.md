# Minikube Laboratory
Today, you will see the isolated effects of Kubernetes components to help you comprehend their use first-hand. You will also gain a more comprehensive view on how these components work together, as well as learn Kubectl commands.

### Prerequisites 
- Install Minikube
- Install Kubectl

## Step 1: The "Self-Healing" Test (Deployments & Pods)
- **Goal**: Prove that Kubernetes is the "Manager" that never sleeps.
  
1. **Action**: Create a deployment with 3 replicas of an Nginx web server.
   
2. **Observation**: Run a suitable Kubectl command to see all three running.
   
3. **The Test**: Manually "kill" one of the pods by deleting it.
   
4. **The Question**: Run the command to see all the pods again immediately. What happened? Why did a new pod appear with a different name?
   
- **Concept tested**: *Desired State vs. Current State.*

## Step 2: The "Permanent Address" Test (Services)
- **Goal**: Understand why we need a Service to talk to "Ephemeral" pods.

1. **Action**: Expose the deployment so it can be reached.

2. **The Test**: Get the URL to view the site.

3. **Observation**: Open the link in a browser. Now, delete all the pods in that deployment.

4. **The Question**: Once the new pods are up, refresh the browser. Does the link still work? Why didn't you have to change the URL even though the "servers" (pods) are brand new?

- **Concept tested**: *Service Discovery and Stable Endpoints.*

## Step 3: The "Cloud Config" Test (ConfigMaps & Secrets)
- **Goal**: Learn to change app behavior without rebuilding the container.
  
1. **Action**: Create a ConfigMap with a "background color" variable.

2. **The Test**: Update the Deployment YAML to inject this environment variable.

3. **The Challenge**: Change the ConfigMap value from "blue" to "red" and trigger a rollout.

4. **The Question**: Why is this better than hardcoding the color "blue" inside the Dockerfile?

- **Concept tested**: *Decoupling configuration from code.*

## Step 4: The "Resource Limit" Test (Scheduling)
- **Goal**: See how Kubernetes manages "Bin Packing" to save money.

1. **Action**: Update the deployment to request more CPU than your Minikube actually has (e.g., request 100 CPUs).

2. **Observation**: Run the command to get the pods

3. **The Question**: Why is the status ``Pending``? Run the command to get the description of the pods, then look at the "Events" section. What is the Scheduler telling you?

- **Concept tested**: *Scheduling Constraints and Resource Management.*

## Final Questions
1. What component noticed the pod was deleted in Step 1?
   
2. What component decided where to put the new pod?

3. Why did the IP of the Service stay the same while the Pod IPs changed?

4. What command would you use to see the "Logs" of a failing pod?
