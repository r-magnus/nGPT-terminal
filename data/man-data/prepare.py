"""
Maps characters of unix_commands.txt to ints.
"Will save train.bin, val.bin containing the ids, and meta.pkl containing the
encoder and decoder and some other related info."
"""
import os
import pickle
import numpy as np

# Define paths
base_dir = os.path.dirname(__file__)
input_file_path = os.path.join(base_dir, 'unix_commands.txt')

# Read dataset
with open(input_file_path, 'r', encoding='utf-8') as f:
    data = f.read()
print(f"Length of dataset in characters: {len(data):,}")

# Get unique characters in dataset
chars = sorted(list(set(data)))
vocab_size = len(chars)
print("All unique characters:", ''.join(chars))
print(f"Vocab size: {vocab_size:,}")

# Create character-to-integer mappings
stoi = {ch: i for i, ch in enumerate(chars)}
itos = {i: ch for i, ch in enumerate(chars)}

# Encoding and decoding functions
def encode(s):
    return [stoi[c] for c in s]  # Convert string to list of integers

def decode(l):
    return ''.join([itos[i] for i in l])  # Convert list of integers to string

# Split dataset into training and validation sets (90% train, 10% validation)
n = len(data)
train_data = data[:int(n * 0.9)]
val_data = data[int(n * 0.9):]

# Encode both splits to integer sequences
train_ids = np.array(encode(train_data), dtype=np.uint16)
val_ids = np.array(encode(val_data), dtype=np.uint16)

print(f"Train dataset has {len(train_ids):,} tokens")
print(f"Validation dataset has {len(val_ids):,} tokens")

# Save encoded data to binary files
train_ids.tofile(os.path.join(base_dir, 'train.bin'))
val_ids.tofile(os.path.join(base_dir, 'val.bin'))

# Save metadata for encoding/decoding later
meta = {
    'vocab_size': vocab_size,
    'itos': itos,
    'stoi': stoi,
}
with open(os.path.join(base_dir, 'meta.pkl'), 'wb') as f:
    pickle.dump(meta, f)

print("Dataset processing complete! Generated 'train.bin', 'val.bin', and 'meta.pkl'.")

# Length of dataset in characters: 811,261
# All unique characters:
# !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~©´×‐–—‘’“”•≤≥─⟨⟩
# Vocab size: 112
# Train dataset has 730,134 tokens
# Validation dataset has 81,127 tokens