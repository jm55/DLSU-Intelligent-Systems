/*
CSINTSY
MCO2 - CHATBOT
CRUZADA, ESCALONA, FRANCISCO, LOYOLA
*/

/*Start function to begin diagnosis*/
header :-
    write("Simply Medical Chatbot"), nl,
    write("by Cruzada, Escalona, Francisco, Loyola"), nl, nl.

checkup :-
    clear,
    header,
    write("What is the patient's name? "),
    read(Patient),
    clear,
    header,
    diagnosis(Patient, Disease),
    display(Patient, Disease),
    treatment(Disease).

display(Patient, Disease) :- 
    (
        /*Display the Disease if is not null, else display no diagnosis*/
        (Disease \= null)->
            format("The patient, ~w, is diagnosed with ~w based from the symptoms presented.",[Patient, Disease]), nl, nl;
            format("No diagnosis was found for ~w with the given symptoms.",[Patient]), nl, nl
    ).

/*Structure for yes or no questions*/
yesno(Patient, Question) :-
    clear,
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

/*Verifies the question if to be asked again via the yes or no list*/
check(Patient, Question) :-
    (
        /*Already asked then set as true, else check if not answered as no or not yet asked*/
        yes(Question) -> true; 
        (
            /*Not yet asked then set as false or ask if not yet asked*/
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
diagnosis(Patient, null).

/*Treatment assembly*/
treatment(abc) :-
    format("The treatment for ~w is ~w.~n", [abc, "xyz"]).
treatment(bcd) :-
    format("The treatment for ~w is ~w.~n", [abc, "wxy"]).
treatment(cde) :-
    format("The treatment for ~w is ~w.~n", [abc, "vwx"]).
treatment(def) :-
    format("The treatment for ~w is ~w.~n", [abc, "uvw"]).
treatment(ace) :-
    format("The treatment for ~w is ~w.~n", [abc, "tuv"]).

/*Clear screen; Just call 'cls.'*/
clear :- write("\33\[2J").