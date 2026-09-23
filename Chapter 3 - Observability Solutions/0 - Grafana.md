# Grafana

## Overview

Grafana is the visualization and dashboarding layer of our observability stack - it's where metrics, logs, and traces from our other tools (Prometheus, Tempo, Pyroscope, and more) actually get looked at side by side. This part covers what Grafana is and how it's built, then points you at official resources and videos to get hands-on with it.

## Goals

- Understand what Grafana is and where it sits relative to the data sources it visualizes.
- Understand Grafana's high-level architecture (frontend, backend, data sources, plugins).
- Get comfortable building a basic dashboard and panel.

## Outcome

1. What is Grafana, and what problem does it solve that looking at each data source's own UI doesn't?
2. At a high level, how do Grafana's frontend and backend interact with a data source when a dashboard loads?
3. What is a data source, and how does Grafana stay agnostic to where the underlying data (metrics, logs, traces) actually lives?
4. Build a simple dashboard with at least one panel. What did you visualize, and why did you pick that panel type?

### Links

#### Documentation & Getting Started

* **Grafana Official Website** — Main page with downloads, docs, and product info:
  [https://grafana.com/](https://grafana.com/)
* **Grafana Tutorials & Guides** — Step‑by‑step tutorials for basic and intermediate skills:
  [https://grafana.com/tutorials/](https://grafana.com/tutorials/)
* **Grafana Fundamentals** — Official fundamentals tutorial covering dashboards, logs, metrics, etc.:
  [https://grafana.com/tutorials/grafana-fundamentals/](https://grafana.com/tutorials/grafana-fundamentals/)
* **Grafana GitHub Repository** — Source code, issues, and contribution guide:
  [https://github.com/grafana/grafana](https://github.com/grafana/grafana)

#### Architecture (How Grafana Works)

* **Grafana Overview & Architecture (Wiki)** — Basic description of Grafana’s purpose, frontend/backend languages, and ecosystem integration:
  [https://en.wikipedia.org/wiki/Grafana](https://en.wikipedia.org/wiki/Grafana)
* **Architecture Explained Article** — Detailed explanation of how Grafana’s frontend, backend, data sources, and plugins interact:
  [https://dev.to/favxlaw/grafana-architecture-explained-how-the-backend-and-data-flow-work-49d0](https://dev.to/favxlaw/grafana-architecture-explained-how-the-backend-and-data-flow-work-49d0)
* **High‑Level Architecture Video** — Video about Grafana architecture components and data flow:
  [https://www.youtube.com/watch?v=SRZlYjKBkPw](https://www.youtube.com/watch?v=SRZlYjKBkPw)

#### Beginner Videos

* **Grafana Introduction in 10 Minutes (Beginner Tutorial)** — General intro to Grafana and core features:
  [https://www.youtube.com/watch?v=ow-eCngnfBQ](https://www.youtube.com/watch?v=ow-eCngnfBQ)
* **What is Grafana & Architecture Explained** — Covers what Grafana is and basic architecture concepts:
  [https://www.youtube.com/watch?v=clPEhemPy2g](https://www.youtube.com/watch?v=clPEhemPy2g)
* **Creating Visualizations with Grafana (Beginners Episode)** — Learn how to build visualizations step by step:
  [https://www.youtube.com/watch?v=051wmmDNJnc](https://www.youtube.com/watch?v=051wmmDNJnc)
* **Visualizing Logs in Grafana** — How to view and use logs panels:
  [https://opsmatters.com/videos/beginners-guide-visualizing-logs-grafana](https://opsmatters.com/videos/beginners-guide-visualizing-logs-grafana)

#### Community & Learning Paths

* **Grafana Learning Journeys** — Guided step‑by‑step learning paths from Grafana Labs:
  [https://grafana.com/docs/learning-journeys/](https://grafana.com/docs/learning-journeys/)
* **Community Forums** — Ask questions and get help:
  [https://community.grafana.com/](https://community.grafana.com/)
* **Webinars & Videos by Grafana Labs** — Official webinars on dashboards, alerting, observability, and integrations:
  [https://grafana.com/videos/](https://grafana.com/videos/)