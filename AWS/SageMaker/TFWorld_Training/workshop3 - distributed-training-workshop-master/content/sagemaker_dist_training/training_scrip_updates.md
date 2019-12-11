---
title: "Updates required to run on SageMaker"
date: 2019-10-28T13:42:13-07:00
weight: 2
---

There are few minor changes required to run a training script on Amazon Sagemaker


##### SageMaker hyperparameters
* SageMaker passes hyperparameters to the training scripts as commandline arguments. Your script must be able to parse these arguments.

##### SageMaker environment variables
* SageMaker makes several environment variables available inside the container that a training script can take advantage of for finding location of the training dataset, number of GPU in the instance, dataset channels and others. A full list of environment variables an be found on the [SageMaker container GitHub repository](https://github.com/aws/sagemaker-containers#important-environment-variables)

```
parser = argparse.ArgumentParser()

# Hyper-parameters
parser.add_argument('--epochs',        type=int,   default=15)
parser.add_argument('--learning-rate', type=float, default=0.001)
parser.add_argument('--batch-size',    type=int,   default=256)
parser.add_argument('--weight-decay',  type=float, default=2e-4)
parser.add_argument('--momentum',      type=float, default='0.9')
parser.add_argument('--optimizer',     type=str,   default='adam')

# SageMaker parameters
parser.add_argument('--model_dir',        type=str)
parser.add_argument('--model_output_dir', type=str,   default=os.environ['SM_MODEL_DIR'])
parser.add_argument('--output_data_dir',  type=str,   default=os.environ['SM_OUTPUT_DATA_DIR'])

# Data directories and other options
parser.add_argument('--gpu-count',        type=int,   default=os.environ['SM_NUM_GPUS'])
parser.add_argument('--train',            type=str,   default=os.environ['SM_CHANNEL_TRAIN'])
parser.add_argument('--validation',       type=str,   default=os.environ['SM_CHANNEL_VALIDATION'])
parser.add_argument('--eval',             type=str,   default=os.environ['SM_CHANNEL_EVAL'])

args = parser.parse_args()
```

##### (Optional) TensorBoard callback for real-time monitoring of training
* Using a keras callback we can upload tensorboard files to Amazon S3 so that we can monitor progress in real-time.
tensorboard already comes installed on the SageMaker JupyterLab instance, and has support for reading event files from Amazon S3.

`tensorboard --logdir s3://{bucket_name}/tensorboard_logs/`

```
class Sync2S3(tf.keras.callbacks.Callback):
    def __init__(self, logdir, s3logdir):
        super(Sync2S3, self).__init__()
        self.logdir = logdir
        self.s3logdir = s3logdir

    def on_epoch_end(self, batch, logs={}):
        os.system('aws s3 sync '+self.logdir+' '+self.s3logdir)
        # ' >/dev/null 2>&1'
```
