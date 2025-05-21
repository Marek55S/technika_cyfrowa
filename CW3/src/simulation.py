import threading
import queue
import time
import random

# Funkcje przejścia (tu kopiujesz swoje funkcje R1_fun, R0_fun itd.)
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
        (R1 and R0 and N)
    )


# Kolejka sygnałów
q = queue.Queue()

# Stan początkowy
R1 = 0
R0 = 0
S = 0
P = 0
N = 0
PR = 0
ST = 0

def producer():
    przyciski = ['S', 'P', 'N', 'R']
    while True:
        sig = random.choice(przyciski)
        q.put(sig)
        print(f"[PRODUCER] Wysłano sygnał: {sig}")
        time.sleep(2)  # co 2 sekundy nowy sygnał

def consumer():
    global R1, R0, S, P, N, PR, ST
    krok = 1

    while True:
        sig = q.get()  # czekaj na sygnał
        # Zeruj sygnały przycisków
        S = P = N = PR = 0

        if sig == 'S':
            S = 1
        elif sig == 'P':
            P = 1
        elif sig == 'N':
            N = 1
        elif sig == 'R':
            PR = 1
        else:
            print(f"[CONSUMER] Nieznany sygnał: {sig}")
            continue

        # Oblicz nowe stany
        R1n = R1_fun(R1, R0, S, P, N, PR, ST)
        R0n = R0_fun(R1, R0, S, P, N, PR, ST)
        Sn = S_fun(R1, R0, S, P, N, PR, ST)
        Pn = P_fun(R1, R0, S, P, N, PR, ST)
        Nn = N_fun(R1, R0, S, P, N, PR, ST)
        PRn = PR_fun(R1, R0, S, P, N, PR, ST)
        STn = ST_fun(R1, R0, S, P, N, PR, ST)

        # Aktualizuj stan
        R1, R0, S, P, N, PR, ST = R1n, R0n, Sn, Pn, Nn, PRn, STn

        print(f"Krok {krok}: Piosenka = {R1}{R0} (numer {(R1 << 1) + R0}), Stan odtwarzacza ST = {ST}, Ostatni sygnał: {sig}")
        krok += 1

# Uruchom wątki
thread_producer = threading.Thread(target=producer, daemon=True)
thread_consumer = threading.Thread(target=consumer, daemon=True)

thread_producer.start()
thread_consumer.start()

# Aby program działał, "utrzymaj" główny wątek przy życiu
try:
    while True:
        time.sleep(0.5)
except KeyboardInterrupt:
    print("\nZakończono symulację.")
