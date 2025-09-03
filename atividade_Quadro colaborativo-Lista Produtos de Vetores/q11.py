import numpy as np

def q11(vetor_a: tuple, vetor_b: tuple, opcao: int)-> np.array:
    try:
        vetor_a = np.array(vetor_a)
        vetor_b = np.array(vetor_b)

        if len(vetor_a) != len(vetor_b):
            print("Erro: Os vetores devem ter o mesmo tamanho!")
            return

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
    except Exception as e:
        print(f"Erro no cálculo dos vetores: {e}")

while True:
    try:
        print("Expressões imbutidas:")
        print("1 - 2*a × (a + b)")
        print("2 - (a + 2b) × (a − 2b)")
        opcao = int(input("Escolha uma das expressões (1 ou 2), ou 3 para sair: "))
        
        if opcao == 3:
            print("Saindo...")
            break
        elif opcao not in [1, 2]:
            print("Opção inválida! Escolha 1, 2 ou 3.")
            continue
            
        comps_a = input("Forneca a tupla do vetor a: ")
        comps_b = input("Forneca a tupla do vetor b: ")
        
        try:
            vetor_a = tuple(int(i) for i in comps_a.split(','))
            vetor_b = tuple(int(i) for i in comps_b.split(','))
            q11(vetor_a, vetor_b, opcao)
        except ValueError:
            print("Erro: Digite apenas números separados por vírgula (ex: 1,2,3)")
        except Exception as e:
            print(f"Erro ao processar os vetores: {e}")
            
    except ValueError:
        print("Erro: Digite apenas números para a opção!")
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário.")
        break
    except Exception as e:
        print(f"Erro inesperado: {e}")