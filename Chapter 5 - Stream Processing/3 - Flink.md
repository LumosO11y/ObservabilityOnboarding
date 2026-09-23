# Flink

## Overview

In this chapter, you'll learn and try Flink, a powerful distributed stream processing platform.

Note that we use Flink with Java, because it's Flink's native programming language.

## Outcome

1. Read Chapters 1 & 2 in the book [Stream Processing with Apache Flink](../assets/Stream%20Processing%20with%20Apache%20Flink.pdf).
2. Watch the videos in the following playlist:
    - [Building Apache Flink Applications in Java](https://www.youtube.com/playlist?list=PLa7VYi0yPIH0QEIcyvZE5p4zMR0ln4aAe)
3. Do the exercise [rides-and-fares](https://github.com/apache/flink-training/tree/master/rides-and-fares) from Apache's flink training repository (don't look at the solution).
4. Read the following pages from Flink's documentation. We encourage you to read more subjects from the documentation that you find interesting!
    - [Anatomy of a flink cluster](https://nightlies.apache.org/flink/flink-docs-master/docs/concepts/flink-architecture/#anatomy-of-a-flink-cluster)
    - [Task slots and parallelism](https://nightlies.apache.org/flink/flink-docs-master/docs/concepts/flink-architecture/#tasks-and-operator-chains)
    - [Operators - Data Transformations](https://nightlies.apache.org/flink/flink-docs-master/docs/dev/datastream/operators/overview/)
    - [Process Function](https://nightlies.apache.org/flink/flink-docs-master/docs/dev/datastream/operators/process_function/)
    - [State](https://nightlies.apache.org/flink/flink-docs-release-1.14/docs/concepts/stateful-stream-processing/#unaligned-checkpointing)
    - [Working With State](https://nightlies.apache.org/flink/flink-docs-master/docs/dev/datastream/fault-tolerance/state/)
    - [State backend and RocksDB](https://flink.apache.org/2021/01/18/using-rocksdb-state-backend-in-apache-flink-when-and-how/)
    - [Flink State Backends](https://nightlies.apache.org/flink/flink-docs-master/docs/ops/state/state_backends/)
    - [Checkpoints](https://nightlies.apache.org/flink/flink-docs-release-1.14/docs/ops/state/checkpoints)
    - [Savepoints](https://nightlies.apache.org/flink/flink-docs-release-1.14/docs/ops/state/savepoints)
5. Do the following exercise inside:
    - Create a Flink-based stream application that reads OTEL spans from a Kafka topic, and every 10 seconds, prints how many spans were in each trace in the last 10 seconds.
    - Ask your HairWasher for the Kafka topic details.

### Study Questions

1. What problem does stream processing solve that batch processing doesn't, and where does Flink fit into that picture?
2. What is a Flink cluster made of? What roles do the JobManager and TaskManager play?
3. What are Task Slots, and how do they relate to parallelism in a Flink job?
4. What is the difference between a DataStream operator like `map`/`filter` and a `ProcessFunction`? When would you reach for a `ProcessFunction` instead?
5. What is "state" in a stateful stream processing job, and why can't you just keep it in a regular Java variable?
6. What is the difference between Keyed State and Operator State?
7. What is RocksDB, and why would you choose the RocksDB state backend over the default in-memory one?
8. What is a Checkpoint, and how does Flink use it to recover from a failure without losing data?
9. What is the difference between a Checkpoint and a Savepoint? When would you take a Savepoint instead of relying on automatic checkpoints?
10. In the hands-on exercise above, you read OTEL spans from Kafka and count spans per trace every 10 seconds. What Flink concept (windowing) does this rely on, and how does it relate to state?
