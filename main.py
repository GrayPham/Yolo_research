import torch
import tensorflow as tf
if torch.cuda.is_available():
    print('PyTorch is using the GPU.')
else:
    print('PyTorch is using the CPU.')

print("Tf:")
print('Num GPUs Available: ', len(tf.config.list_physical_devices('GPU')))
