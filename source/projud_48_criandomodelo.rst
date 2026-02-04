.. coding: utf-8

=======================================================
Criando Modelos de Documento
=======================================================

Nesta aula, será apresentado o procedimento para **criação de modelos de documentos** no sistema **ProJUDI**, utilizando a funcionalidade disponível no menu **Outros > Meus Modelos de Documentos**.

Esses modelos permitem **padronização**, **agilidade** e **automação** na expedição de documentos, por meio do uso de **variáveis dinâmicas**.

Acesso à Funcionalidade
------------------------

Para acessar a área de modelos de documentos:

1. Clique no menu superior **Outros**.
2. Selecione a opção **Meus Modelos de Documentos**.
3. Para visualizar modelos já existentes, clique em **Pesquisar**.
4. Para criar um novo modelo, clique em **Novo**.

Criação de Novo Modelo
-----------------------

Na tela de cadastro do modelo, preencha os seguintes campos:

- **Descrição**:
  - Informe um nome claro e objetivo para o modelo  
    (ex.: *Mandado de Citação Criminal*, *Certidão de Decurso de Prazo*).

- **Tipo de Documento**:
  - Selecione o tipo correspondente, como:
    - Citação
    - Intimação
    - Alvará
    - Mandado
    - Certidão
    - Ofício

- **Competência**:
  - Indique a área de atuação:
    - Cível
    - Criminal
    - Juizado
    - Família, entre outras.

.. note::

   O modelo criado ficará **disponível para todos os usuários da unidade judiciária (vara)**.

Inserção e Edição do Conteúdo
-------------------------------

- Copie e cole o texto do documento no campo **Inserir texto**.
- Utilize o botão **Maximizar** para facilitar a edição e visualização do conteúdo.

Ao colar textos provenientes de editores externos (Word, LibreOffice, etc.), pode ocorrer a inserção de **âncoras ocultas**, identificadas por ícones de bandeira azul.

Para removê-las:

- Clique com o botão direito sobre a âncora;
- Selecione a opção **Remover âncora**.

Formatação do Texto
--------------------

A formatação deve ser realizada preferencialmente por meio do botão **Estilo**, garantindo padronização visual dos documentos.

Opções mais utilizadas:

- **Parágrafo 1**: recuo de 2 cm
- **Parágrafo 2**: recuo de 3 cm (padrão mais utilizado)
- **Parágrafo 3**: recuo de 4 cm
- **Emenda**: utilizado para títulos ou trechos de destaque

.. tip::

   O espaçamento entre linhas (ex.: 1,15 ou 1,5) será preservado conforme o texto colado no editor.

Inserção de Variáveis
----------------------

O ProJUDI permite a utilização de **variáveis automáticas**, que são preenchidas pelo sistema no momento da expedição do documento, conforme os dados do processo.

Exemplos de variáveis:

- ``${nomeParte}`` – Nome da parte ou do réu
- ``${numeroProcesso}`` – Número do processo
- ``${assinatura}`` – Campo de assinatura automática

.. note::

   O uso de variáveis será detalhado de forma aprofundada na **aula seguinte**.

Finalização do Modelo
-----------------------

Após concluir a edição do texto:

1. Clique em **Salvar** para registrar o modelo.
2. Utilize a opção **Pré-visualizar** para conferir o resultado final.
3. Ajuste:
   - Quebras de linha excessivas;
   - Espaços em branco;
   - Recuos e alinhamentos, a fim de manter o documento, preferencialmente, em **uma única lauda**.

Edição e Remoção de Modelos
----------------------------

- Para editar um modelo existente, clique em **Alterar**.
- Para excluir, clique em **Remover**.

Durante a edição, é recomendável:

- Remover espaços indevidos antes do cabeçalho (ex.: “Autos nº ...”);
- Centralizar títulos como **Mandado de Citação**, **Certidão**, etc.;
- Ajustar parágrafos e recuos utilizando exclusivamente o botão **Estilo**.

Conclusão
------------

Após o salvamento, o modelo ficará disponível na listagem de **Meus Modelos de Documentos**, podendo ser utilizado em futuras expedições, com **preenchimento automático das variáveis** e manutenção do padrão institucional da unidade.
