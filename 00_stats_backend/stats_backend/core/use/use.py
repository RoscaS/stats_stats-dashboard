from core.ClassList import _ClassList as ClassList
from core.Serie import _Serie as Serie

# # Coliformes
# s = serie_from_excel('coliformes')
# x = Serie(s)
# X = ClassList(serie=s, interval=100, start=7)


# # Test préparation Ex1
# s = [(15, 5.08), (11, 4.94), (14, 4.99), (5, 4.92), (20, 4.86), (10, 5.04),
# (22, 5.06), (13, 5.09), (5, 4.88), (6, 4.93), (26, 4.91), (8, 4.96), (17,
# 5.01), (15, 5.05), (10, 5.12), (12, 5.02), (16, 5.0), (25, 5.11)]
# x = Serie(s)
# X = ClassList(serie=s, interval=1, start=1)


# # Test préparation Ex2
# v = [82, 88, 59, 69, 50, 36, 25, 20, 18, 17, 9, 8, 8, 5, 0, 2, 4]
# s = [(i, c) for c, i in enumerate(v)]
#
# x = Serie(s)
# X = ClassList(serie=s, interval=1, start=0)


# Test préparation Ex groupe
s = [176, 258, 198, 280, 299, 205, 268, 237, 166, 161, 276, 200, 283, 228, 186,
     184, 181, 177, 162, 216, 184, 234, 268, 186, 190, 263, 273, 168, 162, 261,
     161, 230, 247, 187, 161, 283, 179, 161, 179, 263, 279, 243, 178, 162, 203]

n_intervales = 7
interval = ((max(s) - min(s)) // n_intervales) + 1

x = Serie(s)
X = ClassList(serie=s, interval=interval, start=160)

