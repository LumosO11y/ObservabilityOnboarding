# System & Linux

## Overview

A large part of our work relies on and uses existing infrastructures of data and DevOps. At the base of all the architecture components we use, lie Virtual Machines.

## Goals

- Operating systems, the Kernel, and System calls
- Linux, CNCF, and VMware
- The components of virtual machines and the effect they had on the technological world
- Common Linux commands

## The Virtualization Story

Think back to the distant past, far, far away. Computers were a novelty, and looked completely different than they do today.

### The Past
Before the 1940s, a "computer" was human beings (often women) who sat in a room performing long-form arithmetic for navigation tables or artillery trajectories. The transition to electronic computing was driven by WWII. The ENIAC (1945) was one of the first general-purpose electronic computers. It was a behemoth:
- **Size**: It took up 1,800 square feet.
- **Weight**: 30 tons.
- **Power**: It didn't have microchips. It instead used vacuum tubes, which were fragile glass bulbs that glowed and generated immense heat. They failed constantly, meaning the "uptime" was often measured in hours.

Still, this computer is not entirely different from our current ones. Regardless of whether it's an old mainframe or your modern laptop, every computer follows the *Von Neumann Architecture*, sharing the same 3 main components:
1. **The CPU** (Central Processing Unit): The "brain". It executes instructions and performs calculations.
2. **Memory (RAM)**: The "short-term desk." It holds the data the CPU is currently working on. It's fast but "volatile" (it wipes when the power goes out).
3. **Storage (Hard Drive/SSD)**: The "filing cabinet." This is where data stays permanently.

Computers are fundamentally "on/off" machines. A wire has electricity (1) or it doesn't (0). In the early days, operating a computer was physical labor: plugboards (physically rewiring the machine with cables), punch cards (if you dropped your stack of 5,000 cards, your "program" was ruined), and binary manual entry (flipping physical toggles, one bit at a time, on machines like the Altair 8800).

### The Straw(s) that Broke the Camel's Back
Before virtualization, software was "trapped" inside the physical box it was installed on. This created massive headaches for businesses and engineers:
- **Low Resource Utilization**: Most servers only used 5-15% of their total brainpower (CPU/RAM). The rest was wasted electricity because you couldn't safely run multiple different apps on one machine without them crashing each other.
- **Hardware Dependency**: The OS was "married" to the specific physical parts of the computer. If a motherboard died, you couldn't just move the data to a different model of computer - the system would simply fail to boot.
- **Dependency Hell**: If App A required Java 8 while App B required Java 11, trying to run both on the same machine put you in a stalemate - installing one would break the other. This forced companies to buy a separate physical server for every single application, leading to "Server Sprawl."
- **Slow Provisioning**: A developer needing a new server had to file a request, wait for a purchase order and shipping, then manually "rack and stack" the hardware - weeks or months.
- **Fragile Disaster Recovery**: Restoring a crashed physical server meant finding identical hardware and manually reinstalling the OS and settings from scratch.

### VMs to the Rescue
Virtualization introduced a "middleman" called the Hypervisor - a layer of software that hid the physical hardware from the apps, and changed everything:
- **Server Consolidation**: Instead of 10 physical servers running at 10% capacity, one powerful physical server could run 10 VMs at 90% capacity - saving millions in power, cooling, and space.
- **Hardware Independence**: The Hypervisor presents "generic" virtual hardware to the VM, so you can move a running VM from a Dell server to an HP server with zero downtime.
- **Isolation and Sandboxing**: Each VM is a "bubble." If App A crashes or gets a virus, it cannot "leak" over to App B.
- **Instant Scaling**: Since a VM is just a giant file on a disk, cloning it takes seconds instead of weeks of physical labor.
- **Perfect Portability**: A "Snapshot" lets you hit "Undo" and revert a VM to exactly how it was five minutes ago.

## Exercise: The Linux Manipulation Exercise

**Goal**: Find "hidden" information about the computer using *only* the terminal.
**Scenario**: You have been given a mystery server. You need to identify its "DNA" (hardware), its "Health" (processes), and its "Security" (permissions).
**Instructions**: Note down the commands you used.

1. **The Version Check**: Find out exactly which version of the Linux Kernel is running.
2. **The Heartbeat**: View the CPU information. Is it an Intel, AMD, or ARM chip?
3. **The Long Way Home**: Navigate to the `/var/log` directory. List all files, but show the "long" version so you can see who owns the files.
4. **The Content Hunt**: Find the file named `syslog` or `messages`. Use a command to read only the last 20 lines of that file to see what the system is doing right now.
5. **Create a Secret**: Create a new folder in your home directory called `SecretProject`.
6. **Lock the Door**: Change the permissions so that only you (the owner) can read and write to it, and no one else in the "world" can even see it's there.
   - **Verify**: Run `ls -ld` to prove the permissions changed.
7. **The Birth of a File**: Create an empty file named `notes.txt` without opening an editor.
8. **The Poet**: Write "Hello World!(:" into the file.
9. **The Clone**: Create an exact copy of `notes.txt` and call it `backup_notes.txt`.
10. **The Relocation**: Create a directory called `Archive` and move the backup file into it.
11. **The Search Party**: Find every file in the current directory that ends in `.txt`.
12. **The Cleanup**: Remove the original `notes.txt` file.
13. **The "Nuke" (Use with Caution)**: Delete the `Archive` directory and everything inside it at once.

