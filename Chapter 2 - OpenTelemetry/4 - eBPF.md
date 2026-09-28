# eBPF

## Overview

**eBPF** (extended Berkeley Packet Filter) is a **kernel‑level programmable runtime** that lets you run sandboxed programs inside the Linux kernel **without modifying kernel source or modules**. OpenTelemetry uses it in **OBI** (OpenTelemetry eBPF Instrumentation) to instrument applications from outside the process.

## Goals

- Understand what eBPF is and how it runs code safely inside the kernel.
- Understand how eBPF enables system-level instrumentation, and where it falls short of SDK-based instrumentation.
- Understand what OBI is and where it fits next to the other OpenTelemetry instrumentation options.

## Outcome

1. What is eBPF? How can it run custom code inside the kernel without risking a kernel crash? What role does the verifier play?
2. What kinds of kernel and user-space events can an eBPF program attach to?
3. What are eBPF maps, and how does an eBPF program get its data back to a user-space program?
    - What does an eBPF program need from the host in order to run? What does that mean for running eBPF tools in containers and on Kubernetes?
4. Chapter 1 asked about system-level instrumentation. How does eBPF make it possible, and what can an eBPF-based tool see - and not see - compared to SDK-based instrumentation?
5. What is OBI? How does it produce OpenTelemetry telemetry for an app without touching its code or runtime, and how is that different from the language-specific zero-code instrumentation from the previous part?
6. Which signals can OBI produce today, and what would you still need an SDK for?
7. Name 2 other observability tools built on eBPF and describe what each one does.

### Links

- **OpenTelemetry eBPF Instrumentation (OBI)** — Official docs:
  [https://opentelemetry.io/docs/zero-code/obi/](https://opentelemetry.io/docs/zero-code/obi/)

- **OBI GitHub Repository**:
  [https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation)

- **What is eBPF?** — Introduction to eBPF concepts:
  [https://ebpf.io/what-is-ebpf/](https://ebpf.io/what-is-ebpf/)

- **eBPF Official Docs** — Core technical documentation (concepts, program types, maps, helpers):
  [https://docs.ebpf.io/](https://docs.ebpf.io/)

- **eBPF Foundation Site** — Info about the ecosystem, community, and projects:
  [https://ebpf.foundation/](https://ebpf.foundation/)

- **Get Started with eBPF** — Intro, labs, and tutorials (from the main eBPF community portal):
  [https://ebpf.io/get-started/](https://ebpf.io/get-started/)

- **Linux Kernel BPF Documentation** — Kernel‑level technical reference:
  [https://docs.kernel.org/bpf/index.html](https://docs.kernel.org/bpf/index.html)

- **Go eBPF Library (cilium/ebpf)** — Library to build and load eBPF programs from Go code:
  [https://github.com/cilium/ebpf](https://github.com/cilium/ebpf)
