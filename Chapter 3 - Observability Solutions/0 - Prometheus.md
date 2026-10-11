# Prometheus

## Overview

Prometheus is the de-facto standard for metrics collection in cloud-native systems: a time-series database with its own protocol for getting data in and its own query language, PromQL, for getting data out. This part covers what Prometheus is and how it fits into the wider metrics ecosystem, then moves into PromQL itself.

## Goals

- Understand what Prometheus is and the problem it solves.
- Know a few alternatives to Prometheus, and a few Prometheus-compatible solutions.
- Understand the Prometheus protocol: the pull-based scrape model and the push-based remote-write model.
- Understand the Prometheus metric types and which functions apply to each.
- Understand instant vectors vs. range vectors, and how to select and filter series with label matchers.
- Understand `rate()` vs. `irate()`, aggregation operators, and the `by` clause.
- Understand binary operators (arithmetic, comparison) and the `offset` modifier.
- Understand histograms and how to compute percentiles from them.
- Understand recording rules.
- Understand how OpenTelemetry metrics end up in Prometheus.
- Understand what too high and too low cardinality do to Prometheus and Prometheus-compatible stores, and how to find and fix each.

## Outcome

### Prometheus

1. What is Prometheus, and what problem does it solve?
2. Name 2-3 alternatives to Prometheus for metrics collection/storage. How do they differ from Prometheus at a high level?
3. What does it mean for a solution to be "Prometheus-compatible"? Name 2-3 Prometheus-compatible solutions and what each one adds on top of vanilla Prometheus.
4. Prometheus's default model for getting metrics is scraping. Explain how scraping works: what does Prometheus request, from where, and how often? What format do targets need to expose their metrics in?
5. What is remote_write, and how does it differ from scraping? Why might a team run both at once?

### PromQL

1. What are the Prometheus metric types, and what's an example use case for each? How do they map to the generic metric types you learned about in Chapter 1?
2. Which PromQL functions are meant for Counters, and which for Gauges? What goes wrong if you use `rate()` on a Gauge?
3. What is the difference between an instant vector and a range vector? Give an example PromQL expression using label matchers (`=`, `!=`, `=~`, `!~`).
4. What's the difference between `rate()` and `irate()`? When would you reach for each?
5. Write a PromQL query that returns the percentage of HTTP requests returning a 5xx status, broken down `by (method)`.
6. What's the difference between `sum(rate(metric[5m]))` and taking the rate of a series that has already been summed? Which one is correct, and what goes wrong with the other?
7. What does the `offset` modifier let you do? Give an example.
8. How is a Prometheus histogram stored? Write a query that returns the p95 request latency per service. How accurate is a percentile computed from a histogram, and why? What do native histograms change?

### Recording Rules & OpenTelemetry

1. What is a recording rule, and why would you use one?
2. What are the different ways OpenTelemetry metrics can get into Prometheus? Compare them.
3. What is metric temporality in OpenTelemetry, and which kinds exist? Which one does Prometheus work with, and what has to happen when they don't match? What happens to metric names and attributes on the way in?

### Cardinality

1. In Chapter 1 you learned what cardinality is. In Prometheus, what makes up the identity of a series? How would you estimate how many series a single metric produces?
2. What happens to Prometheus when cardinality gets too high? Which kinds of labels usually cause it?
3. In a running Prometheus, how would you find which metrics and labels contribute the most series?
4. Where can you reduce cardinality: in the instrumented code, in the Collector, and in Prometheus itself? What are the options at each point, and what do you lose with each one?
5. How does a Prometheus-compatible store such as Mimir protect itself from a tenant that suddenly sends far too many series? What does the sender see when that happens?
6. Now the opposite problem: cardinality that is too low. What happens when two different sources write series with exactly the same name and labels? What errors, or silently wrong results, can you get?
7. How can this happen with OpenTelemetry metrics? Think about the attribute translation from the previous section, and about running several replicas of a service or several Collectors. What is the single-writer principle in the OpenTelemetry metrics data model, and how do you keep it?

### Links

**Prometheus**

- [Prometheus Overview](https://prometheus.io/docs/introduction/overview/)
- [Prometheus: Pull vs. Push](https://prometheus.io/docs/introduction/faq/#why-do-you-pull-rather-than-push)
- [Prometheus Remote Write Specification](https://prometheus.io/docs/specs/prw/remote_write_spec/)
- [Prometheus Exposition Formats](https://prometheus.io/docs/instrumenting/exposition_formats/)
- [Grafana Mimir - a Prometheus-compatible, horizontally scalable metrics store](https://grafana.com/oss/mimir/)

**PromQL**

- [Understanding Prometheus Metric Types](https://www.youtube.com/watch?v=fhx0ehppMGM)
- [Understanding Prometheus Histograms](https://www.youtube.com/watch?v=yYbXak-1hew)
- [Understanding Counter Rates and Increases in PromQL](https://www.youtube.com/watch?v=7uy_yovtyqw)
- [Prometheus Querying Basics](https://prometheus.io/docs/prometheus/latest/querying/basics/)
- [Histograms and Summaries](https://prometheus.io/docs/practices/histograms/)

**Recording Rules & OpenTelemetry**

- [Recording Rules](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/)
- [Using Prometheus as your OpenTelemetry backend](https://prometheus.io/docs/guides/opentelemetry/)
- [OpenTelemetry metrics data model: temporality](https://opentelemetry.io/docs/specs/otel/metrics/data-model/#temporality)

**Cardinality**

- [Prometheus: Metric and Label Naming](https://prometheus.io/docs/practices/naming/#labels)
- [Prometheus: Instrumentation Best Practices](https://prometheus.io/docs/practices/instrumentation/#do-not-overuse-labels)
- [OpenTelemetry metrics data model: single-writer](https://opentelemetry.io/docs/specs/otel/metrics/data-model/#single-writer)
