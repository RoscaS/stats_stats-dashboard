import math
import pandas as pd
from collections import Counter
from core.settings import _r, COEF_VAR


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

        self.ordre = None

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
            f"\t{self._get_coeff_info('variation', seuil=COEF_VAR)}" \
            f"\nCoef asymétrie:\t\t{_r(self.coeff_asym())}" \
            f"\t{self._get_coeff_info('asymetrie')}" \
            f"\nCoef appl:\t\t\t{_r(self.coeff_appl())}" \
            f"\t{self._get_coeff_info('applatissement')}" \
            # f"\nCentiles:\t\t\t{list(self.centiles().values())} " \
            # f"\n---------------" \
            # f"\nDeciles:\t\t\t{list(self.deciles().values())} " \
            # f"\n\n{self.serie}"
        return s

    def _flatten_input(self, s):
        """Transforme l'input en liste plate"""
        flat_lst = []
        tuples_lst = [(1, i) if type(i) != tuple else (i[0], i[1]) for i in s]
        for i in tuples_lst:
            flat_lst += [float(i[1]) for j in range(i[0])]
        return flat_lst

    def _serialize_data(self):
        """Serialisation des données"""
        return {
            'study': {
                'general': {
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
                    'ecart_semi_inter_quartile': _r(self.ESI()),
                    'variance': _r(self.variance()),
                    'ecart_type': _r(self.ecart_type()),
                    'coefficient_de_variation': {
                        'data': _r(self.coefficient_variation()),
                        'info': self._get_coeff_info('variation', COEF_VAR)
                    }
                },
                'forme': {
                    'coefficient_asymetrie': {
                        'data': _r(self.coeff_asym()),
                        'info': self._get_coeff_info('asymetrie')
                    },
                    'coefficient_applatissement': {
                        'data': _r(self.coeff_appl()),
                        'info': self._get_coeff_info('applatissement')
                    }
                },
                'quantiles': {
                    'quartiles': self.quartiles(),
                    'deciles': self.deciles(),
                    # 'centiles': self.centiles(),
                },
            }
        }

    def _coeffs_info(self):
        return {
            'variation': {
                'func': self.coefficient_variation,
                '>': f'(coeff > seuil ({COEF_VAR})) Série dispersée.',
                '<': f'(coeff < seuil ({COEF_VAR})) Série homogène.',
                '0': f'(coeff = seuil ({COEF_VAR})) Série entre les deux',
            },
            'asymetrie': {
                'func': self.coeff_asym,
                '>': '(coeff > 0) Série étalée sur la droite.',
                '<': '(coeff < 0) Série étalée sur la gauche.',
                '0': '(coeff = 0) Répartition symétrique.',
            },
            'applatissement': {
                'func': self.coeff_appl,
                '>': '(coeff > 0) Distribution leptokurtique (pointue).',
                '<': '(coeff < 0) Distribution platykurtique (applatie).',
                '0': '(coeff = 0) Distribution mesokurtique (normale).',
            }
        }

    def _nature_caractere(self):
        parse = {}
        return {
            parse['quantitatif']: {
                parse['continu']: lambda: self.serie in 'R',
                parse['discret']: lambda: self.serie in ['a', 'b', 'c']

            },
            parse['qualitatif']: {
                parse['ordinal']: lambda: self.ordre == 'intrinseque',
                parse['nominal']: lambda: self.ordre != 'intrinseque',
            },
        }

    def _get_coeff_info(self, coeff, seuil=0):
        value = self._coeffs_info()[coeff]
        func = value['func']()
        if func > seuil:
            return value['>']
        elif func < seuil:
            return value['<']
        else:
            return value['0']

    def _count(self):
        return {i[0]: i[1] for i in sorted(Counter(self.serie).items())}

    def getData(self):
        data = self._serialize_data()
        data['plot'] = {
            "freq": {
                "ticks": self._count().keys(),
                "eff": self._count().values(),
                "eff_pc": self._count().values(),
            },
            "cum": {
                'ticks': self._count().keys(),
                "freq": self._count().values(),
                "eff": self._count().values()
            }
        }
        return data

    def mediane(self):
        m = self.effectifs // 2
        asc = sorted(self.serie)
        return (asc[m - 1] + asc[m]) / 2 if self.est_paire else asc[m]

    def mode(self):
        c = Counter(self.serie)
        m = c.most_common(1)[0][0]
        return m

    def _quantiles(self, type, population):
        data = pd.DataFrame(population)
        position = [_r((1 / type) * i) for i in range(1, type)]
        quartiles = [_r(data.quantile(i)[0]) for i in position]
        return {c + 1: i for c, i in enumerate(quartiles)}

    def quartiles(self):
        return self._quantiles(4, self.serie)

    def deciles(self, Qn=0):
        return self._quantiles(10, self.serie)

    def centiles(self, Qn=0):
        return self._quantiles(100, self.serie)

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
