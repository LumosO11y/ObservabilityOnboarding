# ArgoCD

## Overview

ArgoCD is a declarative, GitOps continuous delivery tool for Kubernetes: it continuously reconciles what's running in a cluster against what's declared in Git, and pulls changes in rather than having an external system push them out. This part goes deep on how it's built and how to operate it, since it's the pull-based half of the CI/CD picture, alongside the push-based GitlabCI from the previous part.

## Goals

Subjects we will cover:

**Core Architectural Components**

- API Server
- Repository Server
- Application Controller
- Application
- AppProject
- ApplicationSet

**General Lifecycle**

- Reconciliation Loop
- Manual Sync Policy
- Automated Sync Policy
- Drifting

**Orchestration**

- Sync Waves
- Resource Hooks

**Observability Tools**

- Health Checks

## Outcome

<details>
<summary>Questions to test your comprehension of ArgoCD</summary>

### Core Architecture & Philosophy

1. **The Pull Model**: In the CI/CD part you saw the security argument for pull-based deployment. Concretely, where do the cluster credentials live when you deploy with ArgoCD, compared to a GitlabCI job that runs `kubectl apply` from a runner?

2. **The Reconciliation Loop**: How does ArgoCD know when a change has occurred in Git? Explain the difference between using a Webhook and the default polling interval.

3. **Desired vs. Live State**: If a developer manually changes a replica count in the Kubernetes cluster using `kubectl edit`, what happens in ArgoCD if "Self-Heal" is disabled? What if it is enabled?

### Application Management & Syncing

1. **Sync Policies**: Compare and contrast the `Prune`, `SelfHeal`, and `AllowEmpty` sync options. What are the risks of enabling `Prune` on a production database?

2. **The Application CRD**: What are the three mandatory pieces of information required in an Application manifest to link Git to a cluster?

3. **Health Statuses**: What is the difference between an application being `OutOfSync` and being `Degraded`? Can an app be `Synced` but `Degraded`?

### Orchestration & Tooling

1. **Sync Waves**: If Resource A has a sync-wave of `-1` and Resource B has a sync-wave of `5`, which one is applied first? What happens if Resource A fails to reach a `Healthy` state?

2. **Sync Hooks**: How would you use a `PostSync` hook to notify an external API only after a deployment is successful? How do ArgoCD's Sync Hooks (`PreSync`, `Sync`, `PostSync`) compare to the Helm hooks you learned about in the Kubernetes part - are they the same mechanism, or does ArgoCD implement its own?

3. **Helm Integration**: How do you pass multiple value files to a single ArgoCD Application? How does ArgoCD handle Helm "Secrets" or sensitive values?

4. **ApplicationSets**: What is an ApplicationSet, and what are its "Generators"? Explain how a `Git Generator` differs from a `Cluster Generator`.

5. **AppProjects**: What is an AppProject, and which project does an Application belong to if you don't pick one? How would you restrict a team so it can only deploy `Service` and `Deployment` resources, and not `Namespaces` or `ClusterRoles`?

6. **The App-of-Apps Pattern**: Explain the logic of a "Root" application. How do you prevent a deletion of the Root app from accidentally deleting every child application in the cluster?

### Troubleshooting and Observability

1. **Diffing Logic**: How does ArgoCD handle "IgnoreDifferences"? Give a real-world example where you would want ArgoCD to ignore a specific field in a Live object (e.g., HPA replica counts).

</details>

### Exercise

Do part 4 of MCK, which turns what you built in the earlier parts into a service with an ApplicationSet. Go over it with your mentor when you're done.

### Links

- <https://argo-cd.readthedocs.io/en/stable/>
- <https://argo-cd.readthedocs.io/en/stable/core_concepts/>
- <https://medium.com/@veerababu.narni232/a-complete-overview-of-argocd-with-a-practical-example-f4a9a8488cf9>
- <https://argo-cd.readthedocs.io/en/stable/getting_started/>
- <https://argo-cd.readthedocs.io/en/stable/user-guide/projects/>
- <https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/>
