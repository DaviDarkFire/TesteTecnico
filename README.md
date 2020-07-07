# TesteTecnico

Para executar é necessário um terminal com python3, onde ao executar a seguinte linha de comando:

  python run.py

aparecerá o seguinte menu:

  1 - Gerar Dados
  
  2 - Exibir Classificação das Famílias
  
  3 - Exibir esse Menu
  
  Ctrl+c - Sair
  
Em "1 - Gerar Dados" pode-se gerar uma quantidade arbitrária de famílias no arquivo "dados.json".
Para definir essa quantidade altere a variável "FAMILIAS" na linha 13 do arquivo "run.py". O tama-
nho padrão definido é de 1000 famílias.

Em "2 - Exibir Classificação das Famílias" pode-se executar a função pedida no teste técnico. Ao 
optar por essa opção, uma lista de famílias será exibida no terminal, indo das com maior prioridade para as com menores.
Nem todas famílias serão exibidas, aquelas que não eram elegíveis nem foram carregadas para processamento.
Também será gerado um arquivo "contemplados.json" com todas as famílias escolhidas. Pode-se usar esse arquivo
posteriormente para filtrar famílias que ja receberam o benefício.
