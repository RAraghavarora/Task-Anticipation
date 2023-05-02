(define (domain room-planning)
(:requirements :strips :typing)
(:types 
    room
    object
)
(:predicates 
    (room ?r - room)
    (object ?o - object)
    (adjacent ?r1 ?r2 - room)
    (at ?o - object ?r1 - room)
)

(:action move
    :parameters (?o - object ?r1 ?r2 - room)
    :precondition (and 
        (object ?o) 
        (room ?r1) 
        (room ?r2) 
        (adjacent ?r1 ?r2)
    )
    :effect (and 
        (not (at ?o ?r1))
        (at ?o ?r2)
    )
)
)