## imma ablauf path
* greet
  - utter_greet
* provide_topic{"imma_information":"Ablauf", "topic":"Immatrikulation"}
  - utter_imma_ablauf
* thanks
  - utter_goodbye

## imma no information ablauf path
* greet
  - utter_greet
* provide_topic{"topic":"Immatrikulation"}
  - utter_ask_imma_information
* inform_imma{"imma_information":"Ablauf"}
  - utter_imma_ablauf
* thanks
  - utter_goodbye

## ptb richtlinien path
* greet
  - utter_greet
* provide_topic{"ptb_information":"Richtlinien", "topic":"PTB"}
  - utter_ptb_richtlinien
* thanks
  - utter_goodbye

## ptb no information richtlinien path
* greet
  - utter_greet
* provide_topic{"topic":"PTB"}
  - utter_ask_ptb_information
* inform_ptb{"ptb_information":"Richtlinien"}
  - utter_ptb_richtlinien
* thanks
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

