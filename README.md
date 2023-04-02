
# chatGPT-plugin/privateDocs

## O que seria legal de fazer?

Estava pensando em um caso de uso o mais banal possível e ao mesmo tempo algo que eu poderia utilizar. Minha ideia inicial é incorporar na base de dados do chatGPT qualquer documento privado (por exemplo, um PDF de contrato confidencial) para possibilitar um posterior uso. Se ao final eu conseguir perguntar: “Qual o valor do contrato XYZ?”, já seria um sucesso. Se isso funcionar, poderíamos acrescentar outros formatos de dados e formas de manter essa base atualizada constantemente.

## Quais os meus objetivos?

No inicio, queria só aprender mesmo. Se estiver confortável em criar um plugin do zero ao final, entender as limitações e possibilidades, já estaria satisfeito. O que vier além disso é bonus

1.  Já existe algum plugin que faz isso?
    1.  [ChatPDF](https://www.chatpdf.com/)
    2.  [PDF GPT](https://pdfgpt.io/)

Contudo, ambas as ferramentas acima não são exatamente um plugin. Ainda dependem de uma UI por cima do chatGPT para funcionar. O ideal, em termos de aprendizado (principalmente) e usabilidade é realmente ser um plugin para poder ser utilizado como direto na UI original. Sem contar que com um plugin toda a parte de integração automática para consumir os documentos poderia ser feita no background sem necessitar de intervenção manual.

1.  É possível criar um plugin HOJE (está aberto ao público geral)? Se não, quando? Quais os requisitos para ter essa liberação?
    a.  Existe uma [lista de espera](https://openai.com/waitlist/plugins) para criação de plugins, por enquanto fizeram algumas parcerias e irão liberar acessos pouco a pouco.
    b.  Existe uma [API](https://openai.com/product#made-for-developers), porém ela é [paga](https://openai.com/pricing#language-models).

Ou seja, é possível criar, mas nao instalar. Isso não impede de iniciar os trabalhos.

1.  Como criar um plugin de forma geral?
Esse [projeto da OPENAI](https://github.com/openai/chatgpt-retrieval-plugin) já dá um direcionamento bem claro do que é necessário.
Basicamente um plugin é um backend que expõe uma API para o chatGPT utilizar, além de fazer o processamento de novos documentos privados que serão salvos em formato já encoded em um banco de dados.

O trabalho principal será: 1) subir esse projeto exemplo 2) configurar uma integração para automaticamente acrescentar/manter atualizado os documentos.

2.  Qual seria a arquitetura sugerida?
Para simplificar o máximo, iremos pelo caminho mais simples:

#### Choosing a Vector Database 
Redis. Não necessariamente o melhor, mas o mais conhecido e que possui um free tier que iremos conseguir usar.

#### Authentication Methods
Nenhum. Os documentos do primeiro teste serão privados, mas nao confidenciais. Posteriormente podemos adicionar uma autenticação sem problemas.

#### Deployment
Fly.io possui um plano free que podemos utilizar. Outras opcões como AWS poderiam funcionar de forma gratuita também, mas iremos com o Fly.io mesmo.

3.  Quais fontes de informações seriam interessantes todo mundo dar uma olhada antes de iniciar?
Principalmente esse projeto: https://github.com/openai/chatgpt-retrieval-plugin

4.  Quais as expectativas de tempo e esforço?
    1. Nenhuma. Vou quando der, se der. Cada um no seu tempo. Particularmente falando, só irei mexer aos finais de semana.

## Como posso ajudar? Qual a forma de colaboração?

O canal oficial de comunicação é o slack. Não vou colar o link publico aqui, mas me avise caso queira entrar. Uma vez dentro, utilize o github para responder as perguntas acima, submeter PRs, etc. Vamos alinhando diretivas gerais no slack e, quando tivermos um mínimo de direcionamento técnico básico, passamos para a implementação.

## Próximos passos

 1. Clone e deploy do retrieval plugin com o banco de dados de deployment escolhido
 2. Criar uma pipeline de CI/CD para o projeto
 3. Testes FORA DO AMBIENTE do chatGPT via chamadas na API do app recem deployado com documentos privados.
 4. Uma vez liberado a cadastro de plugins, instalar dentro do proprio chatGPT
 5. Especificamente para o confluence, criar uma integração para enviar TODO o conteudo para o plugin e garantir a auto-atualizacao ao longo do tempo.


