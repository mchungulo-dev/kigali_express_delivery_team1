# O(N) done using sequential search
def linear_search(driver_list, target_id):
    for driver in driver_list:
        if driver["driver_id"] == target_id:
            return driver
    return None

# O(log N) binary search
def binary_search(sorted_drivers, target_id):
    low = 0
    high = len(sorted_drivers) - 1

    while low <= high:
        mid = low + (high - low) // 2
        mid_id = sorted_drivers[mid]["driver_id"]

        if mid_id == target_id:
            return sorted_drivers[mid]
        elif mid_id < target_id:
            low = mid + 1
        else:
            high = mid - 1

    return None

# Mapping loop to build fast lookup table
def build_driver_map(driver_list):
    driver_map = {}
    for driver in driver_list:
        driver_map[driver["driver_id"]] = driver
    return driver_map

# O(1) hash map lookup
def hash_lookup(driver_map, target_id):
    return driver_map.get(target_id)