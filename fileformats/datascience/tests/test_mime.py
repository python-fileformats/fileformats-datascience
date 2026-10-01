from fileformats.core import from_mime
from fileformats.datascience import Pickle__Gzip


def test_native_container_roundtrip() -> None:

    mime = Pickle__Gzip.mime_like
    assert Pickle__Gzip is from_mime(mime)
