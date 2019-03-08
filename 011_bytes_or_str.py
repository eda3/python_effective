def to_str(bytes_or_str):
    """

    :param bytes_or_str:
    :return: value:
    """
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode("utf-8")
    else:
        value = bytes_or_str
    return value # instance of "str"


def to_bytes(bytes_or_str):
    """

    :param bytes_or_str:
    :return: value:
    """
    if isinstance(bytes_or_str):
        value = bytes_or_str.encode("utf-8")
    else:
        value = bytes_or_str
    return value # instance of "bytes"