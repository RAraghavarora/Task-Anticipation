(define (domain elevators)
    (:requirements :typing)
    (:types elevator passenger num - object)

    (:predicates
        (passenger-at ?person - passenger ?floor - num)
        (boarded ?person - passenger ?lift - elevator)
        (lift-at ?lift - elevator ?floor - num)
        (next ?n1 - num ?n2 - num)
    )

    (:action move-up
        :parameters (?lift - elevator ?cur ?nxt - num)
        :precondition (and 
            (lift-at ?lift ?cur) 
            (next ?cur ?nxt)
        )
        :effect (and 
            (not (lift-at ?lift ?cur)) 
            (lift-at ?lift ?nxt)
        )
    )

    (:action move-down
        :parameters (?lift - elevator ?cur ?nxt - num)
        :precondition (and 
            (lift-at ?lift ?cur) 
            (next ?nxt ?cur)
        )
        :effect (and 
            (not (lift-at ?lift ?cur)) 
            (lift-at ?lift ?nxt)
        )
    )

    (:action board
        :parameters (?person - passenger ?floor - num ?lift - elevator)
        :precondition (and 
            (lift-at ?lift ?floor)
            (passenger-at ?person ?floor)
        )
        :effect (and 
            (not (passenger-at ?person ?floor))
            (boarded ?person ?lift)
        )
    )
    
    (:action leave
        :parameters (?person - passenger ?floor - num ?lift - elevator)
        :precondition (and 
            (lift-at ?lift ?floor)
            (boarded ?person ?lift)
        )
        :effect (and 
            (passenger-at ?person ?floor)
            (not (boarded ?person ?lift))
        )
    )

)