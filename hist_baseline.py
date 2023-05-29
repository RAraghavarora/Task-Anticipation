import numpy as np

daily_activities_1 = {
    "7:00 AM": "Open Curtains",
    "7:30 AM": "Cut fruits for breakfast",
    "8:00 AM": "Serve breakfast on the dining table",
    "8:30 AM": "Clean and make up the bed in the bedroom",
    "9:00 AM": "Water the plants in the living room",
    "9:30 AM": "Load dirty clothes in the washing machine",
    "10:00 AM": "Vacuum the house",
    "10:30 AM": "Collect trash from every room and throw it in the dustbin",
    "11:00 AM": "Collect the newspaper",
    "11:30 AM": "Collect the dirty dishes and move them to the sink",
    "12:00 PM": "Cook vegetables to prepare lunch",
    "12:30 PM": "Serve lunch",
    "1:00 PM": "Clean dirty dishes in the sink",
    "1:30 PM": "Bring book from living room to home office",
    "2:00 PM": "Clean the windows",
    "3:00 PM": "Serve cookies and warm milk",
    "5:00 PM": "Prepare cake mix and put it in the oven for baking",
    "6:30 PM": "Collect the baked cake, cut it down and serve",
    "7:00 PM": "Collect leftover food and store in the fridge",
    "8:00 PM": "Prepare a nutritious vegetarian dinner with green vegetables",
    "8:30 PM": "Serve the dinner",
    "9:00 PM": "Close lights for all the rooms and lock the house"
}

daily_activities_2 = {
    "6:45 AM": "Open Curtains",
    "7:15 AM": "Clean the bed",
    "8:00 AM": "Prepare and serve milk and cereal breakfast with some fruits",
    "8:30 AM": "Load dirty clothes in the washing machine",
    "9:00 AM": "Vacuum the house",
    "9:45 AM": "Collect and dry the washed clothes",
    "10:00 AM": "Wipe down kitchen counter and appliances",
    "10:30 AM": "Water the indoor plants",
    "11:30 AM": "Make a cup of coffee",
    "12:00 PM": "Cook vegetables to prepare lunch",
    "12:30 PM": "Serve lunch",
    "1:00 PM": "Collect and Clean dirty dishes",
    "1:30 PM": "Wipe the counter in the home office",
    "2:00 PM": "Clean the windows",
    "2:30 PM": "Collect leftover food and store in the fridge",
    "3:00 PM": "Collect the dry clothes",
    "3:30 PM": "Iron the clean clothes",
    "5:00 PM": "Fold and put away the clothes",
    "7:00 PM": "Prepare chinese dinner",
    "8:30 PM": "Serve the dinner",
    "9:00 PM": "Close lights for all the rooms."
}
daily_activities_3 = {
    "7:00 AM": "Prepare coffee",
    "7:15 AM": "Make the bed",
    "7:30 AM": "Prepare breakfast",
    "8:00 AM": "Serve breakfast",
    "8:15 AM": "Load dirty dishes into dishwasher",
    "8:45 AM": "Sweep the kitchen floor",
    "9:00 AM": "Vacuum the living room",
    "9:30 AM": "Dust the furniture",
    "10:00 AM": "Take out the trash",
    "10:30 AM": "Water the plants",
    "11:00 AM": "Start the laundry",
    "11:30 AM": "Clean the bathrooms",
    "12:00 PM": "Mop the floors",
    "12:45 AM": "Fold the laundry",
    "1:30 PM": "Put away the laundry",
    "2:00 PM": "Prepare lunch",
    "2:45 PM": "Serve lunch",
    "4:00 PM": "Clean up after lunch",
    "4:30 PM": "Prepare and serve tea",
    "5:00 PM": "Run the dishwasher",
    "6:00 PM": "Take out the trash and recycling",
    "6:30 PM": "Tidy up common areas such as the living room or family room",
    "7:00 PM": "Prepare dinner",
    "7:30 PM": "Serve Dinner",
    "8:00 PM": "Remove spoilt food",
    "8:30 PM": "Close the lights"
}

all_activities = list(daily_activities_1.values()) + list(daily_activities_2.values()) + list(daily_activities_3.values())

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
tasks = list(set(all_activities))
num_tasks = len(tasks)
transition_matrix = np.zeros((num_tasks, num_tasks))

for i, task1 in enumerate(tasks):
    if task1 in transition_probabilities:
        for j, task2 in enumerate(tasks):
            if task2 in transition_probabilities[task1]:
                transition_matrix[i, j] = transition_probabilities[task1][task2]

# Step 4: Run the MCMC Algorithm
sequence_length = 10
initial_task = "Open Curtains"
sequence = [initial_task]

for _ in range(sequence_length - 1):
    current_task_index = tasks.index(sequence[-1])
    next_task_index = np.random.choice(num_tasks, p=transition_matrix[current_task_index])
    next_task = tasks[next_task_index]
    sequence.append(next_task)

# Print the generated sequence
print(sequence)
