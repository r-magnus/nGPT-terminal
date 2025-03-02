# Train a miniature character-level GPT model on UNIX command dataset

# Setup
import torch

out_dir = 'out-unix-char'
eval_interval = 250  # Evaluate periodically to monitor training
eval_iters = 200
log_interval = 10  # Log progress frequently

# Save only when validation improves
always_save_checkpoint = False

wandb_log = False  # Set to True if using Weights & Biases
wandb_project = 'unix-char'
wandb_run_name = 'mini-gpt-unix'

dataset = 'man-data'
gradient_accumulation_steps = 1
batch_size = 64  # Number of sequences per batch
block_size = 256  # Maximum context length (characters)

# Model architecture
n_layer = 6  # Number of transformer layers
n_head = 6  # Number of attention heads
n_embd = 384  # Embedding dimension
dropout = 0.2  # Dropout rate

# Optimization
learning_rate = 1e-3  # Initial learning rate
max_iters = 5000  # Total training iterations
lr_decay_iters = 5000  # Apply learning rate decay over the full training cycle
min_lr = 1e-4  # Minimum learning rate
beta2 = 0.99  # Adam optimizer beta2 parameter for small token counts
warmup_iters = 100  # Gradual warmup of the learning rate

# Device settings
device = 'cuda' if torch.cuda.is_available() else 'cpu'  # Use GPU if available, otherwise CPU
compile = False  # Set to True if using PyTorch 2.0+ for model compilation
