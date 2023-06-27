(define (problem cookingprob)
  (:domain household)

  (:objects
    vegetables milk - food
    fridge cutting-board stove dining_table - location
    agent47 - person
  )

  (:init
      (can-cut cutting-board)
      (can-cook stove)
      (can-serve dining_table)
      (at-loc vegetables fridge)
      (at-loc milk fridge)
      (not(cooked vegetables))
      (next-to agent47 stove)    
  )

  (:goal
    (and
      (cooked vegetables)
      (served vegetables)
      (served milk)
    )
  )

  (:metric minimize (total-time))

)