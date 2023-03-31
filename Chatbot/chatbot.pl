/*
CSINTSY
MCO2 - CHATBOT
CRUZADA, ESCALONA, FRANCISCO, LOYOLA
*/

/*For prettified printing*/

:-style_check(-singleton).
:- dynamic collect/8, yes/1, no/1. %make these dynamic so that they can be retracted for next run%


header :-
    clear,
    write("Simply Medical Chatbot"), nl,
    write("by Cruzada, Escalona, Francisco, Loyola"), nl, nl.

/*Collect patient's basic health data (can be useful for risk detection)*/
collect(Patient, Age, H, W, Temp, Sys, Dias, HR) :-
    header,
    write("What is the patient's name? "),
    read(Patient),
    write("What is the patient's age ? "),
    read(Age),
    write("What is the patient's height (in cm)? "),
    read(H),
    write("What is the patient's weight (in kg)? "),
    read(W),
    write("What is the patient's temperature (in C)? "),
    read(Temp),
    write("What is the patient's systolic blood pressure (in mmHg)? "),
    read(Sys),
    write("What is the patient's diastolic blood pressure (in mmHg)? "),
    read(Dias),
    write("What is the patient's heartrate (in bpm)? "),
    read(HR).


/*Consider this as the main function*/
checkup :-
    collect(Patient, Age, H, W, Temp, Sys, Dias, HR), nl,
    diagnosis(Patient, Disease, Sys, Dias), nl,
    display_diagnosis(Patient, Disease, Age, H, W, Temp, Sys, Dias, HR),
    undo.

/*Display the collected health data of patient*/
display_data(Patient, Age, H, W, Temp, Sys, Dias, HR) :-
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
    /*display_data(Patient, Age, H, W, Temp, Sys, Dias, HR),*/
    (
        /*Display the Disease if is not null, else display no diagnosis*/
        (Disease \= null)->
            format("The patient, ~w, is diagnosed with ~w based from the symptoms presented.", [Patient, Disease]), nl, nl, treatment(Disease), true;
            format("No diagnosis was found for ~w with the given symptoms.", [Patient]), nl, nl, true
    ), nl, nl.

/*Structure for yes or no questions*/
yesno(Patient, Question) :-
    format("~w, do you ~w ", [Patient, Question]),
    read(Ans),
    (
        /*If yes then assert yes to question; Else then assert no to question and set as false*/
        (Ans == yes ; Ans == y) ->
            assertz(yes(Question));
            assertz(no(Question)), false
    ).


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
dengue(Patient) :-
    check(Patient, "have Fever (y/n)?"),
    check(Patient, "have Fatigue / Weakness / Tiredness (y/n)?"),
    check(Patient, "have Body Pain (y/n)?"),
    check(Patient, "have severe headaches (y/n)?"),
    check(Patient, "have Runny Nose (y/n)?"),
    check(Patient, "have Vomiting (y/n)?"),
    check(Patient, "have Blood on vomit (y/n)?"),
    check(Patient, "have Swollen glands (y/n)?"),
    check(Patient, "have Bleeding gums or nose (y/n)?"),
    check(Patient, "have Persisting vomiting (y/n)?"),
    check(Patient, "have Abdominal Pain (y/n)?").
    /*OR flu*/
    /*check(Patient, "have Flu (y/n)?"). */

flu(Patient) :-
    check(Patient, "have Fever (y/n)?"),
    check(Patient, "have Fatigue / Weakness / Tiredness (y/n)?"),
    check(Patient, "have Body Pain (y/n)?"),
    check(Patient, "have Headaches (y/n)?").

    /*Try to implement: OR colds*/
    /*check(Patient, "have Colds (y/n)?"). */

tuberculosis(Patient) :-
    check(Patient, "have Fever (y/n)?"),
    check(Patient, "have Fatigue / Weakness / Tiredness (y/n)?"),
    check(Patient, "have Sweating / Shivering / Chills (y/n)?"),
    check(Patient, "have Chest pains (y/n)?"),
    check(Patient, "have Loss off Appetite (y/n)?"),
    check(Patient, "have Chough with blood (y/n)?"),
    check(Patient, "have Unexplained weight loss (y/n)?").

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

diarrhea(Patient) :-
    check(Patient, "have Fever (y/n)?"),
    check(Patient, "have Bloating (y/n)?"),
    check(Patient, "have Frequent bowel movements (y/n)?"),
    check(Patient, "have Watery / loose stools (y/n)?"),
    check(Patient, "have Blood on stool (y/n)?").


