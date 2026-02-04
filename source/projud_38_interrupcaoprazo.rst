.. coding: utf-8

===========================================================
Interrupção do Prazo
===========================================================

Nesta aula, será demonstrado como **interromper a contagem de um prazo** no sistema **ProJUDI**.

Quando Utilizar
----------------

O recurso de **Interrupção de Prazo** deve ser utilizado quando houver necessidade de **pausar temporariamente** a contagem de prazo relacionada a uma **citação** ou **intimação**.

⚠️ **Atenção:**  
Atualmente, o sistema ProJUDI permite a interrupção **exclusivamente** de prazos oriundos de:

- Citações;
- Intimações.

Prazos decorrentes de outras movimentações **não são elegíveis** para essa funcionalidade.

Passo a Passo para Interromper um Prazo
----------------------------------------

1. Acesse o processo desejado;
2. Vá até a aba **Movimentações**;
3. Localize a **decisão ou movimentação** que gerou o prazo a ser interrompido;
4. Clique em **“Movimentar a partir desta movimentação”**;
5. No menu lateral esquerdo, selecione:

   ::

      [ Ações ]
      → Outras Ações
         → Interromper o Prazo

6. Na tela **Interromper o Prazo**:

   - O sistema listará automaticamente os **prazos ativos elegíveis**;
   - Selecione o **prazo** que deseja interromper;
   - Informe a **data da interrupção**;
   - Clique em **Interromper o Prazo**.

Resultado da Interrupção
-------------------------

Após a confirmação:

- A interrupção será **registrada como nova movimentação** no processo;
- Na aba **Movimentações**, constará um evento informando:

  - Qual prazo foi interrompido;
  - A quem o prazo se referia (autor, réu, parte intimada, etc.);
  - A data a partir da qual o prazo foi interrompido;
  - A movimentação que originou o prazo (citação ou intimação).

O que Acontece Após a Interrupção
----------------------------------

Após a interrupção:

- O **sistema ProJUDI recalcula automaticamente o prazo**;
- A contagem é **retomada posteriormente**, preservando apenas o **tempo restante** do prazo original;
- Não há perda dos dias já transcorridos antes da interrupção.

Resumo
--------

- A interrupção de prazo é aplicável **somente a citações e intimações**;
- O procedimento é realizado a partir da **movimentação geradora do prazo**;
- O sistema registra a interrupção com **rastreabilidade completa**;
- A contagem do prazo é **automaticamente recalculada**, garantindo segurança jurídica e controle processual.
