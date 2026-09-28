# Helm

## Overview

Helm is the de-facto package manager for Kubernetes: it packages a set of manifests into a reusable, versioned unit (a "chart") that can be templated, installed, upgraded, and rolled back as a single release, instead of a pile of YAML files you apply by hand.

## Goals

- Understand what a Helm chart is and what's inside one.
- Understand what a Helm release is, and how install/upgrade/rollback work.
- Understand Helm's templating engine and how values get injected into templates.
- Understand the Go template language underneath Helm, and how `.tpl` files and named templates keep charts DRY.
- Understand chart dependencies (subcharts) and Helm repositories.
- Understand Helm hooks and what they let you do around a release's lifecycle.
- Get comfortable writing and installing a basic chart.

## Outcome

1. What is a Helm chart? What are the minimum pieces every chart needs to have?
2. What is a Helm release? What's the difference between `helm install` and `helm upgrade`?
3. How does `helm rollback` work? What does Helm actually keep track of to make a rollback possible?
4. Explain Helm's templating: how does a value in `values.yaml` end up substituted into a Kubernetes manifest under `templates/`? Give a small example.
    - Helm templates are written in Go's template language. What does it give you beyond plain value substitution? Show a template that uses a conditional and a loop.
    - What do `{{-` and `-}}` do, and why do they matter so much when the output is YAML?
    - What is a `.tpl` file (e.g. `_helpers.tpl`)? What's special about files in `templates/` whose names start with `_`?
    - What are named templates? How do `define` and `include` work together, and why is `include` usually preferred over `template`?
    - What does the `tpl` function do? When would you want a value in `values.yaml` to contain template syntax itself?
5. What is a chart dependency (subchart)? Give a realistic example of when you'd pull one in instead of writing everything yourself.
6. What is a Helm repository, and how do `helm repo add` / `helm search repo` fit into finding and installing a third-party chart (e.g. the official OpenTelemetry Collector chart)? Where else can charts be stored besides a classic Helm repository? How does installing a chart from an OCI registry differ?
7. What are Helm hooks (e.g. `pre-install`, `post-upgrade`)? What kind of problem would you use one to solve?
8. What's the difference between Helm and Kustomize as ways to manage Kubernetes configuration? When would you reach for one over the other?
9. Write a minimal Helm chart for your Dockerfile Exercise app (Deployment, Service, and ConfigMap from the Kubernetes exercise, with the image tag and replica count in `values.yaml`). Install it, change a value, `helm upgrade`, then `helm rollback` back to the previous release.

### Links

- <https://helm.sh/docs/intro/using_helm/>
- <https://helm.sh/docs/chart_template_guide/getting_started/>
- <https://helm.sh/docs/chart_template_guide/control_structures/>
- <https://helm.sh/docs/chart_template_guide/named_templates/>
- <https://helm.sh/docs/howto/charts_tips_and_tricks/>
- <https://pkg.go.dev/text/template>
- <https://helm.sh/docs/topics/charts/>
- <https://helm.sh/docs/topics/charts_hooks/>
- <https://helm.sh/docs/chart_best_practices/>
- <https://helm.sh/docs/topics/registries/>
- <https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/>
