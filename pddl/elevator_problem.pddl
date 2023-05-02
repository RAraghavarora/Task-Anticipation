(define (problem elevators-problem)
    (:domain elevators)
    (:objects
        floor1 floor2 floor3 floor4 floor5 - num
        rahul raju shyam - passenger
        e1 e2 - elevator
    )
    (:init
        (next floor1 floor2) (next floor2 floor3) (next floor3 floor4) (next floor4 floor5)
        (lift-at e1 floor1) (lift-at e2 floor5)
        (passenger-at rahul floor2) (passenger-at raju floor2) (passenger-at shyam floor4)
    )
    (:goal (and
        (passenger-at rahul floor1)
        (passenger-at raju floor1)
        (passenger-at shyam floor1)
        )
    )
)