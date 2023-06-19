# Dictionary to store the possible tasks for each time slot
routine_day = {
    '7:00 AM': [
        'Open Curtains',
        'Make the bed',
        'Clean the bathroom',
        'Make a cup of coffee'
    ],
    '8:00 AM': [
        'Prepare Breakfast',
        'Clean the kitchen appliances'
    ],
    '9:00 AM': [
        'Serve Breakfast',
        'Vacuum the house',
        'Dust the furniture'
    ],
    '10:00 AM': [
        'Mop the floors',
        'Collect dirty clothes',
        'Water the plants'
    ],
    '11:00 AM': [
        'Clean the fridge',
        'Load dirty clothes'
    ],
    '12:00 PM': [
        'Run the washing machine'
    ],
    '1:00 PM': [
        'Prepare lunch'
    ],
    '2:00 PM': [
        'Serve lunch'
    ],
    '3:00 PM': [
        'Clean the kitchen counters',
        'Dry the clothes'
    ],
    '4:00 PM': [
        'Iron the clothes',
        'Clean dirty dishes in the sink',
        'Add dishes to dishwasher'
    ],
    '5:00 PM': [
        'Fold the clothes',
        'Serve cookies and warm milk',
        'Run the dishwasher'
    ],
    '6:00 PM': [
        'Put the clothes in the closet',
        'Clean the windows'
    ],
    '7:00 PM': [
        'Prepare dinner'
    ],
    '8:00 PM': [
        'Serve dinner'
    ],
    '9:00 PM': [
        'Collect dishes from dishwasher',
        'Put leftover food in fridge',
        'Throw away spoilt food'
    ],
    '10:00 PM': [
        'Take out the trash',
        'Collect the dirty dishes',
        'Close lights for all the rooms',
        'Remove expired food from fridge'
    ]
}

import random
import pprint
import json


for _ in range(10):
    new_dict = {}
    # Assign random tasks to each time slot
    for time_slot in routine_day:
        tasks = routine_day[time_slot]
        new_dict[time_slot] = random.choice(tasks)

    # import pdb; pdb.set_trace()

    # Print the resulting dictionary

    print('routine_day_%d = '%(_+1), end='')
    print(json.dumps(new_dict, indent=4, sort_keys=False))