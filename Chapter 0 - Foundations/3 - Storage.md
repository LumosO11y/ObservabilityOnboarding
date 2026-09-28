# Storage

## Overview

Every database and data system you'll meet later ends up writing its data somewhere: to a local disk, a network share, or an object store. This part covers the storage types and architectures underneath them, so that later parts can talk about volumes, object storage, and disks without explaining them first.

## Goals

- Understand what makes storage persistent or ephemeral, and how disks are measured.
- Understand the three storage types (block, file, and object) and which workloads each one fits.
- Understand the three storage architectures (DAS, NAS, and SAN) and what each one exposes to a server.
- Understand NFS and what changes when a file system lives across a network.
- Understand how storage stays durable when disks fail.

## Outcome

<details>
<summary><strong>Questions you should be able to answer by the end of this block (click to expand)</strong></summary>

**Storage Fundamentals**

1. What is the difference between volatile and persistent storage? What is ephemeral storage?
2. What is the difference between an HDD and an SSD, and how does it change the way software should read and write data?
3. What are IOPS, throughput, and latency? How can a disk score well on one of them and badly on another?
4. What is RAID? Compare two RAID levels of your choice: what does each one protect against, and what does it cost?

**Storage Types**

1. What is block storage? What is file storage? What is object storage?
2. What is the difference between block storage and a file system? Where does each one sit in the stack between an application and a physical disk?
3. How is data addressed in object storage? What can you do to a file that you can't do to an object?
4. For each of the three storage types, give one workload it fits well and one it fits badly, and explain why.

**Storage Architectures**

1. What is DAS? What is NAS? What is a SAN?
2. Which storage type does each of these architectures expose to the server that uses it?
3. Which protocols does a SAN typically run over, and which protocols does a NAS typically serve?
4. An application writes to a disk, and the network between it and its storage drops. What happens on DAS, on NAS, and on a SAN?
5. Pick one cloud provider and find its block, file, and object storage offerings. Which of the architectures above does each one resemble?

**NFS**

1. What is NFS? What does it mean to mount an NFS share, and how does a remote directory end up looking local?
2. How does NFS compare to SMB, and where would you run into each?
3. What is file locking? Why is it risky to have processes on different machines write to the same file over NFS?

**Durability**

1. What is the difference between durability and availability for storage?
2. What is replication? What is erasure coding? What does each one trade off to survive a failed disk or node?
3. What does it mean for an object store to be "S3-compatible", and why would a self-hosted system want to be?
4. Ask your mentor which solutions we use for block, file, and object storage. For the one behind our object storage, which part of it gives us an S3-compatible API?

</details>

### Links

<details>
<summary><strong>Curated reading, grouped by topic (click to expand)</strong></summary>

**Storage Fundamentals**

- <https://www.digitalocean.com/community/tutorials/an-introduction-to-storage-terminology-and-concepts-in-linux>
- <https://www.ibm.com/think/topics/iops>
- <https://en.wikipedia.org/wiki/Standard_RAID_levels>

**Storage Types**

- <https://www.redhat.com/en/topics/data-storage/file-block-object-storage>
- <https://aws.amazon.com/compare/the-difference-between-block-file-object-storage/>
- <https://www.ibm.com/think/topics/object-storage>

**Storage Architectures**

- <https://en.wikipedia.org/wiki/Direct-attached_storage>
- <https://en.wikipedia.org/wiki/Network-attached_storage>
- <https://en.wikipedia.org/wiki/Storage_area_network>
- <https://en.wikipedia.org/wiki/ISCSI>

**NFS**

- <https://en.wikipedia.org/wiki/Network_File_System>
- <https://man7.org/linux/man-pages/man5/nfs.5.html>
- <https://www.digitalocean.com/community/tutorials/how-to-set-up-an-nfs-mount-on-ubuntu-22-04>

**Durability**

- <https://en.wikipedia.org/wiki/Erasure_code>

<details>
<summary>Spoiler: open once you've answered Durability question 4</summary>

- <https://docs.ceph.com/en/latest/start/>
- <https://docs.ceph.com/en/latest/architecture/>

</details>

</details>
