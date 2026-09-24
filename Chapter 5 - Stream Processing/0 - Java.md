# Java

## Overview

In this chapter, you'll learn **Java** fundamentals and deep core concepts. Since you already know how to program, the focus is on Java-specific behavior.

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
- Metaspace
- ClassLoader mechanism
- Bytecode
- JIT Compilation
- Stop-the-world pauses
- G1 GC (default in Java 11)

**Annotations & Lombok**

- Built-in and custom annotations
- Project Lombok and how it reduces boilerplate

**Collections & Streams**

- Collections Framework
- Streams API: `map`, `filter`, `reduce`, `collect`, `flatMap`, `groupingBy`, `partitioningBy`, `parallelStream()`
- Method references
- Optional best practices

**Concurrency**

- Threads and the `ExecutorService`
- `synchronized` and `volatile`
- `CompletableFuture`

**Build Tools & Packaging**

- Maven
- Creating JAR files

## Outcome

Java 11 study questions:

1. What is the difference between a class and an object in Java?
2. How do constructors differ from regular methods in Java?
3. Explain the difference between public, protected, private, and default access modifiers.
4. Can a subclass access the private fields of its parent class? Why or why not?
5. What is the difference between checked and unchecked exceptions? Give examples.
6. How would you implement a custom checked exception?
7. When should you use an interface instead of an abstract class?
8. Can an abstract class have implemented methods? Can an interface? Explain.
9. Why are generics useful in Java collections? Give an example.
10. How do enums improve type safety compared to constant variables?
11. What problem does Optional solve? How do you avoid NullPointerException with it?
12. Give an example of a functional interface and a lambda expression that implements it.
13. What is the difference between the Stack and the Heap in Java memory management?
14. Explain the ClassLoader mechanism and why parent delegation is important.
15. What are stop-the-world pauses, and how does the G1 Garbage Collector reduce them? Why is tuning garbage collection important in the JVM?
16. What is bytecode, and how does the JIT compiler turn it into fast native code at runtime?
17. What is Metaspace, and what lives there as opposed to on the Heap?
18. What are annotations in Java and how are they used?
19. How does Lombok reduce boilerplate code in Java projects?
20. Give an example of a Lombok annotation and explain what it does.
21. What is the difference between `map`, `filter`, and `reduce` in the Streams API?
22. How would you use `flatMap` in a stream of lists?
23. What is the purpose of `collect` and `Collectors.groupingBy` in streams?
24. How can you create and run a parallel stream, and what are its benefits?
25. What is the difference between creating a `Thread` yourself and submitting work to an `ExecutorService`?
26. What problems do `synchronized` and `volatile` solve, and how do they differ?
27. What is a `CompletableFuture`, and how does it help you compose asynchronous work?
28. What is a JAR file and how do you create one in Java?
29. What is Maven and how does it help in Java project management?

### Links

**Official Documentation**

- [Java 11 API Documentation](https://docs.oracle.com/en/java/javase/11/docs/api/)
- [Java Language Specification](https://docs.oracle.com/javase/specs/jls/se11/html/)
- [Java Virtual Machine Specification](https://docs.oracle.com/javase/specs/jvms/se11/html/)

**Core Syntax**

- [Classes & Objects](https://docs.oracle.com/javase/tutorial/java/concepts/)
- [Access Modifiers](https://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html)
- [Exceptions (Checked vs Unchecked)](https://docs.oracle.com/javase/tutorial/essential/exceptions/)
- [Interfaces vs Abstract Classes](https://docs.oracle.com/javase/tutorial/java/IandI/createinterface.html)
- [Generics](https://docs.oracle.com/javase/tutorial/java/generics/)
- [Enums](https://docs.oracle.com/javase/tutorial/java/javaOO/enum.html)
- [Optional](https://docs.oracle.com/javase/8/docs/api/java/util/Optional.html)
- [Functional Interfaces](https://docs.oracle.com/javase/8/docs/api/java/util/function/package-summary.html)

**Core JVM Concepts**

- [JVM Specification (SE 11)](https://docs.oracle.com/javase/specs/jvms/se11/html/)
- [Garbage Collection Tuning](https://docs.oracle.com/en/java/javase/11/gctuning/)
- [Java Memory Model](https://docs.oracle.com/javase/specs/jls/se11/html/jls-17.html)

**Annotations**

- [Java Annotations Tutorial](https://docs.oracle.com/javase/tutorial/java/annotations/)
- [Java SE 11 API – `java.lang.annotation`](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/annotation/package-summary.html)
- [Common Built-in Annotations](https://www.baeldung.com/java-custom-annotations)

**Lombok**

- [Project Lombok Official Site](https://projectlombok.org/)
- [Lombok Features Overview](https://projectlombok.org/features/all)
- [Using Lombok in Java Projects](https://www.baeldung.com/intro-to-project-lombok)
- [Lombok Annotations Reference](https://projectlombok.org/features/index)

**Collections & Streams**

- [Collections Overview](https://docs.oracle.com/javase/8/docs/technotes/guides/collections/overview.html)
- [Streams API](https://docs.oracle.com/javase/tutorial/collections/streams/)

**Concurrency**

- [Java Concurrency Tutorial](https://docs.oracle.com/javase/tutorial/essential/concurrency/)

**Build Tools & Packaging**

- [Maven Guides](https://maven.apache.org/guides/)
- [Creating JAR Files](https://docs.oracle.com/javase/tutorial/deployment/jar/)
