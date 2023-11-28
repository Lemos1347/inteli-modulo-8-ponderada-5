# Atividade ponderada 5 Inteli módulo 8

## Descrição

Esse repositório contém os códigos para a seguinte atividade:

`Utilizando um LLM (local ou API externa), crie um chatbot simples com instruções customizadas para ajudar um usuário a pesquisar normas de segurança em ambientes industriais. O sisema deve contar com uma interface gráfica e responder de forma sucinta e clara sobre o que lhe foi perguntado. O sistema ainda deve ser capaz de contextualizar suas respostas a partir do seguinte documento:` [Workshop rules and safety considerations](https://www.deakin.edu.au/students/study-support/faculties/sebe/abe/workshop/rules-safety)  

## Funcionamento

https://github.com/Lemos1347/inteli-modulo-8-ponderada-5/assets/99190347/b4b7e218-b558-4162-af78-eb1dfb38683a

O arquivo `Modalfile` contém as instruções para a criação do LLM personalizado no Ollama, como importação de um modelo base e uma mensagem de 'sistema'.  
O arquivo `main.py` contém o código para a criação do chatbot e a interface gráfica.

## Como rodar

Para rodar essa aplicação tenha instalado em seu computador e que esteja rodando o [Ollama](https://ollama.ai/).  
Após se certificar disso, clone o repositório e execute o seguinte comando na root do projeto:

```bash
chmod -R o+rx Modalfile
```

Esse comando serve para dar permissões ao Ollama de consumir o arquivo `Modalfile`. Depois, baixe as bibliotecas do projeto:

```bash
pip install -r requirements.txt
```

Por fim basta executar o comando (esse comando criará um LLM personalizado no Ollama com o nome 'ppe-assistent' e depois executará nossa aplicação):

```bash
ollama create ppe-assistent -f Modalfile ; python3 main.py
```

E pronto, o chatbot estará rodando em sua máquina.
