# chatGPT-plugin/privateDocs

## O que é esse projeto?

Esse projeto tem como objetivo criar um plugin para o chatGPT que permita incorporar documentos privados (como um PDF de contrato confidencial) na base de dados para possibilitar um posterior uso. O objetivo é que, ao final, seja possível perguntar: “Qual o valor do contrato XYZ?” e obter uma resposta. Se isso funcionar, poderíamos acrescentar outros formatos de dados e formas de manter essa base atualizada constantemente.

## Objetivos do projeto

O principal objetivo do projeto é aprender sobre a criação de um plugin do zero, entender as limitações e possibilidades. Além disso, criar um plugin que possa ser utilizado diretamente na UI original do chatGPT, sem depender de uma UI por cima do chatGPT para funcionar. 

## Existem plugins similares?

Existem ferramentas que realizam funcionalidades similares, como o ChatPDF e o PDF GPT. Contudo, ambas as ferramentas não são exatamente um plugin e ainda dependem de uma UI por cima do chatGPT para funcionar.

## É possível criar um plugin hoje?

Embora não seja possível instalar um plugin hoje, é possível iniciar o projeto e criar um plugin que esteja pronto quando a instalação for liberada. A OpenAI criou uma API, porém ela é paga. Existe uma lista de espera para criação de plugins, por enquanto fizeram algumas parcerias e irão liberar acessos pouco a pouco.

## Como criar um plugin?

O projeto da OPENAI já dá um direcionamento claro do que é necessário para criar um plugin. Basicamente, um plugin é um backend que expõe uma API para o chatGPT utilizar, além de fazer o processamento de novos documentos privados que serão salvos em formato já encoded em um banco de dados.

O trabalho principal será: 
1. Subir esse projeto exemplo
2. Configurar uma integração para automaticamente acrescentar/manter atualizado os documentos.

## Qual seria a arquitetura sugerida?

Para simplificar o máximo, iremos pelo caminho mais simples:

#### Banco de dados
Pinecone. Possui um free tier bom. Os demais nao possuem free tier OU não estao prontos ainda.(i.e: Redis precisa de um modulo que nao existe no free tier)

#### Métodos de autenticação
Nenhum. Os documentos do primeiro teste serão privados, mas não confidenciais. Posteriormente podemos adicionar uma autenticação sem problemas.

#### Deploy
Fly.io possui um plano free que podemos utilizar. Outras opções como AWS poderiam funcionar de forma gratuita também, mas iremos com o Fly.io mesmo.

## Fontes de informações

Principalmente esse projeto: https://github.com/openai/chatgpt-retrieval-plugin

## Expectativas de tempo e esforço

Não há expectativas de tempo ou esforço definidas. Cada um poderá trabalhar no projeto no seu próprio tempo. 

## Como posso ajudar?

O canal oficial de comunicação é o Slack. Para entrar, é necessário solicitar o link. Uma vez dentro, utilize o Github para responder as perguntas acima, submeter PRs, etc. As diretrizes gerais serão definidas no Slack e, quando tivermos um mínimo de direcionamento técnico básico, passamos para a implementação.

## Próximos passos

 1. Clone e deploy do retrieval plugin com o banco de dados
 2. Criar uma pipeline de CI/CD para o projeto
 3. Testes FORA DO AMBIENTE do chatGPT via chamadas na API do app recem deployado com documentos privados.
 4. Uma vez liberado a cadastro de plugins, instalar dentro do proprio chatGPT
 5. Especificamente para o Confluence, criar uma integração para enviar TODO o conteudo para o plugin e garantir a auto-atualizacao ao longo do tempo.


