import numpy as np

routine_day_1 = {
    "7:00 AM": "Make the bed",
    "8:00 AM": "Clean the kitchen appliances",
    "9:00 AM": "Vacuum the house",
    "10:00 AM": "Water the plants",
    "11:00 AM": "Load dirty clothes",
    "12:00 PM": "Run the washing machine",
    "1:00 PM": "Prepare lunch",
    "2:00 PM": "Serve lunch",
    "3:00 PM": "Dry the clothes",
    "4:00 PM": "Iron the clothes",
    "5:00 PM": "Fold the clothes",
    "6:00 PM": "Clean the windows",
    "7:00 PM": "Prepare dinner",
    "8:00 PM": "Serve dinner",
    "9:00 PM": "Put leftover food in fridge",
    "10:00 PM": "Close lights for all the rooms"
}
routine_day_2 = {
    "7:00 AM": "Make the bed",
    "8:00 AM": "Prepare Breakfast",
    "9:00 AM": "Serve Breakfast",
    "10:00 AM": "Mop the floors",
    "11:00 AM": "Load dirty clothes",
    "12:00 PM": "Run the washing machine",
    "1:00 PM": "Prepare lunch",
    "2:00 PM": "Serve lunch",
    "3:00 PM": "Clean the kitchen counters",
    "4:00 PM": "Clean dirty dishes in the sink",
    "5:00 PM": "Serve cookies and warm milk",
    "6:00 PM": "Clean the windows",
    "7:00 PM": "Prepare dinner",
    "8:00 PM": "Serve dinner",
    "9:00 PM": "Throw away spoilt food",
    "10:00 PM": "Take out the trash"
}
routine_day_3 = {
    "7:00 AM": "Open Curtains",
    "8:00 AM": "Clean the kitchen appliances",
    "9:00 AM": "Dust the furniture",
    "10:00 AM": "Water the plants",
    "11:00 AM": "Load dirty clothes",
    "12:00 PM": "Run the washing machine",
    "1:00 PM": "Prepare lunch",
    "2:00 PM": "Serve lunch",
    "3:00 PM": "Clean the kitchen counters",
    "4:00 PM": "Clean dirty dishes in the sink",
    "5:00 PM": "Run the dishwasher",
    "6:00 PM": "Clean the windows",
    "7:00 PM": "Prepare dinner",
    "8:00 PM": "Serve dinner",
    "9:00 PM": "Collect dishes from dishwasher",
    "10:00 PM": "Remove expired food from fridge"
}
routine_day_4 = {
    "7:00 AM": "Make the bed",
    "8:00 AM": "Prepare Breakfast",
    "9:00 AM": "Serve Breakfast",
    "10:00 AM": "Mop the floors",
    "11:00 AM": "Load dirty clothes",
    "12:00 PM": "Run the washing machine",
    "1:00 PM": "Prepare lunch",
    "2:00 PM": "Serve lunch",
    "3:00 PM": "Clean the kitchen counters",
    "4:00 PM": "Add dishes to dishwasher",
    "5:00 PM": "Run the dishwasher",
    "6:00 PM": "Clean the windows",
    "7:00 PM": "Prepare dinner",
    "8:00 PM": "Serve dinner",
    "9:00 PM": "Put leftover food in fridge",
    "10:00 PM": "Close lights for all the rooms"
}
routine_day_5 = {
    "7:00 AM": "Make the bed",
    "8:00 AM": "Clean the kitchen appliances",
    "9:00 AM": "Dust the furniture",
    "10:00 AM": "Mop the floors",
    "11:00 AM": "Load dirty clothes",
    "12:00 PM": "Run the washing machine",
    "1:00 PM": "Prepare lunch",
    "2:00 PM": "Serve lunch",
    "3:00 PM": "Dry the clothes",
    "4:00 PM": "Clean dirty dishes in the sink",
    "5:00 PM": "Serve cookies and warm milk",
    "6:00 PM": "Clean the windows",
    "7:00 PM": "Prepare dinner",
    "8:00 PM": "Serve dinner",
    "9:00 PM": "Put leftover food in fridge",
    "10:00 PM": "Close lights for all the rooms"
}
routine_day_6 = {
    "7:00 AM": "Make a cup of coffee",
    "8:00 AM": "Clean the kitchen appliances",
    "9:00 AM": "Vacuum the house",
    "10:00 AM": "Mop the floors",
    "11:00 AM": "Load dirty clothes",
    "12:00 PM": "Run the washing machine",
    "1:00 PM": "Prepare lunch",
    "2:00 PM": "Serve lunch",
    "3:00 PM": "Dry the clothes",
    "4:00 PM": "Add dishes to dishwasher",
    "5:00 PM": "Run the dishwasher",
    "6:00 PM": "Clean the windows",
    "7:00 PM": "Prepare dinner",
    "8:00 PM": "Serve dinner",
    "9:00 PM": "Collect dishes from dishwasher",
    "10:00 PM": "Remove expired food from fridge"
}
routine_day_7 = {
    "7:00 AM": "Clean the bathroom",
    "8:00 AM": "Clean the kitchen appliances",
    "9:00 AM": "Dust the furniture",
    "10:00 AM": "Collect dirty clothes",
    "11:00 AM": "Load dirty clothes",
    "12:00 PM": "Run the washing machine",
    "1:00 PM": "Prepare lunch",
    "2:00 PM": "Serve lunch",
    "3:00 PM": "Clean the kitchen counters",
    "4:00 PM": "Clean dirty dishes in the sink",
    "5:00 PM": "Serve cookies and warm milk",
    "6:00 PM": "Clean the windows",
    "7:00 PM": "Prepare dinner",
    "8:00 PM": "Serve dinner",
    "9:00 PM": "Put leftover food in fridge",
    "10:00 PM": "Take out the trash"
}
all_activities = list(routine_day_1.values()) + list(routine_day_2.values()) + list(routine_day_3.values()) + list(routine_day_4.values()) + list(routine_day_5.values()) + list(routine_day_6.values()) + list(routine_day_7.values())

