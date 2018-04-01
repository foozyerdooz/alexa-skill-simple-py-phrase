# alexa-skill-simple-py-phrase

This project aims to contain everything required to implement a simple Amazon Alexa skill
using Alexa Skills Developer Kit to generate the interaction model and an AWS python Lambda function to implement the endpoint logic.

*NOTE: You do not need to own an Echo Dot device, or equivalent, to develop for Alexa: AWS supplies a web based Alexa simulator that you can use to test your solution on.*

An objective of this project was to create a clean boilerplate python function that can be a template for more complex interactions. 

## Getting started for the completely uninitiated

For anyone starting off, you will need an Alexa Skills kit Developer account https://developer.amazon.com/alexa 
*(ProTip: use the same email address for your alexa developer account as you used for registering your Echo dot device)*

You will also need a standard AWS account https://console.aws.amazon.com to be able to create the Lambda function that your Alexa skill uses for a brain...

These are seperate accounts - not linked. Later in the process, you will simply link your Lambda code to your Alexa skill, setting up a two way trust using the AWS arn's of each.

The final puzzle piece is to use your newly developed skill with your Amazon Echo Dot, or equivalent - that magic is done from your phone that controls your Dot. Within the Skills section of the app, there is a 'Developer' section. You should find all of your skills that you are working on (from your Alexa skills developer account) listed here.

## Alexa Skills, Invocations, Intents and Slots

Go ahead - Open up the Alexa Skills developer kit. 

An Alexa **Skill** is the container for your application. Within it you configure Alexa to start your skill by configuring the **Invocation** name: 

e.g. "Alexa, ask Jeeves about fish" - where 'ask Jeeves' is the invocation and 'fish' is data that gets passed to your Lambda function for it to handle. Similarly, you could have said "Alexa, ask Jeeves" without anything else - you would need to configure Alexa to deal with that too.

An *Intent* is where you'll spend most of your time configuring what Alexa will listen for and asking for. Here, we define *utterances* - alternative spoken phrases that may or may not contain data words (e.g. 'fish') that all end up invoking the same *handler* within your connected Lambda function.

e.g. "I'd like to know about *fish*", "Tell me about *snails*", "What's the thing with *dogs*". All of these utterances, if tied to the same **Intent**, would end up being processed by the same handler in Lambda, with only the data that gets passed to Lambda changing ('fish', or 'snails', or 'dogs').

For now, we are starting simple to illustrate the moving parts: A simple invocation with a hard-coded response.

*Note: Everything done below results in the JSON model, included in the is project (**SimplePhrase.json**). You can manually configure the model using the console(below), 
or just drag and drop a pre-baked JSON file model into the **JSON Editor** in the console.*

### Alexa Skills Console Instructions
1. Create a new Skill - 'SimplePhrase'
2. Choose **Custom** model, and click on the *Create Skill* button.
3. Now you will find yourself in the Skills developer console. Click on **Invocation** on the left panel.
4. Type *quote engine* in the Skill Invocation name. 
5. Move on to the **Intents**. The 3 existing built-in intents are there so that Alexa can respond to Cancel, Help and Stop phrases. It isn't necessary to do anything with these built-in intents as this is a simple example. However, as you do more complex interaction logic with Alexa, giving users an exit path and help instructions is important.
6. **Add** a new Intent. Select **Create custom intent**. Call it *GetRandomQuote*.
7. Add a new **Sample Utterance** - *'Hit me with a quote'*. 
8. Add another one *'quote me up'*
9. Add a final one *'what's today's quote'*
10. We are not using **slots** in this example, as there is no data or parameters to be passed into the Lambda function.
11. **Save** the model.
12. **Build** the model.
13. Compare the JSON from the **JSON Editor** with the contens of the file in this project *SimplePhrase.json*. It should match if you have followed the instructions

### Lambda Function

The contents of the *GetRandomQuote.py* file need to be pasted into a new python AWS Lambda function in your AWS account.
Use the AWS Lambda console.

There is a specific order in which things should be done to link lambda to yout Alexa skill:

1. Create your Lambda function un US-East-1 Region - that is one of the few regions that supports Alexa skills triggers
2. Add an Alexa skills trigger to your Lambda function. Add your skill ID from the skill console to the lambda trigger on the AWS lambda console
3. Add the Lambda function ARN to the Skill endpoint *Default Region* on the skills console
4. Build your model again - and everything shouyld be good to be tested


