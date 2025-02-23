# Part 2: Signals

## Overview

In this part, you'll dive into important concepts in Observability.
More specifically, you'll learn in-depth about the different signals: Logs, Metrics, Traces and Profiling.

You'll explore the need for each of them, their use case and the relation between them.
You'll also learn about how they complete each other and grant us the bigger picture.

## Goals

- Understand the difference between traces, logs and metrics.
- Understand the usage for each type of signal, especially the difference between traces and logs.
- Understand what is baggage and how you can use it.
- Understand how you can utilize context to your advantage

## Outcome

The outcome of this part should be a PowerPoint presentation explaining in-depth the concepts of logs, traces, metrics and Profiling and their role when making your system Observable.

#### In your presentation you should answer the following questions:

1. What are signals?
2. What is a span? What does it consist of. 
    * Read about the context field. Why does it consist of ? Why does it contain those specific fields ?
    * Read about span events ? Why are they needed ? How do they differ from regular logs ? 
3. How are traces stored in most Observability backends?
4. What is a log? What does it consist of?
5. How are logs usually stored? (especially in our unit) 
6. Many say logs and traces are very similar, how do they differ and what do they have in common? when will we use each of them
7. What is log correlation?
8. What is a metric? What does it consist of?
9. How are metrics usually stored (especially in our unit)
10. What is cardinality?
11. What are the different types of metrics? explain each type and give examples of usages for each type.
12. What are RED metrics?
13. What is profiling? explain the concept behind it.
14. What issue does profiling come to solve that the other signals don't?
15. What is continuous profiling? Explain the concept behind it.

#### ❗ Don't forget to talk with your mentor to schedule a time for you to present to the whole team :)


### Links

Here are some useful links to start from, Yet again, you are encouraged to search more and update this list of links if you think they are good:

* <https://opentelemetry.io/docs/concepts/signals>
* <https://sematext.com/glossary/three-pillars-of-observability/>
* <https://www.oreilly.com/library/view/distributed-systems-observability/9781492033431/ch04.html>
* [Chapter 4](../../assets/Distributed-Systems-Observability-eBook.pdf)
* <https://iamondemand.com/blog/the-3-pillars-of-system-observability-logs-metrics-and-tracing/>
* https://www.splunk.com/en_us/blog/learn/melt-metrics-events-logs-traces.html
* <https://grafana.com/docs/tempo/latest/operations/best-practices/>
* <https://codersociety.com/blog/articles/metrics-tracing-logging>
* <https://logz.io/blog/logs-or-metrics/>
* <https://opentelemetry.io/blog/2024/profiling/>