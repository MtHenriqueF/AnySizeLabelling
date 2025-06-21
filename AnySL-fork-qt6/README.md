
O repositório tem como intuito migrar o aplicativo [AnySizeLabelling](https://github.com/LPG-Uerj/AnySizeLabeling) que é um fork do repositorio [digitalsreeni-image-annotator](https://github.com/bnsreenu/digitalsreeni-image-annotator) do Qt5 (PyQt5) para Qt6 (PySide6).

---

## Motivação

A versão **Qt5**, utilizada por muitos projetos baseados em **PyQt5**, está entrando em absolência, com suporte oficial limitado e descontinuação de atualizações de segurança e correções de bugs.


---

## Objetivo do repositório

O propósito deste projeto é fornecer:

Um **script de migração automática**, que percorre recursivamente os arquivos `.py` de um projeto, substituindo de forma segura os principais pontos de divergência entre PyQt5 e PySide6.

Alterações de algumas descontinuidades e mudanças de lógicas que ocorre entre PyQt5 e PySide6
---

