from fuel.datasets import H5PYDataset
from fuel.utils import find_in_data_path


class SubredditTopPhotosFeatures22(H5PYDataset):
    filename = 'subreddittopphotos_features.hdf5'

    def __init__(self, which_sets, **kwargs):
        kwargs.setdefault('load_in_memory', True)
        super(SubredditTopPhotosFeatures22, self).__init__(
            file_or_path=find_in_data_path(self.filename),
            which_sets=which_sets,
            **kwargs)

