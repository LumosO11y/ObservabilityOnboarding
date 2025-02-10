# Part 4

## Overview

In this part you'll learn about another concept of OpenTelemetry called instrumentation.
At the end of this part you will understand in-depth what instrumentation means and what are the different kinds of it.
You should also be familiar with instrumentation best practices and you should know how to instrument code.

## Goals
- Learn about the diffrent types of instrumentation.

- Instrument an app by yourself.

## Outcome
You should finish this part after you added instrumentation to an existing component.

In the end of this part you should answer the following questions:

1. Whats the difference between each of the instrumentation solutions?
   1. Why do we need each of them?
   2. When we should use them?
2. Name 2 different of instrumentation SDKs and explain the differences between them.

3. When instrumenting code based applications we usually have the luxury of using a pre-built integration to our base framework (fastapi, flask, etc). There are some cases where we don't have this luxury. What are the 2 ways of instrumentation in this example? explain in detail.
    1. Why won't we always have access to this "integrated instrumentation"?
    2. Give an example of a team from our branch that uses "custom instrumentation". Why did they choose this method?
3. Some would say that manual instrumentation is sort of an art. In what cases should we avoid instrumenting our library/code? What would be considered over-instrumenting?
4. Add instrumentation to an existing code. Talk with your mentor for more info.


### Links

1. <https://opentelemetry.io/docs/concepts/instrumentation/>
2. <https://opentelemetry.io/docs/specs/otel/trace/sdk/>
3. <https://opentelemetry.io/docs/specs/otel/metrics/sdk/>
4. <https://opentelemetry.io/docs/specs/otel/logs/sdk/>
5. <https://opentelemetry.io/docs/specs/otel/resource/sdk/>
6. <https://opentelemetry.io/docs/concepts/instrumentation/code-based/>
7. <https://opentelemetry.io/docs/concepts/instrumentation/zero-code/>
8. <https://www.cncf.io/blog/2022/04/22/opentelemetry-and-python-a-complete-instrumentation-guide/>
9. <https://logz.io/blog/python-opentelemetry-auto-instrumentation/#export>
