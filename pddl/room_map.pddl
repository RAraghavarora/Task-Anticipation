(define (problem room-planning)
  (:domain room-planning)

  (:objects
    knife laptop pillow soap - object
    kitchen home_office bedroom bathroom - room
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
    (adjacent kitchen home_office)
    (adjacent home_office kitchen)
    (adjacent home_office bedroom)
    (adjacent bedroom home_office)
    (adjacent bedroom bathroom)
    (adjacent bathroom bedroom)
    (at knife bedroom)
    (at laptop home_office)
    (at pillow kitchen)
    (at soap home_office))

(:goal
    (and
        (at knife kitchen)
        (at laptop home_office)
        (at pillow bedroom)
        (at soap bathroom)))

)