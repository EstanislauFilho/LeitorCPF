# LeitorCPF


Este projeto trata da criação de scripts python capazes de ler o CPF e o Nome em imagens de Carteiras Nacional de Habilitação (CNH). Para o desenvolvimento deste projeto, foram utilizadas as bibliotecas OpenCV, Pytesseract e a linguagem de programação Python.

![alt text](https://raw.githubusercontent.com/EstanislauFilho/LeitorCPF/main/Imagens/det1.png)
![alt text](https://raw.githubusercontent.com/EstanislauFilho/LeitorCPF/main/Imagens/det2.png)

## Iniciando o Projeto

As instruções a seguir permitirão que você execute, desenvolva e contribua com o projeto em questão. Siga todas as etapas abaixo para executar o projeto LeitorCPF usando as bibliotecas OpenCV, Pytesseract e a linguagem de programação Python.


### Pré-requisitos

Para executar os scripts em python presentes neste projeto, você precisa instalar os seguintes componentes em sua máquina:

```
Python 3.6 ou versão superior.

OpenCV 3.4.1.

Pytesseract 0.3.7
```

## Execução e Teste

Para testar o script main.py, você deve abir o script em seu ambiente de desenvolvimento Python. Em seguida, é nescessário alterar no código o caminho onde se encontra as imagens da pasta dataset.


### Executando o script main.py

Este script python faz a leitura de do CPF e do Nome em imagens de CNH's. Para este experimento foi utilizada a imagens baixas da internet e que se encontram presente na pasta "dataset". Para testá-lo, basta executá-lo no IDE.

Outra forma de executar o script é via terminal, pelo seguinte comando:
```
python3 main.py
```

## Resultado

Durante os testes realizados o algoritmo apresentou certa dificuldade para reconhecer os caracteres principalmente do campo Nome. 

O resultado do experimento realizado pode ser visto na imagem abaixo.
![alt text](https://raw.githubusercontent.com/EstanislauFilho/LeitorCPF/main/Imagens/resultado.png)


## Planejamento

Este projeto foi desenvolvido utilizando a ferramenta Trello para gerenciar as tarefas e as etapas que foram desenvolidas.

O fluxograma abaixo apresenta o fluxo de desenvolvimento do projeto.
![alt text](https://raw.githubusercontent.com/EstanislauFilho/LeitorCPF/main/Imagens/fluxograma.png)

## Desenvolvido com

* [OpenCV](https://opencv.org/) - Biblioteca de Visão Computacional desenvolvida pela Intel em 1999;
* [Python Software Foundation](https://maven.apache.org/) - Linguagem de Programação;
* [Spyder](https://www.jetbrains.com/pycharm/) - IDE usada para o desenvolvimento do Script.


## Versões

Para as versões disponíveis, consulte as tags neste repositório.

## Autor

* **Estanislau de Sena Filho** - *Computer Engineering Student at* [LinkedIn](https://www.linkedin.com/in/estanislau-sena-filho/)

## Licença

Este não é um projeto licenciado. Seu propósito é exclusivo para estudar e aprender sobre visão computacional.
