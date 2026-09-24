# Grafana

## Overview

Grafana is the visualization and dashboarding layer of our observability stack - it's where metrics, logs, and traces from our other tools (Prometheus, Tempo, Pyroscope, and more) actually get looked at side by side. This part covers what Grafana is and how it's built, along with two of Grafana's own backends - Tempo for distributed tracing and Pyroscope for continuous profiling - then points you at official resources and videos to get hands-on with all three.

## Goals

- Understand what Grafana is and where it sits relative to the data sources it visualizes.
- Understand Grafana's high-level architecture (frontend, backend, data sources, plugins).
- Get comfortable building a basic dashboard and panel.
- Get comfortable with the Grafana-specific features that make PromQL queries dynamic and performant (variables, legend format, min step, instant queries).
- Understand how Tempo stores traces and why.
- Understand Tempo's high-level architecture (distributor, ingester, query frontend, object storage).
- Get comfortable writing a basic TraceQL query.
- Understand what running a profiler continuously in production costs, and how Pyroscope keeps that cost low.
- Understand Pyroscope's high-level architecture (how it collects and stores profiling data).
- Get comfortable reading a flame graph in Grafana.

## Outcome

### Grafana

1. What is Grafana, and what problem does it solve that looking at each data source's own UI doesn't?
2. At a high level, how do Grafana's frontend and backend interact with a data source when a dashboard loads?
3. What is a data source, and how does Grafana stay agnostic to where the underlying data (metrics, logs, traces) actually lives?
4. What does `[$__rate_interval]` do, and why is it preferred over a hardcoded range like `[5m]` in a PromQL query on a Grafana dashboard?
5. In Grafana, what do the "Legend Format" and "Min Step" query options control, and when would you enable "Instant Query" on a panel?
6. Build a simple dashboard with at least one panel. What did you visualize, and why did you pick that panel type?

### Tempo

1. How does Tempo store traces, and why does it use object storage instead of a database with full indexes? What trade-off does that create when you want to search for traces?
2. At a high level, what happens to a trace between a service emitting it and you being able to query it in Tempo?
3. What is TraceQL, and how does querying traces differ from querying metrics with PromQL?
4. What's the difference between Tempo's monolithic and microservices deployment modes, and when would you choose one over the other?

### Pyroscope

1. You learned what continuous profiling is in Chapter 1. What does running a profiler continuously in production cost, and how does Pyroscope keep that overhead low enough to leave it on?
2. What is a flame graph, and how do you read one?
3. At a high level, how does Pyroscope collect profiling data from an application, and how does that data end up visualized in Grafana?

### Links

#### Grafana

**Documentation & Getting Started**

