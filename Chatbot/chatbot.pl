/*
CSINTSY
MCO2 - CHATBOT
CRUZADA, ESCALONA, FRANCISCO, LOYOLA
*/

/*For prettified printing*/

:-style_check(-singleton).

header :-
    clear,
    write("Simply Medical Chatbot"), nl,
    write("by Cruzada, Escalona, Francisco, Loyola"), nl, nl.

/*Collect patient's basic health data (can be useful for risk detection)*/
collect(Patient, Age, H, W, Temp, Sys, Dias, HR) :-
    header,
    write("What is the patient's name? "),
    read(Patient),
    header,
    write("What is the patient's age ? "),
    read(Age),
    header,
    write("What is the patient's height (in cm)? "),
    read(H),
    header,
    write("What is the patient's weight (in kg)? "),
    read(W),
    header,
    write("What is the patient's temperature (in C)? "),
    read(Temp),
    header,
    write("What is the patient's systolic blood pressure (in mmHg)? "),
    read(Sys),
    header,    write("What is the patient's diastolic blood pressure (in mmHg)? "),
    read(Dias),
    header,
    write("What is the patient's heartrate (in bpm)? "),
    read(HR).


/*Consider this as the main function*/
checkup :-
    collect(Patient, Age, H, W, Temp, Sys, Dias, HR),
    diagnosis(Patient, Disease, Sys, Dias),
    display_diagnosis(Patient, Disease, Age, H, W, Temp, Sys, Dias, HR),
    undo.
/*Display the collected health data of patient*/
display_data(Patient, Age, H, W, Temp, Sys, Dias, HR) :-
    header,
    format("Patient: ~w", [Patient]), nl,
    format("Age: ~w", [Age]), nl,
    format("Height: ~w cm", [H]), nl,
    format("Weight: ~w kg", [W]), nl,
    format("Body Temperature: ~w C", [Temp]), nl,
    format("Blood Pressure: ~w/~w mmHg", [Sys, Dias]), nl,
    format("Heart Rate: ~w bpm", [HR]), nl,
    nl.

/*Displays the diagnosis of disease depending if there was a disease found or not.*/
display_diagnosis(Patient, Disease, Age, H, W, Temp, Sys, Dias, HR) :-
    display_data(Patient, Age, H, W, Temp, Sys, Dias, HR),
    (
        /*Display the Disease if is not null, else display no diagnosis*/
        (Disease \= null)->            format("The patient, ~w, is diagnosed with ~w based from the symptoms presented.", [Patient, Disease]), nl, nl, treatment(Disease);
            format("No diagnosis was found for ~w with the given symptoms.", [Patient]), nl, nl
    ).

/*Structure for yes or no questions*/
yesno(Patient, Question) :-
    header,
    format("~w, do you ~w ", [Patient, Question]),
    read(Ans),
    (
        /*If yes then assert yes to question; Else then assert no to question and set as false*/
        (Ans == yes ; Ans == y) ->
            assertz(yes(Question));
            assertz(no(Question)), false
    ).

:- dynamic yes/1, no/1.

/*Verifies the question if to be asked again or if has an answer already via the yes or no answer list*/
check(Patient, Question) :-
    (
        /*Check if Question is in yes answer bank, else check if not answered as no or not yet asked*/
        yes(Question) -> true;
        (
            /*Check if Question is in no answer bank, else ask*/
            no(Question) -> false;
            yesno(Patient, Question)
        )
    ).

/*Symptom facts gathering*/

colds(Patient) :-
    check(Patient, "have Dry / Wet Cough (y/n)?"),
    check(Patient, "have Runny Nose (y/n)?"),
    check(Patient, "have Sneezing (y/n)?"),
    check(Patient, "have Sore Throat (y/n)?").

flu(Patient) :-
    check(Patient, "have Fever (y/n)?"),
    check(Patient, "have Fatigue / Weakness / Tiredness (y/n)?"),
    check(Patient, "have Body Pain (y/n)?"),
    check(Patient, "have Headaches (y/n)?"),
    /*Try to implement: OR colds*/
    check(Patient, "have Colds (y/n)?").

diarrhea(Patient) :-
    check(Patient, "have Fever (y/n)?"),
    check(Patient, "have Bloating (y/n)?"),
    check(Patient, "have Frequent bowel movements (y/n)?"),
    check(Patient, "have Watery / loose stools (y/n)?"),
    check(Patient, "have Blood on stool (y/n)?").

tuberculosis(Patient) :-
    check(Patient, "have Fever (y/n)?"),
    check(Patient, "have Fatigue / Weakness / Tiredness (y/n)?"),
    check(Patient, "have Chest pains (y/n)?"),
    check(Patient, "have Sweating / Shivering / Chills (y/n)?"),
    check(Patient, "have Loss off Appetite (y/n)?"),
    check(Patient, "have Chough with blood (y/n)?"),
    check(Patient, "have Unexplained weight loss (y/n)?").

