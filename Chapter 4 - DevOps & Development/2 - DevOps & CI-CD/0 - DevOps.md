# DevOps

## Overview

### The Evolution of Software Delivery: From Waterfall to DevOps

The landscape of software development has undergone a seismic shift over the last few decades.
What began as a rigid, linear process modeled after traditional manufacturing
has transformed into a fluid, continuous loop of creation and feedback. At the heart of this transformation is **DevOps**.

#### Understanding DevOps: More Than Just a Word

DevOps is not a specific software or a job title;
it is a **cultural and professional movement** that stresses communication, collaboration,
and integration between software developers (Dev) and IT operations professionals (Ops).

In a traditional setting, these two groups lived in "silos."
Developers were incentivized to push new features quickly, while Operations was incentivized to keep systems stable and unchanging.
This misalignment created a natural friction that slowed down progress.
DevOps seeks to unite these goals, treating the entire lifecycle—from the first line of code to the final production environment—as a single, shared responsibility.

#### The Starting Point: The Waterfall Model

To understand why DevOps exists, we have to look at where we started. For years, the **Waterfall Model** was the industry standard. It followed a strict, sequential series of phases:
1. **Requirements**: Everything the software needs to do is defined upfront.

2. **Design**: Architects plan the system's structure.

3. **Implementation**: Developers write the code based on the design.

4. **Verification**: The software is handed off to a separate QA team for testing.

5. **Maintenance/Deployment**: The Ops team finally deploys the software to servers.

##### The Fatal Flaws of Waterfall

While Waterfall provided a clear structure, it struggled with the reality of modern technology:
- **Inflexibility**: If a requirement changed halfway through, the project often had to start over.

- **The "Big Bang" Risk**: Testing only happened at the end. If a major bug was discovered, it was incredibly expensive and time-consuming to fix.

- **The Hand-off Gap**: Developers would "throw code over the wall" to Operations. If it crashed in production, Ops blamed Dev for bad code, and Dev blamed Ops for a bad environment.

#### The Catalyst for Change: Why We Moved

As the internet grew, the market demanded faster updates.
Companies like Amazon, Google, and Netflix realized they couldn't wait 12 months for a "Version 2.0."
They needed to ship updates daily, or even hourly.

##### 1. The Need for Velocity

In Waterfall, the "Time to Market" was measured in months or years. In a competitive digital economy, being first to market is a survival trait.

##### 2. The Rise of Agile

Before DevOps, there was Agile. Agile broke Waterfall's long phases into small "sprints."
While Agile fixed the developer's side of the house (making them faster), it actually made the "Ops" problem worse.
Now, developers were throwing code over the wall every two weeks instead of every year, overwhelming the operations teams.

##### 3. Complexity of Infrastructure

With the shift toward Cloud computing and Microservices, managing infrastructure manually became impossible.
We needed a way to manage servers with the same precision we used for code.

#### The DevOps Solution: Continuous Everything

DevOps solved the "Waterfall Wall" by introducing the **Infinite Loop**. Instead of a start and an end, the process became continuous.

##### Key Pillars of the DevOps Move:
- **CI/CD (Continuous Integration / Continuous Deployment)**: Code is automatically tested and merged into a shared repository multiple times a day.
If the tests pass, the code is automatically deployed to production.

- **Infrastructure as Code (IaC)**: Instead of manually configuring servers, engineers write scripts to define the environment.
This ensures that the "Development" environment is an exact twin of the "Production" environment.

- **Observability and Monitoring**: Rather than waiting for a user to complain,
teams use tools to watch metrics in real-time, allowing them to catch and fix issues before they impact the customer.

- **Shared Accountability**: When a system goes down, it isn't "Ops' problem."
The developers who wrote the code work alongside the engineers who maintain the platform to find a solution.

## Goals

Before diving into GitlabCI and ArgoCD, you should know what DevOps is.

**The Culture & Why It Exists**
- What is DevOps (culture vs. tool vs. job title)
- Why is it important
- What problems does it solve
- What problems does it cause (tooling sprawl, alert fatigue, skill requirements)
- What the DevOps cycle includes
- The "Dev vs. Ops" silo problem and shared accountability
- The "You Build It, You Run It" philosophy

**Where DevOps Came From**
- The Waterfall Model and its phases (Requirements, Design, Implementation, Verification, Maintenance/Deployment)
- Why Waterfall struggled at scale (inflexibility, the "Big Bang" risk, the hand-off gap)
- Agile and sprints
- Why Agile alone wasn't enough (it sped up Dev but overwhelmed Ops)
- Time to Market / velocity as a competitive pressure
- The DevOps "Infinite Loop" vs. a linear process

**Core Practices & Pillars**
- Continuous Integration (CI)
- Continuous Delivery vs. Continuous Deployment (CD)
- Infrastructure as Code (IaC)
- Configuration Management
- Environment parity (Dev/Staging/Production)
- Automation (build, test, deploy)
- Version control as a foundation
- Observability and Monitoring as a DevOps pillar, not a separate discipline
- Feedback loops

**Release & Operations Practices**
- Feature flags
- Canary releases and blue-green deployments
- Change management and release cadence
- On-call and incident response
- Blameless postmortems and incident culture
- Toil reduction

**Adjacent Disciplines**
- SRE (Site Reliability Engineering) vs. DevOps - where they overlap and differ
- DevSecOps and "shifting security left"
- GitOps and its relation to Infrastructure as Code

## Outcome

1. What is DevOps, and why is it described as a culture rather than a tool or job title?
2. What were the main phases of the Waterfall Model, and what were its "fatal flaws" that pushed the industry away from it?
3. How did Agile improve on Waterfall, and why did it still leave Operations teams overwhelmed?
4. What is meant by the DevOps "Infinite Loop," and how does it differ from Waterfall's linear process?
5. What is the difference between Continuous Integration, Continuous Delivery, and Continuous Deployment?
6. What is Infrastructure as Code, and why does it help keep Development and Production environments in sync?
7. Why is Observability considered a core pillar of DevOps rather than a separate discipline?
8. What does "shared accountability" mean in a DevOps team, and how does it change who gets paged when something breaks?
9. What is the difference between DevOps and SRE (Site Reliability Engineering)? Where do they overlap?
10. What is GitOps, and how does it relate to the DevOps principle of Infrastructure as Code?
11. What is DevSecOps, and why is "shifting security left" important?
12. What problems can DevOps introduce or make harder (e.g. tooling sprawl, alert fatigue, on-call burden)? How do teams mitigate them?

### Links

**Reading**
- <https://about.gitlab.com/topics/devops/>
- <https://www.geeksforgeeks.org/devops/introduction-to-devops/>
- <https://www.redhat.com/en/topics/devops/what-is-devops>
- <https://www.baeldung.com/ops/devops-overview>
- <https://www.geeksforgeeks.org/devops/devops-lifecycle/>
- <https://www.baeldung.com/cs/continuous-integration-deployment-delivery>
- <https://www.baeldung.com/ops/devops-vs-sre>

**Videos**
- <https://www.youtube.com/watch?v=Xrgk023l4lI>
- <https://www.youtube.com/watch?v=2D8VkHTbI8o>
- <https://www.youtube.com/watch?v=0yWAtQ6wYNM>
