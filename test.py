from intake import open_catalog
local = open_catalog('catalog.yml')
local.example.read()
remote = open_catalog('intake://localhost:5000')
remote.example.read()
