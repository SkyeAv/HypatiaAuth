import hashlib
import secrets
from typing import Self

import redis
import xxhash
from cyclopts import App

CLI: App = App()


class APIKeyGenerator(object):
    def __init__(self: Self, user: str) -> None:
        self.user: str = user
        self.suffix: str = secrets.token_urlsafe(16)

    def make_key(self: Self) -> str:
        suffix: str = self.suffix
        prefix: str = self.user

        api_key: str = f"{prefix}-{suffix}"

        self.api_key: str = api_key
        return api_key

    def set_key(self: Self) -> None:
        r: redis.Redis = redis.Redis("localhost", port=6379, db=0)

        as_bytes: bytes = self.api_key.encode("UTF-8")
        sha256: str = hashlib.sha256(as_bytes).hexdigest()
        hashed: str = xxhash.xxh64(sha256).hexdigest()
        r.set(self.user, hashed)


@CLI.default
def main(username: str) -> None:
    gen: APIKeyGenerator = APIKeyGenerator(username)

    key: str = gen.make_key()
    gen.set_key()

    print("---")
    print("Username:", username)
    print("API Key:", key)
    print("---")
    print(
        "Please securely store your Username And API Key. It will be deleted for security."
    )
    print("---")


if __name__ == "__main__":
    CLI()
