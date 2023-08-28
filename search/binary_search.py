def binary_search(orderd_hay: list[int], needle: int) -> bool:
    low = 0
    high = len(orderd_hay) - 1

    while low <= high:
        mid = (high + low) // 2
        if orderd_hay[mid] == needle:
            return True
        elif orderd_hay[mid] > needle:
            high = mid - 1
        else:
            low = mid + 1
    return False
