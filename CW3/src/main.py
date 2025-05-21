import pandas
import logicmin
from collections import defaultdict

conflict_check = defaultdict(set)

df = pandas.read_csv("../data/fullKMAP.csv", sep = ';')

t = logicmin.TT(7, 7)

mp3_input = df.iloc[:, 0:7].to_numpy().tolist()
mp3_output = df.iloc[:, 7:14].to_numpy().tolist()

mi = ["".join(str(el) for el in element) for element in mp3_input]
mo = ["".join(str(el) for el in element) for element in mp3_output]

for i in range(len(mi)):
    t.add(mi[i], mo[i])

for i in range(len(mi)):
    conflict_check[mi[i]].add(mo[i])

for inp, out_set in conflict_check.items():
    if len(out_set) > 1:
        print(f"⚠️ Konflikt dla wejścia {inp}: {out_set}")

assert len(df) == 128, "Dane są niekompletne (mniej niż 128 wierszy)"
assert df.iloc[:, 0:14].isin([0, 1]).all().all(), "Błąd: dane zawierają coś innego niż 0/1"

sols = t.solve()

print(sols.printN(xnames= ['R1','R0','S', 'P', 'N', 'PR', 'ST'],
ynames = ["R1'", "R0'", "S'", "P'", "N'", "PR'", "ST'"]))
