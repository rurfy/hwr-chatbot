# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from rasa_sdk import Action
from rasa_sdk.events import UserUtteranceReverted

class ActionGreetUser(Action):
"""Greets the User on StartUp"""

def name(self):
    return "action_greet"

def run(self, dispatcher, tracker, domain):
    dispatcher.utter_template("utter_greet", tracker)
    return [UserUtteranceReverted()]
