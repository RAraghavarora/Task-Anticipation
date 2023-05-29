(define (domain household-tasks)
  (:requirements :strips :typing :durative-actions :negative-preconditions)
  (:types
    mug coffee-machine coffee-powder - item
    plate stove pot food - item
    person - agent
    clothes washer - object
  )
  (:predicates
    (clean ?c - item)
    (empty ?c - item)
    (full ?c - item)
    (on ?i - item ?s - stove)
    (cooked ?f - food)
    (served ?f - food)
    (collected ?cl - clothes)
    (loaded ?cl - clothes ?w - washer)
    (washed ?cl - clothes)
  )

  (:durative-action make-coffee
    :parameters (?p - person ?m - mug ?cm - coffee-machine ?cp - coffee-powder)
    :duration (= ?duration 5)
    :condition (and
      (at start (clean ?m))
      (at start (full ?cm))
      (at start (full ?cp))
      (at start (empty ?m))
    )
    :effect (and
      (at end (not (empty ?m)))
      (at end (not (full ?cm)))
      (at end (not (full ?cp)))
      (at end (not (clean ?m)))
    )
  )

  (:durative-action prepare-dinner
    :parameters (?p - person ?s - stove ?pt - pot ?f - food)
    :duration (= ?duration 10)
    :condition (and
      (at start (clean ?pt))
      (at start (not (on ?pt ?s)))
    )
    :effect (and
      
      (at end (cooked ?f))
      (at end (not (clean ?pt)))
    )
  )

  (:durative-action serve-dinner
    :parameters (?p - person ?pl - plate ?f - food)
    :duration (= ?duration 2)
    :condition (and
        (at start (cooked ?f))
        (at start (not (served ?f)))
    )
    :effect (and
        (at end (served ?f))
    )
)

(:durative-action clean-dishes
    :parameters (?p - person ?c - item)
    :duration (= ?duration 3)
    :condition (and
        (at start (not (clean ?c)))
    )
    :effect (and
        (at end (clean ?c))
    )
)

(:durative-action collect-clothes
    :parameters (?p - person ?cl - clothes)
    :duration (= ?duration 4)
    :condition (and
        (at start (not (collected ?cl)))
    )
    :effect (and
        (at end (collected ?cl))
    )
)

(:durative-action load-laundry
    :parameters (?p - person ?cl - clothes ?w - washer)
    :duration (= ?duration 1)
    :condition (and
        (at start (collected ?cl))
        (at start (not (loaded ?cl ?w)))
    )
    :effect (and
        (at end (loaded ?cl ?w))
        (at end (not (collected ?cl)))
    )
)

(:durative-action wash-clothes
    :parameters (?p - person ?cl - clothes ?w - washer)
    :duration (= ?duration 20)
    :condition (and
        (at start (loaded ?cl ?w))
    )
    :effect (and
        (at end (washed ?cl))
        (at end (not (loaded ?cl ?w)))
    )
)

)