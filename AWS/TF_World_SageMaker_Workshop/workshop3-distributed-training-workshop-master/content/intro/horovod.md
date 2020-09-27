---
title: "Distributed training approaches"
date: 2019-10-28T21:11:22-07:00
weight: 5
---
![approaches](/images/intro/approaches.png)

## Horovod
[(horovod.ai)](horovod.ai)

Horovod is based on the MPI concepts:
size, rank, local rank, allreduce, allgather, and broadcast.

* Library for distributed deep learning with support for multiple frameworks including TensorFlow
* Separates infrastructure from ML engineers
* Uses ring-allreduce and uses Message Passing Interface (MPI) popular in the HPC community
* Infrastructure services such as Amazon SageMaker and Amazon EKS provides container and MPI environment

![allreduce](/images/intro/forward_backward.png)

1. Forward pass on each device
1. Backward pass compute gradients
1. ”All reduce” (average and broadcast) gradients across devices
1. Update local variables with “all reduced” gradients

Horovod will run the same copy of the script on all hosts/servers/nodes/instances

![mpi](/images/intro/how_it_runs.png)

`horovodrun -np 16 -H server1:4,server2:4,server3:4,server4:4 python training_script.py`
