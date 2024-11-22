% Hechos básicos: Define padres y cónyuges
padre(juan, maria).
padre(juan, pedro).
padre(carlos, ana).
padre(carlos, luis).
madre(maria, sofia).
madre(maria, diego).
madre(ana, juanito).

% Define cónyuges (matrimonios)
esposo(juan, maria).
esposa(maria, juan).
esposo(carlos, ana).
esposa(ana, carlos).

% Relación: hijo
hijo(Hijo, Padre) :- padre(Padre, Hijo).
hijo(Hijo, Madre) :- madre(Madre, Hijo).

% Relación: abuelo
abuelo(Abuelo, Nieto) :- padre(Abuelo, Padre), padre(Padre, Nieto).
abuelo(Abuelo, Nieto) :- padre(Abuelo, Madre), madre(Madre, Nieto).

% Relación: nieto
nieto(Nieto, Abuelo) :- abuelo(Abuelo, Nieto).

% Relación: tío
tio(Tio, Sobrino) :-
    padre(Padre, Sobrino),
    hermano(Tio, Padre).
tio(Tio, Sobrino) :-
    madre(Madre, Sobrino),
    hermano(Tio, Madre).

% Relación: sobrino
sobrino(Sobrino, Tio) :- tio(Tio, Sobrino).

% Relación: primo
primo(Primo1, Primo2) :-
    padre(Padre1, Primo1),
    padre(Padre2, Primo2),
    hermano(Padre1, Padre2).

primo(Primo1, Primo2) :-
    madre(Madre1, Primo1),
    madre(Madre2, Primo2),
    hermano(Madre1, Madre2).

% Relación: hermano
hermano(Hermano1, Hermano2) :-
    padre(Padre, Hermano1),
    padre(Padre, Hermano2),
    Hermano1 \= Hermano2.

hermano(Hermano1, Hermano2) :-
    madre(Madre, Hermano1),
    madre(Madre, Hermano2),
    Hermano1 \= Hermano2.

% Relación: familiar (une todas las anteriores)
familiar(X, Y) :-
    padre(X, Y);
    madre(X, Y);
    hijo(X, Y);
    abuelo(X, Y);
    nieto(X, Y);
    tio(X, Y);
    sobrino(X, Y);
    primo(X, Y).

% Relación: familiares (genera una lista de todos los familiares)
familiares(Persona, Familiares) :-
    findall(Familiar, familiar(Persona, Familiar), Familiares).

% Relación: casado (los que tienen hijos en común)
casado(Persona1, Persona2) :-
    padre(Persona1, Hijo),
    madre(Persona2, Hijo).

% Relación: feliz (quien es casado)
feliz(Persona) :-
    casado(Persona, _).
