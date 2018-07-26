from setuptools import setup


setup(
    name='azblob',
    version='0.1.0',
    author='Philipp Lang',
    packages=['azblob'],
    url=('https://github.com/plang85/azure_blob_download'),
    license='MIT License',
    description='Download Azure blobs.',
    long_description=open('README.rst').read(),
    classifiers=[
            'Development Status :: 4 - Beta',
            'Programming Language :: Python :: 3.6',
            'License :: OSI Approved :: MIT License',
            'Topic :: Software Development'],
    entry_points={
        'console_scripts': [
            'azblob = azblob.ops:cli'
        ]
    },
    install_requires=[
        "azure-storage-blob>=1.3.0",
        "azure-storage-file>=1.3.0",
        "tqdm>=4.0.0"
    ],
)
