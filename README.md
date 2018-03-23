# Laboratório Python

[![Build Status](https://travis-ci.org/agileclass/lab-python.svg?branch=master)](https://travis-ci.org/agileclass/lab-python)[![Coverage Status](https://coveralls.io/repos/github/agileclass/python-games/badge.svg?branch=master)](https://coveralls.io/github/agileclass/python-games?branch=master)[![N|Solid](https://sonarcloud.io/api/project_badges/measure?project=python-games&metric=alert_status)](https://sonarcloud.io/dashboard?id=python-games)

- IDE: 
https://code.visualstudio.com/download

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

- Enviar alterações pela primeira vez

  > git push --set-upstream origin nomedobranch

- Trocar de branch

  > git checkout nomedobranch

- Fazer merge a partir do master

  >git checkout master

  >git merge nomedobranch

- Remover um branch local e remoto

  > git branch -d nomedobranch

  > git push origin --delete iss53

- Listar branches que não possui merge

  > git branch --no-merged

## Testes Unitários

- Executar todos do testes da pasta 'Games'

  >py -m unittest discover Games

## Cobertura de Código

- Verificar Cobertura de Testes

  >coverage  run --omit=Games/test*  -m unittest discover -v Games

- Relatório de Cobertura de Testes (Formato Texto)

  >coverage report -m

- Relatório de Cobertura de Testes (Formato HTML)

  >coverage html

  ### Chaves de Acesso

- Aceitar chave pública

  > ssh-add