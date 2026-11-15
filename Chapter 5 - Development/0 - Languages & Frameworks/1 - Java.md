# Java

## Overview

In this part, you'll learn **Java** fundamentals and deep core concepts. Since you already know how to program, the focus is on Java-specific behavior.

> **Which Java?** The questions below target Java 17. Ask your mentor which version the services you'll work on use - if it's 21, also look into virtual threads.

## Goals

**Core Syntax & Language Fundamentals**

- Classes & Objects
- Access Modifiers
- Exceptions (Checked vs Unchecked)
- Interfaces vs Abstract Classes
- Generics
- Enums
- Optional
- Functional Interfaces

**Core JVM Concepts**

- Stack vs Heap
- Stop-the-world pauses
- G1 GC (default since Java 9)

**Annotations & Lombok**

- Built-in and custom annotations
- Project Lombok and how it reduces boilerplate

**Collections & Streams**

- Collections Framework
- Streams API: `map`, `filter`, `reduce`, `collect`, `groupingBy`
- Method references
- Optional best practices

**Concurrency**

- `CompletableFuture`

**Build Tools & Packaging**

- Maven

**Modern Java**

- Records, `var`, text blocks, and switch expressions (Java 17)

## Outcome

Java 17 study questions:

1. What is the difference between a class and an object in Java?
2. Explain the difference between public, protected, private, and default access modifiers.
3. What is the difference between checked and unchecked exceptions? Give examples.
4. When should you use an interface instead of an abstract class? Can each of them have implemented methods?
5. Why are generics useful in Java collections? Give an example.
6. How do enums improve type safety compared to constant variables?
7. What problem does Optional solve? How do you avoid NullPointerException with it?
8. Give an example of a functional interface and a lambda expression that implements it.
9. What is the difference between the Stack and the Heap in Java memory management?
10. What are stop-the-world pauses, and how does the G1 Garbage Collector reduce them? Why is tuning garbage collection important in the JVM?
11. What are annotations in Java and how are they used?
12. How does Lombok reduce boilerplate code in Java projects? Give an example of one of its annotations and explain what it does.
13. What is the difference between `map`, `filter`, and `reduce` in the Streams API?
14. What is the purpose of `collect` and `Collectors.groupingBy` in streams?
15. What is a `CompletableFuture`, and how does it help you compose asynchronous work?
16. What is Maven and how does it help in Java project management?
17. What are records? How do they compare to what Lombok gives you?
18. What do `var`, text blocks, and switch expressions each add to the language? Give a short example of each.

### Links

**Official Documentation**

- [Java 17 API Documentation](https://docs.oracle.com/en/java/javase/17/docs/api/)
- [Java Language Specification](https://docs.oracle.com/javase/specs/jls/se17/html/)
- [Java Virtual Machine Specification](https://docs.oracle.com/javase/specs/jvms/se17/html/)

**Core Syntax**

- [Classes & Objects](https://docs.oracle.com/javase/tutorial/java/concepts/)
- [Access Modifiers](https://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html)
- [Exceptions (Checked vs Unchecked)](https://docs.oracle.com/javase/tutorial/essential/exceptions/)
- [Interfaces vs Abstract Classes](https://docs.oracle.com/javase/tutorial/java/IandI/createinterface.html)
- [Generics](https://docs.oracle.com/javase/tutorial/java/generics/)
- [Enums](https://docs.oracle.com/javase/tutorial/java/javaOO/enum.html)
- [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html)
- [Functional Interfaces](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/package-summary.html)

**Core JVM Concepts**

- [JVM Specification (SE 17)](https://docs.oracle.com/javase/specs/jvms/se17/html/)
- [Garbage Collection Tuning](https://docs.oracle.com/en/java/javase/17/gctuning/)
- [Java Memory Model](https://docs.oracle.com/javase/specs/jls/se17/html/jls-17.html)

**Annotations**

- [Java Annotations Tutorial](https://docs.oracle.com/javase/tutorial/java/annotations/)
- [Java SE 17 API – `java.lang.annotation`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/annotation/package-summary.html)
- [Common Built-in Annotations](https://www.baeldung.com/java-default-annotations)

**Lombok**

- [Project Lombok Official Site](https://projectlombok.org/)
- [Lombok Features Overview](https://projectlombok.org/features/)
- [Using Lombok in Java Projects](https://www.baeldung.com/intro-to-project-lombok)

**Collections & Streams**

- [Collections Overview](https://docs.oracle.com/javase/8/docs/technotes/guides/collections/overview.html)
- [Streams API](https://docs.oracle.com/javase/tutorial/collections/streams/)

**Concurrency**

- [Java Concurrency Tutorial](https://docs.oracle.com/javase/tutorial/essential/concurrency/)

**Build Tools & Packaging**

- [Maven Guides](https://maven.apache.org/guides/)
- [Creating JAR Files](https://docs.oracle.com/javase/tutorial/deployment/jar/)

**Modern Java**

- [Records](https://dev.java/learn/records/)
- [Virtual Threads](https://docs.oracle.com/en/java/javase/21/core/virtual-threads.html)
