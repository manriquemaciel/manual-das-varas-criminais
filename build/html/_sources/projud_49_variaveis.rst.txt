=======================================================
Variáveis
=======================================================

Nesta aula, você aprenderá a inserir **variáveis** nos seus modelos de documentos dentro do sistema Projudi. O uso de variáveis é **opcional**, mas muito útil para automação e padronização dos documentos.

O que são variáveis?
---------------------

Variáveis são comandos que são substituídos automaticamente por dados do processo quando o documento é gerado.

Por exemplo:

- ``${assinaturaJuiz}`` → Exibe o nome e cargo do juiz.
- ``${dataAtual}`` → Exibe a data corrente.
- ``${partePassiva}`` → Exibe o nome da parte ré no processo.

Como inserir uma variável
---------------------------

1. Ao editar um modelo de documento, clique no botão **Variável**.
2. Uma janela será aberta com uma lista de variáveis disponíveis.
3. Localize a variável desejada e clique nela para copiá-la.
4. Cole no local do documento onde deseja que a informação apareça.

Exemplos práticos
------------------

**Assinatura do Juiz**

- Variável: ``${assinaturaJuiz}``
- Finalidade: Exibe nome e cargo do juiz de direito
- Onde usar: No rodapé do documento, na linha de assinatura

**Parte passiva (réu)**

- Variável: ``${partePassiva}``
- Finalidade: Inserir automaticamente o nome da parte ré
- Onde usar: Ao longo da sentença ou mandado, para evitar digitação manual

**Data atual**

- Variável: ``${dataAtual}``
- Finalidade: Preencher a data corrente no documento
- Onde usar: Cabeçalhos, rodapés, corpo do documento

.. note::

   Algumas variáveis possuem nomes similares e resultados idênticos. Você pode testar qual se adequa melhor ao seu modelo.

Pré-visualização do documento
-------------------------------

Após inserir as variáveis, clique em **Pré-visualizar** para ver como o documento ficará quando for utilizado. As variáveis serão substituídas automaticamente pelos dados reais do processo:

- O nome do réu (``${partePassiva}``) aparecerá conforme o cadastro.
- A assinatura (``${assinaturaJuiz}``) mostrará o nome do juiz logado.
- A data (``${dataAtual}``) refletirá o dia da expedição do documento.

Dicas importantes
------------------

- Variáveis não precisam de asterisco (*) para funcionar.
- Utilize variáveis para evitar erros de digitação e agilizar o trabalho.
- Você pode utilizar várias variáveis no mesmo documento.

Conclusão
----------

Agora que você já sabe utilizar variáveis, seus modelos ficarão mais dinâmicos, personalizados e prontos para uso automático no sistema Projudi.

Na próxima aula, veremos como **utilizar modelos criados com variáveis** em documentos reais.

