diagnose:-
    guess(Disease),
    write('I think the patient has'),
    nl,
    write(Disease),
    nl,
    write('Thank you. '),
    undo.

guess(dengue) :- dengue, !.
guess(tuberculosis) :- tuberculosis, !.

dengue :-
    verify(fever),
    verify(headache),
    verify(body_pain),
    verify(fatigue_weakness_tiredness),
    verify(nausea).

tuberculosis :-
    verify(fever),
    verify(runny_nose),
    verify(nausea),
    verify(fatigue_weakness_tiredness),
    verify(weight_loss),
    verify(chest_pains),
    verify(night_sweats),
    verify(chills),
    verify(coughing_with_blood).

ask(Question) :-
    write('Are you experiencing the following symptom? '),
    write(Question),
    write('? '),
    read(Response),
    nl,
    (   (Response == yes ; Response == y) ->
    assert(yes(Question));
    assert(no(Question)), fail).

:- dynamic yes/1, no/1.

verify(S) :-
    (   yes(S) -> true;
    (   no(S) -> fail;
    ask(S))).

undo :- retract(yes(_)), fail.
undo :- retract(no(_)), fail.
undo.


