import torch
import torch.nn as nn

# Define the vocabulary size and the embedding size
vocab_size = 7 # Number of tasks
embed_size = 10 # Arbitrary dimension

# Define the RNN cell
rnn = nn.RNNCell(embed_size, embed_size)

# Define an embedding layer to map one-hot vectors to embeddings
embedding = nn.Embedding(vocab_size, embed_size)

# Define a linear layer to map embeddings to logits
linear = nn.Linear(embed_size, vocab_size)

# Define a softmax layer to get probabilities from logits
softmax = nn.Softmax(dim=1)

# Define a list of tasks as one-hot vectors
tasks = [
    [1, 0, 0, 0, 0, 0, 0], # Making coffee
    [0, 1, 0, 0, 0, 0, 0], # Preparing breakfast
    [0, 0, 1, 0, 0, 0, 0], # Cleaning the dishes
    [0, 0, 0, 1, 0, 0, 0], # Wiping the countertops
    [0, 0, 0, 0, 1, 0, 0], # Sweeping and mopping the floor
    [0, 0, 0, 0, 0, 1, 0], # Taking out the trash
    [0, 0, 0, 0, 0, 0, 1] # Making the bed
]

# Convert the list of tasks to a tensor of shape (sequence_length, batch_size=1,
# vocab_size)
tasks = torch.tensor(tasks).unsqueeze(1).float()

# Initialize the hidden state to zeros
hidden = torch.zeros(1, embed_size)

# Loop over the sequence of tasks
for i in range(len(tasks)):
    # Get the current task as an embedding
    input = embedding(tasks[i].argmax(dim=2))
    
    # Pass the input and hidden state to the RNN cell
    hidden = rnn(input.squeeze(1), hidden)
    
    # Pass the hidden state to the linear layer and get logits
    output = linear(hidden)
    
    # Pass the logits to the softmax layer and get probabilities
    probs = softmax(output)
    
    # Print the probabilities of each task as the next task
    print(probs)