- **Grafana Official Website** — Main page with downloads, docs, and product info:
  [https://grafana.com/](https://grafana.com/)
- **Grafana Tutorials & Guides** — Step‑by‑step tutorials for basic and intermediate skills:
  [https://grafana.com/tutorials/](https://grafana.com/tutorials/)
- **Grafana Fundamentals** — Official fundamentals tutorial covering dashboards, logs, metrics, etc.:
  [https://grafana.com/tutorials/grafana-fundamentals/](https://grafana.com/tutorials/grafana-fundamentals/)
- **Grafana GitHub Repository** — Source code, issues, and contribution guide:
  [https://github.com/grafana/grafana](https://github.com/grafana/grafana)
- **Query and Transform Data** — Query options (legend format, min step, instant queries) and transformations:
  [https://grafana.com/docs/grafana/latest/panels-visualizations/query-transform-data/](https://grafana.com/docs/grafana/latest/panels-visualizations/query-transform-data/)

**Architecture (How Grafana Works)**

- **Grafana Overview & Architecture (Wiki)** — Basic description of Grafana’s purpose, frontend/backend languages, and ecosystem integration:
  [https://en.wikipedia.org/wiki/Grafana](https://en.wikipedia.org/wiki/Grafana)
- **Architecture Explained Article** — Detailed explanation of how Grafana’s frontend, backend, data sources, and plugins interact:
  [https://dev.to/favxlaw/grafana-architecture-explained-how-the-backend-and-data-flow-work-49d0](https://dev.to/favxlaw/grafana-architecture-explained-how-the-backend-and-data-flow-work-49d0)
- **High‑Level Architecture Video** — Video about Grafana architecture components and data flow:
  [https://www.youtube.com/watch?v=SRZlYjKBkPw](https://www.youtube.com/watch?v=SRZlYjKBkPw)

**Beginner Videos**

- **Grafana Introduction in 10 Minutes (Beginner Tutorial)** — General intro to Grafana and core features:
  [https://www.youtube.com/watch?v=ow-eCngnfBQ](https://www.youtube.com/watch?v=ow-eCngnfBQ)
- **What is Grafana & Architecture Explained** — Covers what Grafana is and basic architecture concepts:
  [https://www.youtube.com/watch?v=clPEhemPy2g](https://www.youtube.com/watch?v=clPEhemPy2g)
- **Creating Visualizations with Grafana (Beginners Episode)** — Learn how to build visualizations step by step:
  [https://www.youtube.com/watch?v=051wmmDNJnc](https://www.youtube.com/watch?v=051wmmDNJnc)
- **Visualizing Logs in Grafana** — How to view and use logs panels:
  [https://opsmatters.com/videos/beginners-guide-visualizing-logs-grafana](https://opsmatters.com/videos/beginners-guide-visualizing-logs-grafana)

**Community & Learning Paths**

- **Grafana Learning Journeys** — Guided step‑by‑step learning paths from Grafana Labs:
  [https://grafana.com/docs/learning-journeys/](https://grafana.com/docs/learning-journeys/)
- **Community Forums** — Ask questions and get help:
  [https://community.grafana.com/](https://community.grafana.com/)
- **Webinars & Videos by Grafana Labs** — Official webinars on dashboards, alerting, observability, and integrations:
  [https://grafana.com/videos/](https://grafana.com/videos/)

#### Tempo

**Documentation & Getting Started**

- **Official Grafana Tempo Overview** (overview + basic info):
  [https://grafana.com/oss/tempo/](https://grafana.com/oss/tempo/)
- **Tempo Docs — Setup & Tracing Guide** (installation, config, examples):
  [https://grafana.com/docs/tempo/latest/set-up-for-tracing/](https://grafana.com/docs/tempo/latest/set-up-for-tracing/)
- **Tempo GitHub Repository** (source code, examples, deployments):
  [https://github.com/grafana/tempo](https://github.com/grafana/tempo)

**Architecture (How Tempo Works)**

- **Tempo Architecture (official docs)** — describes Tempo components (distributor, ingester, query frontend, object storage, metrics generator) and how traces flow through the system:
  [https://grafana.com/docs/tempo/latest/operations/architecture/](https://grafana.com/docs/tempo/latest/operations/architecture/)

**Beginner Videos**

- **Beyond Tracing with Grafana Tempo — What Do We Do With All This Data**
  [https://www.youtube.com/watch?v=zVHHeO8tAWQ](https://www.youtube.com/watch?v=zVHHeO8tAWQ)
- **How to Get Started with Tempo (Grafana Office Hours)** — tempo basics and TraceQL overview:
  [https://www.youtube.com/watch?v=pUAmL28uzos](https://www.youtube.com/watch?v=pUAmL28uzos)
- **How to Query Span Events with TraceQL (Tempo Tutorial)** — TraceQL basics:
  [https://www.youtube.com/watch?v=3_TID7WUcBY](https://www.youtube.com/watch?v=3_TID7WUcBY)
- **New TraceQL Features (Tempo 2.10 demo)** — extended query features:
  [https://www.youtube.com/watch?v=5aX3NxSVwMw](https://www.youtube.com/watch?v=5aX3NxSVwMw)

**Additional Topics**

- **Tempo Example Setups** — example deployments (Docker Compose / Helm / Kubernetes):
  [https://grafana.com/docs/tempo/latest/getting-started/example-demo-app/](https://grafana.com/docs/tempo/latest/getting-started/example-demo-app/)
- **Monolithic & Microservices Modes** — single binary vs separate components:
  [https://grafana.com/docs/tempo/latest/set-up-for-tracing/setup-tempo/plan/deployment-modes/](https://grafana.com/docs/tempo/latest/set-up-for-tracing/setup-tempo/plan/deployment-modes/)

**Community & Support**

- **Grafana Tempo Community Forum** (discussion, questions, tips):
  [https://community.grafana.com/c/grafana-tempo/40](https://community.grafana.com/c/grafana-tempo/40)

#### Pyroscope

- **Official Website & Documentation** — Learn Pyroscope basics and setup:
  [https://grafana.com/docs/pyroscope/latest/](https://grafana.com/docs/pyroscope/latest/)
- **GitHub Repository** — Explore the source code and examples:
  [https://github.com/grafana/pyroscope](https://github.com/grafana/pyroscope)
- **Getting Started Guide** — How to install and run Pyroscope:
  [https://grafana.com/docs/pyroscope/latest/get-started/](https://grafana.com/docs/pyroscope/latest/get-started/)
- **Architecture Overview** — How Pyroscope collects and stores profiling data:
  [https://grafana.com/docs/pyroscope/latest/reference-pyroscope-architecture/](https://grafana.com/docs/pyroscope/latest/reference-pyroscope-architecture/)
- **Visualizing Profiling Data in Grafana** — Using Pyroscope with Grafana dashboards:
  [https://grafana.com/docs/grafana/latest/datasources/pyroscope/](https://grafana.com/docs/grafana/latest/datasources/pyroscope/)
- **Video: Continuous Profiling with Pyroscope** — Overview and demo:
  [https://www.youtube.com/watch?v=XL2yTCPy2e0](https://www.youtube.com/watch?v=XL2yTCPy2e0)
