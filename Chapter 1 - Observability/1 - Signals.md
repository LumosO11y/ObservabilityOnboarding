# Signals

## Overview

In this part, you'll dive into important concepts in Observability.
More specifically, you'll learn in-depth about the different signals: Logs, Metrics, Traces and Profiling.

You'll explore the need for each of them, their use case and the relation between them.
You'll also learn about how they complete each other and grant us the bigger picture.

## Goals

- Understand the difference between traces, logs and metrics.
- Understand the usage for each type of signal, especially the difference between traces and logs.
- Understand what baggage is and how you can use it.
- Understand how you can utilize context to your advantage, and how that context propagates across service boundaries.
- Understand what sampling is and why it's needed.

## Outcome

The outcome of this part should be a PowerPoint presentation explaining in-depth the concepts of logs, traces, metrics and Profiling and their role when making your system Observable.

In your presentation make sure there is an answer to the following questions:

1. What are signals?
2. What is a span? What does it consist of?
    - Read about the context field. What does it consist of? Why does it contain those specific fields?
    - Read about span events. Why are they needed? How do they differ from regular logs?
3. What is context propagation? When a request crosses from one service to the next over the network, how does the receiving service know which trace and span it belongs to?
    - What is baggage? How is it different from the trace context, and what would be a good (and a bad) thing to put in it?
4. How are traces stored in most Observability backends?
5. A busy service can handle thousands of requests per second, each one producing a trace. What is sampling, and what problem does it solve? What's the difference between head-based and tail-based sampling, and what does each trade off?
6. What is a log? What does it consist of?
7. How are logs usually stored? (especially in our unit)
8. Many say logs and traces are very similar. How do they differ and what do they have in common? When will we use each of them?
9. What is log correlation?
10. What is a metric? What does it consist of?
11. How are metrics usually stored (especially in our unit)?
12. What is cardinality?
13. What are the different types of metrics? Explain each type and give examples of usages for each type.
14. What are RED metrics?
15. What is profiling? Explain the concept behind it.
16. What issue does profiling come to solve that the other signals don't?
17. What is continuous profiling? Explain the concept behind it.

**❗ Don't forget to talk with your mentor to schedule a time for you to present to the whole team :)**

### Links

Here are some useful links to start from, yet again, you are encouraged to search more and update this list of links if you think they are good:

- <https://opentelemetry.io/docs/concepts/signals>
- <https://opentelemetry.io/docs/concepts/context-propagation/>
- <https://opentelemetry.io/docs/concepts/sampling/>
- <https://www.w3.org/TR/baggage/>
- <https://sematext.com/glossary/three-pillars-of-observability/>
- <https://www.oreilly.com/library/view/distributed-systems-observability/9781492033431/ch04.html>
- [Chapter 4](../assets/Distributed-Systems-Observability-eBook.pdf)
- <https://iamondemand.com/blog/the-3-pillars-of-system-observability-logs-metrics-and-tracing/>
- <https://www.splunk.com/en_us/blog/learn/melt-metrics-events-logs-traces.html>
- <https://grafana.com/docs/tempo/latest/operations/best-practices/>
- <https://codersociety.com/blog/articles/metrics-tracing-logging>
- <https://logz.io/blog/logs-or-metrics/>
- <https://opentelemetry.io/blog/2024/profiling/>
- [Chapter 3](../assets/learning-opentelemetry-setting-up-and-operating-a-modern-observability-system.pdf).
- [Chapter 5](../assets/observability-engineering-achieving-production.pdf)
- [Chapter 6](../assets/observability-engineering-achieving-production.pdf)
