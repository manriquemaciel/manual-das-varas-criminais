.. coding: utf-8

.. raw:: pdf

   PageBreak

Análise Múltipla com Movimentação Múltipla
=========================================

Nesta aula, será demonstrado como realizar a **análise múltipla com movimentações consecutivas** no sistema ProJUDI. Trata-se de procedimento no qual, após a análise múltipla inicial, o servidor **continua aplicando outras movimentações sobre o mesmo conjunto de processos**, como, por exemplo, **intimação seguida de suspensão**.

Cenário prático
---------------

Exemplo de aplicação:

- Processos vinculados ao **agrupador**: *Decisão IRDR e Tarifas*.

Objetivo do procedimento:

1. **Intimar as partes** acerca da decisão judicial;
2. **Suspender os processos** em razão do efeito vinculante do IRDR.

Procedimentos
-------------

Passo 1 – Acesso aos processos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Acessar a fila **Retorno de Conclusão**;
2. Utilizar o **filtro por agrupador**, selecionando, por exemplo: *Decisão IRDR e Tarifas*;
3. Clicar em **“Análise Múltipla”**;
4. Selecionar os processos desejados;
5. Clicar em **“Próximo passo”**.

Passo 2 – Primeira movimentação: intimação
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Selecionar a ação **“Intimar”**;
2. Definir os destinatários:
   - Advogado do promovente (autor);
   - Advogado do promovido (réu);
3. Informar:
   - Prazo (em dias úteis ou corridos);
   - Localizador (opcional), por exemplo: *aguardando decisão IRDR*;
4. Clicar em **“Próximo passo”**;
5. Revisar os processos selecionados;
6. Clicar em **“Continuar movimentando”**.

.. warning::

   Caso algum processo possua **duas pendências simultâneas**  
   (ex.: juntada pendente + retorno de conclusão), o sistema **impedirá a movimentação**.

   Nessa hipótese:
   - Acesse individualmente o processo;
   - Elimine uma das pendências (ex.: em **Análise de Juntadas**, clicar em *Dispensar*);
   - Retorne à análise múltipla e repita o procedimento.

Passo 3 – Segunda movimentação: suspensão
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Após a conclusão da intimação:

1. Clicar em **“Movimentar”**;
2. Selecionar a ação **“Suspender”**;
3. Preencher:
   - Data de início da suspensão;
   - Indicar se a suspensão possui prazo determinado;
   - Caso não seja determinado, informar o fundamento (ex.: aguardando julgamento do IRDR);
   - Tipo de suspensão (ex.: *sobrestamento por IRDR*);
4. Clicar em **“Próximo passo”**;
5. Revisar os processos;
6. Clicar em **“Salvar”**.

Ao final, o sistema exibirá a mensagem:

*“Processos movimentados com sucesso.”*

Verificação
-----------

Ao acessar qualquer um dos processos movimentados, deverá constar:

- **Status do processo**: *Suspenso* ou *Sobrestado*;
- **Histórico de movimentações**:
  - Análise da decisão;
  - Intimação das partes;
  - Suspensão do processo.

Resumo
------

- A análise múltipla com movimentação contínua permite aplicar **duas ou mais providências em sequência** sobre um mesmo grupo de processos.
- É especialmente indicada para decisões com **efeitos em cadeia**, tais como:
  - Intimação + suspensão;
  - Citação + remessa;
  - Intimação + arquivamento.
- Trata-se de recurso que proporciona **expressiva economia de tempo**, permitindo a tramitação de dezenas de processos em poucos minutos, com padronização e segurança procedimental.
