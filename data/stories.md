<!-- ## greet story
* greet
  - utter_greet
> check_asked_question -->

## imma ablauf path

* provide_topic_imma{"imma_information":"Ablauf", "topic":"Immatrikulation"}
  - utter_imma_ablauf
* goodbye
  - utter_goodbye

## imma no information ablauf path

* provide_topic_imma{"topic":"Immatrikulation"}
  - utter_ask_imma_information
* inform_imma{"imma_information":"Ablauf"}
  - utter_imma_ablauf
<!-- * goodbye
  - utter_goodbye -->

## ptb richtlinien path
<!-- * greet
  - utter_greet -->

* provide_topic_ptb{"ptb_information":"Richtlinien", "topic":"PTB"}
  - utter_ptb_richtlinien
<!-- * goodbye
  - utter_goodbye -->

## ptb no information richtlinien path
<!-- * greet
  - utter_greet -->

* provide_topic_ptb{"topic":"PTB"}
  - utter_ask_ptb_information
* inform_ptb{"ptb_information":"Richtlinien"}
  - utter_ptb_richtlinien
<!-- * goodbye
  - utter_goodbye -->

## semesterticket erhalten path
* greet
  - utter_greet
* inform_semesterticket_erhalten{"semesterticket_information":"erhalten", "topic":"Semesterticket"}
  - utter_semesterticket_erhalten
* goodbye
  - utter_goodbye

## semesterticket no information erhalten path
* greet
  - utter_greet
* provide_topic_semesterticket{"topic":"Semesterticket"}
  - utter_ask_semesterticket_information
* inform_semesterticket_erhalten{"semesterticket_information":"erhalten"}
  - utter_semesterticket_erhalten
* goodbye
  - utter_goodbye 

## semesterticket aktualisierung path
* greet
  - utter_greet
* inform_semesterticket_aktualisierung{"topic":"Semesterticket", "semesterticket_information":"Aktualisierung"}
  - utter_semesterticket_aktualisierung
* goodbye
  - utter_goodbye

## semesterticket no information aktualisierung path
* greet
  - utter_greet
* provide_topic_semesterticket{"topic":"Semesterticket"}
  - utter_ask_semesterticket_information
* inform_semesterticket_aktualisierung{"semesterticket_information":"Aktualisierung"}
  - utter_semesterticket_aktualisierung
* goodbye
  - utter_goodbye

## semesterticket vbb path
* greet
  - utter_greet
* inform_semesterticket_vbb{"topic":"Semesterticket", "semesterticket_information":"VBB"}
  - utter_semesterticket_vbb
* goodbye
  - utter_goodbye

## semesterticket no information vbb path
* greet
  - utter_greet
* provide_topic_semesterticket{"topic":"Semesterticket"}
  - utter_ask_semesterticket_information
* inform_semesterticket_vbb{"semesterticket_information":"VBB"}
  - utter_semesterticket_vbb
* goodbye
  - utter_goodbye

## semesterticket fahrrad path
* greet
  - utter_greet
* inform_semesterticket_fahrrad{"topic":"Semesterticket", "semesterticket_information":"Fahrrad"}
  - utter_semesterticket_fahrrad
* goodbye
  - utter_goodbye

## semesterticket no information fahrrad path
* greet
  - utter_greet
* provide_topic_semesterticket{"topic":"Semesterticket"}
  - utter_ask_semesterticket_information
* inform_semesterticket_fahrrad{"semesterticket_information":"Fahrrad"}
  - utter_semesterticket_fahrrad
* goodbye
  - utter_goodbye

## semesterticket abc path
* greet
  - utter_greet
* inform_semesterticket_abc{"topic":"Semesterticket", "semesterticket_information":"ABC"}
  - utter_semesterticket_abc
* goodbye
  - utter_goodbye

## semesterticket no information abc path
* greet
  - utter_greet
* provide_topic_semesterticket{"topic":"Semesterticket"}
  - utter_ask_semesterticket_information
* inform_semesterticket_abc{"semesterticket_information":"ABC"}
  - utter_semesterticket_abc
* goodbye
  - utter_goodbye

## semesterticket brandenburg path
* greet
  - utter_greet
* inform_semesterticket_brandenburg{"topic":"Semesterticket","semesterticket_information":"Brandenburg"}
  - utter_semesterticket_brandenburg
* goodbye
  - utter_goodbye

## semesterticket no information brandenburg path
* greet
  - utter_greet
* provide_topic_semesterticket{"topic":"Semesterticket"}
  - utter_ask_semesterticket_information
* inform_semesterticket_brandenburg{"semesterticket_information":"Brandenburg"}
  - utter_semesterticket_brandenburg
* goodbye
  - utter_goodbye

## semesterticket ansprechpartner path
* greet
  - utter_greet
* inform_semesterticket_ansprechpartner{"semesterticket_information":"Ansprechpartner", "topic":"Semesterticket"}
  - utter_semesterticket_ansprechpartner
* goodbye
  - utter_goodbye

## semesterticket no information ansprechpartner path
* greet
  - utter_greet
* provide_topic_semesterticket{"topic":"Semesterticket"}
  - utter_ask_semesterticket_information
* inform_semesterticket_ansprechpartner{"semesterticket_information":"Ansprechpartner"}
  - utter_semesterticket_ansprechpartner
* goodbye
  - utter_goodbye

## semesterticket informationen path
* greet
  - utter_greet
* inform_semesterticket_info{"semesterticket_information":"Informationen", "topic":"Semesterticket"}
  - utter_semesterticket_info
* goodbye
  - utter_goodbye

## semesterticket no information informationen path
* greet
  - utter_greet
* provide_topic_semesterticket{"topic":"Semesterticket"}
  - utter_ask_semesterticket_information
* inform_semesterticket_info{"semesterticket_information":"Informationen"}
  - utter_semesterticket_info
* goodbye
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

