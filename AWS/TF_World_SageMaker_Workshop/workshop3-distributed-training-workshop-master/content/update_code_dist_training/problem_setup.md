---
title: "Problem statement"
date: 2019-10-28T01:12:18-07:00
weight: 1
---

### Converting a single CPU/GPU training script to a multi-node/distributed compatible training script
**Frameworks:** This workshop currently uses TensorFlow 1.14, Keras and Horovod 0.18.

**Dataset:** The CIFAR-10 consists of 60,000 32x32 images belonging to 10 different classes (6,000 images per class).
<br>CIFAR-10 dataset includes:

* 40,000 images for training
* 10,000 images for validation
* 10,000 images for test

Here are the classes in the dataset, as well as 10 random images from each:
![cifar10](https://camo.githubusercontent.com/a426b9aca74c978ecc8b093dddc540f113591858/68747470733a2f2f6d616574333630382e6769746875622e696f2f6e7574732d6d6c2f5f696d616765732f636966617231302e706e67)

{{% notice info %}}
**Note:** Although the dataset is small and this is a simpler problem, all the steps we'll take can easily be applied to large datasets that don't fit in memory. Amazon SageMaker has native pipe-mode support to stream dataset directly from S3 to the training instances. With Amazon EKS, we'll setup an Amazon FSx for lustre file system that's accessible to every worker.
{{% /notice %}}
