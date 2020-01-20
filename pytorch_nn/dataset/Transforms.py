import torch


class ToTensor(object):
    """Convert ndarrays in sample to Tensors."""

    def __call__(self, sample):
        X, Y = sample['X'], sample['Y']

        return {'X': torch.from_numpy(X).float(),
                'Y': torch.from_numpy(Y).float()}


class YTo2D(object):
    """Convert sample['Y'] from 3D to 2D."""

    def __call__(self, sample):
        X, Y = sample['X'], sample['Y']
        if len(Y.shape) == 3:
            Y = Y[:, :, :2]
        else:
            Y = Y[:, :2]

        return {'X': X,
                'Y': Y}
