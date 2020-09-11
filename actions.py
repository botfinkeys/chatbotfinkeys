# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType


class ActionComptePersonnel(Action):

     def name(self) -> Text:
         return "action_compte_personnel"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="tu dois entrer ton mot de passe")

         return []

      
    
#class ActionRepliParDéfaut(Action):

 #    def name(self) -> Text:
  #       return "action_default_fallback"

   #  def run(self, dispatcher: CollectingDispatcher,
    #         tracker: Tracker,
     #        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

      #   dispatcher.utter_message(text="Désolé, je n'ai pas compris, veuillez reformuler!")

       #  return []
