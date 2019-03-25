from core.settings import serie_from_excel
from core.ClassList import _ClassList as ClassList
from core.Serie import _Serie as Serie



# Test CP1




# s1 = serie_from_excel('QCM', 'candidat')
s2 = serie_from_excel('QCM','réponses justes')

n_intervales = 9
interval = ((max(s2) - min(s2)) // n_intervales) + 1


x = Serie(s2)
X = ClassList(serie=s2, interval=interval, start=min(s2))


print(X)
