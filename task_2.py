import random

def get_numbers_ticket(min_value: int, max_value: int, quantity: int) -> list[int]:
    if min_value < 1:
        return []
    if max_value > 1000:
        return []
    if min_value >= max_value:
        return []
    if quantity < 1:
        return []

    pool_size = max_value - min_value + 1
    if quantity > pool_size:
        return []

    number_pool = range(min_value, max_value + 1)
    numbers = random.sample(number_pool, quantity)

    return sorted(numbers)
