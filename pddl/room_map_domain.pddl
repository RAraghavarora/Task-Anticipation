(define (domain room-planning)
    (:requirements :strips :typing :negative-preconditions :derived-predicates)
    (:types 
        room
        object
        agent
    )
    (:predicates 
        (room ?r - room)
        (object ?o - object)
        (agent ?a - agent)
        (adjacent ?r1 - room ?r2 - room)
        (at ?o - object ?r1 - room)
        (carrying ?o - object ?a - agent)
        (in-room ?a - agent ?r1 - room)
        (busy ?a - agent)
    )

    ; (:derived (adjacent ?r2 - room ?r1 - room)
    ;       (adjacent ?r1 ?r2)
    ; )

    (:action move
        :parameters (?a - agent ?r1 - room ?r2 - room)
        :precondition (and 
            (agent ?a) 
            (room ?r1)
            (room ?r2)
            (in-room ?a ?r1)
            (not (in-room ?a ?r2))
            (adjacent ?r1 ?r2)
        )
        :effect (and 
            (not (in-room ?a ?r1))
            (in-room ?a ?r2)
        )
    )
    (:action pick-up
        :parameters (?a - agent ?o - object ?r - room)
        :precondition (and 
            (agent ?a) 
            (object ?o)
            (room ?r)
            (not (busy ?a))
            (in-room ?a ?r)
            (at ?o ?r)
            (not (carrying ?o ?a)) ; Redundant
        )
        :effect (and 
            (carrying ?o ?a)
            (not (at ?o ?r))
            (busy ?a)
        )
    )

    (:action put-down
        :parameters (?a - agent ?o - object ?r - room)
        :precondition (and 
            (agent ?a) 
            (object ?o)
            (room ?r)
            (in-room ?a ?r)
            (carrying ?o ?a)
        )
        :effect (and 
            (not (carrying ?o ?a))
            (at ?o ?r)
            (not (busy ?a))
        )
    )
)