# System & Linux

## Overview

A large part of our work relies on and uses existing infrastructures of data and DevOps. At the base of all the architecture components we use, lie Virtual Machines.

## Goals

- Operating systems, the Kernel, and System calls
- Virtualization, hypervisors, and the components of a virtual machine
- Common Linux commands and permissions
- Processes, signals, cgroups, and namespaces
- Networking basics: ports, TCP/UDP, and DNS
- cron and the crontab syntax
- Linux, the Linux Foundation, and CNCF

## Exercise: The Linux Manipulation Exercise

**Environment**: No Linux machine handy? Do this exercise on [Killercoda](https://killercoda.com/) (free, browser-based Linux terminal, no install needed) or in WSL if you're on Windows. If neither works for you, ask your mentor for a VM.

**Goal**: Find "hidden" information about the computer using *only* the terminal.
**Scenario**: You have been given a mystery server. You need to identify its "DNA" (hardware), its "Health" (processes), and its "Security" (permissions).
**Instructions**: Note down the commands you used.

1. **The Version Check**: Find out exactly which version of the Linux Kernel is running.
2. **The Heartbeat**: View the CPU information. Is it an Intel, AMD, or ARM chip?
3. **The Long Way Home**: Navigate to the `/var/log` directory. List all files, but show the "long" version so you can see who owns the files.
4. **The Content Hunt**: Find the file named `syslog` or `messages`. Use a command to read only the last 20 lines of that file to see what the system is doing right now.
5. **Create a Secret**: Create a new folder in your home directory called `SecretProject`.
6. **Lock the Door**: Change the permissions so that only you (the owner) can read, write, and enter it, and no one else in the "world" can list or open what's inside.
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

1. What was before virtualization? What was "Server Sprawl," and how did it affect the physical design and cost of data centers?
2. What problems did virtualization solve and how?
3. What is an Operating system?
4. What is a kernel?
5. What is a hypervisor?
6. What is the shell?
7. What are the components of an operating system? How do they interact with each other?
8. Explain the role of the Kernel. If an application wants to write data to a hard drive, why can't it just talk to the hardware directly?
9. Describe the step-by-step process that occurs when a user-space application executes a System Call. What is "Context Switching," and why is it necessary for system security?
10. Walk us through what happens the moment you press the power button on a computer. What is the hand-off process between the BIOS/UEFI and the OS Kernel?
11. At what exact point in the boot process does the computer stop being "generic hardware" and start being "Linux"?
12. Compare and contrast Bare Metal and Hosted hypervisors. In what scenario would each be preferred over the other?
13. How does a Virtual Machine "believe" it has its own CPU and RAM when, in reality, it is sharing physical resources with 20 other machines?
14. List the essential components of a VM. Which of these is responsible for making a VM "portable" across different physical servers?
15. We need to move a legacy application from an old physical server to a virtualized environment. What are the biggest risks, and how does the "Hypervisor" layer help make this possible?
16. What is the difference between a Monolithic Kernel and a Microkernel?
17. In Linux, "everything is a file." Explain what this means in the context of hardware devices (like a mouse or a hard drive) located in the `/dev` directory.
18. How is a directory different from a regular file?
19. What is the difference between using `\` and `/` when specifying file paths?
20. What is the difference between "Block Storage" and a "File System"?
21. What is ephemeral storage?
22. What is a cache? What is caching?
23. What are command flags? What are the most common flags? What do they do?
24. How would you find every line containing the word "ERROR" in a log file named `server.log`?
25. What is the difference between `cp` and `mv`?
26. Explain the difference between `chmod` and `chown`.
27. Explain the different levels of permissions and how they come into play.
28. If a file has permissions 755, what can the owner do that the "world" (others) cannot?
29. What is the "root" in Linux? Why is it important?
30. What is the danger in giving files or programs root permissions?
31. How does the Kernel prevent a standard user from accidentally deleting critical system files?
32. If I run `rm -rf /`, why is that the most famous "horror story" in Linux history? What safeguards exist today against running it by accident, and what difference does it make whether you run it as a regular user or as root?
33. How do you check which processes are consuming the most CPU in real-time?
34. A developer tells you their VM is running slow. Using Linux commands, walk us through how you would diagnose whether the bottleneck is CPU, Memory, or Disk I/O.
35. What is a process signal? What is the difference between `SIGTERM` and `SIGKILL`, and why does it matter which one a process receives when it's asked to stop?
36. What are CGroups? What are Linux namespaces? What does each one control, and how are they different?
37. What is a port, and what does it mean for a process to "listen" on one? What is the difference between a server binding to `127.0.0.1` and binding to `0.0.0.0`?
38. What is the difference between TCP and UDP? Give a use case for each.
39. What is DNS? What happens between typing a hostname into a browser and the first HTTP request being sent?
40. From the terminal, how would you find which process is listening on a given port, and how would you send an HTTP request to it?
41. What is cron, and what is a crontab? Write a cron expression that runs a job every day at 3:30 AM, and explain what each of its 5 fields means.
42. Compare and contrast Windows vs Linux. Give use cases for each.
43. What are Distributions/Distros? What are the most common distros for Linux? What are they used for? How do they differ from each other?
44. What is Open Source? Why is it important?
45. What is the Linux Foundation?
46. What is the CNCF (Cloud Native Computing Foundation), and what is its mission?
47. What are famous projects of CNCF?
48. How is the Linux Foundation related to CNCF?

</details>

### Links

<details>
<summary><strong>Curated reading, grouped by topic (click to expand)</strong></summary>

**History of Virtualization**

- <https://www.ibm.com/think/topics/virtualization>
- <https://learningnetwork.cisco.com/s/blogs/a0D3i000002SKQdEAO/a-brief-history-of-network-virtualization>
- <https://www.solarwinds.com/blog/virtualization-how-we-got-here-and-does-it-have-a-future>

**Virtual Machines**

- <https://www.geeksforgeeks.org/operating-systems/virtual-machines-in-operating-system/>
- <https://www.redhat.com/en/topics/virtualization/what-is-a-virtual-machine#vms-vs-containers>
- <https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-a-virtual-machine>
- <https://www.geeksforgeeks.org/linux-unix/difference-between-linux-and-windows/>

**File Systems**

- <https://www.digitalocean.com/community/tutorials/an-introduction-to-storage-terminology-and-concepts-in-linux>
- <https://www.geeksforgeeks.org/operating-systems/file-systems-in-operating-system/>

**Operating Systems and Virtual Machines' Components**

- <https://www.geeksforgeeks.org/operating-systems/introduction-of-operating-system-set-1/>
- <https://www.geeksforgeeks.org/operating-systems/types-of-operating-systems/>
- <https://www.geeksforgeeks.org/operating-systems/kernel-in-operating-system/>
- <https://www.geeksforgeeks.org/operating-systems/introduction-of-system-call/>
- <https://www.geeksforgeeks.org/operating-systems/what-happens-when-we-turn-on-computer/>

**CNCF**

- <https://blog.abhimanyu-saharan.com/posts/a-decade-of-cloud-native-the-cncf-s-10-year-journey>
- <https://kodekloud.com/blog/what-is-the-cloud-native-computing-foundation/>

**Common Linux Commands**

- <https://linux-commands.labex.io/>
- <https://www.geeksforgeeks.org/linux-unix/linux-commands-cheat-sheet/>
- <https://medium.com/@prateek.malhotra004/linux-command-cheat-sheet-100-essential-commands-for-system-administration-and-development-6ee91049d71a>
- <https://www.digitalocean.com/community/tutorials/linux-commands>

**Processes, cgroups & Namespaces**

- <https://man7.org/linux/man-pages/man7/signal.7.html>
- <https://man7.org/linux/man-pages/man7/cgroups.7.html>
- <https://man7.org/linux/man-pages/man7/namespaces.7.html>

**Networking Basics**

- <https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/>
- <https://www.cloudflare.com/learning/dns/what-is-dns/>
- <https://man7.org/linux/man-pages/man8/ss.8.html>

**cron**

- <https://man7.org/linux/man-pages/man5/crontab.5.html>
- <https://crontab.guru/>

</details>
