class _Class:

    def __init__(self, parent, idx, start, end, eff, cum_eff, freq, cum_freq):
        self.range_repr = f"{start} → {end}"
        self.classList = parent
        self.idx = idx
        self.start = start
        self.end = end
        self.centre = (start + end) / 2
        self.effectif = eff
        self.effectif_cum = cum_eff
        self.frequence = freq
        self.frequence_cum = cum_freq
        self.frequence_pc = self.frequence * 100

    def __repr__(self):
        return f"<class Class [{self.start}; {self.end}[>"

    def _serialize_data(self):
        return {
            "idx": self.idx,
            "start": self.start,
            "end": self.end,
            "centre": self.centre,
            "effectif": self.effectif,
            "effectif_cum": self.effectif_cum,
            "frequence": self.frequence,
            "frequence_cum": self.frequence_cum,
            "frequence_pc": self.frequence_pc,
        }

    def getPrev(self):
        return self.classList[self.idx - 1] \
            if self.idx > 0 else self

    def getNext(self):
        return self.classList[self.idx + 1] \
            if self.idx < len(self.classList) - 1 else self
