# ClickHouse

## Overview

ClickHouse is an open-source, column-oriented SQL database built for analytical queries over very large datasets, and one of the databases our team uses. It has become a popular backend for logs, traces, and metrics, both in self-built stacks and in commercial observability products.

This part starts with how ClickHouse stores, merges, and replicates data, and the coordination service that replication depends on. It then covers the table engines and materialized views you'll use to shape data as it arrives, how to design tables for high-volume telemetry, and how ClickHouse fits in with the Collector and Grafana you've already met.

## Goals

**Storage Fundamentals**

- Understand why a column-oriented database suits analytical workloads.
- Understand MergeTree tables, merges, and sorting keys.
- Understand how ClickHouse replicates and shards data.

**The Coordination Service**

- Find out which coordination service ClickHouse replication depends on.
- Understand what it stores, what it guarantees, and how clients and servers communicate with it.
- Understand how it's operated, and which patterns it's used to implement.

**Engines**

- Database engines vs. table engines
- The MergeTree family and when each variant fits
- The Distributed engine

**Views & Columns**

- Incremental and refreshable materialized views
- Default, materialized, and alias columns

**Schema Design for Telemetry**

- Partitioning and TTL
- Compression codecs and `LowCardinality`
- Data-skipping indexes
- Semi-structured data: `JSON` vs. `Map` columns

**Ecosystem**

- Understand why ClickHouse is used as an observability backend, and its trade-offs.
- Understand how well ClickHouse integrates with the rest of an observability stack, such as the Collector, Grafana, and ClickStack.

## Outcome

**Storage Fundamentals**

1. What is a column-oriented database, and why is it faster than a row-oriented one for analytical queries? Relate your answer to OLAP vs. OLTP from Chapter 0.
2. What is the MergeTree family of table engines? What happens during a "merge," and why does ClickHouse prefer fewer, larger inserts?
3. What is the sorting key (`ORDER BY`) of a MergeTree table? How is ClickHouse's primary key different from a primary key in a traditional SQL database?
4. How does ClickHouse replicate and shard data across a cluster? What does it need a coordination service for, and which one does it use?

**The Coordination Service**

Storage Fundamentals question 4 led you to the coordination service that replicated ClickHouse tables depend on. Learn it in its own right:

1. What problem does a coordination service solve, and why do systems use one instead of building their own coordination? ClickHouse also ships its own implementation of this service: what is it, and why might a team still run the original?
2. How is it architected? How many servers make up a cluster, and what roles do they play?
3. How is its data organized? What types of nodes can you create, and what makes each type useful?
4. How do clients connect to it and stay connected? What happens to a client's data when its session expires, and why is that useful?
5. How do the servers agree on the order of writes, and how is each write's place in that order identified? What happens when the leader fails?
6. What consistency guarantees does it give clients? What is a watch, how long does it stay registered after it fires, and what happens to it when the client's session expires? How do clients use watches in practice?
7. What are the basic operational concerns: sizing the cluster, snapshots and transaction logs, and the common issues you'd run into?
8. Which distributed-systems patterns is it commonly used to implement?
9. Compare it to at least one alternative coordination service (e.g. etcd). Give a 1-2 sentence comparison and a simple use case for each.
10. What does ClickHouse keep in it, and what happens to a replicated table when it becomes unavailable?

**Engines**

1. What is the difference between a database engine and a table engine in ClickHouse? Which database engine does a new database get by default, and what does it give you?
2. The MergeTree family includes several variants that change what happens to rows during a merge. Pick three, explain what each one does at merge time, and give an observability use case for each.
3. Why can a `ReplacingMergeTree` table still return duplicate rows in a query? How do you get correct results anyway, and what does it cost?
4. What is the Distributed table engine, and how does it relate to the replication and sharding from question 4 of Storage Fundamentals? Does it store any data itself?

**Views & Columns**

1. What is a view in SQL, and what is a materialized view? What does materializing a view buy you, and what does it cost?
2. How does an incremental materialized view work in ClickHouse, and what exactly triggers it? How is that different from a materialized view in a traditional SQL database?
3. What is a refreshable materialized view, and when would you choose it over an incremental one?
4. Why is a materialized view often paired with an aggregating target table? Sketch one that turns raw spans into per-service request counts per minute.
5. What is the difference between a `DEFAULT`, a `MATERIALIZED`, and an `ALIAS` column? When is each one's value computed, and is it stored on disk?

**Schema Design for Telemetry**

1. What is a partition key, and how is it different from the sorting key? Why is over-partitioning a common mistake?
2. How do you make ClickHouse delete telemetry automatically after a retention period? At what granularity does the deletion happen, and how does your partitioning choice affect its cost?
3. What are compression codecs, and why does choosing them per column matter for telemetry? What does `LowCardinality` do, and which kinds of telemetry columns benefit from it?
4. What is a data-skipping index, and how is it different from an index in a row-oriented database? When would you add one to a logs table?
5. Telemetry attributes are semi-structured. Compare storing them in a `JSON` column vs. a `Map` column: how is each stored, how does a query on a single key perform, and what happens when new keys appear? Which would you choose for span attributes, and why?

