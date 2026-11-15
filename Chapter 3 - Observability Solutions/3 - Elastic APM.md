# Elastic APM

## Overview

**Elastic APM** is the application performance monitoring solution of the Elastic Stack: it collects traces, errors, and metrics from applications, stores them in Elasticsearch, and presents them in Kibana. Its collection architecture has changed several times, and deployments you'll meet in the wild may be on any of these generations, so it's worth knowing all of them.

## Goals

**Evolution of the Architecture**

- APM Server and the classic APM agents
- Elastic Agent, Fleet, and the APM integration
- EDOT (Elastic Distributions of OpenTelemetry)
- Sending OTLP from OpenTelemetry SDKs straight to the APM integration

**Real User Monitoring (RUM)**

- The Elastic APM RUM agent and its framework integrations
- Getting browser data into the APM integration
- Its OpenTelemetry-based successor

**Features**

- The Elastic APM data model: transactions, spans, errors, and metrics
- The Applications UI: services, service map, dependencies, and traces
- Trace-log correlation

**Data Storage: Then and Now**

- Version-named indices in 7.x
- Data streams, ECS, and the classic APM data streams
- OTel-native data streams

**Storage Engines**

- Lucene, the inverted index, doc values, and `_source`
- Index modes: TSDS and LogsDB

**Data Management**

- Index Lifecycle Management (ILM)
- Sampling

## Outcome

**Evolution of the Architecture**

1. What does APM Server do, and where did it sit between the classic APM agents and Elasticsearch? How did the classic agents send data to it?
2. What are Elastic Agent and Fleet? What changed when APM Server started running as the APM integration inside a Fleet-managed Elastic Agent instead of as a standalone binary, and what did teams gain from the switch?
3. What is EDOT? Relate it to the idea of an OpenTelemetry distribution from Chapter 2: what does Elastic add on top of the upstream SDKs and Collector, and what can you still use without it?
4. Our services are instrumented with OpenTelemetry SDKs and send OTLP straight to the APM integration in a Fleet-managed Elastic Agent, with no EDOT Collector in between. How does the APM integration accept OTLP, what happens to the data on its way into Elasticsearch, and what limitations does Elastic document for this setup?

**Real User Monitoring (RUM)**

1. What is the Elastic APM RUM agent? What does it capture in the browser, and how do its framework integrations fit in?
2. RUM data comes from users' browsers rather than from your own servers. How does it reach the APM integration, and what do you have to configure on the APM side before it will accept that data safely?
3. How does a page load or a user interaction captured by the RUM agent connect to the backend traces it triggers?
4. What is the state of the RUM agent's OpenTelemetry-based successor, and what would moving to it involve?

**Features**

1. What is a transaction in Elastic APM, and how does it differ from a span? How does it map onto the OpenTelemetry span model you learned in Chapter 2?
2. What do the service inventory, service map, dependencies view, and trace waterfall in Kibana's Applications UI each show you? Which of the golden signals from Chapter 1 appear on a service's overview page?
3. How does Elastic APM correlate traces with logs? What does a log line need to carry for the link to work?

**Data Storage: Then and Now**

1. How did APM Server 7.x store events in Elasticsearch? What does the index naming pattern tell you about how events were split, and what were the consequences of putting the stack version in the index name?
2. What is a data stream, and how is it different from a plain index behind an alias? How are data streams named, and which data streams do classic APM events end up in?
3. What is ECS (Elastic Common Schema), and why does classic APM data follow it? Where do custom attributes end up in a classic APM document?
4. By default, EDOT writes to OTel-native data streams instead of ECS-based ones. How are the documents shaped differently, and how does Elastic keep existing queries and dashboards working against the new shape? Where does that compatibility break down?

**Storage Engines**

1. What is Lucene, and how does Elasticsearch use it? What is an inverted index, and which kinds of queries is it good at?
2. What are doc values, and what are they for? How do they differ from the inverted index and from `_source`?
3. What is an index mode in Elasticsearch? What do the time series (TSDS) and LogsDB index modes each change about how data is stored, and which signals end up in each in the OTel-native setup?
4. Compare Elasticsearch with ClickHouse from the previous part: how does each handle arbitrary, ever-changing attributes, and where would you still pick one over the other for telemetry?

