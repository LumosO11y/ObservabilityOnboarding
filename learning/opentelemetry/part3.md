# Part 3

## Overview

In this part you'll learn about the OpenTelemetry Collector.
At the end of this part, you'll know in detail about the OpenTelemetry collector and how its built, especially the Collector pipeline system and everything surrounding it. In addition you will grasp the importance of the collector in the OpenTelemetry Ecosystem.

## Outcome

You should have a markdown answering the above questions and in addition 2 containers running.
Make sure you go in-detail and assure you have deep understanding of this part as it will meet you regularly on the day-to-day job.

1. What is the OpenTelemetry Collector?
2. Why is the collector needed? Why should I use the otel collector instead of other products like Logstash or Nifi?
3. Explain in detail the flow of a pipeline in a collector. How does it relate to ETL? Explain what ETL is.
4. How OpenTelemetry collector relates to OTLP?
5. gRPC vs HTTP in the collector.
6. List the architecture paradigms of the collector. What are the pros and cons of each? Make a table that compares between them.
7. List and elaborate in detail on every 
 component that make up the collector. give 2 examples of each.
8. Pick 2 trivial processors that almost every collector should have and elaborate more on them. Explain also why you picked these in particular. If you picked the same as in the last question go back and replace the 2 in your last answer ;)
9. How many pipelines can we have in one collector and how can this be? If multiple are possible, when and why shouldn't you put them together? 
10. How can you scale the collector? When should you scale the collector? When shouldn't you scale it?
11. Running collectors as production ready is an important task. One key ingredient for that is monitoring. How can we monitor the collector? Insert the configuration needed to enable this ability.
12. Say we have an error in our collector, what are the steps that we should follow in order to debug it? Explain in detail.
13. When should the collector be stateful? What state will it keep? Why most of the times won't we keep stateful collectors? what is the pros and cons between the two? Explain in detail.
14. Give an example of a custom component that was made in our branch. What was the process of building this component? Why was it done? Explain in detail how it works. ( You need to ask around;) 
15. List 3 custom distributions of the otel collector. What do they add? Why are there many different distributions? What are the pros and cons of that?
16. What are the 2 main distributions of the collector? What are the differences between them and when should I use each of them? Explain in detail.
17. Deploy a collector on docker. You should be able to configure it.
18. There are many useful tools that you should get familiar with. One of them is telemetrygen. Explain shortly what it is and generate telemetry (preferably traces) that outputs to the collector you deployed in the last question. The output in your collector should be to the console (verbose). The images are in our artifactory.

### Links

Here are some useful links to start from. We highly encourage you to search more and update this list with more links if you think they are suited:
* <https://opentelemetry.io/docs/collector/>

**Read the documentation of OpenTelemetry about the collector, if you find more interesting links please add them here with a PR.**