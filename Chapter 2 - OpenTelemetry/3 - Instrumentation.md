# Instrumentation

## Overview

In this part you'll see how OpenTelemetry implements the instrumentation approaches you learned about in Chapter 1, and you'll instrument a real component yourself.

## Goals

- Understand the OpenTelemetry API vs. the SDK, and the building blocks of an SDK pipeline.
- Understand how OpenTelemetry does automatic (zero-code) and manual (code-based) instrumentation.
- Understand Resources and Instrumentation Scope, and how they describe where telemetry came from.
- Instrument an app by yourself.

## Outcome

You should finish this part after you added instrumentation to an existing component.

By the end of this part you should answer the following questions:

1. What is the difference between the OpenTelemetry API and the SDK? Why are they separate packages, and what happens when a library depends only on the API but the application never installs an SDK?
2. Inside the SDK, what does each of these do: a TracerProvider, a span processor, and an exporter? How does a span travel through them from the moment you end it?
3. What is a Resource? How is it different from the attributes you put on a span?
4. When you create a span or a metric through an SDK, that telemetry gets tagged with an Instrumentation Scope. What does the scope identify, what problem does this solve, and how could you use it downstream?
5. Pick 2 OpenTelemetry language SDKs. How does each one implement zero-code instrumentation, and what does that tell you about the language's runtime?
6. OpenTelemetry offers ready-made instrumentation libraries for common frameworks (e.g. Flask). When there's no such library for the code you need to instrument, what are your options? Explain each in detail.
    1. Why won't we always have access to a ready-made instrumentation library?
    2. Give an example of a team from our unit that uses "custom instrumentation". Why did they choose this method?
7. Some would say that manual instrumentation is sort of an art. In what cases should we avoid instrumenting our library/code? What would be considered over-instrumenting?
8. In Chapter 1's Signals part you read about span events. OpenTelemetry deprecated the Span Event API in 2026. What replaces it, and why did the project make this change? What happens to existing span events, and who has to change their code?
9. Span links let a span point at spans other than its parent.
    1. How do you add a link to a span in the OpenTelemetry API? Does it matter whether you add it when the span starts or later, and how does that relate to what a sampler can see?
    2. Look at the OpenTelemetry messaging semantic conventions. When a consumer processes a batch of messages, which span gets the links, and where does each link point?
10. Add instrumentation to an existing code (ask your mentor for our internal instrumentation docs and which component to use).
    1. See it in the console (use a console exporter)
    2. Send the instrumentation through to a platform the mentor will tell you. Talk with your mentor for more info.

### Links

- <https://opentelemetry.io/docs/concepts/instrumentation/>
- <https://opentelemetry.io/docs/concepts/instrumentation-scope/>
- <https://opentelemetry.io/docs/specs/otel/trace/sdk/>
- <https://opentelemetry.io/docs/specs/otel/metrics/sdk/>
- <https://opentelemetry.io/docs/specs/otel/logs/sdk/>
- <https://opentelemetry.io/docs/specs/otel/resource/sdk/>
- <https://opentelemetry.io/docs/concepts/resources/>
- <https://opentelemetry.io/docs/languages/>
- <https://opentelemetry.io/docs/concepts/instrumentation/code-based/>
- <https://opentelemetry.io/docs/concepts/instrumentation/zero-code/>
- [Deprecating Span Events API](https://opentelemetry.io/blog/2026/deprecating-span-events/)
- [Span Links](https://opentelemetry.io/docs/concepts/signals/traces/#span-links)
- [Messaging Spans Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/messaging/messaging-spans/)
- <https://www.cncf.io/blog/2022/04/22/opentelemetry-and-python-a-complete-instrumentation-guide/>
- <https://logz.io/blog/python-opentelemetry-auto-instrumentation/#export>
- [Chapter 5](../assets/learning-opentelemetry-setting-up-and-operating-a-modern-observability-system.pdf)
- [Chapter 7](../assets/observability-engineering-achieving-production.pdf)
