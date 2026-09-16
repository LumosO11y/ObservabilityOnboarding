# Java

## Overview & Syntax

In this chapter, you'll learn **Java** fundamentals and deep core concepts

---

# Missions

---

## Core Syntax & Language Fundamentals

Since the learner already knows programming, focus on Java-specific behavior.

### Official Documentation

- Java 11 API Documentation  
  https://docs.oracle.com/en/java/javase/11/docs/api/

- Java Language Specification
  https://docs.oracle.com/javase/specs/jls/se11/html/

- Java Virtual Machine Specification 
  https://docs.oracle.com/javase/specs/jvms/se11/html/

---

### Review These Topics

- Classes & Objects  
  https://docs.oracle.com/javase/tutorial/java/concepts/

- Access Modifiers  
  https://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html

- Exceptions (Checked vs Unchecked)  
  https://docs.oracle.com/javase/tutorial/essential/exceptions/

- Interfaces vs Abstract Classes  
  https://docs.oracle.com/javase/tutorial/java/IandI/createinterface.html

- Generics  
  https://docs.oracle.com/javase/tutorial/java/generics/

- Enums  
  https://docs.oracle.com/javase/tutorial/java/javaOO/enum.html

- Optional  
  https://docs.oracle.com/javase/8/docs/api/java/util/Optional.html

- Functional Interfaces  
  https://docs.oracle.com/javase/8/docs/api/java/util/function/package-summary.html

### Core JVM Concepts

- JVM Specification (SE 11)  
  https://docs.oracle.com/javase/specs/jvms/se11/html/

- Garbage Collection Tuning
  https://docs.oracle.com/en/java/javase/11/gctuning/

- Java Memory Model  
  https://docs.oracle.com/javase/specs/jls/se11/html/jls-17.html

Study:

- Stack vs Heap
- Metaspace
- ClassLoader mechanism
- Bytecode
- JIT Compilation
- Stop-the-world pauses
- G1 GC (default in Java 11)

---

Here’s a concise Markdown section with just links for reading:

---

### Annotations

* [Java Annotations Tutorial](https://docs.oracle.com/javase/tutorial/java/annotations/)
* [Java SE 11 API – `java.lang.annotation`](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/annotation/package-summary.html)
* [Common Built-in Annotations](https://www.baeldung.com/java-custom-annotations)

### Lombok

* [Project Lombok Official Site](https://projectlombok.org/)
* [Lombok Features Overview](https://projectlombok.org/features/all)
* [Using Lombok in Java Projects](https://www.baeldung.com/intro-to-project-lombok)
* [Lombok Annotations Reference](https://projectlombok.org/features/index)

---


### Collections Framework

- Collections Overview  
  https://docs.oracle.com/javase/8/docs/technotes/guides/collections/overview.html
  
---

### Stream Package

- Streams API  
  https://docs.oracle.com/javase/tutorial/collections/streams/

Learn:

- `map`
- `filter`
- `reduce`
- `collect`
- `flatMap`
- `groupingBy`
- `partitioningBy`
- `parallelStream()`

Also learn:

- Method references
- Functional interfaces
- Optional best practices

---

## Build Tools & Packaging

### 📦 Maven

https://maven.apache.org/guides/

---

### 📦 Creating JAR Files

https://docs.oracle.com/javase/tutorial/deployment/jar/

---

# Java 11 Study Questions

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
15. How does the G1 Garbage Collector reduce stop-the-world pauses?  
16. What are annotations in Java and how are they used?  
17. How does Lombok reduce boilerplate code in Java projects?  
18. Give an example of a Lombok annotation and explain what it does.  
19. What is the difference between `map`, `filter`, and `reduce` in the Streams API?  
20. How would you use `flatMap` in a stream of lists?  
21. What is the purpose of `collect` and `Collectors.groupingBy` in streams?  
22. How can you create and run a parallel stream, and what are its benefits?  
23. What is a JAR file and how do you create one in Java?  
24. What is Maven and how does it help in Java project management?  
25. Explain stop-the-world pauses and why tuning garbage collection is important in JVM.  