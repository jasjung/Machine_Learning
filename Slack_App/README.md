# Slack App 

- https://api.slack.com/tutorials

## Sending slack message from python 

- https://github.com/slackapi/python-slackclient
- [Build a Slack app in less than 10 minutes!](https://github.com/slackapi/python-slackclient/tree/master/tutorial)
- Message Formating: 
  - https://api.slack.com/docs/message-formatting
  - https://api.slack.com/docs/messages/builder?msg=%7B%22text%22%3A%22I%20am%20a%20test%20message%20http%3A%2F%2Fslack.com%22%2C%22attachments%22%3A%5B%7B%22text%22%3A%22And%20here’s%20an%20attachment!%22%7D%5D%7D

```sh 
pip3 install slackclient
```

### Process 

1. https://api.slack.com/apps/ -> create your app 
2. Add features and functionality -> `Incoming Webhooks`

You can simply send a message by running something like below: 

```sh 
curl -X POST -H 'Content-type: application/json' --data '{"text":"Hello, World!"}' https://hooks.slack.com/services/<your_url>
```