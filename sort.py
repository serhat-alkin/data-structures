class SortAlgorithm:
    @staticmethod
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            if not swapped:
                break


if __name__ == "__main__":
    arr_bubble = [64, 34, 25, 12, 22, 11, 90]
    arr_merge = [12, 11, 13, 5, 6, 7]

    sort_algo = SortAlgorithm()

    print("Bubble Sort:")
    sort_algo.bubble_sort(arr_bubble)
    print(arr_bubble)

