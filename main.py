
from torch.utils.data import DataLoader
from torchvision import transforms
from tqdm import tqdm

from utils import RedEdgeDataset, ndvi


# Initialize Dataset & Dataloader
dataset = RedEdgeDataset(data_dir="data/",
                         transform=transforms.ToTensor())
dataloader = DataLoader(dataset=dataset,
                        batch_size=1,
                        shuffle=False)

for ite, images in enumerate(dataloader):
    print(ite)
    ndvi_value = ndvi(images)
    print(ndvi_value)
    input()
    

