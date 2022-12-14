import setuptools
import os

build_version = os.environ['BUILD_VERSION']

setuptools.setup(
    name='s3-lib',
    version=build_version,
    description='APIs for managing AWS s3 content',
    packages=['s3_lib'],
    python_requires='>=3.8'
)
