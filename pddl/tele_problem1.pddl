(define (problem prob1)	; naming problem as prob1
  (:domain telepresence); using same string name as per domain
  
  (:objects	
		double2 - world_model_robot
                meeting_door1 - world_model_object
		room_light - world_model_object_light
		participant1 admin1 operator1 - world_model_human
		passage1 - world_model_location
		room1 - world_model_meeting_room
		sms_alert1 tele_robot_avatar1 meeting_session1 - robot_actuation
		camera1 - robot_perception
		communication1 - world_model_communication
		)    		; instantiating objects with names
	
  (:init 	
		(battery_charge_location double2)
		(meeting_door_locked meeting_door1)
		(not (lights_on room_light))
		(not (meeting_mode_on tele_robot_avatar1))
		(not (communication_on communication1))
                (not (robot_on double2))
  )			
  ; initial predicate-object state
			
  ;(:goal (meeting_session_on tele_robot_avatar1) ) ; final predicate-object state to start meeting
   (:goal (meeting_mode_on double2) )

 ;(:goal lights_on room_light) ; turn off lights
 ; (not (meeting_mode_on tele_robot_avatar1)) ; close meeting if room empty or asked so
 ; (:goal battery_charge_location double2) ; go to charging location

)

	


