import hashlib


def md5ext(path: str) -> str:
    return hashlib.md5(open(path, "rb").read()).hexdigest()


def extension_from_path(path: str) -> str:
    return path.split("/")[-1].split(".")[-1]


def filename_from_path(path: str) -> str:
    return ".".join(path.split("/")[-1].split(".")[:-1])


def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])
