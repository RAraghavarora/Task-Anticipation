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
  )
  (:action move-to
      :parameters (?p - person ?l1 - location)
      :precondition(not (next-to ?p ?l1))
      :effect(next-to ?p ?l1)
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

  (:action cook-on-stove
    :parameters (?p - person ?f - food ?l - location)
    :precondition (and
      (at ?f ?l)
      (vegetables-cut ?f)
      (not (cooked ?f))
    )
    :effect (cooked ?f)
  )
)

