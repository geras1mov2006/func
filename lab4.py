from functools import partial


def matches(key, value, item):
    return key in item and item[key] == value


def filter_by(key):
    return lambda value: lambda items: list(
        filter(partial(matches, key, value), items)
    )


def apply_filter(key, value, items):
    return filter_by(key)(value)(items)


def filter_by_category(value, items):
    return partial(apply_filter, "category")(value, items)


def greater_than(threshold):
    return lambda x: x > threshold


def numbers_above(threshold, numbers):
    return filter(greater_than(threshold), numbers)


def main(products, numbers):
    print(filter_by("name")("Chair")(products))
    print(filter_by_category("electronics", products))
    print(list(numbers_above(10, numbers)))


main(
    [
        {"name": "Keyboard", "category": "electronics"},
        {"name": "Chair", "category": "furniture"},
        {"name": "Mouse", "category": "electronics"},
    ],
    [18, 4, 25, 10, 7],
)
