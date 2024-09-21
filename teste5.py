def descobrir_interruptores():
    # Estado inicial: todas as lâmpadas desligadas
    lampadas = {"Lâmpada 1": {"estado": "apagada", "temperatura": "fria"},
                "Lâmpada 2": {"estado": "apagada", "temperatura": "fria"},
                "Lâmpada 3": {"estado": "apagada", "temperatura": "fria"}}
    
    # Passo 1: Ligue o interruptor 1 e aguarde
    lampadas["Lâmpada 1"]["estado"] = "ligada"
    lampadas["Lâmpada 1"]["temperatura"] = "quente"
    
    # Passo 2: Desligue o interruptor 1 e ligue o interruptor 2
    lampadas["Lâmpada 1"]["estado"] = "apagada"
    lampadas["Lâmpada 2"]["estado"] = "ligada"
    
    #verifique o estado das lâmpadas:
    print("Verificação das lâmpadas:")
    for lampada, estado in lampadas.items():
        if estado["estado"] == "ligada":
            print(f"{lampada} está acesa, logo está conectada ao Interruptor 2.")
        elif estado["estado"] == "apagada" and estado["temperatura"] == "quente":
            print(f"{lampada} está apagada mas quente, logo está conectada ao Interruptor 1.")
        else:
            print(f"{lampada} está apagada e fria, logo está conectada ao Interruptor 3.")

descobrir_interruptores()
