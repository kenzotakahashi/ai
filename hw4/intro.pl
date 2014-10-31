likes(mary,food).
likes(mary,wine).
likes(john,chess).
likes(john,mary).

likes(john,X) :-  likes(mary,X).

likes(P1,P2) :-
    hobby(P1,H),
    hobby(P2,H),
    P1\==P2.

hobby(john,cooking).
hobby(john,games).
hobby(tim,cooking).
hobby(helen,games).











