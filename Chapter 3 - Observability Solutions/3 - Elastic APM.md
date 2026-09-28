# Elastic APM

## Overview

**Elastic APM** is the application performance monitoring solution of the Elastic Stack: it collects traces, errors, and metrics from applications, stores them in Elasticsearch, and presents them in Kibana. Its collection architecture has changed several times, and deployments you'll meet in the wild may be on any of these generations, so it's worth knowing all of them.

## Goals

**Evolution of the Architecture**

- APM Server and the classic APM agents
- Elastic Agent, Fleet, and the APM integration
- EDOT (Elastic Distributions of OpenTelemetry) and the Managed OTLP Endpoint
- When to stay on the classic path, and how to migrate off it

**Instrumentation Libraries**

- The classic Elastic APM agents, including the RUM agent
- OpenTelemetry bridges
- Where each classic agent stands today, and what replaces it

**Features**

- The Elastic APM data model: transactions, spans, errors, and metrics
- The Applications UI: services, service map, dependencies, and traces
- Correlations, anomaly detection, and trace-log correlation
- Agent central configuration

**Data Storage: Then and Now**

- Version-named indices in 7.x
- Data streams, ECS, and the classic APM data streams
- OTel-native data streams
- Pre-aggregated metrics

**Storage Engines: From Lucene to Columnar**

- Lucene, the inverted index, doc values, and `_source`
- Index modes: TSDS and LogsDB
- The columnar index modes

**Data Management**

- Index Lifecycle Management (ILM) and data stream lifecycle
- Data tiers and searchable snapshots
- Sampling and other ways to reduce storage

## Outcome

**Evolution of the Architecture**

1. What does APM Server do, and where did it sit between the classic APM agents and Elasticsearch? How did the classic agents send data to it?
2. What are Elastic Agent and Fleet? What changed when APM Server started running as the APM integration inside a Fleet-managed Elastic Agent instead of as a standalone binary, and what did teams gain from the switch?
3. What is EDOT? Relate it to the idea of an OpenTelemetry distribution from Chapter 2: what does Elastic add on top of the upstream SDKs and Collector, and what can you still use without it?
4. In recent versions, Elastic Agent can itself run as an OpenTelemetry Collector. How does that relate to the Elastic Agent from question 2, and to the EDOT Collector?
5. What is the Managed OTLP Endpoint, and which component from the older architectures does it take the place of?
6. Elastic still ships and documents the classic APM agents and APM Server. In which situations does Elastic itself recommend staying on the classic path? How would you migrate an existing service from a classic APM agent to an EDOT SDK?

**Instrumentation Libraries**

1. What is an Elastic APM agent, and how does it instrument an application? Which parts of what the agents did does OpenTelemetry now standardize?
2. What is the Elastic APM RUM agent? What does it capture in the browser, and how do its framework integrations fit in? What is the state of its OpenTelemetry-based successor?
3. Several classic agents ship an OpenTelemetry bridge. What does it do, and how does it help a team move toward OpenTelemetry?
4. The classic agents haven't all aged the same way. For each one (RUM, Java, Node.js, Python, .NET, Go, Ruby, PHP, Android, iOS), find its current status: is it actively developed, in maintenance mode, replaced by an EDOT SDK, or left without an EDOT equivalent? What does Elastic recommend instead in each case?
5. What does "maintenance mode" mean for a library you depend on? What are the risks of staying on one, and how would you decide when to migrate a production service off it?

**Features**

1. What is a transaction in Elastic APM, and how does it differ from a span? How does it map onto the OpenTelemetry span model you learned in Chapter 2?
2. What do the service inventory, service map, dependencies view, and trace waterfall in Kibana's Applications UI each show you? Which of the golden signals from Chapter 1 appear on a service's overview page?
3. What do latency and failure correlations do? How does Elastic APM use machine learning for anomaly detection?
4. How does Elastic APM correlate traces with logs? What does a log line need to carry for the link to work?
5. What is agent central configuration, and what problem does it solve? Is it available for EDOT SDKs?

**Data Storage: Then and Now**

1. How did APM Server 7.x store events in Elasticsearch? What does the index naming pattern tell you about how events were split, and what were the consequences of putting the stack version in the index name?
2. What is a data stream, and how is it different from a plain index behind an alias? How are data streams named, and which data streams do classic APM events end up in?
3. What is ECS (Elastic Common Schema), and why does classic APM data follow it? Where do custom attributes end up in a classic APM document?
4. By default, EDOT writes to OTel-native data streams instead of ECS-based ones. How are the documents shaped differently, and how does Elastic keep existing queries and dashboards working against the new shape? Where does that compatibility break down?
5. Elastic APM stores pre-aggregated metrics at several intervals next to the raw events. What are they, why do they exist, and how does the UI decide which ones to query?

**Storage Engines: From Lucene to Columnar**

