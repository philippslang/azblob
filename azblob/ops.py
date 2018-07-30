import argparse
import logging
import os

from azure.storage.blob import BlockBlobService, PublicAccess

from .auxilliaries import tqdmupto

logger = logging.getLogger("azblob")
logger.setLevel(logging.DEBUG)
console_logger_handler = logging.StreamHandler()
console_logger_handler.setLevel(logging.INFO)
console_logger_formatter = logging.Formatter(
    "%(asctime)s|%(name)s|%(levelname)s::%(message)s", "%m-%d@%H:%M"
)
console_logger_handler.setFormatter(console_logger_formatter)
logger.addHandler(console_logger_handler)


def parse_credentials(accountname, accountkey):
    accountname = accountname or os.environ["AZ_ACCOUNT_NAME"]
    accountkey = accountkey or os.environ.get("AZ_ACCOUNT_KEY")
    return accountname, accountkey


def credentials(f):
    def f_with_credentials(blob, container, accountname=None, accountkey=None):
        accountname, accountkey = parse_credentials(accountname, accountkey)
        logger.info("Azure storage account name: '{}'".format(accountname))
        if accountkey is None:
            logger.info("Using anonymous access.")
        return f(blob, container, accountname, accountkey)

    return f_with_credentials


@credentials
def download(container, blob, accountname=None, accountkey=None):
    block_blob_service = BlockBlobService(
        account_name=accountname, account_key=accountkey
    )
    blob_target = os.path.join(os.getcwd(), blob)
    logger.info("downloading '{}/{}' to '{}'".format(container, blob, blob_target))
    with tqdmupto(total=100, ncols=80) as pbar:

        def update(current, total):
            progress = int(100.0 * (current / total) + 0.5)
            pbar.update_to(progress)

        block_blob_service.get_blob_to_path(
            container, blob, blob_target, progress_callback=update
        )


@credentials
def upload(container, blob, accountname=None, accountkey=None):
    pass


def cli():
    # azblob
    parser = argparse.ArgumentParser(
        description="minimal Azure blob storage operations"
    )
    parser.add_argument("-n", "--accountname", default=None)
    parser.add_argument("-k", "--accountkey", default=None)

    subparsers = parser.add_subparsers(dest="blob_command", help="blob operations")

    # azblob download
    parser_get = subparsers.add_parser("download", help="download blobs")
    parser_get.add_argument("container", help="container name")
    parser_get.add_argument("blob", help="blob name (file name)")

    # azblob upload
    parser_get = subparsers.add_parser("upload", help="upload blobs")
    parser_get.add_argument("container", help="container name")
    parser_get.add_argument("file", help="file name (blob name)")

    args = parser.parse_args()
    logger.info("cli args: {}".format(args))

    if args.blob_command == "download":
        download(args.container, args.blob, args.accountname, args.accountkey)
    elif args.blob_command == "upload":
        upload(args.container, args.blob, args.accountname, args.accountkey)


if __name__ == "__main__":
    cli()
