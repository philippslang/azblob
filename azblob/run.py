import argparse

from azure.storage.blob import BlockBlobService, PublicAccess


def get():
    pass


def entry():
    parser = argparse.ArgumentParser(prog='azblob')
    subparsers = parser.add_subparsers(help='Download blobs.', dest='blob_command')

    get_parser = subparsers.add_parser('get', help='Download blobs.')
    get_parser.add_argument('-n', '--account_name')
    get_parser.add_argument('-k', '--account_key')

    options = parser.parse_known_args()

    print(options)
    print(options.blob_command)