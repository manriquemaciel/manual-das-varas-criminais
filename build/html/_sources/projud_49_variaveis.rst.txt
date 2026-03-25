.. coding: utf-8

=======================================================
Variáveis
=======================================================

Nesta aula, será demonstrado como inserir **variáveis** nos modelos de documentos do sistema **ProJUDI**. O uso de variáveis é **opcional**, porém altamente recomendado, pois proporciona **automação**, **padronização** e **redução de erros manuais** na elaboração de documentos.

O que são Variáveis
--------------------

As variáveis são **comandos automáticos** que o sistema substitui por informações reais do processo no momento da geração do documento.

Exemplos de substituição automática:

- ``${assinaturaJuiz}`` → Nome e cargo do magistrado responsável
- ``${dataAtual}`` → Data corrente da expedição do documento
- ``${partePassiva}`` → Nome da parte ré no processo

Como Inserir uma Variável
--------------------------

Para inserir uma variável em um modelo de documento:

1. Acesse a edição do modelo em **Outros > Meus Modelos de Documentos**.
2. Clique no botão **Variável**, localizado no editor de texto.
3. Será exibida uma janela contendo a **lista de variáveis disponíveis**.
4. Localize a variável desejada e clique sobre ela para copiá-la.
5. Cole a variável no ponto exato do texto onde a informação deverá ser exibida.

Exemplos Práticos de Uso
--------------------------

Assinatura do Magistrado
^^^^^^^^^^^^^^^^^^^^^^^^^

- **Variável**: ``${assinaturaJuiz}``
- **Finalidade**: Exibir automaticamente o nome e o cargo do juiz de direito
- **Utilização recomendada**: Rodapé do documento, no campo de assinatura

Parte Passiva (Réu)
^^^^^^^^^^^^^^^^^^^^

- **Variável**: ``${partePassiva}``
- **Finalidade**: Inserir automaticamente o nome da parte ré
- **Utilização recomendada**: Corpo de sentenças, mandados e certidões

Data Atual
^^^^^^^^^^^^

- **Variável**: ``${dataAtual}``
- **Finalidade**: Inserir a data da expedição do documento
- **Utilização recomendada**: Cabeçalho, corpo ou rodapé do documento

.. note::

   Algumas variáveis possuem nomes semelhantes e podem produzir resultados equivalentes. Recomenda-se testar as opções disponíveis para identificar a mais adequada ao modelo utilizado.

Pré-visualização do Documento
-------------------------------

Após a inserção das variáveis, utilize a opção **Pré-visualizar** para conferir o resultado final do documento.

Durante a pré-visualização:

- ``${partePassiva}`` será substituída pelo nome cadastrado da parte ré
- ``${assinaturaJuiz}`` exibirá o nome do magistrado logado
- ``${dataAtual}`` refletirá a data do dia da expedição

Dicas Importantes
------------------

- As variáveis **não exigem asteriscos, chaves adicionais ou configurações extras** para funcionar.
- Podem ser utilizadas **quantas variáveis forem necessárias** em um mesmo documento.
- O uso de variáveis reduz erros de digitação e agiliza significativamente o trabalho da secretaria.

Conclusão
-----------

Com a utilização correta das variáveis, os modelos de documentos tornam-se **dinâmicos**, **padronizados** e **prontos para uso automático** no sistema ProJUDI.

Na próxima aula, será demonstrado como **utilizar modelos com variáveis** na expedição efetiva de documentos processuais.
