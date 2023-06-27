(define (domain household)
  (:requirements :strips :typing :negative-preconditions :durative-actions)
  (:types 
    location
    food
    person
  )
  (:predicates
    (at-loc ?f - food ?l - location)
    (next-to ?p - person ?l - location)
    (carrying ?p - person ?f - food)
    (vegetables-cut ?f - food)
    (cooked ?f - food)
    (served ?f - food)
    (can-cut ?l - location)
    (can-cook ?l - location)
    (can-serve ?l - location)
  )

  (:durative-action move-to
      :parameters (?p - person ?l1 - location ?l2 - location)
      :duration (= ?duration 5)
      :condition(and
        (at start (next-to ?p ?l1))
        (at start (not (next-to ?p ?l2))) ; Redundant
      )
      :effect(and
        (at start (not(next-to ?p ?l1)))
        (at end (next-to ?p ?l2))
      )
  )

  (:action pick-up
    :parameters (?p - person ?f - food ?l - location)
    :precondition (and
        (at-loc ?f ?l)
        (next-to ?p ?l)
    )
    :effect (and
      (not (at-loc ?f ?l))
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
            (at-loc ?f ?l)
      )
  )
  (:durative-action cut-vegetables
    :parameters (?p - person ?f - food ?l - location)
    :duration (= ?duration 5)
    :condition (and
      (at start (at-loc ?f ?l))
      (at start(next-to ?p ?l))
      (at start (not (vegetables-cut ?f)))
      (over all (can-cut ?l))
    )
    :effect 
    (at end (vegetables-cut ?f))
  )

  (:durative-action cook
    :parameters (?p - person ?f - food ?l - location)
    :duration (= ?duration 10)
    :condition (and
      (at start (at-loc ?f ?l))
      (at start (vegetables-cut ?f))
      (at start (not (cooked ?f)))
      (over all (can-cook ?l))
    )
    :effect 
    (at end (cooked ?f))
  )

  (:action serve
    :parameters (?p - person ?f - food ?l - location)
    :precondition (and
      (at-loc ?f ?l)
      (next-to ?p ?l)
      (can-serve ?l)
    )
    :effect (served ?f)
  )
)

