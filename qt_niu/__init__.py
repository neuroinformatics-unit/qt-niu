from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("qt-niu")
except PackageNotFoundError:
    # package is not installed
    pass
