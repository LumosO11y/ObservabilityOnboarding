# Lumos Observability Onboarding :satellite:

Welcome to Lumos! This repository is your gateway to a structured onboarding program designed to bring you up to speed on the Observability and Monitoring ecosystem we work in every day. The program is organized into chapters, each with goals, questions to answer, curated reading, and hands-on exercises.

Start here: [Chapter 0 - Foundations/0 - Welcome](./Chapter%200%20-%20Foundations/0%20-%20Welcome.md)

## Table of Contents

## Chapter 0: Foundations

The big-picture fundamentals: core data concepts, systems & Linux, and ZooKeeper. This chapter is deliberately concept-first - no tooling yet.

- **[Welcome](./Chapter%200%20-%20Foundations/0%20-%20Welcome.md)** - introduction to the onboarding process and how it's organized.
- **[Big Data Core Concepts](./Chapter%200%20-%20Foundations/1%20-%20Big%20Data%20Core%20Concepts.md)** - the data landscape: the five V's, ETL vs. ELT, OLAP vs. OLTP, data lakes, CAP theorem, and more.

- **[System & Linux](./Chapter%200%20-%20Foundations/2%20-%20System%20&%20Linux.md)** - virtualization history, why it replaced bare metal, a hands-on Linux terminal exercise, and the questions/reading to go with it.

- **[Zookeeper](./Chapter%200%20-%20Foundations/3%20-%20Zookeeper.md)** - distributed coordination: Znodes, sessions, watches, and leader election.

## Chapter 1: Observability

What Observability actually means, the different signals (logs, metrics, traces, profiling), instrumentation, and the platforms that turn telemetry into insight. Estimated duration: ~5 days.

- **[Introduction](./Chapter%201%20-%20Observability/0%20-%20Introduction.md)**
- **[Signals](./Chapter%201%20-%20Observability/1%20-%20Signals.md)** - logs, metrics, traces, and profiling.
- **[Instrumentation](./Chapter%201%20-%20Observability/2%20-%20Instrumentation.md)**
- **[Platforms & APM](./Chapter%201%20-%20Observability/3%20-%20Platforms%20&%20APM.md)** - SLIs/SLOs/SLAs, golden signals, RUM, and comparing observability platforms.

## Chapter 2: OpenTelemetry

From the concept of OpenTelemetry to its specification, the Collector, and hands-on instrumentation. Estimated duration: 5 days max.

- **[Introduction](./Chapter%202%20-%20OpenTelemetry/0%20-%20Introduction.md)**
- **[Specification & OTLP](./Chapter%202%20-%20OpenTelemetry/1%20-%20Specification%20&%20OTLP.md)**
- **[The OpenTelemetry Collector](./Chapter%202%20-%20OpenTelemetry/2%20-%20Collector.md)** - includes a hands-on collector deployment.
- **[Instrumentation](./Chapter%202%20-%20OpenTelemetry/3%20-%20Instrumentation.md)** - includes instrumenting a real component.
- **[Additional Concepts](./Chapter%202%20-%20OpenTelemetry/4%20-%20Additional%20Concepts.md)** - sampling, OTTL, OpAMP, context propagation, and more.

## Chapter 3: Observability Solutions

The concrete platforms we (and the wider ecosystem) use to query and visualize telemetry - the Grafana stack today, with room to grow into other observability solutions.

- **[Grafana](./Chapter%203%20-%20Observability%20Solutions/0%20-%20Grafana.md)**
- **[PromQL](./Chapter%203%20-%20Observability%20Solutions/1%20-%20PromQL.md)** - querying metrics in Grafana.
- **[Tempo](./Chapter%203%20-%20Observability%20Solutions/2%20-%20Tempo.md)** - distributed tracing backend.
- **[Pyroscope](./Chapter%203%20-%20Observability%20Solutions/3%20-%20Pyroscope.md)** - continuous profiling.

## Chapter 4: DevOps & Development

The practitioner's toolbox: containerizing and orchestrating workloads, and the CI/CD tools that ship them.

**Docker**
- **[Containerization](./Chapter%204%20-%20DevOps%20&%20Development/0%20-%20Docker/0%20-%20Containerization.md)** - images, containers, why containers replaced VMs, and Docker fundamentals.
- **[Dockerfile Exercise](./Chapter%204%20-%20DevOps%20&%20Development/0%20-%20Docker/1%20-%20Dockerfile%20Exercise.md)** - build and run your first Dockerfile against the sample app in `1 - Dockerfile Exercise App/`.

**Kubernetes**
- **[Orchestration](./Chapter%204%20-%20DevOps%20&%20Development/1%20-%20Kubernetes/0%20-%20Orchestration.md)** - why containers alone aren't enough in the cloud, and how Kubernetes solves it.
- **[Exercise](./Chapter%204%20-%20DevOps%20&%20Development/1%20-%20Kubernetes/1%20-%20Exercise.md)** - Minikube hands-on lab.

**DevOps & CI-CD**
- **[DevOps](./Chapter%204%20-%20DevOps%20&%20Development/2%20-%20DevOps%20&%20CI-CD/0%20-%20DevOps.md)** - why the industry moved from Waterfall to DevOps.
- **[CI/CD](./Chapter%204%20-%20DevOps%20&%20Development/2%20-%20DevOps%20&%20CI-CD/1%20-%20CI-CD.md)** - CI vs. CD, and push-based vs. pull-based deployment models.
- **[ArgoCD](./Chapter%204%20-%20DevOps%20&%20Development/2%20-%20DevOps%20&%20CI-CD/2%20-%20ArgoCD.md)** - GitOps-style, pull-based continuous deployment.
- **[GitlabCI](./Chapter%204%20-%20DevOps%20&%20Development/2%20-%20DevOps%20&%20CI-CD/3%20-%20GitlabCI.md)** - push-based pipelines.

## Chapter 5: Stream Processing

The engineering stack behind our pipelines. Estimated duration: ~10 days.

- **[Java](./Chapter%205%20-%20Stream%20Processing/0%20-%20Java.md)**
- **[Spring](./Chapter%205%20-%20Stream%20Processing/1%20-%20Spring.md)**
- **[Kafka](./Chapter%205%20-%20Stream%20Processing/2%20-%20Kafka.md)**
- **[Flink](./Chapter%205%20-%20Stream%20Processing/3%20-%20Flink.md)** - ends with a hands-on Flink + Kafka + OTEL exercise.
- **[Metrics](./Chapter%205%20-%20Stream%20Processing/4%20-%20Metrics.md)**

## Chapter 6: Appendix

Optional, supplementary reading - useful background, not required to progress.

- **[ClickHouse](./Chapter%206%20-%20Appendix/0%20-%20ClickHouse.md)**
- **[eBPF](./Chapter%206%20-%20Appendix/1%20-%20eBPF.md)**
- **[Getting Into a Large Codebase](./Chapter%206%20-%20Appendix/2%20-%20Getting%20Into%20a%20Large%20Codebase.md)** - tips for navigating our codebase once you start contributing.

## Feedback :speech_balloon:

When you finish onboarding, please fill out [Feedback.md](./Feedback.md) - your experience helps us improve this process for the next person.

## Contribution :raised_hands:

If you have suggestions or ideas to enhance the onboarding for future members, feel free to contribute. Fork, create a feature branch, commit your changes, and open a pull request.
