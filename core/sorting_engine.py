class SortingEngine:
    def mergesort(self, items, key_func, reverse=False):
        #Ordenamiento mediante algoritmo Mergesort
        if len(items) <= 1:
            return items

        mid = len(items) // 2
        left_half = self.mergesort(items[:mid], key_func, reverse)
        right_half = self.mergesort(items[mid:], key_func, reverse)

        return self._merge(left_half, right_half, key_func, reverse)

    def _merge(self, left, right, key_func, reverse):
        #Funcion auxiliar para fusionar dos sublistas ordenadas
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            left_val = key_func(left[i])
            right_val = key_func(right[j])

            condition = left_val > right_val if reverse else left_val <= right_val

            if condition:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        while i < len(left):
            result.append(left[i])
            i += 1

        while j < len(right):
            result.append(right[j])
            j += 1

        return result

    def shellsort(self, items, key_func, reverse=False):
        #Ordenamiento mediante algoritmo Shellsort
        arr = list(items)
        n = len(arr)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                temp_val = key_func(temp)
                j = i

                while j >= gap:
                    current_val = key_func(arr[j - gap])
                    condition = current_val < temp_val if reverse else current_val > temp_val

                    if condition:
                        arr[j] = arr[j - gap]
                        j -= gap
                    else:
                        break

                arr[j] = temp
            gap //= 2

        return arr
