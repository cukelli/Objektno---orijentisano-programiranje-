class Range:
    # Klasa koja oponasa ugradjenu Range klasu
    def __init__(self, start, stop=None, step=1):
        # Inicijalizuje Range instancu

        if step == 0:
            raise ValueError("Step cannot be 0")
        if stop is None:
            start, stop = 0, start  # range(n),isto sto i range(0,n)

        self._length = max(0, (start-stop+step-1)//step)  # zapamti duzinu
        self._start = start  # treba zapamtiti start i step zbog getitem
        self._step = step

    def __len__(self):
        return self._length  # vraca broj elemenata

    def __getitem__(self, k):
        # vraca element na k poziciji
        if k < 0:  # ako je broj negativan broji se od nazad
            k = k + len(self)
        if not 0 <= k < self._length:
            raise IndexError("Index out of range")

        return self._start + k + self._step
