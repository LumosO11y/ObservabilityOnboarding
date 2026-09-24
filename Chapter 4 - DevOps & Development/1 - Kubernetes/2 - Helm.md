# Helm

## Overview

Helm is the de-facto package manager for Kubernetes: it packages a set of manifests into a reusable, versioned unit (a "chart") that can be templated, installed, upgraded, and rolled back as a single release, instead of a pile of YAML files you apply by hand.

## Goals

- Understand what a Helm chart is and what's inside one.
- Understand what a Helm release is, and how install/upgrade/rollback work.
- Understand Helm's templating engine and how values get injected into templates.
- Understand chart dependencies (subcharts) and Helm repositories.
- Understand Helm hooks and what they let you do around a release's lifecycle.
- Get comfortable writing and installing a basic chart.

## Outcome

1. What is a Helm chart? What are the minimum pieces every chart needs to have?
2. What is a Helm release? What's the difference between `helm install` and `helm upgrade`?
3. How does `helm rollback` work? What does Helm actually keep track of to make a rollback possible?
4. Explain Helm's templating: how does a value in `values.yaml` end up substituted into a Kubernetes manifest under `templates/`? Give a small example.
5. What is a chart dependency (subchart)? Give a realistic example of when you'd pull one in instead of writing everything yourself.
6. What is a Helm repository, and how do `helm repo add` / `helm search repo` fit into finding and installing a third-party chart (e.g. the official OpenTelemetry Collector chart)?
7. What are Helm hooks (e.g. `pre-install`, `post-upgrade`)? What kind of problem would you use one to solve?
8. What's the difference between Helm and Kustomize as ways to manage Kubernetes configuration? When would you reach for one over the other?
9. Write a minimal Helm chart for a simple app of your choice. Install it, change a value, `helm upgrade`, then `helm rollback` back to the previous release.

### Links

- <https://helm.sh/docs/intro/using_helm/>
- <https://helm.sh/docs/chart_template_guide/getting_started/>
- <https://helm.sh/docs/topics/charts/>
- <https://helm.sh/docs/topics/charts_hooks/>
- <https://helm.sh/docs/chart_best_practices/>
- <https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/>
