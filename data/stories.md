## search corona cases
* greet
	- utter_greet
* search_provider{"location":"Delhi"}
	- action_cases_search
* thanks
	- utter_goodbye

## search total cases
* greet
	- utter_greet
* total_search
	- action_cases_search_total
* thanks
	- utter_goodbye

## search corona cases ask location
* greet
	- utter_greet
* tell_me
	- utter_ask
* search_provider{"location":"Delhi"}
	- action_cases_search
* thanks
	- utter_goodbye

## search corona cases many times
* greet
	- utter_greet
* tell_me
	- utter_ask
* search_provider{"location":"Delhi"}
	- action_cases_search
* search_provider{"location":"Delhi"}
	- action_cases_search
* search_provider{"location":"Delhi"}
	- action_cases_search
* search_provider{"location":"Delhi"}
	- action_cases_search
* search_provider{"location":"Delhi"}
	- action_cases_search
* search_provider{"location":"Delhi"}
	- action_cases_search
* search_provider{"location":"Delhi"}
	- action_cases_search
* search_provider{"location":"Delhi"}
	- action_cases_search	
* thanks
	- utter_goodbye

## search corona cases in country
* greet
	- utter_greet
* country_search{"country":"United States of America"}
	- action_cases_search_country
* thanks
	- utter_goodbye

## search corona cases ask country
* greet
	- utter_greet
* tell_me
	- utter_ask
* country_search{"country":"United States of America"}
	- action_cases_search_country
* thanks
	- utter_goodbye

## search corona cases many times country + location
* greet
	- utter_greet
* tell_me
	- utter_ask
* search_provider{"location":"Delhi"}
	- action_cases_search
* country_search{"country":"United States of America"}
	- action_cases_search_country
* search_provider{"location":"Delhi"}
	- action_cases_search
* country_search{"country":"United States of America"}
	- action_cases_search_country
* search_provider{"location":"Delhi"}
	- action_cases_search
* search_provider{"location":"Delhi"}
	- action_cases_search
* country_search{"country":"United States of America"}
	- action_cases_search_country
* search_provider{"location":"Delhi"}
	- action_cases_search	
* thanks
	- utter_goodbye

## search corona cases in city
* greet
	- utter_greet
* city_search{"city'":"Mumbai"}
	- action_cases_search_city
* thanks
	- utter_goodbye

## search corona cases ask city
* greet
	- utter_greet
* tell_me
	- utter_ask
* city_search{"city":"Mumbai"}
	- action_cases_search_city
* thanks
	- utter_goodbye

## search corona cases many times city + location
* greet
	- utter_greet
* tell_me
	- utter_ask
* search_provider{"location":"Delhi"}
	- action_cases_search
* city_search{"city":"Mumbai"}
	- action_cases_search_city
* search_provider{"location":"Delhi"}
	- action_cases_search
* city_search{"city":"Mumbai"}
	- action_cases_search_city
* search_provider{"location":"Delhi"}
	- action_cases_search
* search_provider{"location":"Delhi"}
	- action_cases_search
* city_search{"city":"Mumbai"}
	- action_cases_search_city
* search_provider{"location":"Delhi"}
	- action_cases_search	
* thanks
	- utter_goodbye

## search corona cases many times city + location + country + total
* greet
	- utter_greet
* tell_me
	- utter_ask
* search_provider{"location":"Delhi"}
	- action_cases_search
* city_search{"city":"Mumbai"}
	- action_cases_search_city
* search_provider{"location":"Delhi"}
	- action_cases_search
* country_search{"country":"United States of America"}
	- action_cases_search_country
* total_search
	- action_cases_search_total
* search_provider{"location":"Delhi"}
	- action_cases_search
* search_provider{"location":"Delhi"}
	- action_cases_search
* country_search{"country":"United States of America"}
	- action_cases_search_country
* city_search{"city":"Mumbai"}
	- action_cases_search_city
* total_search
	- action_cases_search_total
* search_provider{"location":"Delhi"}
	- action_cases_search
* search_provider{"location":"Delhi"}
	- action_cases_search
* search_provider{"location":"Delhi"}
	- action_cases_search
* country_search{"country":"United States of America"}
	- action_cases_search_country
* search_provider{"location":"Delhi"}
	- action_cases_search
* city_search{"city":"Mumbai"}
	- action_cases_search_city
* search_provider{"location":"Delhi"}
	- action_cases_search
* total_search
	- action_cases_search_total
* search_provider{"location":"Delhi"}
	- action_cases_search
