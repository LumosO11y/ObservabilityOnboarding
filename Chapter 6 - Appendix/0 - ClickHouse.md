# ClickHouse

## Overview

ClickHouse is a high‑performance, open‑source **column‑oriented database** optimized for online analytical processing (OLAP) workloads. It’s designed to run **very fast analytical queries** on large datasets using SQL, supports real‑time data ingestion, and scales across distributed clusters, making it ideal for analytics, dashboards, and data warehousing.

## Outcome

1. What is a column-oriented database, and why is it faster than a row-oriented one for analytical queries? Relate your answer to OLAP vs. OLTP from Chapter 0.
2. What is the MergeTree family of table engines? What happens during a "merge," and why does ClickHouse prefer fewer, larger inserts?
3. What is the sorting key (`ORDER BY`) of a MergeTree table? How is ClickHouse's primary key different from a primary key in a traditional SQL database?
4. How does ClickHouse replicate and shard data across a cluster? What does it use ZooKeeper (or ClickHouse Keeper) for?
5. Why is ClickHouse a popular choice for storing observability data like logs and traces? What trade-offs does it make to get there?

### Links

- **MergeTree Table Engine**:
  [https://clickhouse.com/docs/engines/table-engines/mergetree-family/mergetree](https://clickhouse.com/docs/engines/table-engines/mergetree-family/mergetree)

- **Replication**:
  [https://clickhouse.com/docs/architecture/replication](https://clickhouse.com/docs/architecture/replication)

- **Official Documentation & Guides** — Main ClickHouse docs site:
  [https://clickhouse.com/docs/en/](https://clickhouse.com/docs/en/)

- **Official GitHub Repository (Database)** — Source code, releases, and contributions:
  [https://github.com/ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)

- **Docs Source Repo (Documentation Only)** — Markdown docs for ClickHouse:
  [https://github.com/ClickHouse/clickhouse-docs](https://github.com/ClickHouse/clickhouse-docs)

- **Quick Start / Tutorials** — Tutorials, examples, and quick start steps:
  (Use the “Get Started” and “Quick Start” sections on the docs site linked above.)

- **Learning Resources** — Courses and guides on ClickHouse fundamentals:  
  [https://clickhouse.com/learn](https://clickhouse.com/learn)
