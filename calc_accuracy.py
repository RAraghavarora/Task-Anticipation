import re
import ast

def calculate_time_difference(predicted, ground_truth):
    '''
    predicted, ground_truth: dictionaries
    '''
    time_difference = 0
    total_time_slots = len(ground_truth)

    for time_slot in ground_truth:
        predicted_task = predicted.get(time_slot)
        ground_truth_task = ground_truth.get(time_slot)

        if predicted_task == ground_truth_task:
            continue

        gt_time = next((key for key, val in ground_truth.items() if val == predicted_task), None) # Get the time slot where the predicted task is actually scheduled
        if not gt_time:
            # Predicted task is not in gt
            # print(ground_truth_task)
            continue
        time_difference += abs(list(predicted.keys()).index(time_slot) - list(ground_truth.keys()).index(gt_time))
        # print(time_slot, '\t', time_difference)

    average_time_difference = time_difference / total_time_slots
    normalized_time_difference = average_time_difference / total_time_slots 

    return normalized_time_difference


def accuracy_check(predicted, ground_truth):
    '''
    predicted, ground_truth: list of dictionaries
    '''
    accuracies = []
    for predicted_routine, gt_routine in zip(predicted, ground_truth):
        matches = 0
        for time, task in predicted_routine.items():
            if time in gt_routine and gt_routine[time] == task:
                matches += 1
        accuracy = matches / len(ground_truth)
        accuracies.append(accuracy)
    return accuracies




predicted = []
ground_truth = []


for _ in range(5):
    routine_day_7 = {}
    gt = {}
    with open('gpt_prompts/%d.txt'%(_), 'r') as file:
        content = file.read()
        
        # Extract routine_day_7
        matches = re.findall(r'routine_day_7\s*=\s*{([^}]*)}', content)
        if matches:
            routine_day_7 = ast.literal_eval("{" + matches[0] + "}")
        
        # Extract ground_truth
        matches = re.findall(r'ground_truth\s*=\s*{([^}]*)}', content)
        if matches:
            gt = ast.literal_eval("{" + matches[0] + "}")
    
    predicted.append(routine_day_7)
    ground_truth.append(gt)

acc = accuracy_check(predicted, ground_truth)

print("Accuracy = ", sum(acc)/len(acc))

eff = []
for predicted, ground_truth in zip(predicted, ground_truth):
    efficiency = calculate_time_difference(predicted, ground_truth)
    eff.append(1-efficiency)

print('efficiency = ', sum(eff)/len(eff))