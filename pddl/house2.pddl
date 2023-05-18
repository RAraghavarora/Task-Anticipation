(define (domain house)
  (:requirements :strips :typing :negative-preconditions)
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

  (:action make-coffee
    :parameters (?p - person ?m - mug ?cm - coffee-machine ?cp - coffee-powder)
    :precondition (and
      (clean ?m)
      (full ?cm)
      (full ?cp)
      (empty ?m)
    )
    :effect (and
      (not (empty ?m))
      (not (full ?cm))
      (not (full ?cp))
      (not (clean ?m))
    )
  )

  (:action prepare-dinner
    :parameters (?p - person ?s - stove ?pt - pot ?f - food)
    :precondition (and
      (clean ?pt)
      (not (on ?pt ?s))
    )
    :effect (and
      (cooked ?f)
      (not (clean ?pt))
    )
  )

  (:action serve-dinner
    :parameters (?p - person ?pl - plate ?f - food)
    :precondition (and
        (cooked ?f)
        (not (served ?f))
    )
    :effect (and
        (served ?f)
    )
)

(:action clean-dishes
    :parameters (?p - person ?c - item)
    :precondition (and
        (not (clean ?c))
    )
    :effect (and
        (clean ?c)
    )
)

(:action collect-clothes
    :parameters (?p - person ?cl - clothes)
    :precondition (and
        (not (collected ?cl))
    )
    :effect (and
        (collected ?cl)
    )
)

(:action load-laundry
    :parameters (?p - person ?cl - clothes ?w - washer)
    :precondition (and
        (collected ?cl)
        (not (loaded ?cl ?w))
    )
    :effect (and
        (loaded ?cl ?w)
        (not (collected ?cl))
    )
)

(:action wash-clothes
    :parameters (?p - person ?cl - clothes ?w - washer)
    :precondition (and
        (loaded ?cl ?w)
    )
    :effect (and
        (washed ?cl)
        (not (loaded ?cl ?w))
    )
)

)