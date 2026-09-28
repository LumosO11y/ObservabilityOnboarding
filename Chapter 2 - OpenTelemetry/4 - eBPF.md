# eBPF

## Overview

eBPF is a Linux kernel technology that lets small programs run inside the kernel itself, and many observability, security, and networking tools are built on it. You met system-level instrumentation in Chapter 1; eBPF is the main technology behind it on Linux today.

This part starts with how eBPF works and what it can hook into, then covers how OpenTelemetry uses it to instrument applications without code changes: OBI (OpenTelemetry eBPF Instrumentation), and language-specific auto-instrumentation for languages like Go. It ends with how the same technology is used for security and networking, and why the power to load eBPF programs is itself a security concern.

## Goals

- Understand what eBPF is and how it runs code safely inside the kernel.
- Understand how eBPF enables system-level instrumentation, and where it falls short of SDK-based instrumentation.
- Understand what OBI is and where it fits next to the other OpenTelemetry instrumentation options.
- Understand why some languages, like Go, rely on eBPF for zero-code instrumentation.
- Know how eBPF is used beyond observability, in security and networking tools, and the risks that come with it.

## Outcome

1. What is eBPF? How can it run custom code inside the kernel without risking a kernel crash? What role does the verifier play?
2. What kinds of kernel and user-space events can an eBPF program attach to?
3. What are eBPF maps, and how does an eBPF program get its data back to a user-space program?
4. What does an eBPF program need from the host in order to run? What does that mean for running eBPF tools in containers and on Kubernetes?
5. Chapter 1 asked about system-level instrumentation. How does eBPF make it possible, and what can an eBPF-based tool see - and not see - compared to SDK-based instrumentation?
6. What is OBI? How does it produce OpenTelemetry telemetry for an app without touching its code or runtime, and how is that different from the language-specific zero-code instrumentation from the previous part?
7. Which signals can OBI produce today, and what would you still need an SDK for?
8. Think back to how zero-code instrumentation worked for the languages you picked in the previous part. Why is that approach much harder for a compiled language like Go? How does OpenTelemetry's Go auto-instrumentation use eBPF to get around it, and how is that different from what OBI does? Which other languages are in a similar position?
9. Name 2 other observability tools built on eBPF and describe what each one does.
10. eBPF is also widely used for runtime security. How can an eBPF-based tool detect, or even block, suspicious behavior on a host, and what can it do that a security agent running only in user space can't? Name one such tool.
11. eBPF is also used for networking. Where in a packet's path through the kernel can an eBPF program attach (e.g. XDP), and what does that let networking tools do? Name one networking tool built on eBPF and what it replaces.
12. The same power cuts both ways. Why is being able to load eBPF programs a sensitive privilege, and how could an attacker abuse it? What does the kernel do to limit who can load them?

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
- [cilium/ebpf: a Go library for eBPF](https://github.com/cilium/ebpf)
