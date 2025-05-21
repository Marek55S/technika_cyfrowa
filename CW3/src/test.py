import pandas as pd

# Wczytaj dane
df = pd.read_csv("../data/fullKMAP.csv", sep = ';')
print(df.columns.tolist())

# Funkcje uproszczone
def ST_fun(R1, R0, S, P, N, PR, ST):
    return int(
        (R1 and R0 and S and not N and PR) or
        (R1 and R0 and S and N and not PR) or
        (not R1 and not R0 and not N and PR) or
        (not R1 and not P and not N and PR) or
        (not R1 and not R0 and N and not PR) or
        (not R1 and not P and N and not PR) or
        (not S and P and not N and PR) or
        (not S and P and N and not PR) or
        (S and not P and not PR) or
        (R0 and S and not P) or
        (R1 and S and not P) or
        (not P and ST) or
        (S and ST)
    )

def PR_fun(R1, R0, S, P, N, PR, ST):
    return int(
        (not R1 and R0 and S and P and N) or
        PR
    )

def N_fun(R1, R0, S, P, N, PR, ST):
    return int(
        (not R0 and N) or
        (not S and N) or
        (N and PR) or
        (R1 and N)
    )

def P_fun(R1, R0, S, P, N, PR, ST):
    return P  # P' <= P

def S_fun(R1, R0, S, P, N, PR, ST):
    return S  # S' <= S

def R0_fun(R1, R0, S, P, N, PR, ST):
    return int(
        (not R0 and not N and PR) or
        (not R0 and N and not PR) or
        (R0 and not N and not PR) or
        (R0 and N and PR)
    )

def R1_fun(R1, R0, S, P, N, PR, ST):
    return int(
        (not R1 and not R0 and not N and PR) or
        (not R1 and R0 and N and not PR) or
        (R1 and not R0 and not PR) or
        (R1 and N and PR) or
        (R1 and R0 and not N)
    )

# Funkcja testująca
def test_fun(real_data, f, label):
    for r1 in range(2):
        for r0 in range(2):
            for s in range(2):
                for p in range(2):
                    for n in range(2):
                        for pr in range(2):
                            for st in range(2):
                                index = r1 * 64 + r0 * 32 + s * 16 + p * 8 + n * 4 + pr * 2 + st
                                if f(r1, r0, s, p, n, pr, st) != real_data[index]:
                                    print(f'Błąd w {label} na indeksie {index} dla wejścia ({r1},{r0},{s},{p},{n},{pr},{st})')
                                    print(f(r1, r0, s, p, n, pr, st))
                                    print(real_data[index])
                                    return False
    print(f'{label} działa poprawnie ✅')
    return True

# Pobranie kolumn z df i testy
test_fun(df["R'1"].tolist(), R1_fun, "R1'")
test_fun(df["R'0"].tolist(), R0_fun, "R0'")
test_fun(df["S'"].tolist(),  S_fun,  "S'")
test_fun(df["P'"].tolist(),  P_fun,  "P'")
test_fun(df["N'"].tolist(),  N_fun,  "N'")
test_fun(df["PR'"].tolist(), PR_fun, "PR'")
test_fun(df["ST'"].tolist(), ST_fun, "ST'")
