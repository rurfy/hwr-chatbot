# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from rasa_sdk import Action

class ActionGreetUser(Action):

    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher, tracker, domain):

        dispatcher.utter_template("utter_greet", tracker)

        return []
