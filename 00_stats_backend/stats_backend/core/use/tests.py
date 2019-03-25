from core.ClassList import _ClassList as ClassList
from core.Serie import _Serie as Serie
from core.settings import excel_file

s1 = [(2, 44), (3, 46), (7, 48), (11, 50), (8, 52), (6, 54), (3, 56)]
s2 = [0, 1, (2, 2), (5, 3), (7, 4), (8, 5), (2, 6)]


df = pd.read_excel(excel_file('coliformes'))
data = list(df['DATA'])

x = Serie(data)
X = ClassList(data, 7, 100)

y = Serie(s1)
Y = ClassList(s1, 43, 2)

z = Serie(s2)
Z = ClassList(s2, 0, 2)


