import random

tasks = ['Open Curtains', 'Prepare breakfast', 'Prepare lunch', 'Prepare dinner', 'Serve breakfast', 'Serve lunch', 'Serve dinner', 'Make the bed', 'Water the plants', 'Collect dirty clothes', 'Prepare food', 'Serve food', 'Load dirty clothes', 'Run the washing machine', 'Vacuum the house', 'Dry the clothes', 'Take out the trash', 'Prepare food', 'Serve food', 'Put leftover food in the fridge']

routine_day_1 = {
    '7:00 AM': 'Open Curtains',
    '8:00 AM': 'Prepare breakfast',
    '9:00 AM': 'Serve breakfast',
    '10:00 AM': 'Make the bed',
    '11:00 AM': 'Water the plants',
    '12:00 PM': 'Collect dirty clothes',
    '1:00 PM': 'Prepare lunch',
    '2:00 PM': 'Serve lunch',
    '3:00 PM': 'Load dirty clothes',
    '4:00 PM': 'Run the washing machine',
    '5:00 PM': 'Vacuum the house',
    '6:00 PM': 'Dry the clothes',
    '7:00 PM': 'Take out the trash',
    '8:00 PM': 'Prepare dinner',
    '9:00 PM': 'Serve dinner',
    '10:00 PM': 'Put leftover food in the fridge'
}

routine_day_2 = {
    '7:00 AM': 'Prepare breakfast',
    '8:00 AM': 'Serve breakfast',
    '9:00 AM': 'Open Curtains',
    '10:00 AM': 'Make the bed',
    '11:00 AM': 'Water the plants',
    '12:00 PM': 'Prepare lunch',
    '1:00 PM': 'Serve lunch',
    '2:00 PM': 'Collect dirty clothes',
    '3:00 PM': 'Load dirty clothes',
    '4:00 PM': 'Run the washing machine',
    '5:00 PM': 'Vacuum the house',
    '6:00 PM': 'Dry the clothes',
    '7:00 PM': 'Take out the trash',
    '8:00 PM': 'Prepare dinner',
    '9:00 PM': 'Serve dinner',
    '10:00 PM': 'Put leftover food in the fridge'
}

routine_day_3 = {
    '7:00 AM': 'Open Curtains',
    '8:00 AM': 'Water the plants',
    '9:00 AM': 'Prepare breakfast',
    '10:00 AM': 'Serve breakfast',
    '11:00 AM': 'Collect dirty clothes',
    '12:00 PM': 'Load dirty clothes',
    '1:00 PM': 'Run the washing machine',
    '2:00 PM': 'Dry the clothes',
    '3:00 PM': 'Prepare lunch',
    '4:00 PM': 'Serve lunch',
    '5:00 PM': 'Vacuum the house',
    '6:00 PM': 'Take out the trash',
    '7:00 PM': 'Prepare dinner',
    '8:00 PM': 'Serve dinner',
    '9:00 PM': 'Make the bed',
    '10:00 PM': 'Put leftover food in the fridge',
}

routine_day_4 = {
    '7:00 AM': 'Open Curtains',
    '8:00 AM': 'Make the bed',
    '9:00 AM': 'Water the plants',
    '10:00 AM': 'Prepare breakfast',
    '11:00 AM': 'Serve breakfast',
    '12:00 PM': 'Vacuum the house',
    '1:00 PM': 'Collect dirty clothes',
    '2:00 PM': 'Load dirty clothes',
    '3:00 PM': 'Prepare lunch',
    '4:00 PM': 'Serve lunch',
    '5:00 PM': 'Run the washing machine',
    '6:00 PM': 'Dry the clothes',
    '7:00 PM': 'Take out the trash',
    '8:00 PM': 'Prepare dinner',
    '9:00 PM': 'Serve dinner',
    '10:00 PM': 'Put leftover food in the fridge'
}

