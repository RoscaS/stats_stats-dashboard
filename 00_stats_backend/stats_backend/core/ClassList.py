import math

from core.Serie import _Serie
from core.Class import _Class
from core.settings import _r


class _ClassList(_Serie):

    def __init__(self, serie, start, interval):
        super().__init__(serie)
        self.interval = interval
        self.start = start
        self.classes = self._build_classes()

    def __getitem__(self, item):
        return self.classes[item]

    def __str__(self):
        s = f"{super().__str__()}" \
            f"\n---------------" \
            f"\nClasse modale:\t\t{self.classe_modale()[0]}" \
            f"\n---------------" \
            f"\n{self.histogram()}"
        return s

    def getData(self):
        data = self._serialize_data()
        general = data['study']['general']
        general['classe_modale'] = self.classe_modale()[0].range_repr
        data['plot'] = {
            "data": {i.range_repr: i.effectif for i in self.classes},  # Delete ?
            "classes": [i._serialize_data() for i in self.classes],
            "freq": {
                # "ticks": [i.range_repr for i in self.classes],
                "ticks": [self.start]+[i.end for i in self.classes],
                "eff": [i.effectif for i in self.classes],
                "eff_pc": [_r(i.frequence_pc) for i in self.classes],
            },
            "cum": {
                'ticks': [f"{i.start}{' ' * 5}{i.end}" for i in self.classes],
                "freq": [_r(i.frequence_cum) for i in self.classes],
                "eff": [i.effectif_cum for i in self.classes]
            }
        }
        return data

    def _build_classes(self):
        count = 0
        classes = []
        for i in range((self.etendue // self.interval) + 1):
            start = i * self.interval + self.start
            end = start + self.interval
            eff = len([j for j in self.serie if j >= start and j < end])
            count += eff
            cum_eff = count
            freq = eff / self.effectifs
            cum_freq = count / self.effectifs
            classes.append(_Class(
                self, i, start, end, eff, cum_eff, freq, cum_freq
            ))
        return classes

    def _classe_du_quantile(self, valeur):
        """Trouve la classe où se trouve `valeur` (si quartiles .24, .5, .75)"""
        for i in self.classes:
            if (i.frequence_cum >= valeur):
                return i.getNext()

    def _quantile(self, valeur):
        classe = self._classe_du_quantile(valeur)
        a = classe.start
        b = self.interval
        c = valeur - classe.getPrev().frequence_cum
        d = classe.frequence_cum - valeur
        return a + ((b * c) / d)

    def effectifs(self, cumule=False):
        return [i.effectif_cum if cumule else i.effectif for i in self.classes]

    def frequences(self, cumule=False, pourcent=False):
        p = lambda: 100 if pourcent else 1
        c = lambda x: x.frequence_cum if cumule else x.frequence
        return [_r(c(i) * p()) for i in self.classes]

    def centres(self):
        return [i.centre for i in self.classe_modale()]

    def mediane(self):
        return self._quantile(0.5)

    def classe_modale(self):
        maximum = max([i.effectif for i in self.classes])
        return [i for i in self.classes if i.effectif == maximum]

    def mode(self):
        classe = self.classe_modale()[0]
        a = classe.start
        b = classe.effectif - classe.getPrev().effectif
        d = classe.effectif - classe.getNext().effectif
        c = self.interval
        return a + (b * c) / (b + d)

    def quartiles(self):
        q1 = self._quantile(0.25)
        q2 = self.mediane()
        q3 = self._quantile(0.75)
        return {1: _r(q1), 2: _r(q2), 3: _r(q3)}

    def variance(self):
        """(v) Moyenne des carrés des écarts à la moyenne"""
        return sum(
            [(i - self.moyenne) ** 2 for i in self.serie]
        ) / (self.effectifs - 1)

    def ecart_type(self):
        """(sigma)"""
        return math.sqrt(self.variance())

    def moment_centre(self, degre):
        """(mu)"""
        f = lambda x: x.centre - self.moyenne
        x = [(f(i) ** degre) * i.effectif for i in self.classes]
        return sum(x) / self.effectifs

    def histogram(self):
        histo = "\n\t\t\t  c\t\tfreq\tfreq^"
        for i in self.classes:
            interval = f"[{i.start}, {i.end}["
            baton = "".join("#" for i in range(i.effectif))
            centre = f"({_r(i.centre)})"
            freq = _r(i.frequence)
            freq_cum = _r(i.frequence_cum)
            histo += f"\n{interval}\t{centre}\t{freq} " \
                f"\t{freq_cum} \t{baton} {len(baton)}"
        return histo
