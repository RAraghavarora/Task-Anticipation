(define (problem room-planning)
  (:domain room-planning)

  (:objects
    knife laptop pillow soap - object
    kitchen home_office bedroom bathroom - room
    Agent47 - agent
  )

  (:init
    (room kitchen)
    (room home_office)
    (room bedroom)
    (room bathroom)
    (object knife)
    (object laptop)
    (object pillow)
    (object soap)
    (agent Agent47)
    (adjacent kitchen home_office)
    (adjacent home_office bedroom)
    (adjacent bathroom bedroom)
    (adjacent kitchen bathroom)
    (adjacent bedroom kitchen)
    (at knife bedroom)
    (at laptop home_office)
    (at pillow kitchen)
    (at soap home_office)
    (in-room Agent47 kitchen)
    )

(:goal
    (and
        (at pillow bedroom)
        (at knife kitchen)
        (at laptop home_office)
        (at soap bathroom)
    )
)

)