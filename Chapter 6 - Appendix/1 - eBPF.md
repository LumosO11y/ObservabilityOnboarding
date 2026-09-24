# eBPF

## Overview

**eBPF** (extended Berkeley Packet Filter) is a **kernel‑level programmable runtime** that lets you run sandboxed programs inside the Linux kernel **without modifying kernel source or modules**. It’s used broadly for **observability, networking, tracing, performance profiling, and security** by attaching small programs to kernel events or hooks at runtime.

## Outcome

1. What is eBPF? How can it run custom code inside the kernel without risking a kernel crash? What role does the verifier play?
2. What kinds of kernel and user-space events can an eBPF program attach to?
3. What are eBPF maps, and how does an eBPF program get its data back to a user-space program?
4. Chapter 1 asked about system-level instrumentation. How does eBPF make it possible, and what can an eBPF-based tool see - and not see - compared to SDK-based instrumentation?
5. Name 2 observability tools built on eBPF and describe what each one does.

### Links

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