pneumonia(Patient) :-
    check(Patient, "have Fever (y/n)?"),
    check(Patient, "have Fatigue / Weakness / Tiredness (y/n)?"),
    check(Patient, "have Chest pains (y/n)?"),
    check(Patient, "have Sweating / Shivering / Chills (y/n)?"),
    check(Patient, "have Wheezing / Breathlessness (y/n)?").
    /*OR Diarrhea*/
    /*check(Patient, "have Diarrhea (y/n)?").*/

measles(Patient) :-
    check(Patient, "have Fever (y/n)?"),
    check(Patient, "have Runny Nose (y/n)?"),
    check(Patient, "have Sore Throat (y/n)?"),
    check(Patient, "have Skin Rashes (y/n)?"),
    check(Patient, "have Conjunctivities (y/n)?"),
    /*Not sure how to display this*/
    check(Patient, "have Tiny white spots (y/n)?").
    /*OR flu*/
    /*check(Patient, "have Flu (y/n)?").*/


pharyngitis(Patient)  :-
    check(Patient, "have Sore Throat (y/n)?"),
    check(Patient, "have Dry / Scratchy throat (y/n)?"),
    check(Patient, "have Pain when swallowing (y/n)?"),
    check(Patient, "have Pain when speaking (y/n)?").

diabetes(Patient) :-
    check(Patient, "have Polydipsia (Excess thrist) (y/n)?"),
    check(Patient, "have Polyphagia (Always hungry) (y/n)?"),
    check(Patient, "have Polyuria (Frequent urination) (y/n)?"),
    check(Patient, "have Unexplained weight loss (y/n)?"),
    check(Patient, "have Blurry vision (y/n)?"),
    check(Patient, "have Irritable / moody (y/n)?"),
    check(Patient, "have Fatigue / Weakness / Tiredness (y/n)?"),
    check(Patient, "have Slow-healing sores (y/n)?").


hypertension(Patient, Sys, Dias) :-
    (Sys >= 140, Dias >= 90);
    (check(Patient, "have an average BP of >=130/85 at home (y/n)?");
     check(Patient, "had a one time BP measurement of 180/110 (y/n)? ")).



/*Diagnosis assembly*/
diagnosis(Patient, hypertension, Sys, Dias) :- hypertension(Patient, Sys, Dias), !.
diagnosis(Patient, dengue, Sys, Dias) :- dengue(Patient) , !.
diagnosis(Patient, flu, Sys, Dias) :- flu(Patient), !.
diagnosis(Patient, tuberculosis, Sys, Dias) :- tuberculosis(Patient) , !.
diagnosis(Patient, malaria, Sys, Dias) :- malaria(Patient) , !.
diagnosis(Patient, diarrhea, Sys, Dias) :- diarrhea(Patient) , !.
diagnosis(Patient, pneumonia, Sys, Dias) :- pneumonia(Patient) , !.
diagnosis(Patient, measles, Sys, Dias) :- measles(Patient) , !.
diagnosis(Patient, pharyngitis, Sys, Dias) :- pharyngitis(Patient) , !.
diagnosis(Patient, diabetes, Sys, Dias) :- diabetes(Patient) , !.
diagnosis(_, _, Sys, Dias).

/*For writing list of treatments*/
list_treatments([]).
list_treatments([H|L]) :-
    write(H),nl,list_treatments(L).

/*Treatment assembly*/
treatment(hypertension) :-
    format("The treatment for ~w are:~n~n", [hypertension]),
    list_treatments([
                        "1. Lifestyle-related changes", "1.1. Eating a heart-healthy diet with less salt.","1.2. Getting regular physical activity.",
                        "1.3. Maintaining a healthy weight or losing weight.", "1.4. Limiting alcohol intake.", "1.5. Avoid smoking.",
                        "1.6. Getting 7 to 9 hours of sleep daily.","2. Medications (as per doctor's prescription) such as: ",
                        "2.1. Water pills (diuretics)", "2.2. Angiotensin-converting enzyme (ACE) inhibitors", "2.3. Angiotensin II receptor blockers (ARBs)",
                        "2.4. Calcium channel blockers", "2.5. Alpha blockers", "2.6. Alpha-beta blockers", "2.7. Beta blockers", "2.8. Aldosterone antagonists",
                        "2.9. Renin inhibitors", "2.10. Vasodilators", "2.11. Central-acting agents"
                    ]).
