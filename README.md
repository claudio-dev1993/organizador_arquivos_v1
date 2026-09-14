# Organizador automático de arquivos

Automação em **Python** para mover arquivos automaticamente para pastas específicas de acordo com o seu formato (extensão). O horário e os dias da semana de execução podem ser configurados diretamente durante a instalação, através de um assistente de instalação para Windows que irá criar uma tarefa agendada no task manager do SO para ser executada automaticamente.

## 📋 Sobre o projeto

Usuários que baixam arquivos da internet regularmente acabam acumulando-os na pasta raiz de "Downloads", precisando movê-los manualmente para as pastas correspondentes. O **Organizador de Arquivos** automatiza essa tarefa, identificando o tipo de cada arquivo pela extensão e movendo-o para a pasta de destino correta, sem necessidade de intervenção do usuário.

### Benefícios

- Aumento de produtividade, liberando o usuário para outras atividades
- Maior regularidade na organização dos arquivos baixados
- Redução do tempo gasto com a tarefa de minutos manuais para apenas alguns segundos

## ⚙️ Como funciona

1. O programa acessa a pasta padrão de Downloads do Windows
2. Verifica se existem arquivos na raiz da pasta
3. Identifica o tipo de cada arquivo pela extensão
4. Move o arquivo para a pasta de destino correspondente (Por exemplo: Arquivos .mp3 serão movidos para C:\Users\user_name\Music)
5. Repete o processo até que não restem arquivos na raiz da pasta
6. Registra todas as movimentações em um arquivo de log
7. Caso uma extensão não seja identificada uma pasta com nome "nao_categorizados" será criada na raiz da pasta Downloads do Windows e o arquivo irá para esta pasta.

## Diretórios utilizados pelo programa (assumindo ser uma unidade C:)
- C:\Users\user\Downloads - pasta onde será feita a varredura de arquivos
- C:\Users\claud\Downloads\nao_categorizados - pasta onde ficam arquivos sem extensão ou não identificados pelo script
- C:\Users\user\AppData\Roaming\OrganizadorArquivos\logs_organizador_arquivos - pasta dos logs gerados pela aplicação
- C:\Users\claud\Documents - arquivos típicos de documentos
- C:\Users\claud\Pictures - arquivos típicos de imagens
- C:\Users\claud\Music - arquivos típicos de áudio
- C:\Users\claud\Videos - arquivos típicos de vídeo
  
## 💻 Instalação
1. Baixe o executável para Windows
2. Siga o assistente de instalação e defina os dias e horários de execução
3. Conclua a instalação e pronto.
4. Um atalho pode ser criado na área de trabalho que permite a execução manual do script

## 📄 Documentação
Aqui é descrito qual era o cenário a ser automatizado e como foi elaborada a solução do problema através dos documentos criados.

### Descrição do processo atual
[Descrição do Processo Atual](docs/Descricao-do-Processo-Atual.docx)

### Modelagem(AS-IS) do processo atual
Processo manual realizado pelo usuário antes da automação:

![Modelagem AS-IS do processo Organizador de Arquivos](docs/modelagem-as-is.png)

### Modelagem(TO-BE) do processo
Processo executado pelo programa, sem intervenção do usuário:

![Modelagem TO-BE do processo Organizador de Arquivos](docs/modelagem-to-be.png)

### PDD - Process Definition Document
Documento de Definição do processo:

[PDD – Documento de Definição de Processo](docs/PDD-Organizador-de-Arquivos.pdf)
  
## Limitações da automação
1. Não é possível definir manualmente o caminho de destino para os arquivos.
2. Só é possível agendar os dias e horário de execução durante a instalação.
3. Não é possível definir manualmente pasta de origem dos arquivos.
4. O programa está em desenvolvimento e pode apresentar falhas durante a execução (verificar logs na pasta específica).
