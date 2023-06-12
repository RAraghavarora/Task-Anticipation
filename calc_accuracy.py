def accuracy_check(routines, ground_truth):
    accuracies = []
    for routine in routines:
        matches = 0
        for time, task in routine.items():
            if time in ground_truth and ground_truth[time] == task:
                matches += 1
        accuracy = matches / len(ground_truth)
        accuracies.append(accuracy)
    return accuracies


routines_day_6 = [
{ 
'7:00 AM': 'Open Curtains',
'8:00 AM': 'Prepare food',
'9:00 AM': 'Serve food',
'10:00 AM': 'Make the bed',
'11:00 AM': 'Water the plants',
'12:00 PM': 'Collect dirty clothes',
'1:00 PM': 'Prepare food',
'2:00 PM': 'Serve food',
'3:00 PM': 'Load dirty clothes',
'4:00 PM': 'Run the washing machine',
'5:00 PM': 'Dry the clothes',
'6:00 PM': 'Vacuum the house',
'7:00 PM': 'Take out the trash',
'8:00 PM': 'Prepare food',
'9:00 PM': 'Serve food',
'10:00 PM': 'Put leftover food in the fridge'
},
{ 
'7:00 AM': 'Prepare food', 
'8:00 AM': 'Serve food', 
'9:00 AM': 'Open Curtains', 
'10:00 AM': 'Make the bed', 
'11:00 AM': 'Water the plants', 
'12:00 PM': 'Prepare food', 
'1:00 PM': 'Serve food', 
'2:00 PM': 'Collect dirty clothes', 
'3:00 PM': 'Load dirty clothes', 
'4:00 PM': 'Run the washing machine', 
'5:00 PM': 'Dry the clothes', 
'6:00 PM': 'Vacuum the house', 
'7:00 PM': 'Take out the trash', 
'8:00 PM': 'Prepare food', 
'9:00 PM': 'Serve food', 
'10:00 PM': 'Put leftover food in the fridge'
},
{
'7:00 AM': 'Open Curtains',
'8:00 AM': 'Prepare food',
'9:00 AM': 'Serve food',
'10:00 AM': 'Make the bed',
'11:00 AM': 'Water the plants',
'12:00 PM': 'Collect dirty clothes',
'1:00 PM': 'Prepare food',
'2:00 PM': 'Serve food',
'3:00 PM': 'Load dirty clothes',
'4:00 PM': 'Run the washing machine',
'5:00 PM': 'Vacuum the house',
'6:00 PM': 'Dry the clothes',
'7:00 PM': 'Take out the trash',
'8:00 PM': 'Prepare food',
'9:00 PM': 'Serve food',
'10:00 PM': 'Put leftover food in the fridge'
},
]

routines_day_7 = [
    
]