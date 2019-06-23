from core.settings import serie_from_excel
from core.ClassList import _ClassList as ClassList
from core.Serie import _Serie as Serie

############################## Test CP1

# s = serie_from_excel('QCM','réponses justes')
#
# n_intervales = 9
# interval = ((max(s) - min(s)) // n_intervales) + 1
#
#
# x = Serie(s)
# X = ClassList(serie=s, interval=interval, start=6)
# print(X)


############################## Test CP1

s = [52, 88, 95, 108, 68, 88, 98, 108, 69, 88, 98, 109, 70, 89, 98, 109, 78, 89,
     99, 113, 78, 89, 99, 115, 79, 92, 101, 115, 81, 92, 101,
     119, 83, 95, 103, 128, 88, 95, 106, 139]

n_intervales = 9
# interval = ((max(s) - min(s)) // n_intervales) + 1
interval = 10

x = Serie(s)
X = ClassList(serie=s, interval=interval, start=50)
print(X)

##############################
