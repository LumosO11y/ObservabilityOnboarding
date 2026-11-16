# eBPF

## Overview

eBPF is a Linux kernel technology that lets small programs run inside the kernel itself, and many observability, security, and networking tools are built on it. You met system-level instrumentation in Chapter 1; eBPF is the main technology behind it on Linux today.

## Goals

- Understand what eBPF is and how it runs code safely inside the kernel.
- Understand how eBPF enables system-level instrumentation, and where it falls short of SDK-based instrumentation.
- Understand what OBI is and where it fits next to the other OpenTelemetry instrumentation options.
- Understand why some languages, like Go, rely on eBPF for zero-code instrumentation.
- Know how eBPF is used for runtime security, and the risks that come with being able to load eBPF programs.

## Outcome

1. What is eBPF? How can it run custom code inside the kernel without risking a kernel crash? What role does the verifier play?
2. What is an eBPF hook point? Pick 3 different kinds of hooks (at least one in the kernel and one in user space), and for each one explain what it attaches to and give an observability use case. If two hook types could capture the same event, what would make a tool prefer one over the other?
3. What are eBPF maps, and how does an eBPF program get its data back to a user-space program?
4. What does an eBPF program need from the host in order to run? What does that mean for running eBPF tools in containers and on Kubernetes?
5. Revisit your Chapter 1 answer on system-level instrumentation. Now that you know how eBPF works, what would you correct or add?
6. What is OBI? How does it produce OpenTelemetry telemetry for an app without touching its code or runtime?
7. Which signals can OBI produce today, and what would you still need an SDK for?
8. Think back to how zero-code instrumentation worked for the languages you picked in the previous part. Why is that approach much harder for a compiled language like Go? How does OpenTelemetry's Go auto-instrumentation use eBPF to get around it, and how is that different from what OBI does? Which other languages are in a similar position?
9. Name 2 other observability tools built on eBPF and describe what each one does.
10. eBPF is also widely used for runtime security. How can an eBPF-based tool detect, or even block, suspicious behavior on a host, and what can it do that a security agent running only in user space can't? Name one such tool.
11. The same power cuts both ways. Why is being able to load eBPF programs a sensitive privilege, and how could an attacker abuse it? What does the kernel do to limit who can load them?

### Links

- [OpenTelemetry eBPF Instrumentation (OBI)](https://opentelemetry.io/docs/zero-code/obi/)
- [OBI GitHub Repository](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation)
- [OpenTelemetry Go Zero-Code Instrumentation](https://opentelemetry.io/docs/zero-code/go/)
- [OpenTelemetry Go Auto-Instrumentation Repository](https://github.com/open-telemetry/opentelemetry-go-instrumentation)
- [What is eBPF?](https://ebpf.io/what-is-ebpf/)
- [eBPF Docs](https://docs.ebpf.io/)
- [eBPF Foundation](https://ebpf.foundation/)
- [Get Started with eBPF](https://ebpf.io/get-started/)
- [eBPF Applications Landscape](https://ebpf.io/applications/)
- [Linux Kernel BPF Documentation](https://docs.kernel.org/bpf/index.html)
