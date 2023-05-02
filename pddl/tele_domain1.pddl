(define (domain telepresence)
  (:requirements 	:strips 
			:typing
			:equality
			:negative-preconditions
			:disjunctive-preconditions
  )
  (:types 	
		world_model_robot
                world_model_object_light
		world_model_object
		world_model_human
		world_model_location
		world_model_meeting_room
		robot_actuation
		robot_perception
                human_actuation
  )
  (:predicates 	(battery_charge_location ?r - world_model_robot)
		(before_room_entry_location ?r - world_model_robot)
		(inside_meeting_room_location ?r - world_model_robot)
		(robot_on ?r - world_model_robot)

		(meeting_door_locked ?d - world_model_object)
		(lights_on ?l - world_model_object_light)
		(meeting_mode_on ?r - world_model_robot)
		(communication_on ?c - world_model_communication)

		(human_actuation_request ?admin - world_model_human)
  )
  (:action activate_robot
              :parameters (?robot - world_model_robot)
	      :precondition ( not (robot_on ?robot)  )		
	      :effect (robot_on ?robot)
  )
  (:action transit_battery_charge_loc_to_room_entry_loc
	:parameters (?robot - world_model_robot)
        :precondition (and (battery_charge_location ?robot)
		           (robot_on ?robot)
		      )
	:effect (before_room_entry_location ?robot)
  )
  (:action open_locked_door_alert
	:parameters (?robot - world_model_robot
		     ?door -  world_model_object
		     ?admin - world_model_human
		    )
        :precondition (and (before_room_entry_location ?robot)
			   (meeting_door_locked ?door)
		      )
	:effect (human_actuation_request ?admin)
  )
  (:action unlock_door_human_actuation  ; later this can be encoded as missing robot capability
	:parameters (?robot - world_model_robot
		     ?door -  world_model_object
		     ?admin - world_model_human
		     )
	:precondition (and (before_room_entry_location ?robot)
			(meeting_door_locked ?door)
			(human_actuation_request ?admin)
		      )
	:effect ( not(meeting_door_locked ?door) )
  )
 (:action enter_meeting_door
	:parameters (?robot - world_model_robot
		     ?door -  world_model_object
		    )
        :precondition (and (before_room_entry_location ?robot)
		          (not (meeting_door_locked ?door))
		      )
	:effect (inside_meeting_room_location ?robot)
  )
(:action switch_on_communication
	:parameters (?robot - world_model_robot
		     ?comm - world_model_communication
		    )
        :precondition (and (inside_meeting_room_location ?robot)
		          (not  (communication_on ?comm))
		      )
	:effect (communication_on ?comm)
  )
 (:action switch_on_light
	:parameters (?robot - world_model_robot
		     ?room_light - world_model_object_light
		    )
        :precondition (and (inside_meeting_room_location ?robot)
		          (not  (lights_on ?room_light))
		      )
	:effect (lights_on ?room_light)
  )

  (:action activate_meeting_mode
           :parameters (?robot - world_model_robot
			?meeting_door - world_model_object
			?room_light - world_model_object_light
			?comm - world_model_communication)
           :precondition (and	(inside_meeting_room_location ?robot)
			        (not (meeting_mode_on ?robot))
                                (lights_on ?room_light)
				(communication_on ?comm)
			 )
           :effect 
           (meeting_mode_on ?robot)
  )
)
