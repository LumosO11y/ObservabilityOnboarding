# Grafana

## Overview

Grafana is the visualization and dashboarding layer of our observability stack - it's where metrics, logs, and traces from our other tools actually get looked at side by side. Together with Grafana Labs' own backends it forms the **LGTM stack**. This part covers what Grafana is and how it's built, a high-level look at the LGTM stack, and two of its backends in more depth: Tempo and Pyroscope.

## Goals

- Understand what Grafana is and where it sits relative to the data sources it visualizes.
- Understand Grafana's high-level architecture (frontend, backend, data sources, plugins).
- Get comfortable building a basic dashboard and panel.
- Get comfortable with the Grafana-specific features that make PromQL queries dynamic and performant (variables, legend format, min step, instant queries).
- Know what the LGTM stack is, and what Loki and Mimir each do at a high level.
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

### The LGTM Stack

1. At a high level, what are Loki and Mimir, and what problem does each one solve? How does Mimir relate to the Prometheus you learned about in the previous part?
2. How do the pieces of the LGTM stack fit together? Which component receives which signal, and where does Grafana come in?

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

<details>
<summary>Curated reading</summary>

**Grafana: Documentation & Getting Started**

- [Grafana Official Website](https://grafana.com/)
- [Grafana Tutorials & Guides](https://grafana.com/tutorials/)
- [Grafana Fundamentals](https://grafana.com/tutorials/grafana-fundamentals/)
- [Grafana GitHub Repository](https://github.com/grafana/grafana)
- [Query and Transform Data](https://grafana.com/docs/grafana/latest/visualizations/panels-visualizations/query-transform-data/)

**Grafana: Architecture**

- [Grafana (Wikipedia)](https://en.wikipedia.org/wiki/Grafana)
- [Grafana Architecture Explained](https://dev.to/favxlaw/grafana-architecture-explained-how-the-backend-and-data-flow-work-49d0)
- [High-Level Architecture (video)](https://www.youtube.com/watch?v=SRZlYjKBkPw)

**Grafana: Beginner Videos**

- [Grafana Introduction in 10 Minutes](https://www.youtube.com/watch?v=ow-eCngnfBQ)
- [What is Grafana & Architecture Explained](https://www.youtube.com/watch?v=clPEhemPy2g)
- [Creating Visualizations with Grafana](https://www.youtube.com/watch?v=051wmmDNJnc)
- [Visualizing Logs in Grafana](https://opsmatters.com/videos/beginners-guide-visualizing-logs-grafana)

**Grafana: Community & Learning Paths**

- [Grafana Learning Journeys](https://grafana.com/docs/learning-journeys/)
- [Community Forums](https://community.grafana.com/)
- [Webinars & Videos by Grafana Labs](https://grafana.com/videos/)

**The LGTM Stack**

- [Grafana Labs Open-Source Stack](https://grafana.com/oss/)
- [Loki Overview](https://grafana.com/docs/loki/latest/get-started/overview/)
- [Mimir Documentation](https://grafana.com/docs/mimir/latest/)

**Tempo**

- [Grafana Tempo Overview](https://grafana.com/oss/tempo/)
- [Tempo Docs: Set Up for Tracing](https://grafana.com/docs/tempo/latest/set-up-for-tracing/)
- [Tempo GitHub Repository](https://github.com/grafana/tempo)
- [Tempo Architecture](https://grafana.com/docs/tempo/latest/introduction/architecture/)
- [Deployment Modes](https://grafana.com/docs/tempo/latest/set-up-for-tracing/setup-tempo/plan/deployment-modes/)
- [Tempo Example Setups](https://grafana.com/docs/tempo/latest/set-up-for-tracing/setup-tempo/example-demo-app/)
- [Beyond Tracing with Grafana Tempo (video)](https://www.youtube.com/watch?v=zVHHeO8tAWQ)
- [How to Get Started with Tempo (video)](https://www.youtube.com/watch?v=pUAmL28uzos)
- [How to Query Span Events with TraceQL (video)](https://www.youtube.com/watch?v=3_TID7WUcBY)
- [New TraceQL Features, Tempo 2.10 (video)](https://www.youtube.com/watch?v=5aX3NxSVwMw)
- [Grafana Tempo Community Forum](https://community.grafana.com/c/grafana-tempo/40)

**Pyroscope**

- [Pyroscope Documentation](https://grafana.com/docs/pyroscope/latest/)
- [Pyroscope GitHub Repository](https://github.com/grafana/pyroscope)
- [Getting Started](https://grafana.com/docs/pyroscope/latest/get-started/)
- [Pyroscope Architecture](https://grafana.com/docs/pyroscope/latest/reference-pyroscope-architecture/)
- [Pyroscope Data Source in Grafana](https://grafana.com/docs/grafana/latest/datasources/pyroscope/)
- [Continuous Profiling with Pyroscope (video)](https://www.youtube.com/watch?v=XL2yTCPy2e0)

</details>
