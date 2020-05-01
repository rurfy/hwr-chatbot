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

## studentenausweis kaputt path
* greet
  - utter_greet
* studentenausweis_kaputt{"topic":"Studentenausweis","studentenausweis":"kaputt"}
  - utter_studentenausweis_kaputt
* goodbye
  - utter_goodbye

## studentenausweis no information kaputt path
* greet
  - utter_greet
* provide_topic_studentenausweis{"topic":"Studentenausweis"}
  - utter_ask_studentenausweis
* studentenausweis_kaputt{"studentenausweis":"kaputt"}
  - utter_studentenausweis_kaputt
* goodbye
  - utter_goodbye

## studentenausweis verloren path
* greet
  - utter_greet
* studentenausweis_verloren{"topic":"Studentenausweis","studentenausweis":"verloren"}
  - utter_studentenausweis_verloren
* goodbye
  - utter_goodbye

## studentenausweis no information verloren path
* greet
  - utter_greet
* provide_topic_studentenausweis{"topic":"Studentenausweis"}
  - utter_ask_studentenausweis
* studentenausweis_verloren{"studentenausweis":"verloren"}
  - utter_studentenausweis_verloren
* goodbye
  - utter_goodbye

## studienberatung
* greet
 - utter_greet
* provide_topic_studienberatung{"topic":"Studienberatung"}
 - utter_ask_studienberatung
* goodbye
 - utter_goodbye

## matrikelnummer
* greet
  - utter_greet
* provide_topic_matrikelnummer
  - utter_ask_matrikelnummer
* goodbye
  - utter_goodbye

## benutzerkonto moodle path
* greet
  - utter_greet
* benutzerkonto_moodle{"topic":"Benutzerkonto","benutzerkonto":"Moodle"}
  - utter_benutzerkonto_moodle
* goodbye
  - utter_goodbye

## benutzerkonto no information moodle path
* greet
  - utter_greet
* provide_topic_benutzerkonto{"topic":"Benutzerkonto"}
  - utter_ask_benutzerkonto
* benutzerkonto_moodle{"benutzerkonto":"Moodle"}
  - utter_benutzerkonto_moodle
* goodbye
  - utter_goodbye

## benutzerkonto computer path
* greet
  - utter_greet
* benutzerkonto_computer{"topic":"Benutzerkonto","benutzerkonto":"Computer"}
  - utter_benutzerkonto_computer
* goodbye
  - utter_goodbye

## benutzerkonto no information computer path
* greet
  - utter_greet
* provide_topic_benutzerkonto{"topic":"Benutzerkonto"}
  - utter_ask_benutzerkonto
* benutzerkonto_computer{"benutzerkonto":"Computer"}
  - utter_benutzerkonto_computer
* goodbye
  - utter_goodbye

## benutzerkonto pw path
* greet
  - utter_greet
* benutzerkonto_pw{"topic":"Benutzerkonto","benutzerkonto":"Passwort"}
  - utter_benutzerkonto_pw
* goodbye
  - utter_goodbye

## benutzerkonto no information pw path
* greet
  - utter_greet
* provide_topic_benutzerkonto{"topic":"Benutzerkonto"}
  - utter_ask_benutzerkonto
* benutzerkonto_pw{"benutzerkonto":"Passwort"}
  - utter_benutzerkonto_pw
* goodbye
  - utter_goodbye

## mail adresse path
* greet
  - utter_greet
* mail_adresse{"topic":"Mail","mail":"Adresse"}
  - utter_mail_adresse
* goodbye
  - utter_goodbye

## mail no information adresse path
* greet
  - utter_greet
* provide_topic_mail{"topic":"Mail"}
  - utter_ask_mail
* mail_adresse{"mail":"Adresse"}
  - utter_mail_adresse
* goodbye
  - utter_goodbye

## mail abrufen path
* greet
  - utter_greet
* mail_abrufen{"topic":"Mail","mail":"abrufen"}
  - utter_mail_abrufen
* goodbye
  - utter_goodbye

## mail no information abrufen path
* greet
  - utter_greet
* provide_topic_mail{"topic":"Mail"}
  - utter_ask_mail
* mail_abrufen{"mail":"abrufen"}
  - utter_mail_abrufen
* goodbye
  - utter_goodbye

## mail portal path
* greet
  - utter_greet
* mail_portal{"topic":"Mail","mail":"Portal"}
  - utter_mail_portal
* goodbye
  - utter_goodbye

## mail no information portal path
* greet
  - utter_greet
* provide_topic_mail{"topic":"Mail"}
  - utter_ask_mail
* mail_portal{"mail":"Portal"}
  - utter_mail_portal
* goodbye
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

