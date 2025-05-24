def NOT(x): return 0 if x else 1
def AND(*args): return int(all(args))
def OR(*args): return int(any(args))

def simulate_fsm_from_string(input_string):
    R1 = R0 = ST = CN = CPR = 0
    state_log = []
    S = P = N = PR = 0

    for step, ch in enumerate(input_string, start=1):


        if ch == 's': S = NOT(S)
        elif ch == 'p': P = NOT(P)
        elif ch == 'n': N = NOT(N)
        elif ch == 'r': PR = NOT(PR)
        elif ch == '0': pass  # puszczenie
        else: raise ValueError(f"Nieznany znak wejścia: '{ch}'")

        CPR_ = OR(
            AND(NOT(CN), NOT(N), PR),
            AND(NOT(CN), CPR, N),
            AND(CN, N, PR),
            AND(CN, CPR, NOT(N))
        )

        CN_ = N

        ST_ = OR(
            AND(CPR, NOT(N), NOT(PR)),
            AND(CN, CPR, NOT(PR)),
            AND(CN, NOT(N)),
            AND(ST, NOT(P)),
            S
        )

        R0_ = OR(
            AND(NOT(R0), CPR, NOT(N), NOT(PR)),
            AND(NOT(R0), CN, CPR, NOT(PR)),
            AND(NOT(R0), CN, NOT(N)),
            AND(R0, NOT(CN), NOT(CPR)),
            AND(R0, NOT(CN), PR),
            AND(R0, NOT(CN), N),
            AND(R0, NOT(CPR), N),
            AND(R0, N, PR)
        )

        R1_ = OR(
            AND(NOT(R1), NOT(R0), NOT(CN), CPR, NOT(N), NOT(PR)),
            AND(NOT(R1), NOT(R0), CN, CPR, N, NOT(PR)),
            AND(NOT(R1), R0, CN, NOT(N)),
            AND(R1, NOT(R0), CN, NOT(N)),
            AND(R1, NOT(R0), NOT(CPR)),
            AND(R1, NOT(R0), PR),
            AND(R1, NOT(CN), N),
            AND(R1, R0, NOT(CN)),
            AND(R1, R0, N)
        )

        state_log.append({
            'step': step,
            'input': ch,
            'R1': R1, 'R0': R0, 'ST': ST, 'CN': CN, 'CPR': CPR,
            "R1'": R1_, "R0'": R0_, "ST'": ST_, "CN'": CN_, "CPR'": CPR_
        })

        R1, R0, ST, CN, CPR = R1_, R0_, ST_, CN_, CPR_

    return state_log

if __name__ == '__main__':
    result = simulate_fsm_from_string("snsnsnns")
    for entry in result:
        print(entry)