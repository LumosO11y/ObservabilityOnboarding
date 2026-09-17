# Kafka

## Overview

In this chapter, you'll learn Apache Kafka fundamentals: producers, consumers, brokers, topics, and partitions.

## Outcome

1. What is Apache Kafka, and what problem does it solve compared to a traditional message queue?
2. What is a Topic, and how does it relate to a Partition?
3. How does Kafka use partitions to achieve both ordering guarantees and horizontal scalability? What's the tradeoff?
4. What is a Broker, and how do multiple brokers form a Kafka cluster?
5. What is an Offset, and how does a consumer use it to track its position in a partition?
6. What is a Consumer Group, and how does Kafka divide partitions among the consumers in a group?
7. What is replication in Kafka? What is the difference between a leader and a follower replica?
8. What is the difference between "at-least-once," "at-most-once," and "exactly-once" delivery semantics?
9. How is a message routed to a specific partition? What role does the partition key play?
10. What is retention, and how does Kafka decide when to delete old messages?
11. Why is message ordering only guaranteed within a partition, not across an entire topic?
12. How does a Producer decide which partition to send a message to when no key is provided?
13. In our pipeline, Kafka carries OTEL spans between services. Why is a message broker like Kafka a good fit for connecting an instrumented app to a stream processor like Flink?

### Links

**Official Documentation (Architecture, APIs, Concepts)**
- <https://kafka.apache.org/documentation/>
- <https://docs.confluent.io/kafka/introduction.html>

**Videos — Fundamentals & Architecture**
- <https://www.youtube.com/watch?v=tpUj_f4_pWc> (Kafka intro – core components: producers/consumers/brokers/topics/partitions)
- <https://www.youtube.com/playlist?list=PLt1SIbA8guusxiHz9bveV-UHs_biWFegU> (Apache Kafka full beginner playlist)
- <https://www.youtube.com/watch?v=cNFAP9OnJjo> (Apache Kafka Crash Course – brokers/topics/partitions basics)
- <https://www.youtube.com/watch?v=J-xfe3zAtwY> (Full Kafka course for beginners)

**Videos — Deeper Concepts**
- <https://www.youtube.com/watch?v=r4c0whAOCGI> (Kafka Topics and Partitions deep dive)
- <https://www.youtube.com/watch?v=bsADIO5fdJ0> (Kafka architecture explained: partitions, producers, consumers, offsets)
- <https://www.youtube.com/watch?v=lh_tjm0yPz4> (Kafka Producers explained – how data gets written)
- <https://www.youtube.com/watch?v=V6l-oQeDdcI> (Topics, partitions & consumer groups explained)

**Tutorials & Practical Guides**
- <https://notes.kodekloud.com/docs/Event-Streaming-with-Kafka/Building-Blocks-of-Kafka/Demo-Topics-Partitions-and-Brokers> (Create topics, partitions, brokers CLI steps)
- <https://www.linkedin.com/learning/complete-guide-to-apache-kafka-for-beginners/topics-partitions-and-offsets> (video course – topics/partitions/offsets)
