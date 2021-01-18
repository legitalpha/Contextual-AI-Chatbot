from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import random
import csv
import sys

class ActionFacilitySearch(Action):

    def name(self) -> Text:
        return "action_facility_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        facility = tracker.get_slot("facility_type")
        location = tracker.get_slot("location").capitalize()

        csv_file = csv.reader(open("C:\\Contextual AI Assistant\\hospital.csv", "r"), delimiter=",")
        address = []
        for row in csv_file:
            if location == row[1]:
                address.append(row[5])
        k = len(address)-1
        address = address[random.randint(0, k)]
        dispatcher.utter_message("Here is the address of the {}:{}".format(facility, address))
        return [SlotSet("address", address)]

# class FacilityForm(FormAction):
#
#     def name(self) -> Text:
#         return "facility_form"
#
#     @staticmethod
#     def required_slots(tracker: Tracker) -> List[Text]:
#         return ["facility_type", "location"]
#
#     def slot_mappings(self) -> Dict[Text, Any]:
#         return {"facility_type": self.from_entity(entity="facility_type", intent=["inform", "search_provider"]),
#                 "location": self.from_entity(entity="location", intent=["inform", "search_provider"])}
#
#     def submit(self, dispatcher: CollectingDispatcher,
#                tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
#
#         location = tracker.get_slot('location')
#         facility_type = tracker.get_slot('facility_type')
#
#         results = _find_facilities(location, facility_type)
#         button_name = _resolve_name(FACILITY_TYPES, facility_type)
#         if len(results) == 0:
#             dispatcher.utter_message("Sorry, we could not find a {} in {}.".format(button_name, location.title()))
#             return []
#         buttons = []
#         for r in results[:3]:
#             if facility_type == FACILITY_TYPES["hospital"]["resource"]:
#                 facility_id = r.get("provider_id")
#                 name = r["hospital_name"]
#             elif facility_type == FACILITY_TYPES["nursing_home"]["resource"]:
#                 facility_id = r["federal_provider_number"]
#                 name = r["provider_name"]
#             else:
#                 facility_id = r["provider_number"]
#                 name = r["provider_name"]
#
#             payload = "/inform{\"facility_id\":\"" + facility_id + "\"}"
#             buttons.append({"title": "{}".format(name.title()), "payload": payload})
#         if len(buttons) == 1:
#            message = "Here is a {} near you:".format(button_name)
#         else:
#             if button_name == "home health agency":
#                 button_name = "home health agencie"
#             message = "Here are {} {}s near you".format(len(buttons), button_name)
#         dispatcher.utter_button_message(message, buttons)
#         return []