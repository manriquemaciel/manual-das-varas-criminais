.. coding: utf-8

===============================================================
Contagem do Prazo nas Intimações e Citações
===============================================================

Nesta aula, será explicado como o sistema **ProJUDI** realiza a **contagem automática dos prazos processuais** decorrentes de **intimações** e **citações**, com base na data da postagem, da leitura e nas regras legais aplicáveis.

Visão Geral
------------

O ProJUDI permite ao servidor visualizar de forma **automática, detalhada e segura** a contagem dos prazos processuais, a partir:

- Da **data da postagem** do ato;
- Da **data da leitura eletrônica**, quando realizada;
- Da aplicação das regras legais de contagem de prazo.

Essa funcionalidade garante **transparência**, **precisão** e **segurança jurídica** na tramitação dos processos.

Acesso à Contagem do Prazo
----------------------------

Para acessar a contagem do prazo:

1. Acesse o processo desejado;
2. Clique na aba **Movimentações**;
3. Selecione a movimentação correspondente à **citação** ou **intimação**;
4. Alternativamente, acesse a aba **Citações e Intimações** e clique na pendência indicada como **Decurso de Prazo**.

Análise pelo Decurso de Prazo
-------------------------------

Na aba **Citações e Intimações**, há uma coluna específica denominada **Decurso do Prazo**, na qual são listados:

- Atos cujo prazo **já transcorreu**;
- Atos com prazo em curso ou aguardando leitura.

Ao clicar sobre a pendência, o sistema direcionará o usuário para a **tela da intimação ou citação** correspondente.

Tela da Intimação ou Citação
------------------------------

Na tela do ato, o sistema exibe as seguintes informações:

- **Data da postagem**;
- **Data da leitura**, quando realizada;
- **Data prevista para o decurso do prazo**;
- **Status do prazo**, tais como:
  
  - Aguardando leitura;
  - Em curso;
  - Prazo decorrido.

.. note::
   Ao clicar sobre a **data do decurso**, o sistema disponibiliza o detalhamento completo do cálculo do prazo.

Detalhamento do Cálculo do Prazo
---------------------------------

O botão **Detalhamento do Cálculo do Prazo** apresenta:

- Data da **leitura eletrônica**;
- Data de **início do prazo**;
- Quantidade de **dias úteis contabilizados**;
- **Feriados e finais de semana desconsiderados**;
- Data de **término do prazo**;
- Situação atual do prazo.

Exemplo ilustrativo:

::

    Leitura: 10/09
    Início do prazo: 11/09
    Dias computados: 5 dias úteis
    Feriado: 13/09 (desconsiderado)
    Término: 18/09
    Status: Prazo Decorrido

Ações Possíveis após o Decurso
--------------------------------

Após identificado o decurso do prazo, a Secretaria poderá:

- **Analisar o decurso**, com:
  
  - Inserção de **certidão de decurso de prazo**;
  - Lançamento de **ato ordinatório**;
  - Movimentação direta do processo (ex.: conclusão, intimação, suspensão);

- **Dispensar a pendência**, quando não houver providência a ser adotada;
- **Acompanhar prazos futuros**, referentes a novas intimações ou citações.

Intimações Recentes
---------------------

Quando a intimação ou citação for **recente**, o sistema exibirá apenas a **data da postagem**, sem apresentar ainda:

- Data da leitura;
- Início do prazo;
- Data do decurso.

.. warning::
   Isso ocorre porque o sistema observa o prazo legal de até **10 (dez) dias** para que o destinatário realize a leitura da intimação eletrônica, conforme o art. 5º da Lei nº 11.419/2006. Somente após esse período, se não houver leitura, o sistema considera a **leitura automática**.

Resumo
--------

A contagem automática de prazos no ProJUDI proporciona:

- Transparência na tramitação dos atos processuais;
- Precisão na contagem dos prazos, com exclusão automática de feriados e finais de semana;
- Facilidade para análise e tomada de providências a partir das pendências.

.. note::
   Recomenda-se sempre a conferência da aba **Detalhamento do Cálculo do Prazo**, como forma de assegurar a correta interpretação e aplicação dos prazos processuais.