## Outcome

<details>
<summary><strong>Questions you should be able to answer by the end of this block (click to expand)</strong></summary>

1. What was before virtualization?
2. What problems did virtualization solve and how?
3. What is an Operating system?
4. What is a kernel?
5. What is a hypervisor?
6. What is the shell?
7. What are the components of an operating system? Of a virtual machine? How do they interact with each other?
8. Explain the role of the Kernel as the "intermediary." If an application wants to write data to a hard drive, why can't it just talk to the hardware directly?
9. Describe the step-by-step process that occurs when a user-space application executes a System Call. What is "Context Switching," and why is it necessary for system security?
10. Walk us through what happens the moment you press the power button on a computer. What is the hand-off process between the BIOS/UEFI and the OS Kernel?
11. Compare and contrast Bare Metal and Hosted hypervisors. In what scenario would each be preferred over the other?
12. How does a Virtual Machine "believe" it has its own CPU and RAM when, in reality, it is sharing physical resources with 20 other machines?
13. List the essential components of a VM. Which of these is responsible for making a VM "portable" across different physical servers?
14. In Linux, "everything is a file." Explain what this means in the context of hardware devices (like a mouse or a hard drive) located in the `/dev` directory.
15. How would you find every line containing the word "ERROR" in a log file named `server.log`?
16. Explain the difference between `chmod` and `chown`.
17. What is the difference between `cp` and `mv`?
18. How is a directory different from a regular file?
19. What is the difference between using `\` and `/` when specifying file paths?
20. How do you check which processes are consuming the most CPU in real-time?
21. If a file has permissions 755, what can the owner do that the "world" (others) cannot?
22. Explain the different levels of permissions and how they come into play.
23. What are CGroups?
24. Before virtualization, what was "Server Sprawl," and how did it affect the physical design and cost of data centers?
25. What is CNCF?
26. What is the mission of the CNCF (Cloud Native Computing Foundation)?
27. What are famous projects of CNCF?
28. What is the Linux Foundation?
29. How is the Linux Foundation related to CNCF?
30. What is Open Source? Why is it important?
31. A developer tells you their VM is running slow. Using Linux commands, walk us through how you would diagnose whether the bottleneck is CPU, Memory, or Disk I/O.
32. We need to move a legacy application from an old physical server to a virtualized environment. What are the biggest risks, and how does the "Hypervisor" layer help make this possible?
33. How does the Kernel prevent a standard user from accidentally deleting critical system files?
34. What is the difference between a Monolithic Kernel and a Microkernel?
35. What is the difference between "Block Storage" and a "File System"?
36. What is a cache? What is caching?
37. What is ephemeral storage?
38. At what exact point in the boot process does the computer stop being "generic hardware" and start being "Linux"?
39. Compare and contrast Windows vs Linux. Give use cases for each.
40. What are Distributions/Distros? What are the most common distros for Linux? What are they used for? How do they differ from each other?
41. What is the "root" in Linux? Why is it important?
42. If I run `rm -rf /`, why is that the most famous "horror story" in Linux history, and how does the Kernel permissions system (User vs. Root) try to prevent a beginner from doing it by accident?
43. What is the danger in giving files or programs root permissions?
44. What are command flags? What are the most common flags? What do they do?

</details>

### Links

<details>
<summary><strong>Curated reading, grouped by topic (click to expand)</strong></summary>

**History of Virtualization**
- https://www.ibm.com/think/topics/virtualization
- https://learningnetwork.cisco.com/s/blogs/a0D3i000002SKQdEAO/a-brief-history-of-network-virtualization
- https://www.solarwinds.com/blog/virtualization-how-we-got-here-and-does-it-have-a-future

**Virtual Machines**
- https://www.geeksforgeeks.org/operating-systems/virtual-machines-in-operating-system/
- https://www.redhat.com/en/topics/virtualization/what-is-a-virtual-machine#vms-vs-containers
- https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-a-virtual-machine
- https://www.geeksforgeeks.org/linux-unix/difference-between-linux-and-windows/

**File Systems**
- https://www.digitalocean.com/community/tutorials/an-introduction-to-storage-terminology-and-concepts-in-linux
- https://www.geeksforgeeks.org/operating-systems/file-systems-in-operating-system/

**Operating Systems and Virtual Machines' Components**
- https://www.geeksforgeeks.org/operating-systems/introduction-of-operating-system-set-1/
- https://www.geeksforgeeks.org/operating-systems/types-of-operating-systems/
- https://www.geeksforgeeks.org/operating-systems/kernel-in-operating-system/
- https://www.geeksforgeeks.org/operating-systems/introduction-of-system-call/
- https://www.geeksforgeeks.org/operating-systems/what-happens-when-we-turn-on-computer/

**CNCF**
- https://blog.abhimanyu-saharan.com/posts/a-decade-of-cloud-native-the-cncf-s-10-year-journey
- https://kodekloud.com/blog/what-is-the-cloud-native-computing-foundation/

**Common Linux Commands**
- https://linux-commands.labex.io/
- https://www.geeksforgeeks.org/linux-unix/linux-commands-cheat-sheet/
- https://medium.com/@prateek.malhotra004/linux-command-cheat-sheet-100-essential-commands-for-system-administration-and-development-6ee91049d71a
- https://www.digitalocean.com/community/tutorials/linux-commands

</details>
