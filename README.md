# Lumos Team Onboarding :satellite:

Welcome to Lumos! This repository is your gateway to a structured onboarding program designed to bring you up to speed on everything you need to know to work on our team - from core concepts to actual things you might need and use. The program is organized into chapters, each with goals, questions to answer, curated reading, and hands-on exercises.

The full onboarding takes roughly 7 weeks (~36 working days, not counting the optional Appendix).

Start here: [Chapter 0 - Foundations/0 - Welcome](./Chapter%200%20-%20Foundations/0%20-%20Welcome.md)

## Table of Contents

### Chapter 0: Foundations

The big-picture fundamentals: core data concepts and systems & Linux. This chapter is deliberately concept-first - no tooling yet. Estimated duration: ~3 days.

- **[Welcome](./Chapter%200%20-%20Foundations/0%20-%20Welcome.md)** (~0.5 day) - introduction to the onboarding process and how it's organized.
- **[Big Data Core Concepts](./Chapter%200%20-%20Foundations/1%20-%20Big%20Data%20Core%20Concepts.md)** (~1 day) - the data landscape: the five V's, ETL vs. ELT, OLAP vs. OLTP, data lakes, CAP theorem, and more.
- **[System & Linux](./Chapter%200%20-%20Foundations/2%20-%20System%20&%20Linux.md)** (~1.5 days) - operating systems, virtualization, processes, networking basics, a hands-on Linux terminal exercise, and cron.

### Chapter 1: Observability

What Observability actually means, the different signals (logs, metrics, traces, profiling), instrumentation, and the platforms that turn telemetry into insight. Estimated duration: ~5 days.

- **[Introduction](./Chapter%201%20-%20Observability/0%20-%20Introduction.md)** (~1 day) - what Observability really means, how it differs from monitoring, and Data Observability.
- **[Signals](./Chapter%201%20-%20Observability/1%20-%20Signals.md)** (~2 days, incl. the presentation) - logs, metrics, traces, and profiling, plus context propagation, baggage, and sampling.
- **[Instrumentation](./Chapter%201%20-%20Observability/2%20-%20Instrumentation.md)** (~0.5 day) - manual vs. automatic, and in-process vs. system-level instrumentation.
- **[Platforms & APM](./Chapter%201%20-%20Observability/3%20-%20Platforms%20&%20APM.md)** (~1.5 days) - SLIs/SLOs/SLAs, golden signals, RUM, and comparing observability platforms.

### Chapter 2: OpenTelemetry

From the concept of OpenTelemetry to its specification, the Collector, and hands-on instrumentation. Estimated duration: ~5 days.

- **[Introduction](./Chapter%202%20-%20OpenTelemetry/0%20-%20Introduction.md)** (~0.5 day) - where OpenTelemetry came from, what it is, and how the project is organized.
- **[Specification & OTLP](./Chapter%202%20-%20OpenTelemetry/1%20-%20Specification%20&%20OTLP.md)** (~1 day) - Protobuf, gRPC, OTLP, semantic conventions, and OpAMP.
- **[The OpenTelemetry Collector](./Chapter%202%20-%20OpenTelemetry/2%20-%20Collector.md)** (~2.5 days) - pipelines, components, scaling, OTTL, and a hands-on collector deployment.
- **[Instrumentation](./Chapter%202%20-%20OpenTelemetry/3%20-%20Instrumentation.md)** (~1 day) - the API vs. the SDK, Resources and Instrumentation Scope, and instrumenting a real component.

### Chapter 3: Observability Solutions

The concrete platforms we (and the wider ecosystem) use to query and visualize telemetry - the Grafana stack today, with room to grow into other observability solutions. Estimated duration: ~3 days.

- **[Prometheus](./Chapter%203%20-%20Observability%20Solutions/0%20-%20Prometheus.md)** (~1.5 days) - what Prometheus is, alternatives, scraping vs. remote-write, and querying with PromQL.
- **[Grafana](./Chapter%203%20-%20Observability%20Solutions/1%20-%20Grafana.md)** (~1.5 days) - the dashboarding layer (including PromQL in Grafana), plus its Tempo (tracing) and Pyroscope (profiling) backends.

### Chapter 4: DevOps & Development

The practitioner's toolbox: containerizing and orchestrating workloads, and the CI/CD tools that ship them. Estimated duration: ~10 days (Docker ~2, Kubernetes ~5, DevOps & CI-CD ~3).

