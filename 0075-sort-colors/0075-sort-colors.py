class Solution:
    def sortColors(self, array: List[int]) -> None:
        for i in range(len(array) - 1):
            for j in range(len(array) - i - 1):
                if array[j] > array [j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
        return array