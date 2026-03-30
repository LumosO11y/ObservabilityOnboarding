# Overview
Prometheus Query Language (PromQL) is a functional query language that allows you to select and aggregate time-series data in real-time.
In Grafana, PromQL is the engine that transforms raw metrics into dashboards.
## 1. The Basics: Selecting Data
PromQL expressions result in one of four types of data, but in Grafana, you almost always work with
**Instant vectors** (a single value per series at a point in time) or **Range vectors** (a set of values over time).
### Metric Identifiers & Selectors: 
To get data, start with the metric name and filter it using labels in curly braces ``{}``.  
Here are some examples making use of regular conditional conventions:

- Equality (``=``): ``http_requests_total{status="200"}``

- Negative Equality (``!=``): ``http_requests_total{status!="500"}``

- Regex Match (``=~``): ``http_requests_total{handler=~"/api/v1/.*"}``

- Negative Regex (``!~``): ``http_requests_total{job!~"node-.*"}``

### Range Vectors: 
In Grafana, range vectors are used inside functions like ``rate()``. You define the time window using brackets:

- ``[5m]`` – Last 5 minutes.

- ``[$__rate_interval]`` – **Grafana Best Practice**: This dynamic variable automatically adjusts based on your dashboard's time range and scrape interval to prevent data gaps.

## 2. Intermediate: Functions and Aggregations
Raw counters are rarely useful on their own. We use functions to see trends.
### Rate vs. Irrate
These are fundamental functions of PromQL:
- ``rate()``: Calculates the per-second average rate of increase over the time range. Best for alerting and long-term trends.

- ``irrate()``: "Instant rate." Looks at the last two data points. Best for high-resolution dashboards showing "spiky" behavior.

*Note*: Only use ``rate()`` on **Counters** (metrics that only go up, like total requests).

### Aggregation Operators
To combine multiple series into one line (e.g., total CPU across all cores):
- ``sum()``: Adds values together.

- ``avg()``: Calculates the mean.

- ``max()`` / ``min()``: Finds peaks or valleys.

**The** ``by`` **clause**: Use this to keep specific dimensions.
``sum(rate(http_requests_total[5m])) by (method)`` — This gives you a separate line for GET, POST, etc.

## 3. Advanced Filtering & Arithmetic
You can perform math across different metrics, provided their labels match.
### Binary Operators
- Arithmetic: ``+``, ``-``, ``*``, ``/``, ``%``, ``^``

- Comparison: ``==``, ``!=``, ``>``, ``<``

**Example**: Calculating Error Percentage  
``(sum(rate(http_requests_total{status=~"5.."}[5m])) / sum(rate(http_requests_total[5m]))) * 100``

### Offset Modifier
To compare today's traffic with the same time last week, use ``offset``:  
``http_requests_total offset 1w``

## 4. Maximizing Grafana Efficiency
To make your PromQL queries performant and dynamic in Grafana, use these specific features:
- **Variables**: Replace hardcoded values with dropdowns. exmaple:
``{instance="$instance"}``
- **Legend Format**: Use ``{{label_name}}`` to clean up the graph legend. exmaple: ``{{method}} - {{status}}``
- **Min Step**: Ensures Prometheus doesn't return more data points than your screen has pixels (Set in the Query Options).
- **Instant Query**: Use for Stat or Gauge panels where only the latest value matters (Toggle "Instant" in the query editor).

## Common Pitfalls to Avoid
- **Rating a Gauge**: Never use ``rate()`` on a metric that can go down (like memory usage). Use ``avg_over_time()`` instead.
- **Aggregation Order**: Always ``sum()`` the ``rate()``, not the other way around.
  - **Correct**: ``sum(rate(metric[5m]))``
  - **Incorrect**: ``rate(sum(metric)[5m])`` (This breaks if a pod restarts).
