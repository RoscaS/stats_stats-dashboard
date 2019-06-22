from core.settings import serie_from_excel
from core.ClassList import _ClassList as ClassList
from core.Serie import _Serie as Serie



############################## Test CP1



# s = serie_from_excel('QCM', 'candidat')
s = serie_from_excel('QCM','réponses justes')

n_intervales = 9
interval = ((max(s) - min(s)) // n_intervales) + 1


x = Serie(s)
X = ClassList(serie=s, interval=interval, start=6)
# print(X)


##############################
