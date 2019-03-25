from core.ClassList import _ClassList as ClassList
from core.Serie import _Serie as Serie
from core.settings import serie_from_excel

# s = serie_from_excel('coliformes')
# x = Serie(s)
# X = ClassList(serie=s, interval=100, start=7)


s = [
    (15, 5.08),
    (11, 4.94),
    (14, 4.99),
    (5, 4.92),
    (20, 4.86),
    (10, 5.04),
    (22, 5.06),
    (13, 5.09),
    (5, 4.88),
    (6, 4.93),
    (26, 4.91),
    (8, 4.96),
    (17, 5.01),
    (15, 5.05),
    (10, 5.12),
    (12, 5.02),
    (16, 5.0),
    (25, 5.11)
]

x = Serie(s)
X = ClassList(serie=s, interval=1, start=1)

# print(x)
print(x.quartiles())
