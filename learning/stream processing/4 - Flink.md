# Flink

## Overview

In this chapter, you'll learn and try Flink, a powerful distributed stream processing platform.

Note that we use Flink with Java, because it's Flink's native programming language.

## Missions

1. Read Chapters 1 & 2 in the book "Stream Processing with Apache Flink" (the book is located in `assets` folder).
2. Watch the videos in the follwoing playlist:
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
