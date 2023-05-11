(define (problem laundry-problem)
(:domain household-tasks)
    (:objects
        john - person
        mug1 - mug
        cm1 - coffee-machine
        cp1 - coffee-powder
        plate1 - plate
        stove1 - stove
        pot1 - pot
        food1 - food
        clothes1 clothes2 - clothes
        washer1 - washer
    )
    (:init
        (clean mug1)
        (full cm1)
        (full cp1)
        (empty mug1)
        (clean plate1)
        (clean pot1)
        (not (on pot1 stove1))
    )
    (:goal (and
        (served food1)
        ; (washed clothes1)
        ; (washed clothes2)
    ))
)
