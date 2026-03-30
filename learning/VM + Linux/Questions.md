Questions that you should know the answer to at the end of the study block:
1. What was before virtualization?
2. What problems did virtualization solve and how?
3. What is an Operating system?
4. What is a kernel?
5. What is a hypervisor?
6. What is the shell?
7. What are the components of an operating system? Of a virtual machine? How do they interact with each other?
8. Explain the role of the Kernel as the "intermediary." If an application wants to write data to a hard drive, why can’t it just talk to the hardware directly?
9. Describe the step-by-step process that occurs when a user-space application executes a System Call. What is "Context Switching," and why is it necessary for system security?
10. Walk us through what happens the moment you press the power button on a computer. What is the hand-off process between the BIOS/UEFI and the OS Kernel?
11. Compare and contrast Bare Metal and Hosted hypervisors. In what scenario would each be preferred over the other?
12. How does a Virtual Machine "believe" it has its own CPU and RAM when, in reality, it is sharing physical resources with 20 other machines?
13. List the essential components of a VM. Which of these is responsible for making a VM "portable" across different physical servers?
14. In Linux, "everything is a file." Explain what this means in the context of hardware devices (like a mouse or a hard drive) located in the ``/dev`` directory.
15. How would you find every line containing the word "ERROR" in a log file named ``server.log``?
16. Explain the difference between ``chmod`` and ``chown``.
17. What is the difference between ``cp`` and ``mv``?
18. How is a directory different from a regular file?
19. What is the difference between using ``\`` and ``/`` when specifying file paths?
20. How do you check which processes are consuming the most CPU in real-time?
21. If a file has permissions 755, what can the owner do that the "world" (others) cannot?
22. Explain the different levels of permissions and how they come into play
23. What are CGroups?
24. Before virtualization, what was "Server Sprawl," and how did it affect the physical design and cost of data centers?
25. What is CNCF?
26. What is the mission of the CNCF (Cloud Native Computing Foundation)?
27. What are famous projects of CNCF?
28. What is the Linux Foundations?
29. How is the Linux Foundation related to CNCF?
30. What is Open Source? Why is it important?
31. A developer tells you their VM is running slow. Using Linux commands, walk us through how you would diagnose whether the bottleneck is CPU, Memory, or Disk I/O.
32. We need to move a legacy application from an old physical server to a virtualized environment. What are the biggest risks, and how does the 'Hypervisor' layer help make this possible?
33. How does the Kernel prevent a standard user from accidentally deleting critical system files?
34. What is the difference between a Monolithic Kernel and a Microkernel?
35. What is the difference between 'Block Storage' and a 'File System'?
36. What is a cache? What is caching?
37. What is ephemeral storage?
38. At what exact point in the boot process does the computer stop being 'generic hardware' and start being 'Linux'?
39. Compare and contrast Windows vs Linux. Give use cases for each
40. What are Distributions/Distros? what are the most common distros for Linux? What are they used for? How do they differ from each other?
41. What is the "root" in Linux? why is it important?
42. If I run rm -rf /, why is that the most famous 'horror story' in Linux history, and how does the Kernel permissions system (User vs. Root) try to prevent a beginner from doing it by accident?
43. What is the danger in giving files or programs root permissions?
44. What are command flags? what are the most common flags? what do they do?
