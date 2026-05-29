from collections.abc import AsyncIterator
from typing import Any, Self

class DictCursor: ...

class Cursor:
    async def execute(
        self, query: str, args: tuple[Any, ...] | None = None
    ) -> int: ...
    async def fetchall(self) -> list[dict[str, Any]]: ...
    async def __aenter__(self) -> Self: ...
    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: object,
    ) -> None: ...

class Connection:
    def cursor(self, cursorclass: type[DictCursor] = DictCursor) -> Cursor: ...
    async def __aenter__(self) -> Self: ...
    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: object,
    ) -> None: ...

class _AcquireContextManager:
    async def __aenter__(self) -> Connection: ...
    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: object,
    ) -> None: ...

class Pool:
    def acquire(self) -> _AcquireContextManager: ...
    def close(self) -> None: ...
    async def wait_closed(self) -> None: ...

async def create_pool(
    *,
    host: str = "127.0.0.1",
    port: int = 3306,
    user: str = "root",
    password: str = "",
    db: str | None = None,
    autocommit: bool = False,
    minsize: int = 1,
    maxsize: int = 10,
) -> Pool: ...
