entrada(paella, 200).
entrada(gazpacho, 150).
entrada(pasta, 300).
entrada(ensalada_cesar, 180).
entrada(sopa_de_verduras, 120).

principal(filete_de_cerdo, 400).
principal(pollo_asado, 280).
principal(bisteck_a_lo_pobre, 500).
principal(trucha, 160).
principal(bacalao, 300).
principal(salmon_a_la_plancha, 350).
principal(lasagna, 450).

postre(flan, 200).
postre(naranja, 50).
postre(nueces, 500).
postre(yogurt, 100).
postre(helado, 250).

% Interfaz principal del sistema

principal :-
    write('SISTEMA DE GESTIÓN DE CALORÍAS - "MI MEJOR COMIDA"'), nl,
    menu.

menu :-
    repeat,
    nl,
    write('-------- MENÚ --------'), nl,
    write('1. Calcular calorías de un menú específico'), nl,
    write('2. Mostrar combinaciones bajas en calorías'), nl,
    write('3. Salir'), nl,
    write('Seleccione una opción (1-3): '), read(Opcion),
    (Opcion == 1 -> calcular_calorias_menu, fail;
     Opcion == 2 -> mostrar_combinaciones_bajas, fail;
     Opcion == 3 -> write('Saliendo del sistema. ¡Hasta pronto!'), nl, !;
     write('Opción no válida. Intente nuevamente.'), nl, fail).


% Calorías de menú específico

calcular_calorias_menu :-
    write('Entradas: paella, gazpacho, pasta, ensalada_cesar, sopa_de_verduras.'), nl,
    write('Ingrese una entrada: '), read(Entrada),
    validar_entrada(Entrada, CaloriaE),

    write('Platos principales: filete_de_cerdo, pollo_asado, bisteck_a_lo_pobre, trucha, bacalao, salmon_a_la_plancha, lasagna.'), nl,
    write('Ingrese un plato principal: '), read(Principal),
    validar_principal(Principal, CaloriaP),

    write('Postres: flan, naranja, nueces, yogurt, helado.'), nl,
    write('Ingrese un postre: '), read(Postre),
    validar_postre(Postre, CaloriaPo),

    Total is CaloriaE + CaloriaP + CaloriaPo,
    nl,
    write('--- RESUMEN DEL MENÚ ---'), nl,
    format('Entrada: ~w (~w cal)~n', [Entrada, CaloriaE]),
    format('Principal: ~w (~w cal)~n', [Principal, CaloriaP]),
    format('Postre: ~w (~w cal)~n', [Postre, CaloriaPo]),
    format('TOTAL: ~w calorías~n', [Total]).


% Validadores con control

validar_entrada(E, C) :- entrada(E, C), !.
validar_entrada(_, _) :-
    write('Entrada no válida. Intente de nuevo.'), nl,
    calcular_calorias_menu, fail.

validar_principal(P, C) :- principal(P, C), !.
validar_principal(_, _) :-
    write('Plato principal no válido. Intente de nuevo.'), nl,
    calcular_calorias_menu, fail.

validar_postre(P, C) :- postre(P, C), !.
validar_postre(_, _) :-
    write('Postre no válido. Intente de nuevo.'), nl,
    calcular_calorias_menu, fail.


% Combinaciones bajas en calorías

mostrar_combinaciones_bajas :-
    repeat,
    write('Ingrese el máximo de calorías deseado (número entero positivo): '), 
    read(Limite),
    (   integer(Limite), Limite > 0 -> 
        nl,
        write('--- MENÚS BAJOS EN CALORÍAS ---'), nl,
        buscar_combinacion(Limite),
        !
    ;   write('Entrada incorrecta. Debe ingresar un número entero positivo.'), nl,
        fail
    ).

buscar_combinacion(Limite) :-
    entrada(E, CE),
    principal(P, CP),
    postre(PO, CPO),
    Total is CE + CP + CPO,
    Total =< Limite,
    nl,
    format('* Entrada: ~w (~w cal)~n', [E, CE]),
    format('  Principal: ~w (~w cal)~n', [P, CP]),
    format('  Postre: ~w (~w cal)~n', [PO, CPO]),
    format('  TOTAL: ~w calorías~n', [Total]),
    fail.
buscar_combinacion(_).
