import torch

print('GPU IS AVAILABLE:', torch.cuda.is_available())
print('YEEEEAH')
with open('input.txt') as file:
    print(file.readlines())

