# -*- coding: utf-8 -*-
from __future__ import print_function
import math
import string
import random


STATE_START = "Start"
STATE = STATE_START

# This is the welcome message for when a user starts the skill without a specific intent
WELCOME_MESSAGE = "Welcome to the simple Quote Engine!  You can ask me for a random quote, by saying quote me up, or hit me with a quote, or whats todays quote?. What would you like to do?"
#This is the message a user will hear when they try to cancel or stop the skill"
#or when they finish a quiz.
EXIT_SKILL_MESSAGE = "Thank you for using Quote Engine!  Let's play again soon!"

#This is the message a user will hear when they ask Alexa for help in your skill.
HELP_MESSAGE = ("I know lots of random quotes. Simply say gimme a quote, or, hit me with a quote, or, quote me up, or, what's today's quote. Let's go!")

# some SSML helper tags
SAYAS_INTERJECT = "<say-as interpret-as='interjection'>"
SAYAS_SPELLOUT = "<say-as interpret-as='spell-out'>"
SAYAS = "</say-as>"
BREAKSTRONG = "<break strength='strong'/>"

# --------------- entry point -----------------

def lambda_handler(event, context):
    """ App entry point  """
    if event['request']['type'] == "LaunchRequest":
        return on_launch()
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'])

# --------------- response handlers -----------------

def on_intent(request, session):
    """ Called on receipt of an Intent  """

    intent = request['intent']
    intent_name = request['intent']['name']

    #print("on_intent " +intent_name)
    get_state(session)

    if 'dialogState' in request:
        #delegate to Alexa until dialog sequence is complete
        if request['dialogState'] == "STARTED" or request['dialogState'] == "IN_PROGRESS":
            return dialog_response("", False)

    # process the intents
    if intent_name == "GetRandomQuote":
        return do_random_quote(request)
    elif intent_name == "AMAZON.HelpIntent":
        return do_help()
    elif intent_name == "AMAZON.StopIntent":
        return do_stop()
    elif intent_name == "AMAZON.CancelIntent":
        return do_stop()

    else:
        print("invalid intent reply with help")
        return do_help()

def do_stop():
    """  stop the app """
    attributes = {"state":globals()['STATE']}
    return response(attributes, response_plain_text(EXIT_SKILL_MESSAGE, True))

def do_help():
    """ return a help response  """
    attributes="HELP"
    return response(attributes, response_plain_text(HELP_MESSAGE, False))

def on_launch():
    """compiles a SSML message that gets spoken when the skill first starts
    
    Returns:
        Response object -- SSML message to get spoken by Alexa
    """
    attributes="LAUNCH"
    speech_message = SAYAS_INTERJECT + "g'day" + SAYAS + BREAKSTRONG + WELCOME_MESSAGE
    return response( attributes,response_ssml_text(speech_message, False))

def on_session_ended(request):
    """ called on session end  """

    if request['reason']:
        end_reason = request['reason']
        print("on_session_ended reason: " + end_reason)
    else:
        print("on_session_ended")

def get_state(session):
    """ get and set the current state  """

    global STATE

    if 'state' in session['attributes']:
        STATE = session['attributes']['state']
    else:
        STATE = STATE_START


#---------------------------- Random Quote --------------------------------
#
#--------------------------------------------------------------------------

def do_random_quote(request):
    """ get a random quote and send it back to Alexa  """
    attributes="Quote"
    speech_message="this is a test quote"
    return response( attributes,response_plain_text(speech_message, False))

# --------------- speech response handlers -----------------
#  for details of Json format see:
#  https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/alexa-skills-kit-interface-reference

def response_plain_text(output, endsession):
    """ create a simple json plain text response  """

    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'shouldEndSession': endsession
    }


def response_ssml_text(output, endsession):
    """ create a simple json plain text response  """

    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': "<speak>" +output +"</speak>"
        },
        'shouldEndSession': endsession
    }

def dialog_response(attributes, endsession):
    """  create a simple json response with card """

    return {
        'version': '1.0',
        'sessionAttributes': attributes,
        'response':{
            'directives': [
                {
                    'type': 'Dialog.Delegate'
                }
            ],
            'shouldEndSession': endsession
        }
    }

def response(attributes, speech_response):
    """ create a simple json response """

    return {
        'version': '1.0',
        'sessionAttributes': attributes,
        'response': speech_response
    }