1. What is Lucene, and how does Elasticsearch use it? What is an inverted index, and which kinds of queries is it good at?
2. What are doc values, and what are they for? How do they differ from the inverted index and from `_source`?
3. What is an index mode in Elasticsearch? What is a time series data stream (TSDS), what does it change about how metrics are stored, and what does it require from your mappings?
4. What is LogsDB, and what does it change about how logs are stored? What is synthetic `_source`, and what do you give up for it? Which signals end up in LogsDB and which in TSDS in the OTel-native setup, and what did classic APM data streams use instead?
5. Elasticsearch has had doc values, a form of columnar storage, for most of its life. Why doesn't that make it a columnar database?
6. Elasticsearch recently added columnar index modes. Research them: what are they, how do they compare to LogsDB and TSDS, and how mature are they today?
7. Compare Elasticsearch's columnar mode with ClickHouse from the previous part. How does each handle arbitrary, ever-changing attributes, and where would you still pick one over the other for telemetry?

**Data Management**

1. What is Index Lifecycle Management (ILM)? What phases can a policy have, and which actions can run in each?
2. What are data tiers, and how do searchable snapshots let you keep old telemetry queryable at lower cost?
3. Which ILM policies does Elastic APM ship with by default? How do you change the retention of a single data stream without editing a managed policy that an upgrade would overwrite?
4. What is data stream lifecycle, and how is it different from ILM? Where would you run into it?
5. Revisit head-based vs. tail-based sampling from Chapter 1. Where does tail-based sampling run in the classic Elastic architecture, and what are its caveats when you use EDOT?
6. Besides retention and sampling, what other levers does Elastic give you to reduce APM storage? What does the Storage Explorer show you?

### Links

<details>
<summary>Curated reading</summary>

**Evolution of the Architecture**

