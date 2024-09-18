import os

def listar_usuarios_windows():
    try:
        print("Contas de Usuários no Windows:")
        # Executa o comando 'net user' diretamente no sistema
        os.system('net user')
        
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    listar_usuarios_windows()
    

