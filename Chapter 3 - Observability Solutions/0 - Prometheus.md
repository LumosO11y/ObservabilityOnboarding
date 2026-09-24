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
