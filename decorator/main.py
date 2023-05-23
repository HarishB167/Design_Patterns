from .stream import Stream
from .cloud_stream import CloudStream
from .encrypted_cloud_stream import EncryptedCloudStream
from .compressed_cloud_stream import CompressedCloudStream

def store_credit_card(stream: Stream):
    stream.write("1234-1234-1234-1234")

if __name__ == "__main__":
    store_credit_card(EncryptedCloudStream(CompressedCloudStream(CloudStream())))
