(define (domain household)
  (:requirements :strips :typing :negative-preconditions)
  (:types 
    location
    food
    person
  )
  (:predicates
    (at ?f - food ?l - location)
    (next-to ?p - person ?l - location)
    (carrying ?p - person ?f - food)
    (vegetables-cut ?f - food)
    (cooked ?f - food)
    (served ?f - food)
    (can-cut ?l - location)
    (can-cook ?l - location)
    (can-serve ?l - location)
  )
  (:action move-to
      :parameters (?p - person ?l1 - location ?l2 - location)
      :precondition(and
        (next-to ?p ?l1)
        (not (next-to ?p ?l2)) ; Redundant
      )
      :effect(and
        (next-to ?p ?l2)
        (not(next-to ?p ?l1))
      )
  )
  (:action pick-up
    :parameters (?p - person ?f - food ?l - location)
    :precondition (and
        (at ?f ?l)
        (next-to ?p ?l)
    )
    :effect (and
      (not (at ?f ?l))
      (carrying ?p ?f)
    )
  )
  (:action put-down
      :parameters (?p - person ?f - food ?l - location)
      :precondition (and
          (carrying ?p ?f)
          (next-to ?p ?l)
       )
      :effect (and 
            (not(carrying ?p ?f))
            (at ?f ?l)
      )
  )
  (:action cut-vegetables
    :parameters (?p - person ?f - food ?l - location)
    :precondition (and
      (at ?f ?l)
      (next-to ?p ?l)
      (not (vegetables-cut ?f))
      (can-cut ?l)
    )
    :effect (vegetables-cut ?f)
  )

  (:action cook
    :parameters (?p - person ?f - food ?l - location)
    :precondition (and
      (at ?f ?l)
      (vegetables-cut ?f)
      (not (cooked ?f))
      (can-cook ?l)
    )
    :effect (cooked ?f)
  )

  (:action serve
    :parameters (?p - person ?f - food ?l - location)
    :precondition (and
      (at ?f ?l)
      (next-to ?p ?l)
      (can-serve ?l)
    )
    :effect (served ?f)
  )
)

