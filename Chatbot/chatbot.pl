/*
CSINTSY
MCO2 - CHATBOT
CRUZADA, ESCALONA, FRANCISCO, LOYOLA
*/

/*For prettified printing*/
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
    header,
    write("What is the patient's diastolic blood pressure (in mmHg)? "),
    read(Dias),
    header,
    write("What is the patient's heartrate (in bpm)? "),
    read(HR).

/*Consider this as the main function*/
checkup :-
    collect(Patient, Age, H, W, Temp, Sys, Dias, HR),
    diagnosis(Patient, Disease),
    display_diagnosis(Patient, Disease, Age, H, W, Temp, Sys, Dias, HR).

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
        (Disease \= null)->
            format("The patient, ~w, is diagnosed with ~w based from the symptoms presented.", [Patient, Disease]), nl, nl, treatment(Disease);
            format("No diagnosis was found for ~w with the given symptoms.", [Patient]), nl, nl
    ).

/*Structure for yes or no questions*/
yesno(Patient, Question) :-
    header,
    format("~w do you ~w ", [Patient, Question]),
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
symptom(Patient, a) :-
    check(Patient, "have a (y/n)?").
symptom(Patient, b) :-
    check(Patient, "have b (y/n)?").
symptom(Patient, c) :-
    check(Patient, "have c (y/n)?").
symptom(Patient, d) :-
    check(Patient, "have d (y/n)?").
symptom(Patient, e) :-
    check(Patient, "have e (y/n)?").
symptom(Patient, f) :-
    check(Patient, "have f (y/n)?").

/*Diagnosis assembly*/
diagnosis(Patient, abc) :-
    symptom(Patient, a),
    symptom(Patient, b),
    symptom(Patient, c).
diagnosis(Patient, bcd) :-
    symptom(Patient, b),
    symptom(Patient, c),
    symptom(Patient, d).
diagnosis(Patient, cde) :-
    symptom(Patient, c),
    symptom(Patient, d),
    symptom(Patient, e).
diagnosis(Patient, def) :-
    symptom(Patient, d),
    symptom(Patient, e),
    symptom(Patient, f).
diagnosis(Patient, ace) :-
    symptom(Patient, a),
    symptom(Patient, c),
    symptom(Patient, e).
diagnosis(_, _).

/*Treatment assembly*/
treatment(abc) :-
    format("The treatment for ~w is ~w.~n", [abc, "xyz"]).
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