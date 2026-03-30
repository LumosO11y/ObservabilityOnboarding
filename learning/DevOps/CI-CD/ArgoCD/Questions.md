# Overview
Questions to test your comprehension of ArgoCD

## Core Architecture & Philosophy
1. **The Pull Model**: Explain why ArgoCD is considered more secure than a traditional Jenkins pipeline that uses ``kubectl apply`` from an external runner.

2. **Controller Responsibilities**: What is the specific role of the ``repo-server`` versus the ``application-controller``? Which one is responsible for rendering Helm charts?

3. **The Reconciliation Loop**: How does ArgoCD know when a change has occurred in Git? Explain the difference between using a Webhook and the default polling interval.

4. **Desired vs. Live State**: If a developer manually changes a replica count in the Kubernetes cluster using ``kubectl edit``, what happens in ArgoCD if "Self-Heal" is disabled? What if it is enabled?

5. **Caching**: Why does ArgoCD use Redis, and what kind of data is stored there?


## Application Management & Syncing
1. **Sync Policies**: Compare and contrast the ``Prune``, ``SelfHeal``, and ``AllowEmpty`` sync options. What are the risks of enabling ``Prune`` on a production database?

2. **The Application CRD**: What are the three mandatory pieces of information required in an Application manifest to link Git to a cluster?

3. **Health Statuses**: What is the difference between an application being ``OutOfSync`` and being ``Degraded``? Can an app be ``Synced`` but ``Degraded``?

4. **Refresh Types**: When would you use a ``Hard Refresh`` instead of a standard ``Refresh`` in the UI?

5. **Sync Options**: Explain the ``ServerSideApply=true`` sync option. When is this necessary (e.g., dealing with large CRDs or Field Managers)?


## Orchestration and Orchestration Tools
1. **Sync Waves**: If Resource A has a sync-wave of ``-1`` and Resource B has a sync-wave of ``5``, which one is applied first? What happens if Resource A fails to reach a ``Healthy`` state?

2. **Sync Hooks**: How would you use a ``PostSync`` hook to notify an external API only after a deployment is successful?

3. **Helm Integration**: How do you pass multiple value files to a single ArgoCD Application? How does ArgoCD handle Helm "Secrets" or sensitive values?

4. **Kustomize**: How does ArgoCD handle Kustomize "images" transformations without you having to manually edit the ``kustomization.yaml``?

5. **The App-of-Apps Pattern**: Explain the logic of a "Root" application. How do you prevent a deletion of the Root app from accidentally deleting every child application in the cluster?

## Scaling and Multi-Tenancy
1. **ApplicationSets**: What are "Generators"? Explain how a ``Git Generator`` differs from a ``Cluster Generator``.

2. **AppProjects**: How do you restrict a specific team so they can only deploy ``Service`` and ``Deployment`` resources, but not ``Namespaces`` or ``ClusterRoles``?

3. **Multi-Cluster**: How does ArgoCD manage applications on a "Destination" cluster that is different from the one ArgoCD is installed on? What credentials are used?

4. **RBAC**: How do you map an OIDC group (like a GitHub Team) to a specific "Admin" or "ReadOnly" role within an ArgoCD Project?

## Troubleshooting and Observability
