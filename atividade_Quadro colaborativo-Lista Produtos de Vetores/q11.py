import numpy as np

def q11(vetor_a: tuple, vetor_b: tuple, opcao: int)-> np.array:

    vetor_a = np.array(vetor_a)
    vetor_b = np.array(vetor_b)

    if opcao == 1:
        vetor_c = 2 * vetor_a
        vetor_d = vetor_a + vetor_b

        print(vetor_c)
        print(vetor_d)

        vetor_e = np.cross(vetor_c, vetor_d)
        print(vetor_e)
    elif opcao == 2:

        vetor_c = vetor_a + 2 * vetor_b
        vetor_d = vetor_a - 2 * vetor_b

        print(vetor_c)
        print(vetor_d)

        vetor_e = np.cross(vetor_c, vetor_d)
        print(vetor_e)

while True:
    print("Expressões imbutidas:")
    print("1 - 2*a × (a + b)")
    print("2 - (a + 2b) × (a − 2b)")
    opcao = int(input("Escolha uma das expressões (1 ou 2), ou 3 para sair: "))
    if opcao == 3:
        print("Saindo...")
        break
    comps_a = input("Forneca a tupla do vetor a: ")
    comps_b = input("Forneca a tupla do vetor b: ")
    vetor_a = tuple(int(i) for i in comps_a.split(','))
    vetor_b = tuple(int(i) for i in comps_b.split(','))
    q11(vetor_a, vetor_b, opcao)

