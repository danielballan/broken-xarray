from intake import open_catalog
local = open_catalog('catalog.yml')
remote = open_catalog('intake://localhost:5000')
uid = '9b24c09f-ef87-4b43-af1c-e89c7e29751e'
remote_run = remote.filled_example[uid]()
remote_ds = remote_run.primary.to_dask()
remote_ds['fccd_image'].compute()  # raises ValueError
