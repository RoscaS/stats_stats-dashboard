import math
from collections import Counter
from core.settings import _r


class _Serie:
    """
    Entrées valables:
        * `[1, 3, 3, 6, 8, 9, 9]`\n
        * `[1,5, (2,10), 3,9, (4,2),8, (2,3)]`
        avec `(a, b)` = `(freq, valeur)`
    """

    def __init__(self, serie):
        self.serie = self._flatten_input(serie)
        self.effectifs = len(self)
        self.est_paire = self.effectifs % 2 == 0
        self.etendue = max(self.serie) - min(self.serie)
        self.centre = self.etendue / 2
        self.moyenne = sum(self.serie) / self.effectifs

    def __len__(self):
        return len(self.serie)

    def __str__(self):
        s = f"\nEffectifs:\t\t\t{len(self)}" \
            f"\nMin:\t\t\t\t{min(self.serie)}" \
            f"\nMax:\t\t\t\t{max(self.serie)}" \
            f"\nÉtendue:\t\t\t{self.etendue}" \
            f"\nMode:\t\t\t\t{_r(self.mode())}" \
            f"\n---------------" \
            f"\nCentre:\t\t\t\t{_r(self.centre)}" \
            f"\nMoyenne:\t\t\t{_r(self.moyenne)}" \
            f"\nMedianne:\t\t\t{_r(self.mediane())} " \
            f"\n---------------" \
            f"\nQuartiles:\t\t\t{list(self.quartiles().values())} " \
            f"\nÉcart inter-q:\t\t{_r(self.EIQ())}" \
            f"\nÉcart semi-inter-q:\t{_r(self.ESI())}" \
            f"\nÉcart abs moyen:\t{_r(self.EAM())}" \
            f"\n---------------" \
            f"\nVariance:\t\t\t{_r(self.variance())} " \
            f"\nÉcart-type:\t\t\t{_r(self.ecart_type())}" \
            f"\nCoef variation:\t\t{_r(self.coefficient_variation())}% " \
            f"pop {'disp' if self.coefficient_variation() >= 15 else 'homog'}" \
            f"\nCoef asymétrie:\t\t{_r(self.coeff_asym())}\t" \
            f"étirement à {'g' if self.coeff_asym() > 0 else 'd'} (0 = sym)" \
            f"\nCoef appl:\t\t\t{_r(self.coeff_appl())}\t" \
            f"{'pointe' if self.coeff_appl() > 0 else 'applatie'} (0 = norm)" \
            f""
        return s

    def _flatten_input(self, s):
        """Transforme l'input en liste plate"""
        flat_lst = []
        tuples_lst = [(1, i) if type(i) != tuple else (i[0], i[1]) for i in s]
        for i in tuples_lst:
            flat_lst += [int(i[1]) for j in range(i[0])]
        return flat_lst

    def _serialize_data(self):
        """Serialisation des données"""
        return {
            'global': {
                'effectifs': self.effectifs,
                'min': min(self.serie),
                'max': max(self.serie),
                'etendue': self.etendue,
                'mode': _r(self.mode()),
            },
            'centre': {
                'centre': _r(self.centre),
                'moyenne': _r(self.moyenne),
                'mediane': _r(self.mediane()),
            },
            'dispersion': {
                'ecart_absolu_moyen': _r(self.EAM()),
                'ecart_semi_inter_quartile:': _r(self.ESI()),
                'variance': _r(self.variance()),
                'ecart_type': _r(self.ecart_type()),
                'coefficient_de_variation': _r(self.coefficient_variation()),
            },
            'forme': {
                'coefficient_assymetrie': _r(self.coeff_asym()),
                'coefficient_applatissement': _r(self.coeff_appl())
            },
            'quantiles': {
                'quartiles': list(self.quartiles().values()),
            },
        }

    def getData(self):
        data = self._serialize_data()
        data['plot'] = {
            'x': self._count().keys(),
            'y': self._count().values()
        }
        return data

    def _count(self):
        return Counter(self.serie)

    def mediane(self):
        m = self.effectifs // 2
        asc = sorted(self.serie)
        return (asc[m - 1] + asc[m]) / 2 if self.est_paire else asc[m]

    def mode(self):
        c = Counter(self.serie)
        m = c.most_common(1)[0][0]
        return m

    def quartiles(self):
        c = (self.effectifs // 2)
        a = _Serie(self.serie[:c])
        b = _Serie(self.serie[(c if self.est_paire else c + 1):])
        return {1: a.mediane(), 2: self.mediane(), 3: b.mediane()}

    def EIQ(self):
        """Écart inter-quartiles"""
        q = self.quartiles()
        return q[3] - q[1]

    def ESI(self):
        """Écart semi-inter-quartiles"""
        return self.EIQ() / 2

    def EAM(self):
        """Écart absolu moyen"""
        return sum(
            [abs(i - self.moyenne) for i in self.serie]
        ) / self.effectifs

    def variance(self):
        """(v) Moyenne des carrés des écarts à la moyenne"""
        return sum(
            [(i - self.moyenne) ** 2 for i in self.serie]
        ) / self.effectifs

    def ecart_type(self):
        '''(sigma)'''
        return math.sqrt(self.variance())

    def coefficient_variation(self):
        """
        * cv < 15% => population homogène
        * cv > 15% => population dispersée
        """
        return (self.ecart_type() / self.moyenne) * 100

    def moment_centre(self, degre):
        """(mu)"""
        x = [(i - self.moyenne) ** degre for i in self.serie]
        return sum(x) / self.effectifs

    def coeff_fisher(self, degre):
        """(gama)"""
        return self.moment_centre(degre) / self.ecart_type() ** degre

    def coeff_asym(self):
        """(gama_1)"""
        return self.coeff_fisher(3)

    def coeff_appl(self):
        """(gama_2)"""
        return self.coeff_fisher(4) - 3

