

start :-
    /*# write('What is the patient''s name? '),
    # read(Patient), get_single_char(Code), */
    write('Are you experiencing the following symptoms: '),
    nl,
    diagnose(Disease),
    format("The patient probably has ~w.", [Disease]),
    nl,
    advice.
    /*undo.*/

start :-
    format("Cannot properly diagnose the disease.").
    /*undo.*/

ask(Question) :-
	/*#write(Patient),write(', do you'),write(Question),*/
    format("Do you experience ~w? ", [Question]),
	read(N),
	( (N == yes ; N == y)
      ->
       assert(yes(Question)) ;
       assert(no(Question)), fail).
	
:- dynamic yes/1,no/1.	

verify(S) :-
    (   yes(S) -> true;
    (   no(S) -> fail;
    ask(S))).

undo :- retract(yes(_)), fail.
undo :- retract(no(_)), fail.
undo.

/* Order the diseases by the most number of symptoms first*/
diagnose(colds) :- colds, !.
diagnose(flu) :- flu, !.
diagnose(diarrhea) :- diarrhea, !.
diagnose(tuberculosis) :- tuberculosis, !.
diagnose(pneumonia) :- pneumonia, !.
diagnose(diabetes) :- diabetes, !.
/*diagnose(unknown).*/

colds :-
    verify("Dry / Wet Cough"),
    verify("Runny Nose"),
    verify("Sneezing"),
    verify("Sore Throat").

flu :-
    verify("Fever"),
    verify("Fatigue / Weakness / Tiredness"),
    verify("Body Pain"),
    verify("Headaches"),
    /*Try to implement: OR colds*/
    verify("Colds").

diarrhea :-
    verify("Fever"),
    verify("Bloating"),
    verify("Frequent bowel movements"),
    verify("Abdominal Pain"),
    verify("Watery / loose stools"),
    verify("Blood on stool").

tuberculosis :-
    verify("Fever"),
    verify("Fatigue / Weakness / Tiredness"),
    verify("Chest pains"),
    verify("Sweating / Shivering / Chills"),
    verify("Loss off Appetite"),
    verify("Chough with blood"),
    verify("Unexplained weight loss").

pneumonia :-
    verify("Fever"),
    verify("Fatigue / Weakness / Tiredness"),
    verify("Chest pains"),
    verify("Sweating / Shivering / Chills"),
    verify("Wheezing / Breathlessness"),

    /*OR Diarrhea*/
    verify("Diarrhea").

diabetes :-
    verify("Fatigue / Weakness / Tiredness"),
    verify("Unexplained weight loss"),
    verify("Blurry vision"),
    verify("Irritable / moody"),
    verify("Polydipsia (Excess thrist)"),
    verify("Polyphagia (Always hungry)"),
    verify("Polyuria (Frequent urination)"),
    verify("Slow-healing sores").

measles :-
    verify("Fever"),
    verify("Runny Nose"),
    verify("Sore Throat"),
    verify("Skin Rashes"),
    verify("Conjunctivities"),
    /*Not sure how to display this*/
    verify("Tiny white spots"),

    /*OR flu*/
    verify("Flu").


dengue :- 
    verify("Fever"),
    verify("Fatigue / Weakness / Tiredness"),
    verify("Body Pain"),
    verify("Runny Nose"),
    verify("Vomiting"),
    verify("Blood on vomit"),
    verify("Swollen glands"),
    verify("Bleeding gums or nose"),
    verify("Persisting vomiting"),
    verify("Severe Abdominal pain"),

    /*OR flu*/
    verify("Flu").

malaria :- 
    verify("Fever"),
    verify("Fatigue / Weakness / Tiredness"),
    verify("Sweating / Shivering / Chills"),
    verify("Body Pain"),
    verify("Wheezing / Breathlessness"),
    verify("Rapid heart rate"),
    verify("Dry / Wet Cough"),
    verify("Abdominal Pain").

hypertension :- 
    verify("BP").

pharyngitis :-
    verify("Sore Throat"),
    verify("Dry / Scratchy throat"),
    verify("Pain when swallowing"),
    verify("Pain when speaking").

/*Testing pa*/
treatment("Dry / Wet Cough", "a").
treatment("Runny Nose", "b").
treatment("Sneezing", "c").
treatment("Sore Throat", "d").


advice :- 
    findall(X, yes(X), S),
    printAdvice(S).

printAdvice([]).
printAdvice([H|T]) :-
    write(H),
    treatment(H, Y),
    write(Y),
    nl,
    printAdvice(T).
