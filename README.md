# Laboratório Python

- IDE: https://code.visualstudio.com/download
- Git: https://git-scm.com/book/pt-br/v1/Primeiros-passos-Instalando-Git
- Python: Versão 3.6
  - Configurar VS: [link](https://stackoverflow.com/questions/43313903/how-to-setup-visual-studio-code-to-find-python-3-interpreter-in-windows-10)
  - Orientação a Objetos: [link](http://pythonclub.com.br/introducao-classes-metodos-python-basico.html)
- Tutorial Python: https://wiki.python.org.br/AprendaProgramar
## Comandos Git
### Clone
- Baixar um branche específico
  >git clone [repositorio] -b [nomedobrache]
  - Exemplo
  git clone https://github.com/agileclass/python-games.git -b taboada
### Alterações
- Obter últimas alterações
  >git pull
- Verificar alterações locais
  >git status
- Adicionar alterações
  > git add .
- Registrar comentários
  >git commit -m "comentário"
- Adicionar e fazer commit
  >git commit -a -m 'comentario'
- Enviar ao repositório remoto
  >git push
### Branch
- Verifique nome do branch atual
  > git branch
- Criar brach
  > git checkout -b nomedobranch
- Trocar de branch
  > git checkout nomedobranch
### Chaves de Acesso
- Aceitar chave pública
  > ssh-add
## Testes
- Executar todos do testes da pasta 'Games'
>py -m unittest discover Games