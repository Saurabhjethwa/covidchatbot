import requests
import json
from fuzzywuzzy import fuzz
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionCasesSearch(Action):

     def name(self) -> Text:
         return "action_cases_search"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
         loc_name = tracker.get_slot('location')
         loc_name = loc_name.capitalize()
           
         result = requests.get("https://covid-19india-api.herokuapp.com/v2.0/helpline_numbers")      
         state = result.text
         x1 = json.loads(state)
         x1 = x1[1]
         x1 = x1['contact_details']
         for dict1 in x1:
            if dict1['state_or_UT']== loc_name:
                num = dict1['helpline_number']
        

         result = requests.get("https://covid-19india-api.herokuapp.com/v2.0/state_data")
         state = result.text
         x = json.loads(state)
         x= x[1]
         for dict in x['state_data']:
             if fuzz.ratio(dict['state'],loc_name) >= 75:
                 abc = dict
                 dispatcher.utter_message("Corona Virus Cases in {} : \nActive Cases: {} \nActive Rate: {} \nConfirmed Cases: {} \nDeath Rate: {} \nDeaths : {}  \
                                            \nRecovered: {} \nRecovered Rate : {} \nHelpline number : {} \n".format(dict['state'],dict['active'],dict['active_rate'],dict['confirmed'],dict['death_rate']
                                            ,dict['deaths'],dict['recovered'],dict['recovered_rate'],num))
                 
         #dispatcher.utter_message("Enter correct location!")
         return []
         
         

class ActionCasesSearchTotal(Action):

     def name(self) -> Text:
         return "action_cases_search_total"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
         #loc_name = tracker.get_slot('total')
         result = requests.get("https://api.rootnet.in/covid19-in/stats/latest")
         state = result.text
         x = json.loads(state)
         x = x['data']
         x = x['summary']

         dispatcher.utter_message("Corona Virus Cases in India : \nTotal Cases: {} \nDischarged: {} \nDeaths: {} \n".format(x['total'],x['discharged'],x['deaths']))
                 
         return []


class ActionCasesSearchCountry(Action):

     def name(self) -> Text:
         return "action_cases_search_country"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
         loc_name = tracker.get_slot('country')
         loc_name = loc_name.capitalize()

         result = requests.get("https://api.covid19api.com/summary")
         state = result.text
         x = json.loads(state)
         x = x['Countries']

         for dict in x:
             if fuzz.ratio(dict['Country'],loc_name) >= 80:
                 dispatcher.utter_message("Corona Virus Cases in {} : \nNew Confirmed Cases: {} \nTotal Confirmed Cases: {} \nNew Death Cases: {} \
                                               \nTotal Death Cases: {} \nNew Recovered Cases : {}  \
                                            \nTotal Recovered Cases: {} \n".format(dict['Country'],dict['NewConfirmed'],dict['TotalConfirmed'],dict['NewDeaths'],dict['TotalDeaths']
                                            ,dict['NewRecovered'],dict['TotalRecovered']))
                 
         #dispatcher.utter_message("Enter correct location!")
         return []


class ActionCasesSearchCity(Action):

     def name(self) -> Text:
         return "action_cases_search_city"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
         dis_name = tracker.get_slot('city')
         dis_name = dis_name.capitalize()

         result = requests.get("https://api.covid19india.org/v3/min/data.min.json")
         state = result.text
         x = json.loads(state)
         
         for abc in x:
            if abc not in ['LD','TT','UN']:
                l=[]
                l = list(x[abc]['districts'].keys())
                for i in l:
                    if fuzz.ratio(i,dis_name) >= 90:
                        dic = {'city': 'Dont Know','confirmed': 0, 'deceased': 0, 'recovered': 0}
                        dname = x[abc].get('districts')
                        dname = dname[dis_name]['total']
                        dic.update(dname)
                        dic['city'] = i
                        dispatcher.utter_message("Corona Virus Cases in {} : \nConfirmed Cases: {} \nDesceased Cases: {} \nRecovered Cases: {} \
                                              \n".format(dic['city'],dic['confirmed'],dic['deceased'],dic['recovered']))
                    else:
                        pass

         #dispatcher.utter_message("Enter correct location!")
         return []

