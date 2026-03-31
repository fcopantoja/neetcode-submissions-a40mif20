import bisect
from collections import defaultdict

class TimeMap:
    def __init__(self):
        # Diccionario donde:
        # key -> lista de pares (timestamp, value)
        # Usamos lista porque necesitamos mantener orden por timestamp
        self.hash_dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Insertamos directamente (timestamp, value)
        # IMPORTANTE: LeetCode garantiza que los timestamps llegan en orden creciente
        # por lo que la lista ya queda ordenada automáticamente
        self.hash_dict[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        # Si la key no existe, no hay valores
        if key not in self.hash_dict:
            return ""

        arr = self.hash_dict[key]

        # Usamos bisect_right para encontrar la posición donde
        # insertaríamos (timestamp, valor_max) manteniendo orden
        #
        # chr(127) es un truco: es el carácter más "grande" en ASCII,
        # así nos aseguramos de encontrar el último timestamp <= timestamp
        i = bisect.bisect_right(arr, (timestamp, chr(127)))

        # Si i == 0, significa que todos los timestamps son mayores
        # al que buscamos → no hay valor válido
        if i == 0:
            return ""

        # Si no, el valor correcto es el inmediatamente anterior
        # porque es el timestamp más cercano <= dado
        return arr[i - 1][1]