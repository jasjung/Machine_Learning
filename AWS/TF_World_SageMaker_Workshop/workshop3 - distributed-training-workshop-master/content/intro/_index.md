+++
title = "Introduction"
date = 2019-10-27T15:22:24-07:00
weight = 1
chapter = true
+++

# Introduction
In a typical machine learning development workflow, there are two main stages where you can get benefit from scaling out.

![parallel distributed](/images/intro/parallel_distributed.png)

1. Running large-scale parallel experiments: In this scenario our goal is to find the best model/hyperparameters/network architecture by exploring a space of possibilities.
1. Running distributed training of a single model: In this scenario our goal is to train a single model faster, by distributing its computation across nodes in a cluster.

### The focus of this workshop is distributed training of a single model
