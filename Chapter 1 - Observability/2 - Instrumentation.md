# Instrumentation

## Overview

In this part you will learn about yet another concept of Observability called Instrumentation. You will learn how to make your system observable and about the different ways you can implement this concept.

## Goals

- Understand the concept of Instrumentation.
- Learn about different implementations of Instrumentation (manual vs. automatic).
- Understand the difference between SDK-based (in-process) instrumentation and system-level (out-of-process) instrumentation.
- Learn about different Instrumentation technologies

## Outcome

The outcome of this part should be a detailed markdown containing everything you learned about this concept.

In your markdown make sure there is an answer to the following questions:

1. What is Instrumentation? Explain the concept and why it is important in making your application "observable".
2. What are the different ways of "instrumenting" your application? Can you use these methods at all times? Explain how each works in general.
3. What doesn't automatic instrumentation allow that manual instrumentation does?
4. Explain the different use-cases of automatic and manual instrumentation.
5. What is SDK-based instrumentation? Where does it run relative to your application, and what does it need from your application's runtime to work?
6. What is system-level instrumentation (e.g. instrumentation done from inside the kernel)? How does it differ from SDK-based instrumentation in terms of what it can see and what it requires from you?
7. Compare SDK-based and system-level instrumentation on: depth/richness of the data collected, performance overhead, language/runtime coupling, and how much application code needs to change.
8. Give a real or hypothetical scenario where SDK-based instrumentation isn't possible or practical, and system-level instrumentation would be the better (or only) option.

### Links

- <https://opentelemetry.io/docs/concepts/instrumentation/>
- <https://cloud.google.com/stackdriver/docs/instrumentation/overview>
- <https://baselime.io/glossary/instrumentation>
- <https://clairettran.medium.com/observability-and-instrumentation-99258f61f7a7>
- <https://logz.io/learn/opentracing-jaeger-guide-to-instrumentation/>
- <https://opencensus.io/introduction/>
- [Chapter 5](../assets/learning-opentelemetry-setting-up-and-operating-a-modern-observability-system.pdf)
- [Chapter 7](../assets/observability-engineering-achieving-production.pdf)
