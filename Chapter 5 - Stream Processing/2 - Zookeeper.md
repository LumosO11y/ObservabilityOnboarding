# Zookeeper

## Overview

ZooKeeper is a distributed coordination service. Instead of building coordination mechanisms (leader election, config distribution, distributed locks) from scratch, systems lean on ZooKeeper to provide them.

### Schedule
Estimated Duration: 0.5 day.

## Goals

- Understand what problem ZooKeeper solves and why systems reach for it instead of rolling their own coordination.
- Get familiar with ZooKeeper's core concepts: Znodes, sessions, watches, and consistency guarantees.
- Understand the common distributed-systems patterns ZooKeeper is used to implement.

## Outcome

Write a short markdown answering the following:

1. What is ZooKeeper, and how is its architecture organized?
2. How does ZooKeeper handle consistency and notifications? Explain:
   - Sequential consistency
   - Watches, and how they're one-time triggers
   - How clients use watches in practice
3. What are Znodes, and what types of Znodes exist?
4. What are sessions, and how does ZooKeeper handle failures and node lifecycle? Explain:
   - Session lifecycle and heartbeats
   - Session expiration
   - Persistent vs. ephemeral (sequential) nodes
   - Failover and leader elections
   - ZXID
5. What are the basic operational concerns in ZooKeeper? At a high level, describe:
   - Ensemble deployment and scaling considerations
   - Snapshots and transaction logs
   - Common issues you'd run into operating it
6. Which architectural patterns is ZooKeeper commonly used to implement?
7. Compare ZooKeeper to at least one alternative coordination approach (e.g. etcd, Consul). Give a 1-2 sentence comparison and a simple use case for each.
8. Describe a simple real-world coordination scenario (2 paragraphs) and how ZooKeeper - or an alternative - would solve it.

### Links

- [Apache ZooKeeper Documentation](https://zookeeper.apache.org/)
- [ZooKeeper Recipes and Solutions](https://zookeeper.apache.org/doc/current/recipes.html)