**Docker**

- **[Containerization](./Chapter%204%20-%20DevOps%20&%20Development/0%20-%20Docker/0%20-%20Containerization.md)** (~1.5 days) - images, containers, why containers replaced VMs, and Docker fundamentals.
- **[Dockerfile Exercise](./Chapter%204%20-%20DevOps%20&%20Development/0%20-%20Docker/1%20-%20Dockerfile%20Exercise.md)** (~0.5 day) - build and run your first Dockerfile against the sample app in `1 - Dockerfile Exercise App/`.

**Kubernetes**

- **[Orchestration](./Chapter%204%20-%20DevOps%20&%20Development/1%20-%20Kubernetes/0%20-%20Orchestration.md)** (~3 days) - why containers alone aren't enough in the cloud, how Kubernetes solves it, and its distributions (OpenShift, Rancher, and more).
- **[Exercise](./Chapter%204%20-%20DevOps%20&%20Development/1%20-%20Kubernetes/1%20-%20Exercise.md)** (~1 day) - Minikube hands-on lab.
- **[Helm](./Chapter%204%20-%20DevOps%20&%20Development/1%20-%20Kubernetes/2%20-%20Helm.md)** (~1 day) - packaging, templating, and releasing Kubernetes manifests.

**DevOps & CI-CD**

- **[DevOps](./Chapter%204%20-%20DevOps%20&%20Development/2%20-%20DevOps%20&%20CI-CD/0%20-%20DevOps.md)** (~0.5 day) - why the industry moved from Waterfall to DevOps, and its core practices.
- **[CI/CD](./Chapter%204%20-%20DevOps%20&%20Development/2%20-%20DevOps%20&%20CI-CD/1%20-%20CI-CD.md)** (~0.5 day) - CI vs. CD, and push-based vs. pull-based deployment models.
- **[GitlabCI](./Chapter%204%20-%20DevOps%20&%20Development/2%20-%20DevOps%20&%20CI-CD/2%20-%20GitlabCI.md)** (~1 day) - push-based pipelines.
- **[ArgoCD](./Chapter%204%20-%20DevOps%20&%20Development/2%20-%20DevOps%20&%20CI-CD/3%20-%20ArgoCD.md)** (~1 day) - GitOps-style, pull-based continuous deployment.

### Chapter 5: Stream Processing

The engineering stack behind our pipelines. Estimated duration: ~10 days.

- **[Java](./Chapter%205%20-%20Stream%20Processing/0%20-%20Java.md)** (~2.5 days) - the language, the JVM, collections & streams, concurrency, and Maven.
- **[Spring](./Chapter%205%20-%20Stream%20Processing/1%20-%20Spring.md)** (~1.5 days) - dependency injection, beans, and building REST APIs with Spring Boot.
- **[Zookeeper](./Chapter%205%20-%20Stream%20Processing/2%20-%20Zookeeper.md)** (~0.5 day) - distributed coordination: Znodes, sessions, watches, and leader election.
- **[Kafka](./Chapter%205%20-%20Stream%20Processing/3%20-%20Kafka.md)** (~1.5 days) - topics, partitions, consumer groups, delivery guarantees, and its use of ZooKeeper.
- **[Flink](./Chapter%205%20-%20Stream%20Processing/4%20-%20Flink.md)** (~4 days) - state, checkpoints, time and windowing, ending with a hands-on Flink + Kafka + OTEL exercise.

### Chapter 6: Appendix

Optional, supplementary reading - useful background, not required to progress. No time is allotted; read it whenever you have slack.

- **[ClickHouse](./Chapter%206%20-%20Appendix/0%20-%20ClickHouse.md)** - the column-oriented OLAP database, and why it suits observability data.
- **[eBPF](./Chapter%206%20-%20Appendix/1%20-%20eBPF.md)** - running sandboxed programs in the kernel, and how it powers system-level instrumentation.
- **[Getting Into a Large Codebase](./Chapter%206%20-%20Appendix/2%20-%20Getting%20Into%20a%20Large%20Codebase.md)** - tips for navigating our codebase once you start contributing.

## Feedback :speech_balloon:

When you finish onboarding, please fill out [Feedback.md](./Feedback.md) - your experience helps us improve this process for the next person.

## Contribution :raised_hands:

If you have suggestions or ideas to enhance the onboarding for future members, feel free to contribute. Fork, create a feature branch, commit your changes, and open a pull request.