treatment(flu) :-
    format("The treatment for ~w are:~n~n", [flu]),
    list_treatments([
                        "Urgent Treatment:", "Seek medical attention if fever is above 38.9C or if there are persistent coughs (may indicate pneumonia).",
                        "", "Common Treatment:", "1. Extended resting until symptoms are gone.", "2. Drink lots of clear fluids.",
                        "3. Don't smoke.", "4. Don't take antibiotics until specifically prescribed.", "", "Specific Treatment:",
                        "1. Runny/Stuffy Nose:", "1.1 Take decongestants.",
                        "1.2 Take salt-water nasal sprays.", "1.3 Use humidifiers or take hot showers.","2. Coughs",
                        "2.1 Take Dextromethorphan (consult with doctor first).", "2.2 Inhale steam/water vapor to loosen mucus.", "3. Sore Throat",
                        "3.1 Take Phenol found on lozenges and sprays.", "3.2 Gargling with warm salt water.", "3.3 Drink tea with lemon.",
                        "4. Fever/Pain - Take Acetaminophen, Aspirin, or Ibuprofen."
                    ]).
treatment(colds) :-
    format("The treatment for ~w are:~n~n", [colds]),
    list_treatments([
						"1. Rest and sleep.", "2. Drink plenty of water (fruit juice or squash mixed with water is OK) to avoid dehydration.",
						"3. Gargle salt water to soothe a sore throat (not suitable for children)."
                    ]).
treatment(diarrhea) :-
    format("The treatment for ~w are:~n~n", [diarrhea]),
    list_treatments([
                        "1. Avoid milk-based, greasy, fibrous, or very sweet foods.", "2. Avoid caffeine and alcohol.",
                        "3. Do not eat solid foods if you have signs of dehydration.", "4. Drink fluids with electrolytes or sodium.",
                        "5. Eat normal foods within 12 hours that are non-irritating to the intesting (i.e., bland foods)."
                    ]).
treatment(tuberculosis) :-
    format("The treatment for ~w are:~n~n", [tuberculosis]),
    list_treatments([
                        "1. Take medication (as per doctor's prescription)", "2. Stay at home with proper ventilation.",
                        "3. Cover your moth and wear a face mask."
                    ]).
treatment(pneumonia) :-
    format("The treatment for ~w are:~n~n", [pneumonia]),
    list_treatments([
                        "Note: The treatment will be a case-by-case basis, please consult your doctor for full information.", "",
                        "1. Take antibiotics (as per doctor's prescription).", "2. Rest, drink a lot of water, and take medicine for fever.",
                        "3. Consult with a doctor or go to a hospital should the symptoms get worse especailly for difficulty of breathing."
                    ]).
treatment(diabetes) :-
    format("The treatment for ~w are:~n~n", [diabetes]),
    list_treatments([
                        "1. Have a healthy diet.", "2. Do more physical activities.", "3. Avoid foods with sugar and saturated fats.",
                        "4. Avoid smoking.", "5. For Type 1 Diabetes: Consult doctor for recommendations for insulin injections as well as for orally administered drugs that aides the pancreas in producing more insulin."
                    ]).
treatment(measles) :-
    format("The treatment for ~w are:~n~n", [measles]),
    list_treatments([
                        "1. Isolate yourself or people with measles.", "2. Vaccinate other people at home against measles, especially those that haven't contracted it yet."
                    ]).
treatment(dengue) :-
    format("The treatment for ~w are:~n~n", [dengue]),
    list_treatments([
                        "Urgent treatment: Consult with a doctor or go to a hospital should symptoms worsen or stay for too long.", "",
                        "Common Treatment: ", "1. Rest", "2. Stay Hydrated.", "3. If possible, take a dengue fever vaccine (ask your doctor for more information.",
                        "4. Avoid having a mosquito bites by covering your skin."
                    ]).
treatment(malaria) :-
    format("The treatment for ~w are:~n~n", [malaria]),
    list_treatments([
                        "1. Avoid having a mosquito bites by covering your skin.", "2. Take anti-malaria medical drugs or a vaccine (as per doctor's prescrition)."
                    ]).
treatment(pharyngitis) :-
    format("The treatment for ~w are:~n~n", [pharyngitis]),
    list_treatments([
                        "Note: The treatment will depend base on cause of the sore throat, please consult your doctor for further information.",
                        "Nonetheless, the following are the general treatments based on cause.", "", "For viral pharyngitis: ",
                        "1. Take salt water gargles", "2. Take pain relievers", "3. Drink extra fluids (e.g., water)", "", "For bacterial/fungal pharyngitis: ",
                        "1. Treated with antibiotics or antifungal medications respectively (as per doctor's prescription)",
                        "2. Patients with strep throat are advised to consult with a doctor for possible antibiotic therapy."
                    ]).

/*Clear screen; Just call 'clear.'*/
clear :- write("\33\[2J").

/*Reset kb*/
undo :- retractall(yes(_)), fail.
undo :- retractall(no(_)), fail.
undo :- retractall(collect(_)), fail.
undo.
