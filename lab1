import csv
from operator import itemgetter, mul


def parse_csv(data: str) -> list[dict]:
    return list(csv.DictReader(data.splitlines()))


def compute_revenue(rows: list[dict]) -> float:
    return sum(
        map(
            mul,
            map(float, map(itemgetter("quantity"), rows)),
            map(float, map(itemgetter("price"), rows)),
        ),
        0.0,
    )


def top_item(rows: list[dict]) -> dict | None:
    return max(
        zip(
            map(
                mul,
                map(float, map(itemgetter("quantity"), rows)),
                map(float, map(itemgetter("price"), rows)),
            ),
            rows,
        ),
        key=itemgetter(0),
    )[1]


if __name__ == "__main__":
    print(compute_revenue(parse_csv("item,quantity,price\nApple,10,0.5\nBanana,5,0.3\nCherry,2,3.0\n")))
    print(top_item(parse_csv("item,quantity,price\nApple,10,0.5\nBanana,5,0.3\nCherry,2,3.0\n")))
