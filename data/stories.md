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
