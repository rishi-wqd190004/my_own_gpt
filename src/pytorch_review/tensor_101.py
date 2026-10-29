import torch

tensor0d = torch.tensor(1)

tesnor1d = torch.tensor([1,2,3])

tensor2d = torch.tensor([
    [1,2],
    [3,4]
])

# 3D tensor from a nested pyton list
tensor3d = torch.tensor([[[1,2], [3,4]],
                         [[5,6], [7,8]]])

print(tensor3d.dtype)

# convert dtype of int64 to float32
float_vec_3d = tensor3d.to(torch.float32)
print(float_vec_3d.dtype)