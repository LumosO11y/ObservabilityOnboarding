# Tempo

## Overview

Tempo is Grafana's distributed tracing backend - it's where the traces your services emit (via OpenTelemetry) get stored and queried, and it's built to correlate with the metrics and logs you already see in Grafana. This part covers how Tempo is built and how to query traces with TraceQL, then points you at official resources and videos.

## Goals

- Understand what a distributed trace is and why Tempo stores it the way it does.
- Understand Tempo's high-level architecture (distributor, ingester, query frontend, object storage).
- Get comfortable writing a basic TraceQL query.

## Outcome

1. What is a distributed trace, and what problem does it solve that logs and metrics alone don't?
2. At a high level, what happens to a trace between a service emitting it and you being able to query it in Tempo?
3. What is TraceQL, and how does querying traces differ from querying metrics with PromQL?
4. What's the difference between Tempo's monolithic and microservices deployment modes, and when would you choose one over the other?

### Links

#### Documentation & Getting Started

* **Official Grafana Tempo Overview** (overview + basic info):
  [https://grafana.com/oss/tempo/](https://grafana.com/oss/tempo/)
* **Tempo Docs — Setup & Tracing Guide** (installation, config, examples):
  [https://grafana.com/docs/tempo/latest/set-up-for-tracing/](https://grafana.com/docs/tempo/latest/set-up-for-tracing/)
* **Tempo GitHub Repository** (source code, examples, deployments):
  [https://github.com/grafana/tempo](https://github.com/grafana/tempo)

#### Architecture (How Tempo Works)

* **Tempo Architecture (official docs)** — describes Tempo components (distributor, ingester, query frontend, object storage, metrics generator) and how traces flow through the system:
  [https://grafana.com/docs/tempo/latest/operations/architecture/](https://grafana.com/docs/tempo/latest/operations/architecture/)

#### Beginner Videos

* **Beyond Tracing with Grafana Tempo — What Do We Do With All This Data**
  [https://www.youtube.com/watch?v=zVHHeO8tAWQ](https://www.youtube.com/watch?v=zVHHeO8tAWQ)
* **How to Get Started with Tempo (Grafana Office Hours)** — tempo basics and TraceQL overview:
  [https://www.youtube.com/watch?v=pUAmL28uzos](https://www.youtube.com/watch?v=pUAmL28uzos)
* **How to Query Span Events with TraceQL (Tempo Tutorial)** — TraceQL basics:
  [https://www.youtube.com/watch?v=3_TID7WUcBY](https://www.youtube.com/watch?v=3_TID7WUcBY)
* **New TraceQL Features (Tempo 2.10 demo)** — extended query features:
  [https://www.youtube.com/watch?v=5aX3NxSVwMw](https://www.youtube.com/watch?v=5aX3NxSVwMw)

#### Additional Topics

* **Tempo Example Setups** — example deployments (Docker Compose / Helm / Kubernetes):
  [https://grafana.com/docs/tempo/latest/getting-started/example-demo-app/](https://grafana.com/docs/tempo/latest/getting-started/example-demo-app/)
* **Monolithic & Microservices Modes** — single binary vs separate components:
  [https://grafana.com/docs/tempo/latest/set-up-for-tracing/setup-tempo/plan/deployment-modes/](https://grafana.com/docs/tempo/latest/set-up-for-tracing/setup-tempo/plan/deployment-modes/)

#### Community & Support

* **Grafana Tempo Community Forum** (discussion, questions, tips):
  [https://community.grafana.com/c/grafana-tempo/40](https://community.grafana.com/c/grafana-tempo/40)
