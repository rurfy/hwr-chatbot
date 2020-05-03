<!-- ## greet story
* greet
  - utter_greet
> check_asked_question -->

## imma ablauf path

* provide_topic_imma{"imma":"Ablauf", "topic":"Immatrikulation"}
  - utter_imma_ablauf
* goodbye
  - utter_goodbye

## imma no information ablauf path

* provide_topic_imma{"topic":"Immatrikulation"}
  - utter_ask_imma
* imma_ablauf{"imma":"Ablauf"}
  - utter_imma_ablauf
* goodbye
  - utter_goodbye

## imma ansprechpartner path

* provide_topic_imma{"imma":"Ansprechpartner", "topic":"Immatrikulation"}
  - utter_imma_ansprechpartner
* goodbye
  - utter_goodbye 

## imma no information ansprechpartner path

* provide_topic_imma{"topic":"Immatrikulation"}
  - utter_ask_imma
* imma_ansprechpartner{"imma":"Ansprechpartner"}
  - utter_imma_ansprechpartner
* goodbye
  - utter_goodbye

## imma bescheinigung path

* provide_topic_imma{"imma":"Bescheinigung", "topic":"Immatrikulation"}
  - utter_imma_bescheinigung
* goodbye
  - utter_goodbye 

## imma no information bescheinigung path

* provide_topic_imma{"topic":"Immatrikulation"}
  - utter_ask_imma
* imma_bescheinigung{"imma":"Bescheinigung"}
  - utter_imma_bescheinigung
* goodbye
  - utter_goodbye



## ptb richtlinien path
* greet
  - utter_greet
* provide_topic_ptb{"ptb":"Richtlinien", "topic":"PTB"}
  - utter_ptb_richtlinien
* goodbye
  - utter_goodbye

## ptb no information richtlinien path
* greet
  - utter_greet
* provide_topic_ptb{"topic":"PTB"}
  - utter_ask_ptb
* ptb_richtlinien{"ptb":"Richtlinien"}
  - utter_ptb_richtlinien
* goodbye
  - utter_goodbye

## ptb umfang path
* greet
  - utter_greet
* provide_topic_ptb{"ptb":"Umfang", "topic":"PTB"}
  - utter_ptb_umfang
* goodbye
  - utter_goodbye

## ptb no information umfang path
* greet
  - utter_greet
* provide_topic_ptb{"topic":"PTB"}
  - utter_ask_ptb
* ptb_umfang{"ptb":"Umfang"}
  - utter_ptb_umfang
* goodbye
  - utter_goodbye



## semesterticket erhalten path
* greet
  - utter_greet
* semesterticket_erhalten{"semesterticket":"erhalten", "topic":"Semesterticket"}
  - utter_semesterticket_erhalten
* goodbye
  - utter_goodbye

## semesterticket no information erhalten path
* greet
  - utter_greet
* provide_topic_semesterticket{"topic":"Semesterticket"}
  - utter_ask_semesterticket
* semesterticket_erhalten{"semesterticket":"erhalten"}
  - utter_semesterticket_erhalten
* goodbye
  - utter_goodbye 

## semesterticket aktualisierung path
* greet
  - utter_greet
* semesterticket_aktualisierung{"topic":"Semesterticket", "semesterticket":"Aktualisierung"}
  - utter_semesterticket_aktualisierung
* goodbye
  - utter_goodbye

## semesterticket no information aktualisierung path
* greet
  - utter_greet
* provide_topic_semesterticket{"topic":"Semesterticket"}
  - utter_ask_semesterticket
* semesterticket_aktualisierung{"semesterticket":"Aktualisierung"}
  - utter_semesterticket_aktualisierung
* goodbye
  - utter_goodbye

## semesterticket vbb path
* greet
  - utter_greet
* semesterticket_vbb{"topic":"Semesterticket", "semesterticket":"VBB"}
  - utter_semesterticket_vbb
* goodbye
  - utter_goodbye

## semesterticket no information vbb path
* greet
  - utter_greet
* provide_topic_semesterticket{"topic":"Semesterticket"}
  - utter_ask_semesterticket
* semesterticket_vbb{"semesterticket":"VBB"}
  - utter_semesterticket_vbb
* goodbye
  - utter_goodbye

## semesterticket fahrrad path
* greet
  - utter_greet
* semesterticket_fahrrad{"topic":"Semesterticket", "semesterticket":"Fahrrad"}
  - utter_semesterticket_fahrrad
* goodbye
  - utter_goodbye

## semesterticket no information fahrrad path
* greet
  - utter_greet
* provide_topic_semesterticket{"topic":"Semesterticket"}
  - utter_ask_semesterticket
* semesterticket_fahrrad{"semesterticket":"Fahrrad"}
  - utter_semesterticket_fahrrad
* goodbye
  - utter_goodbye

## semesterticket abc path
* greet
  - utter_greet
* semesterticket_abc{"topic":"Semesterticket", "semesterticket":"ABC"}
  - utter_semesterticket_abc
* goodbye
  - utter_goodbye

## semesterticket no information abc path
* greet
  - utter_greet
* provide_topic_semesterticket{"topic":"Semesterticket"}
  - utter_ask_semesterticket
