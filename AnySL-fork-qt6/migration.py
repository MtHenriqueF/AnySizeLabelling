
# migration.py
import os

# --- CONFIGURAÇÃO ---
# Caminho para o diretório raiz do projeto que contém o código-fonte.
# O script irá procurar por arquivos .py recursivamente a partir daqui.
DIRETORIO_PROJETO = "./AnySizeLabeling" 
# --------------------


# Mapeamento de substituições de PyQt5 para PySide6
substituicoes = {
    # Imports principais
    "from PyQt5": "from PySide6",
    
    # Módulos específicos (para casos como PyQt5.QtCore.Qt)
    "PyQt5.QtCore": "PySide6.QtCore",
    "PyQt5.QtGui": "PySide6.QtGui",
    "PySide6.QtWebEngineWidgets": "PySide6.QtWebEngineWidgets",
    
    # Decoradores de Sinais, Slots e Propriedades
    "pyqtSignal": "Signal",
    "pyqtSlot": "Slot",
    "pyqtProperty": "Property",
    
    # Substituições de namespaces se necessário (opcional, mas bom ter)
    "QtCore.pyqtSignal": "QtCore.Signal",
    "QtCore.pyqtSlot": "QtCore.Slot",
    "QtCore.pyqtProperty": "QtCore.Property",
}

def converter_arquivos(diretorio):
    """Percorre o diretório e aplica as substituições nos arquivos .py."""
    print(f"Iniciando varredura no diretório: {os.path.abspath(diretorio)}\n")
    arquivos_modificados = 0
    
    for dirpath, _, filenames in os.walk(diretorio):
        for filename in filenames:
            if filename.endswith(".py"):
                caminho_arquivo = os.path.join(dirpath, filename)
                
                try:
                    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                        conteudo = f.read()
                except Exception as e:
                    print(f"-> Erro ao ler {caminho_arquivo}: {e}")
                    continue

                conteudo_original = conteudo
                for antigo, novo in substituicoes.items():
                    conteudo = conteudo.replace(antigo, novo)

                if conteudo != conteudo_original:
                    arquivos_modificados += 1
                    print(f"Modificando: {caminho_arquivo}")
                    try:
                        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                            f.write(conteudo)
                    except Exception as e:
                        print(f"-> Erro ao escrever em {caminho_arquivo}: {e}")

    print(f"\nConversão concluída! {arquivos_modificados} arquivo(s) modificado(s).")
    print("Próximos passos: ajuste 'requirements.txt' e 'setup.py', e teste o aplicativo.")


if __name__ == "__main__":
    if not os.path.isdir(DIRETORIO_PROJETO):
        print(f"ERRO: Diretório do projeto '{DIRETORIO_PROJETO}' não encontrado.")
        print("Verifique se o script 'migration.py' está no lugar certo (um nível acima da pasta do projeto).")
    else:
        converter_arquivos(DIRETORIO_PROJETO)