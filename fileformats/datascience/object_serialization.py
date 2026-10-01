from fileformats.application import Gzip
from fileformats.core.mixin import WithMagicVersion
from fileformats.generic import BinaryFile


class ObjectSerialisation(BinaryFile): ...


class Pickle(WithMagicVersion, ObjectSerialisation):
    """Python's native byte-encoded serialization format"""

    ext = ".pkl"
    magic_pattern = rb"\x80([\x02-\xff])"
    magic_pattern_maxlength = 2

    @classmethod
    def decode_version(cls, version_bytes: bytes) -> str:
        # The protocol version is stored as the integer value
        # of the byte
        return str(version_bytes[0])


class Pickle__Gzip(Gzip[Pickle]):  # type: ignore[type-arg]
    """Python pickle file that has been gzipped"""

    ext = "pkl.gz"
    alternate_exts = (".pklz",)
    iana_mime = "application/x-pickle+gzip"
