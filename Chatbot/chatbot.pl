/*Start function to begin diagnosis*/
checkup :-
    write("What is the patient's name? "),
    read(Patient),
    diagnosis(Patient, Disease),
    display(Patient, Disease),
    treatment(Disease).

display(Patient, Disease) :- 
    (
        (Disease \= null)->
            print_list([Patient, ' was diagnosed with ', Disease, ' based from the symptoms presented.']), nl;
            format("No diagnosis was found for ~w with the given symptoms.",[Patient]), nl
    ).

/*Structure for yes or no questions*/
yesno(Patient, Question) :-
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
        /*Already asked then set as true, else check if not answered as no or yet asked*/
        yes(Question) -> true; 
        (
            /*Not yet asked then set as false*/
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
    format("Treatment for ~w is ~w.~n", [abc, "xyz"]).
treatment(bcd) :-
    format("Treatment for ~w is ~w.~n", [abc, "wxy"]).
treatment(cde) :-
    format("Treatment for ~w is ~w.~n", [abc, "vwx"]).
treatment(def) :-
    format("Treatment for ~w is ~w.~n", [abc, "uvw"]).
treatment(ace) :-
    format("Treatment for ~w is ~w.~n", [abc, "tuv"]).

/*Print contents of a list like in Python*/
print_list([]).
print_list([Word | Words]) :-
    write(Word), print_list(Words).

/*Clear screen; Just call 'cls.'*/
clear :- write("\33\[2J").