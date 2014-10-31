male(james1).
male(james2).
male(charles1).
male(charles2).
male(george1).
female(catherine).
female(elizabeth).
female(sophia).

parentOf(james1,charles1).
parentOf(james1,elizabeth).
parentOf(charles1,catherine).
parentOf(charles1,charles2).
parentOf(charles1,james2).
parentOf(elizabeth,sophia).
parentOf(sophia,george1).


motherOf(M,X) :-
	parentOf(M,X),
	female(M),
	M\==X.

fatherOf(F,X) :-
	parentOf(F,X),
	male(F),
	F\==X.

siblingOf(X,Y) :-
	parentOf(Z,X),
	parentOf(Z,Y),
	X\==Y.

sisterOf(X,Y) :-
	siblingOf(X,Y),
	female(X),
	X\==Y.

brotherOf(X,Y) :-
	siblingOf(X,Y),
	male(X),
	X\==Y.

grandparentOf(X,Z) :-
	parentOf(X,Y),
	parentOf(Y,Z),
	X\==Z.

auntOf(X,Y) :-
	sisterOf(X,Z),
	parentOf(Z,Y),
	X\==Y.

uncleOf(X,Y) :-
	brotherOf(X,Z),
	parentOf(Z,Y),
	X\==Y.

cousinOf(X,Y) :-
	uncleOf(Z,X),
	parentOf(Z,Y),
	X\==Y.

cousinOf(X,Y) :-
	auntOf(Z,X),
	parentOf(Z,Y),
	X\==Y.



/*

spouseOf(X,Y) :-
	parentOf(X,Z),
	parentOf(Y,Z),
	X\==Y.

husbandOf(X,Y) :-
	spouseOf(X,Y),
	male(X),
	X\==Y.

wifeOf(X,Y) :-
	spouseOf(X,Y),
	female(X),
	X\==Y.

*/