import numpy as np

def calcular_kasaroc_ultra(C, C_0, n, delta, alpha, beta, gamma, lambda_param):
    """
    Executa o cálculo matemático da fórmula KaSaroc Ultra com proteção quântica.
    """
    # Aplicação do escudo de módulo para suportar números complexos
    modulo_C = np.abs(C)
    modulo_n = np.abs(n)
    
    # Cálculo dos termos estabilizados por logaritmo natural
    termo_numerador = np.log((modulo_C / C_0) + 1.0) ** alpha
    termo_resistencia = beta * (delta ** gamma) * (modulo_n ** lambda_param)
    
    # Proteção contra divisão por zero em cenários de colapso total
    if (termo_numerador + termo_resistencia) == 0:
        return 0.0
        
    K = termo_numerador / (termo_numerador + termo_resistencia)
    return float(K)

def menu_simulador():
    print("="*50)
    print("      SIMULADOR UNIVERSAL KASAROC ULTRA v1.0      ")
    print("="*50)
    print("Escolha o regime de teste biológico/físico:")
    print("1 - Engenharia de Redes (Tráfego Real em Mbps)")
    print("2 - Astrofísica (Efeito Buraco Negro na Relatividade)")
    print("3 - Neurobiologia (Disparo e Fadiga de Neurônios)")
    print("4 - Teste Customizado (Injetar seus próprios números)")
    print("="*50)
    
    opcao = input("Digite o número do teste: ")
    
    # Configurações de fábrica testadas no comitê científico
    if opcao == "1":
        print("\n[+] Executando: Engenharia de Redes")
        # Tráfego de pico, escala em Mbps, latência em ms
        K = calcular_kasaroc_ultra(C=1500, C_0=100, n=2.5, delta=1.5, alpha=1.0, beta=0.5, gamma=1.0, lambda_param=1.0)
        print(f"Resultado da Eficiência (K): {K:.4f} ({K*100:.2f}%)")
        
    elif opcao == "2":
        print("\n[+] Executando: Astrofísica Limite")
        # Distorção extrema de espaço-tempo e gravidade massiva
        K = calcular_kasaroc_ultra(C=50000, C_0=1, n=100+50j, delta=10.0, alpha=0.5, beta=5.0, gamma=2.0, lambda_param=1.5)
        print(f"Resultado do Sinal na Singularidade (K): {K:.4f} ({K*100:.2f}%)")
        
    elif opcao == "3":
        print("\n[+] Executando: Neurobiologia")
        # Estímulo de membrana celular química
        K = calcular_kasaroc_ultra(C=85, C_0=10, n=1.2, delta=1.0, alpha=1.5, beta=0.2, gamma=1.0, lambda_param=1.0)
        print(f"Resultado do Disparo Nervoso (K): {K:.4f} ({K*100:.2f}%)")
        
    elif opcao == "4":
        print("\n[+] Modo de Configuração Manual Ativo")
        try:
            C = complex(input("Valor do Estímulo C (aceita complexos ex: 10+5j): "))
            C_0 = float(input("Constante de Escala C_0: "))
            n = complex(input("Valor do Ruído/Latência n (aceita complexos): "))
            delta = float(input("Fator de Distância Espacial (delta): "))
            alpha = float(input("Expoente Alfa: "))
            beta = float(input("Multiplicador Beta: "))
            gamma = float(input("Expoente Gama: "))
            lambda_param = float(input("Expoente Lambda: "))
            
            K = calcular_kasaroc_ultra(C, C_0, n, delta, alpha, beta, gamma, lambda_param)
            print(f"\nResultado Customizado (K): {K:.4f} ({K*100:.2f}%)")
        except ValueError:
            print("[-] Erro: Certifique-se de digitar números válidos.")
    else:
        print("[-] Opção inválida.")

if __name__ == "__main__":
    menu_simulador()
      
