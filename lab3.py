from dataclasses import dataclass
from enum import Enum, auto


class LoadState(Enum):
    LOADING = 1
    SUCCESS = 2
    ERROR = 3


@dataclass(frozen=True)
class User:
    name: str
    age: int
    email: str


@dataclass(frozen=True)
class Success[T]:
    value: T


@dataclass(frozen=True)
class Failure[E]:
    error: E


type Result[T, E] = Success[T] | Failure[E]


def check_users(users: list[User]) -> Result[list[User], str]:
    return Success(users) if users else Failure("Список пользователей пуст")


def load_users() -> Result[list[User], str]:
    return check_users([
        User("Анна", 25, "anna@example.com"),
        User("Борис", 31, "boris@example.com"),
    ])


if __name__ == "__main__":
    print(load_users())
    print(check_users([]))
