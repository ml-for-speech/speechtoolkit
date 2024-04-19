import torch


def device_map(device):
    if device == "auto":
        device = "cuda" if torch.cuda.is_available() else "cpu"
    if type(device) == str:
        device = torch.device(device)
    return device
