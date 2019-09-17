import intake
import intake.container
from databroker.intake_xarray_core.base import DataSourceMixin
import xarray


class ExampleDataSource(DataSourceMixin):
    container = 'xarray'
    name = 'example-data-source'
    version = '0.0.1'
    partition_access = True

    def __init__(self, zarr_path, *args, **kwargs):
        self._zarr_path = zarr_path
        self.urlpath = ''  # must be set to satisfy base class
        self._ds = None
        super().__init__(*args, **kwargs)

    def _open_dataset(self):
        if self._ds is None:
            self._ds = xarray.open_zarr(self._zarr_path)


intake.registry['example-data-source'] = ExampleDataSource
intake.container.container_map['example-data-source'] = ExampleDataSource
