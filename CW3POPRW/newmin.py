import pandas
import logicmin
from collections import defaultdict

conflict_check = defaultdict(set)

df = pandas.read_csv("./truth_table3.csv", sep = ';')

t = logicmin.TT(9, 5)

mp3_input = df.iloc[:, 0:9].to_numpy().tolist()
mp3_output = df.iloc[:, 9:14].to_numpy().tolist()

mi = ["".join(str(el) for el in element) for element in mp3_input]
mo = ["".join(str(el) for el in element) for element in mp3_output]

for i in range(len(mi)):
    t.add(mi[i], mo[i])

for i in range(len(mi)):
    conflict_check[mi[i]].add(mo[i])

for inp, out_set in conflict_check.items():
    if len(out_set) > 1:
        print(f"⚠️ Konflikt dla wejścia {inp}: {out_set}")



sols = t.solve()

print(sols.printN(xnames= ['R1','R0','ST','CN','CPR','S', 'P', 'N', 'PR'],
ynames = ["R1'", "R0'", "ST'", "CN'","CPR'"]))