* country_search{"country":"United States of America"}
	- action_cases_search_country
* search_provider{"location":"Delhi"}
	- action_cases_search
* city_search{"city":"Mumbai"}
	- action_cases_search_city
* search_provider{"location":"Delhi"}
	- action_cases_search
* total_search
	- action_cases_search_total
* search_provider{"location":"Delhi"}
	- action_cases_search
* country_search{"country":"United States of America"}
	- action_cases_search_country
* search_provider{"location":"Delhi"}
	- action_cases_search
* city_search{"city":"Mumbai"}
	- action_cases_search_city
* search_provider{"location":"Delhi"}
	- action_cases_search
* search_provider{"location":"Delhi"}
	- action_cases_search	
* total_search
	- action_cases_search_total
* search_provider{"location":"Delhi"}
	- action_cases_search
* country_search{"country":"United States of America"}
	- action_cases_search_country
* thanks
	- utter_goodbye

## search corona cases many times city + location + country + total (Direct)
* search_provider{"location":"Delhi"}
	- action_cases_search
* city_search{"city":"Mumbai"}
	- action_cases_search_city
* search_provider{"location":"Delhi"}
	- action_cases_search
* country_search{"country":"United States of America"}
	- action_cases_search_country
* total_search
	- action_cases_search_total
* search_provider{"location":"Delhi"}
	- action_cases_search
* search_provider{"location":"Delhi"}
	- action_cases_search
* country_search{"country":"United States of America"}
	- action_cases_search_country
* city_search{"city":"Mumbai"}
	- action_cases_search_city
* total_search
	- action_cases_search_total
* search_provider{"location":"Delhi"}
	- action_cases_search
* search_provider{"location":"Delhi"}
	- action_cases_search
* search_provider{"location":"Delhi"}
	- action_cases_search
* country_search{"country":"United States of America"}
	- action_cases_search_country
* search_provider{"location":"Delhi"}
	- action_cases_search

## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## Story from conversation with affe4423dbdf4a62ace01cbb04ea8720 on June 26th 2020

* search_provider{"PERSON":"madhya pradesh","location":"madhya pradesh"}
    - slot{"location":"madhya pradesh"}
    - action_cases_search
* search_provider{"GPE":"punjab","location":"punjab"}
    - slot{"location":"punjab"}
    - action_cases_search
* search_provider{"location":"assam"}
    - slot{"location":"assam"}
    - action_cases_search
* search_provider{"GPE":"pradesh"}
    - action_cases_search
* search_provider{"PERSON":"uttar pradesh","location":"uttar pradesh"}
    - slot{"location":"uttar pradesh"}
    - action_cases_search
* country_search{"GPE":"russia","country":"russia"}
    - slot{"country":"russia"}
    - action_cases_search_country
* country_search{"GPE":"china","country":"china"}
    - slot{"country":"china"}
    - action_cases_search_country
* country_search{"GPE":"Russia","country":"Russia"}
    - slot{"country":"Russia"}
    - action_cases_search_country
* country_search{"GPE":"russia","country":"russia"}
    - slot{"country":"russia"}
    - action_cases_search_country
* country_search{"GPE":"thailand","country":"thailand"}
    - slot{"country":"thailand"}
    - action_cases_search_country
* country_search{"GPE":"singapore","country":"singapore"}
    - slot{"country":"singapore"}
    - action_cases_search_country
* country_search{"GPE":"russia","country":"russia"}
    - slot{"country":"russia"}
    - action_cases_search_country
* country_search{"GPE":"moscow"}
    - action_cases_search_country
* country_search{"GPE":"Moscow"}
    - action_cases_search_country
* country_search{"GPE":"canada","country":"canada"}
    - slot{"country":"canada"}
    - action_cases_search_country
* country_search{"GPE":"iceland","country":"iceland"}
    - slot{"country":"iceland"}
    - action_cases_search_country
* country_search{"GPE":"ghana","country":"ghana"}
    - slot{"country":"ghana"}
    - action_cases_search_country
* country_search{"GPE":"greece","country":"greece"}
    - slot{"country":"greece"}
    - action_cases_search_country
* country_search{"GPE":"italy","country":"italy"}
    - slot{"country":"italy"}
    - action_cases_search_country
* country_search{"GPE":"spain","country":"spain"}
    - slot{"country":"spain"}
    - action_cases_search_country
* country_search{"GPE":"russia","country":"russia"}
    - slot{"country":"russia"}
    - action_cases_search_country
