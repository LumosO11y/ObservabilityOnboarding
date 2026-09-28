# Spring

## Overview

In this part, you'll learn Spring Framework fundamentals and Spring Boot - and, since this is an observability team, how a Spring Boot app exposes its own metrics and traces.

## Goals

- Understand Inversion of Control and Dependency Injection, and how Spring implements them.
- Understand beans, the Spring container, and the ways to configure and inject them.
- Understand what Spring Boot adds on top of Spring.
- Know how to build a simple REST API with Spring Boot.
- Understand how Spring Boot apps are made observable: Actuator, Micrometer, and OpenTelemetry.

## Outcome

Study questions:

1. What is Spring? Why do we need it?
2. What is POJO?
3. What is IOC?
4. What is DI?
5. How does Spring implement the DI and IOC patterns? How does its container work with beans? What actions does it perform?
6. What is Spring ApplicationContext and Spring BeanFactory?
7. In what ways can Spring do DI?
8. What is a Bean? And how do I define them?
9. What is Autowire? In what ways can I do Autowire for a specific bean? How does Spring know which bean to inject?
10. Can I create two beans of the same type? If so, how does Spring know which one to inject?
11. What is @Component?
12. What are the differences between Component and Bean? Why do we need them?
13. What is @ComponentScan?
14. What is @Configuration? And what is the purpose of classes with this annotation?
15. Where does Spring perform injection in our configuration? What formats are allowed for writing the configuration?
16. What is Spring Boot?
17. What is @EnableAutoConfiguration?
18. What is @SpringBootApplication?
19. What are Spring Boot Starters? Which one should I use if I want to write a REST application?
20. What is RestController?
21. How can we process a request with a JSON body to our API? And how can we perform validations automatically?

### Observability in Spring Boot

1. What is Spring Boot Actuator? What endpoints does it provide, and should all of them be exposed publicly?
2. What is Micrometer, and how does it relate to Spring Boot metrics? How would you get them into Prometheus?
3. What are the different ways a Spring Boot app can produce OpenTelemetry traces? Compare them. When would you pick each?

### Links

- [Spring Framework Guide by Marco Behler](https://www.marcobehler.com/guides/spring-framework) - What is Spring Framework: Dependency Injection in Java
- [Introduction to Spring Framework (GeeksforGeeks)](https://www.geeksforgeeks.org/advance-java/introduction-to-spring-framework/) - Introduction to Spring Framework
- [Spring vs Spring Boot (DZone)](https://dzone.com/articles/understanding-the-basics-of-spring-vs-spring-boot) - The basics of Spring vs Spring Boot
- [Spring vs Spring Boot Comparison (Baeldung)](https://www.baeldung.com/spring-vs-spring-boot) - A comparison between Spring and Spring Boot
- [Spring Core Annotations (Baeldung)](https://www.baeldung.com/spring-core-annotations) - Spring core annotations
- [Spring Tutorial (Baeldung)](https://www.baeldung.com/spring-tutorial) - Extra tutorials for deeper learning
- [Building a RESTful Web Service (Spring guide)](https://spring.io/guides/gs/rest-service)
- [Validation in Spring Boot](https://docs.spring.io/spring-boot/reference/io/validation.html)
- [Spring Boot Actuator](https://docs.spring.io/spring-boot/reference/actuator/index.html)
- [Actuator Metrics (Micrometer)](https://docs.spring.io/spring-boot/reference/actuator/metrics.html)

<details>
<summary>Spoiler: open once you've answered "Observability in Spring Boot" question 3</summary>

- [Actuator Tracing](https://docs.spring.io/spring-boot/reference/actuator/tracing.html)
- [OpenTelemetry Java agent](https://opentelemetry.io/docs/zero-code/java/agent/)
- [OpenTelemetry Spring Boot starter](https://opentelemetry.io/docs/zero-code/java/spring-boot-starter/)

</details>
