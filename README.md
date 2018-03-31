# alexa-skill-simple-py-phrase
This project aims to contain everything required to implement a simple Amazon Alexa skill
using Alexa Skills Developer Kit to generate the interaction model and an AWS python Lambda function to implement the endpoint logic.

*NOTE: You do not need to own an Echo Dot device, or equivalent, to develop for Alexa: AWS supplies a web based Alexa simulator that you can use to test your solution on.*

## Getting started for the completely uninitiated
For anyone starting off, you will need an Alexa Skills kit Developer account https://developer.amazon.com/alexa 

*(ProTip: use the same email address for your alexa developer account as you used for registering your Echo dot device)*

You will also need a standard AWS account https://console.aws.amazon.com to be able to create the Lambda function that your Alexa skill uses for a brain...

These are seperate accounts - not linked. Later in the process, you will simply link your Lambda code to your Alexa skill, setting up a two way trust using the AWS arn's of each.

The final puzzle piece is to use your newly developed skill with your Amazon Echo Dot, or equivalent - that magic is done from your phone that controls your Dot. Within the Skills section of the app, there is a 'Developer' section. You should find all of your skills that you are working on (from your Alexa skills developer account) listed here.