# Step 2: Compute Transition Probabilities
transition_counts = {}
for i in range(len(all_activities) - 1):
    current_task = all_activities[i]
    next_task = all_activities[i+1]
    if current_task not in transition_counts:
        transition_counts[current_task] = {}
    if next_task not in transition_counts[current_task]:
        transition_counts[current_task][next_task] = 0
    transition_counts[current_task][next_task] += 1

transition_probabilities = {}
for current_task, next_tasks in transition_counts.items():
    total_count = sum(next_tasks.values())
    transition_probabilities[current_task] = {next_task: count / total_count for next_task, count in next_tasks.items()}

# Step 3: Define the Transition Probability Matrix
seen = set()
tasks = [x for x in all_activities if x not in seen and not seen.add(x)]

num_tasks = len(tasks)
transition_matrix = np.zeros((num_tasks, num_tasks))

for i, task1 in enumerate(tasks):
    if task1 in transition_probabilities:
        for j, task2 in enumerate(tasks):
            if task2 in transition_probabilities[task1]:
                transition_matrix[i, j] = transition_probabilities[task1][task2]

# Step 4: Run the MCMC Algorithm
sequence_length = 16
initial_task = "Open Curtains"
sequence = [initial_task]

for _ in range(sequence_length - 1):
    current_task_index = tasks.index(sequence[-1])
    next_task_index = np.random.choice(num_tasks, p=transition_matrix[current_task_index])
    next_task = tasks[next_task_index]
    sequence.append(next_task)

# Print the generated sequence
import pprint
pprint.pprint(sequence)

import numpy as np
import matplotlib.pyplot as plt

# Assuming you have the following variables defined:
# transition_probabilities: Dictionary of transition probabilities
# tasks: List of unique tasks
# transition_matrix: Transition probability matrix

# Plot Transition Probabilities
plt.figure(figsize=(8, 6))
plt.imshow(transition_matrix.T, cmap='Wistia')
plt.xticks(np.arange(len(tasks)), range(len(tasks)), rotation=90)
plt.yticks(np.arange(len(tasks)), tasks)
plt.colorbar(label='Transition Probability')
plt.title('Transition Probability Matrix')
# plt.xlabel('Next Task')
# plt.ylabel('Current Task')
plt.tight_layout()
plt.grid()
plt.savefig('fig1.png')

# Plot Task Sequence Distribution
task_counts = [sum(transition_probabilities.get(task, {}).values()) for task in tasks]

plt.figure(figsize=(8, 6))
plt.bar(tasks, task_counts)
plt.title('Task Sequence Distribution')
plt.xlabel('Task')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.savefig('fig2.png')

import pdb; pdb.set_trace()