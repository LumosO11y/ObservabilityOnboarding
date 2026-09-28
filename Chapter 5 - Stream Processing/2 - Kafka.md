# Kafka

## Overview

In this part, you'll learn Apache Kafka fundamentals: producers, consumers, brokers, topics, and partitions. We run Kafka 2.7, which still depends on ZooKeeper.

## Goals

- Understand Kafka's core building blocks and how they fit together.
- Understand how Kafka achieves ordering, scalability, durability, and delivery guarantees.
- Understand how Kafka uses ZooKeeper, and what replaces it in newer versions.
- Understand why Kafka fits into our telemetry pipeline.

## Outcome

1. What is Apache Kafka, and what problem does it solve compared to a traditional message queue?
2. What is a Topic, and how does it relate to a Partition?
3. How does Kafka use partitions to achieve both ordering guarantees and horizontal scalability? What's the tradeoff?
4. What is a Broker, and how do multiple brokers form a Kafka cluster?
5. What is an Offset, and how does a consumer use it to track its position in a partition?
6. What is a Consumer Group, and how does Kafka divide partitions among the consumers in a group?
7. What is replication in Kafka? What is the difference between a leader and a follower replica?
8. What is the difference between "at-least-once," "at-most-once," and "exactly-once" delivery semantics?
9. How is a message routed to a specific partition? What role does the partition key play, and what happens when no key is provided?
10. What is retention, and how does Kafka decide when to delete old messages? What is log compaction, and how is it different?
11. What does the producer's `acks` setting control, and what is the ISR (In-Sync Replicas)? Together, how do they decide whether an acknowledged write can still be lost?
12. What is consumer lag, and why is it one of the most important Kafka metrics to watch? How could you use it to autoscale consumers (think back to KEDA from the Kubernetes part)?
13. The Kafka version we run (2.7) depends on ZooKeeper, the coordination service you learned about in the ClickHouse part of Chapter 3. What does Kafka keep in ZooKeeper, and what is the controller's role in that setup?
14. What is KRaft? Where does cluster metadata live in a KRaft cluster, and how do brokers learn about changes to it?
15. Why did the Kafka project decide to move away from ZooKeeper? What limitations of the ZooKeeper-based design was KRaft meant to fix?
16. Trace the transition across versions: in which release did KRaft first appear, when was it declared production-ready, and when was ZooKeeper support removed entirely?
17. What does staying on 2.7 mean for us? What would a move to a KRaft-based version involve, and why can't a ZooKeeper-based cluster jump straight to the newest release?
18. In our pipeline, Kafka carries OTEL spans between services. Why is a message broker like Kafka a good fit for connecting an instrumented app to a stream processor like Flink?

### Links

**Official Documentation (Architecture, APIs, Concepts)**

- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [Confluent: Introduction to Kafka](https://docs.confluent.io/kafka/introduction.html)
- [Log Compaction Basics](https://kafka.apache.org/documentation/#design_compactionbasics)

**ZooKeeper and KRaft**

- [ZooKeeper in the Kafka 2.7 docs](https://kafka.apache.org/27/documentation.html#zk)
- [KIP-500: the proposal to replace ZooKeeper](https://cwiki.apache.org/confluence/display/KAFKA/KIP-500%3A+Replace+ZooKeeper+with+a+Self-Managed+Metadata+Quorum)
- [KIP-833: marking KRaft production-ready](https://cwiki.apache.org/confluence/display/KAFKA/KIP-833%3A+Mark+KRaft+as+Production+Ready)
- [KRaft in the current Kafka docs](https://kafka.apache.org/documentation/#kraft)
- [Confluent's KRaft overview](https://developer.confluent.io/learn/kraft/)
- [Kafka 4.0 release announcement](https://kafka.apache.org/blog/2025/03/18/apache-kafka-4.0.0-release-announcement/)

**Videos: Fundamentals & Architecture**

- [Kafka Intro: Core Components](https://www.youtube.com/watch?v=tpUj_f4_pWc)
- [Apache Kafka full beginner playlist](https://www.youtube.com/playlist?list=PLt1SIbA8guusxiHz9bveV-UHs_biWFegU)
- [Apache Kafka Crash Course](https://www.youtube.com/watch?v=cNFAP9OnJjo)
- [Full Kafka course for beginners](https://www.youtube.com/watch?v=J-xfe3zAtwY)

**Videos: Deeper Concepts**

- [Kafka Topics and Partitions deep dive](https://www.youtube.com/watch?v=r4c0whAOCGI)
- [Kafka architecture explained: partitions, producers, consumers, offsets](https://www.youtube.com/watch?v=bsADIO5fdJ0)
- [Kafka Producers Explained](https://www.youtube.com/watch?v=lh_tjm0yPz4)
- [Topics, partitions & consumer groups explained](https://www.youtube.com/watch?v=V6l-oQeDdcI)

**Tutorials & Practical Guides**

- [Create topics, partitions, brokers CLI steps](https://notes.kodekloud.com/docs/Event-Streaming-with-Kafka/Building-Blocks-of-Kafka/Demo-Topics-Partitions-and-Brokers)
- [Complete Guide to Apache Kafka for Beginners (LinkedIn Learning)](https://www.linkedin.com/learning/complete-guide-to-apache-kafka-for-beginners/topics-partitions-and-offsets)
