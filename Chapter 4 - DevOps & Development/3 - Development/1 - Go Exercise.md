# Go Exercise

## Overview

In this exercise, you'll use the Go you just learned to implement a **consistent hash ring**, a small algorithm that shows up all over distributed systems, including the observability pipelines you'll work on. Research the algorithm yourself first; the task below only tells you what to build, not how it works.

## Goals

- Understand what consistent hashing is and what problem it solves.
- Write idiomatic, tested Go: a module, an exported API, table-driven tests, and a benchmark.
- Make a data structure safe for concurrent use, and prove it with the race detector.
- Measure an algorithm's behavior yourself instead of taking it on faith.

## The task

Create a new Go module containing a `hashring` package with this API:

```go
// New returns an empty ring where every node is placed on the ring `replicas` times.
func New(replicas int) *Ring

// Add places one or more nodes on the ring.
func (r *Ring) Add(nodes ...string)

// Remove takes a node off the ring. Removing an unknown node is a no-op.
func (r *Ring) Remove(node string)

// Get returns the node responsible for key, or false if the ring is empty.
func (r *Ring) Get(key string) (string, bool)
```

**Requirements:**

1. Use a hash function from the Go standard library. Be ready to explain your choice.
2. `Get` must not scan every point on the ring.
3. A `*Ring` must be safe to use from many goroutines at once, with `Get` being far more frequent than `Add` or `Remove`.
4. Write table-driven tests that cover at least: an empty ring, a single node, the same key always mapping to the same node, and removing a node that was never added.
5. Write a test that calls `Get`, `Add`, and `Remove` from several goroutines concurrently, and make sure `go test -race ./...` passes.
6. Write a benchmark for `Get` on a ring of 10 nodes.
7. `gofmt` and `go vet` must report nothing.

**The experiment:**

Write a small `main` package (or a test) that:

1. Builds a ring of 5 nodes and assigns 100,000 random keys to it. Print how many keys each node got.
2. Removes one node, and counts how many of the keys now map to a *different* node.
3. Repeats steps 1-2 with a naive `hash(key) % numberOfNodes` assignment instead of the ring.
4. Repeats steps 1-2 for `replicas` values of 1, 10, 100, and 500.

## Outcome

Your working module (tests and benchmark passing) and a markdown file answering the questions below, to go over with your mentor.

1. What is consistent hashing, and what problem does it solve?
2. Using your experiment's numbers, compare how many keys moved when you removed a node from the ring versus from the naive modulo assignment. Explain the difference.
3. What are virtual nodes (your `replicas`)? Put your results for 1, 10, 100, and 500 replicas in a table. How does the replica count affect how evenly keys are spread, and what does a higher count cost you?
4. Which hash function did you pick, and why? Which properties of a hash function matter for this use case, and which don't? Would a cryptographic hash be a better or worse choice here?
5. How does your `Get` find the right node without scanning the whole ring? What is its time complexity, and what does your benchmark show?
6. Which synchronization primitive did you use to make the ring safe for concurrent use, and why that one?
7. In the Collector part, you saw that some processing (like tail sampling) needs every span of a trace to reach the same collector instance. If you put your ring in front of a pool of collectors, what would you use as the key? Which Collector component does this kind of routing, and what can it route by?
8. What happens to in-flight state on the remaining collectors when a collector instance is added to or removed from that pool? Is consistent hashing enough to make scaling painless?
9. How does a ClickHouse `Distributed` table decide which shard a row goes to? Is that consistent hashing? What does it mean for existing data when you add a shard?

### Links

- [Consistent hashing (Wikipedia)](https://en.wikipedia.org/wiki/Consistent_hashing)
- [Consistent Hashing and Random Trees (the original paper)](https://www.cs.princeton.edu/courses/archive/fall09/cos518/papers/chash.pdf)
- [Consistent Hashing: Algorithmic Tradeoffs](https://dgryski.medium.com/consistent-hashing-algorithmic-tradeoffs-ef6b8e2fcae8)
- [Go: `sort` package](https://pkg.go.dev/sort)
- [Go: `hash/fnv` package](https://pkg.go.dev/hash/fnv)
- [Go: `hash/crc32` package](https://pkg.go.dev/hash/crc32)
- [Go: `sync` package](https://pkg.go.dev/sync)
- [Go Wiki: Table-driven tests](https://go.dev/wiki/TableDrivenTests)
- [Load Balancing Exporter](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/exporter/loadbalancingexporter)
- [ClickHouse: Distributed table engine](https://clickhouse.com/docs/engines/table-engines/special/distributed)
