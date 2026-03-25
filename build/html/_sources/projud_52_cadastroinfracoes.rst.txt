.. coding: utf-8

===============================================================
Cadastro de Infrações e Penas para Fins de Prescrição
===============================================================

O cadastro de **infrações e penas** no sistema **Projudi** é fundamental para que o próprio sistema realize o **cálculo automático do prazo prescricional**, com base na legislação penal vigente.

Esse recurso é essencial para a gestão eficiente de processos criminais, auxiliando tanto a **secretaria judicial** quanto o **gabinete do magistrado** no controle de prazos e prevenção de nulidades.

Onde cadastrar?
----------------

No processo criminal aberto:

1. Desça até a seção **Informações Adicionais**.
2. Clique em **Infrações e Penas**.
3. Caso apareça a mensagem *“Sem infração e pena”*, clique para **adicionar** o cadastro.

Preenchimento dos Campos
-------------------------

Na tela de cadastro, preencha os seguintes campos:

- **Parte**  
  Será selecionada automaticamente conforme o réu vinculado ao processo.

- **Lei**  
  Utilize os atalhos disponíveis para seleção rápida  
  (exemplo: *Código Penal*).

- **Artigo**  
  Informe o número do artigo  
  (exemplo: ``121`` – Homicídio).

- **Descrição**  
  Detalhe a forma do crime, se necessário  
  (exemplo: qualificado, tentado, consumado).

- **Complemento**  
  Campo opcional para especificações adicionais  
  (exemplo: motivo torpe, recurso que dificultou a defesa da vítima).

- **Hediondo?**  
  Marque a opção se o crime for classificado como hediondo.

- **Incidente**  
  Informe se o réu é:
  - Primário
  - Reincidente comum
  - Reincidente específico

- **Concurso de Crimes?**  
  Marque se houver concurso material, formal ou crime continuado.

Após o preenchimento, clique em **Salvar**.

Resultado e Cálculo da Prescrição
----------------------------------

Após o cadastro da infração e da pena:

- O sistema exibirá automaticamente a **data estimada da prescrição**  
  (exemplo: ``05/09/2025``).

- Ao clicar em **Detalhes**, será possível visualizar o cálculo completo, contendo:
  - **Data do fato**
  - **Data de nascimento do réu**
  - **Prazo base considerado**
  - **Reduções aplicadas**
    - Exemplo: menor de 21 anos na data do fato (redução de 50%)
  - **Fundamento legal**
    - Exemplo: art. 109 do Código Penal
  - **Tipo de prescrição**
    - Prescrição da pretensão punitiva
    - Prescrição da pretensão executória

Importante
^^^^^^^^^^^

Caso o sistema não identifique informações essenciais, como a **data de recebimento da denúncia**, será utilizada, por padrão, a **data do fato** como termo inicial do cálculo prescricional.

Por isso, é indispensável que as **movimentações processuais** estejam corretamente lançadas para garantir a precisão do cálculo.

Utilidade
----------

O cadastro correto de infrações e penas permite:

- Acompanhamento **automatizado** dos prazos prescricionais.
- Prevenção de **extinção da punibilidade** por decurso de prazo.
- Planejamento estratégico das diligências e movimentações.
- Apoio à gestão da secretaria e do gabinete.
- Maior **segurança jurídica** na tramitação do processo penal.
