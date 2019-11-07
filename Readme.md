# Atena

## Resumo

Veículos autônomos são robôs que dispõem de sensores e sistemas avançados de controle que lhes permitem movimentar de forma independente e sem intervenção de um motorista humano. Esses robôs têm sido desenvolvidos
como solução para o problema dos acidentes de trânsito que causam grande número de vítimas. Neste trabalho, o objetivo é simular um mini veículo autônomo capaz de parar frente a obstáculos, seguir a pista corretamente e interpretar a sinalização de trânsito em um cenário dinâmico para se chegar a um destino determinado inicialmente. O protótipo de baixo custo utiliza um computador Raspberry-Pi e uma câmera para executar ações como: identificação de placas de sinalização, detecção de delimitações da pista, acionamento da buzina, além de determinar o controle de movimentação e velocidade. Para detecção e reconhecimento da sinalização horizontal e vertical, são utilizados algoritmos de visão computacional. Algoritmos de controle de movimentação e velocidade foram implementados para possibilitar o movimento do robô no ambiente. O projeto poderá facilitar o aprendizado de crianças e adolescentes sobre as aplicações de sistemas inteligentes e possibilitará que educadores trabalhem com as placas de sinalização, regras de circulação para pedestres e motoristas, esquemas referenciais e a importância de respeitar as normas de trânsito de forma lúdica.

Palavras-chave: Inteligência Artificial. Veículo autônomo. Educação.


## 1. Introdução

Um robô autônomo é um sistema que dispõe de sensores e outros sistemas de hardware e software que lhe permitem movimentar de forma independente e sem intervenção humana. Robôs autônomos têm sido desenvolvidos para solucionar problemas em diversas áreas, tais como medicina, indústria, logística, entretenimento e também no trânsito das cidades.
Os robôs que atuam no trânsito têm que ser capazes de interpretar corretamente as informações do seu ambiente, evitar situações perigosas para as pessoas e para ele mesmo, movimentar-se de acordo com as normas de trânsito e alcançar o seu destino, tarefas que são bastante desafiadoras tanto para robôs quanto para seres humanos. O Código de Trânsito Brasileiro (CTB) define regras específicas de circulação que devem ser respeitadas por todos os usuários da via. A partir daí, surge a necessidade de criar métodos mais interativos de aprendizagem, sendo a robótica uma grande aliada do processo.
Neste contexto, este projeto trabalha com alguns aspectos da dinâmica do trânsito utilizando um mini robô autônomo em um cenário urbano com vias, placas, pedestres, dentre outros elementos.

### 1.1 Objetivos

O objetivo do trabalho é possibilitar, com a utilização de um protótipo de veículo elétrico em um cenário educativo, a demonstração de conceitos de robótica e também o aprendizado da dinâmica do trânsito, como por exemplo:
* Controle de movimentação e velocidade;
* Detecção de delimitações da pista;
* Parada obrigatória;
* Detecção de faixa de pedestres;
* Detecção de outras placas;
* Leitura dos caracteres das placas de localização;
* Funcionamento do semáforo;
* Navegação até o destino escolhido; e
* Parada ao detectar obstáculos dinâmicos.

### 1.2. Cronograma

O desenvolvimento do projeto teve início em agosto de 2019, após a equipe ter sido formada em julho. Durante os meses de agosto, setembro e outubro foram realizadas diversas tarefas que podem ser resumidas nas seguintes etapas:
* Desenvolvimento do Protótipo;
* Desenvolvimento da Pista;
* Preparação das Imagens e Objetos e Treinamento;
* Implementação e teste de Algoritmos no  Robô; e
* Interface do Robô.


## 2. Desenvolvimento do projeto

O robô construído para o projeto possui um computador embarcado Raspberry Pi, uma câmera, um sensor de distância à laser, fototransistores, uma ponte H, motores, baterias, e sua estrutura foi desenvolvida com madeira MDF e uma chapa metálica. Os dados dos sensores são utilizados pelos algoritmos de visão computacional para obter informações sobre o ambiente. Algoritmos de controle de movimentação e velocidade foram implementados para possibilitar o movimento do robô no cenário.
As seções a seguir apresentam as tarefas realizadas em cada etapa do projeto e, quando necessário, a fundamentação teórica resumida dos conceitos envolvidos. Uma ferramenta que ajudou bastante na organização das tarefas, no gerenciamento do cronograma e no compartilhamento de informações entre os integrantes do projeto foi o Trello, uma aplicação web que permite fazer uma lista de tarefas com vários recursos relacionados. 

### 2.1. Desenvolvimento do Protótipo 

Esta etapa consistiu em:
* Elaboração do Projeto do Protótipo;
* Configurações do Raspberry Pi 3 B+;
* Implementação dos Componentes e Sensores;
* Montagem do Protótipo; e
* Testes Básicos.

Iniciamos nosso projeto desenvolvendo um protótipo de carro elétrico, com capacidade de embarcar os componentes eletrônicos propostos. Em seguida, realizamos a instalação e configuração dos softwares necessários para o funcionamento do computador embarcado Raspberry Pi. Uma rede virtual privada (VNC) foi criada para que fosse possível acessar remotamente o computador embarcado no robô, permitindo a transmissão das imagens para um monitor externo. Alguns itens como parafusos, espaçadores e Jumpers foram necessários para a montagem do protótipo e o modo de fixação e adaptação de cada elemento do projeto no chassi foi pensado com intuito de facilitar a mobilidade do protótipo.

![alt text](https://raw.githubusercontent.com/EstanislauFilho/Atena/master/Imagens/Atena.png)

## Desenvolvido com

* [Python Software Foundation](https://maven.apache.org/) - Linguagem de programação;
* [OpenCV](https://opencv.org/) - Biblioteca de Visão Computacional desenvolvido pela Intel em 1999;
* [PyCharm](https://www.jetbrains.com/pycharm/) - IDE de desenvolvimento.

## Contribuição

Leia Contribuindo.md para obter detalhes sobre o processo de envio de solicitações pull ao desenvolvedor.

## Versão

Para as versões disponíveis, consulte as tags neste repositório.

## Autores

* **Estanislau de Sena Filho** - *Estudante de Engenharia de Computação no* [CEFET-MG](http://www.cefetmg.br/)
* **José Antônio Carneiro Ávila** - *Estudante de Engenharia de Computação no* [CEFET-MG](http://www.cefetmg.br/)
* **Natália Cosse Batista** - *D.Sc. Professora no* [CEFET-MG](http://www.cefetmg.br/)

## Licença

Este não é um projeto licenciado. Seu objetivo é exclusivo para estudar e aprender sobre visão computacional.

## Agradecimentos

* Professora Sílvia Albuquerque
* Madeireira Paranaense  
* PrintBH Produções 
* Itamar Gonçalves