**Data Management**

1. What is Index Lifecycle Management (ILM)? What phases can a policy have, and which actions can run in each?
2. Which ILM policies does Elastic APM ship with by default? How do you change the retention of a single data stream without editing a managed policy that an upgrade would overwrite?
3. Revisit head-based vs. tail-based sampling from Chapter 1. Where does tail-based sampling run in the classic Elastic architecture, and what are its caveats when you use EDOT?

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
- [EDOT Collector](https://www.elastic.co/docs/reference/edot-collector)
- [EDOT SDKs](https://www.elastic.co/docs/reference/opentelemetry/edot-sdks)
- [Use OpenTelemetry with Elastic APM](https://www.elastic.co/docs/solutions/observability/apm/opentelemetry)
- [Limitations of Elastic OpenTelemetry](https://www.elastic.co/docs/reference/opentelemetry/compatibility/limitations)
- [Upgrade to Version 9.0](https://www.elastic.co/docs/solutions/observability/apm/upgrade-to-version-9)

**Real User Monitoring (RUM)**

- [Real User Monitoring (RUM)](https://www.elastic.co/docs/solutions/observability/apm/apm-agents/real-user-monitoring-rum)
- [APM RUM JavaScript Agent](https://www.elastic.co/docs/reference/apm/agents/rum-js)
- [RUM Framework-specific Integrations](https://www.elastic.co/docs/reference/apm/agents/rum-js/framework-specific-integrations)
- [EDOT Browser](https://www.elastic.co/docs/reference/opentelemetry/edot-sdks/browser)

**Features**

- [Application Data Types](https://www.elastic.co/docs/solutions/observability/apm/data-types)
- [Traces in Elastic APM](https://www.elastic.co/docs/solutions/observability/apm/traces)
- [Metrics in Elastic APM](https://www.elastic.co/docs/solutions/observability/apm/metrics)
- [Service Map](https://www.elastic.co/docs/solutions/observability/apm/service-map)
- [Logs in Elastic APM](https://www.elastic.co/docs/solutions/observability/apm/logs)

**Data Storage: Then and Now**

- [Explore Data in Elasticsearch (APM Server 7.10)](https://www.elastic.co/guide/en/apm/server/7.10/exploring-es-data.html)
- [Data Streams](https://www.elastic.co/docs/manage-data/data-store/data-streams)
- [APM Data Streams](https://www.elastic.co/docs/solutions/observability/apm/data-streams)
- [ECS & OpenTelemetry](https://www.elastic.co/docs/reference/ecs/ecs-opentelemetry)
- [Elastic OpenTelemetry Data Streams](https://www.elastic.co/docs/reference/opentelemetry/data-streams)
- [OpenTelemetry Data Streams Compared to Classic APM](https://www.elastic.co/docs/reference/opentelemetry/compatibility/data-streams)
- [Templates](https://www.elastic.co/docs/manage-data/data-store/templates)
- [View the Elasticsearch Index Template](https://www.elastic.co/docs/solutions/observability/apm/view-elasticsearch-index-template)

**Storage Engines**

- [Apache Lucene](https://lucene.apache.org/core/)
- [Index Basics](https://www.elastic.co/docs/manage-data/data-store/index-basics)
- [Doc Values](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/doc-values)
- [`_source` Field](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/mapping-source-field)
- [Time Series Data Streams (TSDS)](https://www.elastic.co/docs/manage-data/data-store/data-streams/time-series-data-stream-tsds)
- [Logs Data Streams (LogsDB)](https://www.elastic.co/docs/manage-data/data-store/data-streams/logs-data-stream)

**Data Management**

- [Index Lifecycle Management](https://www.elastic.co/docs/manage-data/lifecycle/index-lifecycle-management)
- [Custom ILM with APM Server (7.10)](https://www.elastic.co/guide/en/apm/server/7.10/ilm.html)
- [ILM for APM Indices](https://www.elastic.co/docs/solutions/observability/apm/index-lifecycle-management)
- [Transaction Sampling](https://www.elastic.co/docs/solutions/observability/apm/transaction-sampling)
- [Tail-based Sampling](https://www.elastic.co/docs/solutions/observability/apm/apm-server/tail-based-sampling)

</details>