routine_day_5 = {
    '7:00 AM': 'Open Curtains',
    '8:00 AM': 'Prepare breakfast',
    '9:00 AM': 'Serve breakfast',
    '10:00 AM': 'Make the bed',
    '11:00 AM': 'Water the plants',
    '12:00 PM': 'Collect dirty clothes',
    '1:00 PM': 'Prepare lunch',
    '2:00 PM': 'Serve lunch',
    '3:00 PM': 'Load dirty clothes',
    '4:00 PM': 'Run the washing machine',
    '5:00 PM': 'Dry the clothes',
    '6:00 PM': 'Vacuum the house',
    '7:00 PM': 'Take out the trash',
    '8:00 PM': 'Prepare dinner',
    '9:00 PM': 'Serve dinner',
    '10:00 PM': 'Put leftover food in the fridge'
}

routine_day_6 = { 
    '7:00 AM': 'Open Curtains', 
    '8:00 AM': 'Water the plants', 
    '9:00 AM': 'Make the bed', 
    '10:00 AM': 'Prepare breakfast', 
    '11:00 AM': 'Serve breakfast', 
    '12:00 PM': 'Vacuum the house', 
    '1:00 PM': 'Collect dirty clothes', 
    '2:00 PM': 'Prepare lunch', 
    '3:00 PM': 'Serve lunch', 
    '4:00 PM': 'Load dirty clothes', 
    '5:00 PM': 'Run the washing machine', 
    '6:00 PM': 'Dry the clothes', 
    '7:00 PM': 'Take out the trash', 
    '8:00 PM': 'Prepare dinner', 
    '9:00 PM': 'Serve dinner', 
    '10:00 PM': 'Put leftover food in the fridge' 
}

routine_day_7 = { 
    '7:00 AM': 'Open Curtains', 
    '8:00 AM': 'Prepare breakfast', 
    '9:00 AM': 'Serve breakfast', 
    '10:00 AM': 'Water the plants', 
    '11:00 AM': 'Make the bed', 
    '12:00 PM': 'Prepare lunch', 
    '1:00 PM': 'Serve lunch', 
    '2:00 PM': 'Vacuum the house', 
    '3:00 PM': 'Collect dirty clothes', 
    '4:00 PM': 'Load dirty clothes', 
    '5:00 PM': 'Run the washing machine', 
    '6:00 PM': 'Dry the clothes', 
    '7:00 PM': 'Take out the trash', 
    '8:00 PM': 'Prepare dinner', 
    '9:00 PM': 'Serve dinner', 
    '10:00 PM': 'Put leftover food in the fridge' 
}


prompt = '''
# Based on following routine, predict a possible task sequence for day 7

tasks = ['Open Curtains', 'Prepare breakfast', 'Prepare lunch', 'Prepare dinner', 'Serve breakfast', 'Serve lunch', 'Serve dinner', 'Make the bed', 'Water the plants', 'Collect dirty clothes', 'Load dirty clothes', 'Run the washing machine', 'Vacuum the house', 'Dry the clothes', 'Take out the trash', 'Put leftover food in the fridge', 'Throw discarded food in the trash']

routine_day_1 = %s

routine_day_2 = %s

routine_day_3 = %s

routine_day_4 = %s

routine_day_5 = %s

routine_day_6 = %s

# Anticipate the output of routine_day_7

routine_day_7 = {
    '7:00 AM': '',
    '8:00 AM': '',
    '9:00 AM': '',
    '10:00 AM': '',
    '11:00 AM': '',
    '12:00 PM': '',
    '1:00 PM': '',
    '2:00 PM': '',
    '3:00 PM': '',
    '4:00 PM': '',
    '5:00 PM': '',
    '6:00 PM': '',
    '7:00 PM': '',
    '8:00 PM': '',
    '9:00 PM': '',
    '10:00 PM': ''
}

'''

for _ in range(100):
    output_file = open('gpt_prompts/%d.txt'%(_), 'w')
    routines = [routine_day_1, routine_day_2, routine_day_3, routine_day_4, routine_day_5, routine_day_6, routine_day_7]
    selected_routines = random.sample(routines, 6)

    remaining_routine = [routine for routine in routines if routine not in selected_routines]

    output_file.write(prompt%tuple(selected_routines))
    output_file.write('\n*************\n')
    output_file.write("ground_truth = " + str(remaining_routine[0]))
    output_file.close()