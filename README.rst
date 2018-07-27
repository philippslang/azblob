Azure Blob
==========

.. image:: https://img.shields.io/badge/code%20style-black.000000.svg
 :target: https://github.com/ambv/black

One-line CLI to download from Azure blob storage. Supports private blobs.


Installation
------------

To install:

.. code-block: bash

    $ pip install azblob

CLI
---

Using credentials from environment

.. code-block:: bash

    $ export AZBLOB_ACCOUNTNAME=xxx
    $ export AZBLOB_ACCOUNTKEY=yyy
    $ # downloads 'blob' from 'container' to cwd
    $ azblob download my_container my_blob


Using credentials from command line

.. code-block:: bash

    $ # using account 'xxx' with access key 'yyy'
    $ # downloads 'blob' from 'container' to cwd
    $ azblob -n xxx -k yyy download my_container my_blob
