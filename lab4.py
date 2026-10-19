from functools import partial

def matches(key, value, item):
    return key in item and item[key] == value


filter_by = lambda key: lambda value: lambda items: list(
    filter(partial(matches, key, value), items)
)


def apply_filter(key, value, items):
    return filter_by(key)(value)(items)


filter_by_category = partial(apply_filter, "category")


def greater_than(threshold):
    return lambda x: x > threshold


if __name__ == "__main__":
    products = [
        {"name": "Keyboard", "category": "electronics"},
        {"name": "Chair", "category": "furniture"},
        {"name": "Mouse", "category": "electronics"},
    ]

    print(filter_by("name")("Chair")(products))
    print(filter_by_category("electronics", products))

    numbers = [18, 4, 25, 10, 7]
    print(list(filter(greater_than(10), numbers)))