**Ecosystem**

1. Why is ClickHouse a popular choice for storing observability data like logs and traces? What trade-offs does it make to get there?
2. How does telemetry get from an OpenTelemetry Collector into ClickHouse? Look at the tables the exporter creates: which of the schema design choices above does its schema use?
3. How do you query ClickHouse from Grafana? What does the official plugin support for logs and traces, and where does it fall short compared to the Prometheus and Tempo integrations from the Grafana part?
4. What is ClickStack, and what are its components? How does it compare to building your own stack from ClickHouse and Grafana?
5. ClickHouse's integrations catalog labels each integration with a support level. What do the levels mean, and why should that label factor into choosing an integration?

### Links

<details>
<summary>Curated reading</summary>

**Storage Fundamentals**

- [MergeTree Table Engine](https://clickhouse.com/docs/reference/engines/table-engines/mergetree-family/mergetree)
- [Replication](https://clickhouse.com/docs/guides/oss/deployment-and-scaling/examples/1-shard-2-replicas)

**The Coordination Service**

<details>
<summary>Spoiler: open once you've answered Storage Fundamentals question 4</summary>

- [ClickHouse Keeper](https://clickhouse.com/docs/guides/oss/deployment-and-scaling/keeper)
- [ZooKeeper Overview](https://zookeeper.apache.org/doc/current/zookeeperOver.html)
- [ZooKeeper Programmer's Guide](https://zookeeper.apache.org/doc/current/zookeeperProgrammers.html)
- [ZooKeeper Internals](https://zookeeper.apache.org/doc/current/zookeeperInternals.html)
- [ZooKeeper Administrator's Guide](https://zookeeper.apache.org/doc/current/zookeeperAdmin.html)
- [ZooKeeper Recipes and Solutions](https://zookeeper.apache.org/doc/current/recipes.html)

</details>

**Engines**

- [Database Engines](https://clickhouse.com/docs/reference/engines/database-engines)
- [Table Engines](https://clickhouse.com/docs/reference/engines/table-engines)
- [ReplacingMergeTree](https://clickhouse.com/docs/reference/engines/table-engines/mergetree-family/replacingmergetree)
- [SummingMergeTree](https://clickhouse.com/docs/reference/engines/table-engines/mergetree-family/summingmergetree)
- [AggregatingMergeTree](https://clickhouse.com/docs/reference/engines/table-engines/mergetree-family/aggregatingmergetree)
- [CollapsingMergeTree](https://clickhouse.com/docs/reference/engines/table-engines/mergetree-family/collapsingmergetree)
- [Distributed Table Engine](https://clickhouse.com/docs/reference/engines/table-engines/special/distributed)

**Views & Columns**

- [Materialized View (Wikipedia)](https://en.wikipedia.org/wiki/Materialized_view)
- [Materialized Views in ClickHouse](https://clickhouse.com/docs/concepts/features/materialized-views)
- [Incremental Materialized Views](https://clickhouse.com/docs/concepts/features/materialized-views/incremental-materialized-view)
- [Refreshable Materialized Views](https://clickhouse.com/docs/concepts/features/materialized-views/refreshable-materialized-view)
- [`CREATE TABLE` (column defaults)](https://clickhouse.com/docs/reference/statements/create/table)

**Schema Design for Telemetry**

- [Schema Design for Observability](https://clickhouse.com/docs/guides/use-cases/observability/build-your-own/schema-design)
- [Custom Partitioning Key](https://clickhouse.com/docs/reference/engines/table-engines/mergetree-family/custom-partitioning-key)
- [TTL](https://clickhouse.com/docs/concepts/features/operations/delete/ttl)
- [Compression in ClickHouse](https://clickhouse.com/docs/guides/clickhouse/data-modelling/compression/compression-in-clickhouse)
- [`LowCardinality`](https://clickhouse.com/docs/reference/data-types/lowcardinality)
- [Data-Skipping Indexes](https://clickhouse.com/docs/concepts/features/performance/skip-indexes/skipping-indexes)
- [`JSON` Data Type](https://clickhouse.com/docs/reference/data-types/newjson)
- [`Map` Data Type](https://clickhouse.com/docs/reference/data-types/map)

**Ecosystem**

- [ClickStack Overview](https://clickhouse.com/docs/clickstack/overview)
- [OpenTelemetry Collector ClickHouse Exporter](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/exporter/clickhouseexporter)
- [Connecting Grafana to ClickHouse](https://clickhouse.com/docs/integrations/connectors/data-visualization/grafana)
- [Grafana ClickHouse Data Source Plugin](https://grafana.com/grafana/plugins/grafana-clickhouse-datasource/)
- [Integrations Catalog](https://clickhouse.com/docs/integrations/home)

**General**

- [Official Documentation](https://clickhouse.com/docs/)
- [ClickHouse Learning Resources](https://clickhouse.com/learn)
- [ClickHouse GitHub Repository](https://github.com/ClickHouse/ClickHouse)

</details>
