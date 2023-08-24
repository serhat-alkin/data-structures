class SearchAlgorithm:
    @staticmethod
    def linear_search(arr, target):
        for i, num in enumerate(arr):
            if num == target:
                return i
        return -1

    @staticmethod
    def binary_search(arr, target):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

if __name__ == "__main__":
    arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    target = 12

    search_algo = SearchAlgorithm()

    linear_result = search_algo.linear_search(arr, target)
    if linear_result != -1:
        print(f"Linear Search: Element {target} found at index {linear_result}")
    else:
        print("Linear Search: Element not found")

    binary_result = search_algo.binary_search(arr, target)
    if binary_result != -1:
        print(f"Binary Search: Element {target} found at index {binary_result}")
    else:
        print("Binary Search: Element not found")