- [Elastic APM Overview (7.10)](https://www.elastic.co/guide/en/apm/get-started/7.10/overview.html)
- [APM Components (7.10)](https://www.elastic.co/guide/en/apm/get-started/7.10/components.html)
- [Work with APM Server](https://www.elastic.co/docs/solutions/observability/apm/apm-server)
- [APM Server Binary](https://www.elastic.co/docs/solutions/observability/apm/apm-server/binary)
- [Fleet-managed APM Server](https://www.elastic.co/docs/solutions/observability/apm/apm-server/fleet-managed)
- [Switch to the Elastic APM Integration](https://www.elastic.co/docs/solutions/observability/apm/switch-to-elastic-apm-integration)
- [Fleet and Elastic Agent Overview](https://www.elastic.co/docs/reference/fleet)
- [Elastic OpenTelemetry (EDOT)](https://www.elastic.co/docs/reference/opentelemetry)
- [Elastic OpenTelemetry Reference Architecture](https://www.elastic.co/docs/reference/opentelemetry/architecture)
- [Elastic OpenTelemetry Compared to Upstream](https://www.elastic.co/docs/reference/opentelemetry/compatibility/edot-vs-upstream)
- [Run Elastic Agent as an OTel Collector](https://www.elastic.co/docs/reference/fleet/otel-agent)
- [EDOT Collector](https://www.elastic.co/docs/reference/edot-collector)
- [EDOT SDKs](https://www.elastic.co/docs/reference/opentelemetry/edot-sdks)
- [Managed OTLP Endpoint](https://www.elastic.co/docs/reference/opentelemetry/managed-inputs/managed-otlp-endpoint)
- [Use OpenTelemetry with Elastic APM](https://www.elastic.co/docs/solutions/observability/apm/opentelemetry)
- [Limitations of Elastic OpenTelemetry](https://www.elastic.co/docs/reference/opentelemetry/compatibility/limitations)
- [Upgrade to Version 9.0](https://www.elastic.co/docs/solutions/observability/apm/upgrade-to-version-9)

**Instrumentation Libraries**

- [Elastic APM Agents (classic)](https://www.elastic.co/docs/solutions/observability/apm/apm-agents)
- [APM RUM JavaScript Agent](https://www.elastic.co/docs/reference/apm/agents/rum-js)
- [RUM Framework-specific Integrations](https://www.elastic.co/docs/reference/apm/agents/rum-js/framework-specific-integrations)
- [Real User Monitoring (RUM)](https://www.elastic.co/docs/solutions/observability/apm/apm-agents/real-user-monitoring-rum)
- [EDOT Browser](https://www.elastic.co/docs/reference/opentelemetry/edot-sdks/browser)
- [EDOT Android](https://www.elastic.co/docs/reference/opentelemetry/edot-sdks/android)
- [EDOT SDKs Compatibility](https://www.elastic.co/docs/reference/opentelemetry/compatibility/sdks)
- [Java Agent OpenTelemetry Bridge](https://www.elastic.co/docs/reference/apm/agents/java/opentelemetry-bridge)
- [Go Agent OpenTelemetry API](https://www.elastic.co/docs/reference/apm/agents/go/opentelemetry-api)
- [Elastic Go APM Agent Repository](https://github.com/elastic/apm-agent-go)
- [Migrating from the Elastic Go APM Agent to the OpenTelemetry Go SDK](https://www.elastic.co/observability-labs/blog/elastic-go-apm-agent-to-opentelemetry-go-sdk)
- [Migrating from the Java APM Agent to EDOT Java](https://www.elastic.co/docs/reference/opentelemetry/edot-sdks/java/migration)

**Features**

- [Application Data Types](https://www.elastic.co/docs/solutions/observability/apm/data-types)
- [Traces in Elastic APM](https://www.elastic.co/docs/solutions/observability/apm/traces)
- [Metrics in Elastic APM](https://www.elastic.co/docs/solutions/observability/apm/metrics)
- [Service Map](https://www.elastic.co/docs/solutions/observability/apm/service-map)
- [Find Transaction Latency and Failure Correlations](https://www.elastic.co/docs/solutions/observability/apm/find-transaction-latency-failure-correlations)
- [Integrate with Machine Learning](https://www.elastic.co/docs/solutions/observability/apm/machine-learning)
- [Logs in Elastic APM](https://www.elastic.co/docs/solutions/observability/apm/logs)
- [Agent Central Configuration](https://www.elastic.co/docs/solutions/observability/apm/apm-agents/central-configuration)
- [EDOT SDKs Central Configuration](https://www.elastic.co/docs/solutions/observability/apm/opentelemetry/edot-sdks-central-configuration)

**Data Storage: Then and Now**

- [Explore Data in Elasticsearch (APM Server 7.10)](https://www.elastic.co/guide/en/apm/server/7.10/exploring-es-data.html)
- [Data Streams](https://www.elastic.co/docs/manage-data/data-store/data-streams)
- [APM Data Streams](https://www.elastic.co/docs/solutions/observability/apm/data-streams)
- [ECS & OpenTelemetry](https://www.elastic.co/docs/reference/ecs/ecs-opentelemetry)
- [Elastic OpenTelemetry Data Streams](https://www.elastic.co/docs/reference/opentelemetry/data-streams)
- [OpenTelemetry Data Streams Compared to Classic APM](https://www.elastic.co/docs/reference/opentelemetry/compatibility/data-streams)
- [Templates](https://www.elastic.co/docs/manage-data/data-store/templates)
- [View the Elasticsearch Index Template](https://www.elastic.co/docs/solutions/observability/apm/view-elasticsearch-index-template)

**Storage Engines: From Lucene to Columnar**

- [Apache Lucene](https://lucene.apache.org/core/)
- [Index Basics](https://www.elastic.co/docs/manage-data/data-store/index-basics)
- [Doc Values](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/doc-values)
- [`_source` Field](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/mapping-source-field)
- [Time Series Data Streams (TSDS)](https://www.elastic.co/docs/manage-data/data-store/data-streams/time-series-data-stream-tsds)
- [Logs Data Streams (LogsDB)](https://www.elastic.co/docs/manage-data/data-store/data-streams/logs-data-stream)
- [Elasticsearch's Columnar Storage](https://www.elastic.co/search-labs/blog/elasticsearch-doc-values-columnar-database)
- [Elasticsearch Columnar Database: One Platform for Search and Analytics](https://www.elastic.co/search-labs/blog/elasticsearch-columnar-storage)
- [Elasticsearch Release Notes](https://www.elastic.co/docs/release-notes/elasticsearch)

**Data Management**

- [Index Lifecycle Management](https://www.elastic.co/docs/manage-data/lifecycle/index-lifecycle-management)
- [Custom ILM with APM Server (7.10)](https://www.elastic.co/guide/en/apm/server/7.10/ilm.html)
- [ILM for APM Indices](https://www.elastic.co/docs/solutions/observability/apm/index-lifecycle-management)
- [Data Tiers](https://www.elastic.co/docs/manage-data/lifecycle/data-tiers)
- [Searchable Snapshots](https://www.elastic.co/docs/deploy-manage/tools/snapshot-and-restore/searchable-snapshots)
- [Data Stream Lifecycle](https://www.elastic.co/docs/manage-data/lifecycle/data-stream)
- [Transaction Sampling](https://www.elastic.co/docs/solutions/observability/apm/transaction-sampling)
- [Tail-based Sampling](https://www.elastic.co/docs/solutions/observability/apm/apm-server/tail-based-sampling)
- [Manage Storage](https://www.elastic.co/docs/solutions/observability/apm/manage-storage)
- [Reduce Storage](https://www.elastic.co/docs/solutions/observability/apm/reduce-storage)
- [Storage Explorer](https://www.elastic.co/docs/solutions/observability/apm/storage-explorer)

</details>
