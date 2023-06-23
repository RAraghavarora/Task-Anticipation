(define (problem cookingprob)
  (:domain household)

  (:objects
    vegetables milk - food
    fridge cutting-board stove - location
    agent47 - person
  )

  (:init
      (at vegetables fridge)
      (not(cooked vegetables))
      (next-to agent47 stove)
      (can-cut cutting-board)
    )

(:goal
    (cooked vegetables)
)

)