* semesterticket_abc{"semesterticket":"ABC"}
  - utter_semesterticket_abc
* goodbye
  - utter_goodbye

## semesterticket brandenburg path
* greet
  - utter_greet
* semesterticket_brandenburg{"topic":"Semesterticket","semesterticket":"Brandenburg"}
  - utter_semesterticket_brandenburg
* goodbye
  - utter_goodbye

## semesterticket no information brandenburg path
* greet
  - utter_greet
* provide_topic_semesterticket{"topic":"Semesterticket"}
  - utter_ask_semesterticket
* semesterticket_brandenburg{"semesterticket":"Brandenburg"}
  - utter_semesterticket_brandenburg
* goodbye
  - utter_goodbye

## semesterticket ansprechpartner path
* greet
  - utter_greet
* semesterticket_ansprechpartner{"semesterticket":"Ansprechpartner", "topic":"Semesterticket"}
  - utter_semesterticket_ansprechpartner
* goodbye
  - utter_goodbye

## semesterticket no information ansprechpartner path
* greet
  - utter_greet
* provide_topic_semesterticket{"topic":"Semesterticket"}
  - utter_ask_semesterticket
* semesterticket_ansprechpartner{"semesterticket":"Ansprechpartner"}
  - utter_semesterticket_ansprechpartner
* goodbye
  - utter_goodbye

## semesterticket informationen path
* greet
  - utter_greet
* semesterticket_info{"semesterticket":"Informationen", "topic":"Semesterticket"}
  - utter_semesterticket_info
* goodbye
  - utter_goodbye

## semesterticket no information informationen path
* greet
  - utter_greet
* provide_topic_semesterticket{"topic":"Semesterticket"}
  - utter_ask_semesterticket
* semesterticket_info{"semesterticket":"Informationen"}
  - utter_semesterticket_info
* goodbye
  - utter_goodbye



## studiengebu inhalt path
* greet
  - utter_greet
* studiengebu_inhalt{"studiengebu":"Inhalt", "topic":"Studiengebühren"}
  - utter_studiengebu_inhalt
* goodbye
  - utter_goodbye

## studiengebu no information inhalt path
* greet
  - utter_greet
* provide_topic_studiengebu{"topic":"Studiengebühren"}
  - utter_ask_studiengebu
* studiengebu_inhalt{"studiengebu":"Inhalt"}
  - utter_studiengebu_inhalt
* goodbye
  - utter_goodbye

## studiengebu kosten path
* greet
  - utter_greet
* studiengebu_kosten{"studiengebu":"Kosten", "topic":"Studiengebühren"}
  - utter_studiengebu_kosten
* goodbye
  - utter_goodbye

## studiengebu no information kosten path
* greet
  - utter_greet
* provide_topic_studiengebu{"topic":"Studiengebühren"}
  - utter_ask_studiengebu
* studiengebu_kosten{"studiengebu":"Kosten"}
  - utter_studiengebu_kosten
* goodbye
  - utter_goodbye

## studiengebu ueberweisung path
* greet
  - utter_greet
* studiengebu_ueberweisung{"studiengebu":"Überweisung", "topic":"Studiengebühren"}
  - utter_studiengebu_ueberweisung
* goodbye
  - utter_goodbye

## studiengebu no information ueberweisung path
* greet
  - utter_greet
* provide_topic_studiengebu{"topic":"Studiengebühren"}
  - utter_ask_studiengebu
* studiengebu_ueberweisung{"studiengebu":"Überweisung"}
  - utter_studiengebu_ueberweisung
* goodbye
  - utter_goodbye

## studiengebu zahlung path
* greet
  - utter_greet
* studiengebu_zahlung{"studiengebu":"Zahlung", "topic":"Studiengebühren"}
  - utter_studiengebu_zahlung
* goodbye
  - utter_goodbye

## studiengebu no information zahlung path
* greet
  - utter_greet
* provide_topic_studiengebu{"topic":"Studiengebühren"}
  - utter_ask_studiengebu
* studiengebu_zahlung{"studiengebu":"Zahlung"}
  - utter_studiengebu_zahlung
* goodbye
  - utter_goodbye

## studiengebu beleg path
* greet
  - utter_greet
* studiengebu_beleg{"studiengebu":"Beleg", "topic":"Studiengebühren"}
  - utter_studiengebu_beleg
* goodbye
  - utter_goodbye

## studiengebu no information beleg path
* greet
  - utter_greet
* provide_topic_studiengebu{"topic":"Studiengebühren"}
  - utter_ask_studiengebu
* studiengebu_beleg{"studiengebu":"Beleg"}
  - utter_studiengebu_beleg
* goodbye
  - utter_goodbye

## studiengebu infos path
* greet
  - utter_greet
* studiengebu_weitere_infos{"studiengebu":"Infos", "topic":"Studiengebühren"}
  - utter_studiengebu_infos
* goodbye
  - utter_goodbye

## studiengebu no information infos path
* greet
  - utter_greet
* provide_topic_studiengebu{"topic":"Studiengebühren"}
  - utter_ask_studiengebu
* studiengebu_weitere_infos{"studiengebu":"Infos"}
  - utter_studiengebu_infos
* goodbye
  - utter_goodbye


## say goodbye
* goodbye
  - utter_goodbye

