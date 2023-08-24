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
            
    @staticmethod
    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            SortAlgorithm.merge_sort(left_half)
            SortAlgorithm.merge_sort(right_half)

            i, j, k = 0, 0, 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

if __name__ == "__main__":
    arr_bubble = [64, 34, 25, 12, 22, 11, 90]
    arr_merge = [12, 11, 13, 5, 6, 7]

    sort_algo = SortAlgorithm()

    print("Bubble Sort:")
    sort_algo.bubble_sort(arr_bubble)
    print(arr_bubble)

    print("Merge Sort:")
    sort_algo.merge_sort(arr_merge)
    print(arr_merge)