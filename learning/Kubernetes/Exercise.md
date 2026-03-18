# Minikube Laboratory
Today, you will see the isolated effects of Kubernetes components to help you comprehend their use first-hand. You will also gain a more comprehensive view on how these components work together, as well as familiarize yourself with Kubectl commands.

### Prerequisites 
- Install Minikube
- Install Kubectl

## Step 1: The "Self-Healing" Test (Deployments & Pods)
- Goal: Prove that Kubernetes is the "Manager" that never sleeps.
1. **Action**: Create a deployment with 3 replicas of an Nginx web server:
2. **Observation**: Run a suitable Kubectl command to see all three running.
3. **The Test**: Manually "kill" one of the pods by deleting it.
4. **The Question**: Run the command to see all the pods again immediately. What happened? Why did a new pod appear with a different name?
Concept tested: Desired State vs. Current State.


