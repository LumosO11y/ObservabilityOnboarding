# The OpenTelemetry Collector

## Overview

In this part you'll learn about the OpenTelemetry Collector.
At the end of this part, you'll know in detail about the OpenTelemetry collector and how it's built, especially the Collector pipeline system and everything surrounding it. In addition you will grasp the importance of the collector in the OpenTelemetry Ecosystem.

## Goals

- Understand what the Collector is and why it sits between your applications and your backends.
- Understand the Collector pipeline and every component type that makes it up.
- Understand how to deploy, scale, monitor, and debug the Collector in production.
- Know the Collector distributions and when to use each.
- Deploy and configure a Collector yourself, and send telemetry through it.

## Outcome

You should have a markdown answering the questions below and in addition 2 containers running.
Make sure you go in-detail and assure you have deep understanding of this part as it will meet you regularly on the day-to-day job.

1. What is the OpenTelemetry Collector?
2. Why is the collector needed? Why should I use the OTel collector instead of other products like Logstash or Nifi?
3. Explain in detail the flow of a pipeline in a collector. How does it relate to ETL?
4. How does the OpenTelemetry collector relate to OTLP?
5. When would you send OTLP to a collector over gRPC, and when over HTTP? What are the trade-offs?
6. List the architecture paradigms of the collector. What are the pros and cons of each? Make a table that compares them to each other. (There should be 5 in total)
7. List and elaborate in detail on every component that makes up the collector. Give 2 examples of each, and explain their use. (including Extensions and Connectors). Make sure to choose useful ones.
8. Pick 2 processors that almost every collector should have (different from the ones you used as examples in the previous question) and elaborate more on them. Explain why you picked these in particular.
9. What are the different scopes of the transformation processor?
10. What is OTTL (OpenTelemetry Transformation Language), and what problem does it solve for the transformation processor? Give 2 examples of when you'd need to use it.
11. How many pipelines can we have in one collector and how can this be? If multiple are possible, when and why shouldn't you put them together?
12. How can you scale the collector? When should you scale the collector? When shouldn't you scale it?
13. What is the sending queue on a collector exporter, and what problem does it solve? What configuration controls its capacity and concurrency, and what happens to telemetry once the queue is full?
    - If a pipeline has 2 exporters, how does data reach both of them? Does the queue get shared between the two exporters, or does each one manage its own? What happens if one exporter's backend is slow/down but the other's isn't?
14. Running collectors as production ready is an important task. One key ingredient for that is monitoring. How can we monitor the collector? Insert the configuration needed to enable this ability.
15. Say we have an error in our collector, what are the steps that we should follow in order to debug it? Explain in detail.
16. When should the collector be stateful? What state will it keep? Why won't we keep stateful collectors most of the time? What are the pros and cons between the two? Explain in detail.
17. The collector can make sampling decisions itself instead of leaving that entirely to the SDK. Compare the `probabilistic_sampler` processor to the `tail_sampling` processor: what does each one need to see in order to make its decision, and what does that require from how you deploy and scale your collectors?
18. What are the 2 main distributions of the collector? What are the differences between them and when should I use each of them? Explain in detail.
19. List 3 custom distributions of the otel collector. What do they add? Why are there many different distributions? What are the pros and cons of that?
20. Deploy a collector on docker. You should be able to configure it.
21. Write a short OTTL statement that converts HTTP status codes from string to int, and add it to the collector you deployed.
22. There are many useful tools that you should get familiar with. One of them is telemetrygen. Give a short explanation of what it is and generate telemetry (preferably traces) that outputs to the collector you deployed. The output in your collector should be to the console (verbose). The images are in our artifactory.

### Links

Here are some useful links to start from. We highly encourage you to search more and update this list with more links if you think they are suited:

- <https://opentelemetry.io/docs/collector/>
- <https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/pkg/ottl/README.md>
- [Chapter 8](../assets/learning-opentelemetry-setting-up-and-operating-a-modern-observability-system.pdf)
- [Chapter 18](../assets/observability-engineering-achieving-production.pdf)

**Read the documentation of OpenTelemetry about the collector, if you find more interesting links please add them here with a PR.**