pneumonia(Patient) :-
    check(Patient, "have Fever (y/n)?"),
    check(Patient, "have Fatigue / Weakness / Tiredness (y/n)?"),
    check(Patient, "have Chest pains (y/n)?"),
    check(Patient, "have Sweating / Shivering / Chills (y/n)?"),
    check(Patient, "have Wheezing / Breathlessness (y/n)?"),
    /*OR Diarrhea*/
    check(Patient, "have Diarrhea (y/n)?").

diabetes(Patient) :-
    check(Patient, "have Fatigue / Weakness / Tiredness (y/n)?"),
    check(Patient, "have Unexplained weight loss (y/n)?"),
    check(Patient, "have Blurry vision (y/n)?"),
    check(Patient, "have Irritable / moody (y/n)?"),
    check(Patient, "have Polydipsia (Excess thrist) (y/n)?"),
    check(Patient, "have Polyphagia (Always hungry) (y/n)?"),
    check(Patient, "have Polyuria (Frequent urination) (y/n)?"),
    check(Patient, "have Slow-healing sores (y/n)?").

measles(Patient) :-
    check(Patient, "have Fever (y/n)?"),
    check(Patient, "have Runny Nose (y/n)?"),
    check(Patient, "have Sore Throat (y/n)?"),
    check(Patient, "have Skin Rashes (y/n)?"),
    check(Patient, "have Conjunctivities (y/n)?"),
    /*Not sure how to display this*/
    check(Patient, "have Tiny white spots (y/n)?"),
    /*OR flu*/
    check(Patient, "have Flu (y/n)?").

dengue(Patient) :-
    check(Patient, "have Fever (y/n)?"),
    check(Patient, "have Fatigue / Weakness / Tiredness (y/n)?"),
    check(Patient, "have Body Pain (y/n)?"),
    check(Patient, "have Runny Nose (y/n)?"),
    check(Patient, "have Vomiting (y/n)?"),
    check(Patient, "have Blood on vomit (y/n)?"),
    check(Patient, "have Swollen glands (y/n)?"),
    check(Patient, "have Bleeding gums or nose (y/n)?"),
    check(Patient, "have Persisting vomiting (y/n)?"),
    check(Patient, "have Abdominal Pain (y/n)?"),
    /*OR flu*/
    check(Patient, "have Flu (y/n)?").


malaria(Patient)  :-
    check(Patient, "have Fever (y/n)?"),
    check(Patient, "have Fatigue / Weakness / Tiredness (y/n)?"),
    check(Patient, "have Sweating / Shivering / Chills (y/n)?"),
    check(Patient, "have Body Pain (y/n)?"),
    check(Patient, "have Wheezing / Breathlessness (y/n)?"),
    check(Patient, "have Rapid heart rate (y/n)?"),
    check(Patient, "have Dry / Wet Cough (y/n)?"),
    check(Patient, "have Persisting vomiting (y/n)?"),
    check(Patient, "have Abdominal Pain (y/n)?").

hypertension(Sys, Dias) :-
    Sys >= 140,
    Dias >= 90.


pharyngitis(Patient)  :-
    check(Patient, "have Sore Throat (y/n)?"),
    check(Patient, "have Dry / Scratchy throat (y/n)?"),
    check(Patient, "have Pain when swallowing (y/n)?"),
    check(Patient, "have Pain when speaking (y/n)?").


/*Diagnosis assembly*/
diagnosis(Patient, hypertension, Sys, Dias) :- hypertension(Sys, Dias), !.
diagnosis(Patient, colds, Sys, Dias) :- colds(Patient), !.
diagnosis(Patient, flu, Sys, Dias) :- flu(Patient) , !.
diagnosis(Patient, diarrhea, Sys, Dias) :- diarrhea(Patient) , !.
diagnosis(Patient, tuberculosis, Sys, Dias) :- tuberculosis(Patient) , !.
diagnosis(Patient, pneumonia, Sys, Dias) :- pneumonia(Patient) , !.
diagnosis(Patient, diabetes, Sys, Dias) :- diabetes(Patient) , !.
diagnosis(Patient, measles, Sys, Dias) :- measles(Patient) , !.
diagnosis(Patient, dengue, Sys, Dias) :- dengue(Patient) , !.
diagnosis(Patient, malaria, Sys, Dias) :- malaria(Patient) , !.
diagnosis(Patient, pharyngitis, Sys, Dias) :- pharyngitis(Patient) , !.
diagnosis(_, _, Sys, Dias).

/*Treatment assembly*/
treatment(flu) :-
    format("The treatment for ~w is ~w.~n", [flu, "test"]).
treatment(bcd) :-
    format("The treatment for ~w is ~w.~n", [bcd, "wxy"]).
treatment(cde) :-
    format("The treatment for ~w is ~w.~n", [cde, "vwx"]).
treatment(def) :-
    format("The treatment for ~w is ~w.~n", [def, "uvw"]).
treatment(ace) :-
    format("The treatment for ~w is ~w.~n", [ace, "tuv"]).

/*Clear screen; Just call 'clear.'*/
clear :- write("\33\[2J").

/*Reset symptom kb*/
undo :- retract(yes(_)), fail.
undo :- retract(no(_)), fail.
undo.
