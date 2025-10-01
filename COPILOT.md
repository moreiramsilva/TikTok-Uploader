\# 🤖 TikTok Uploader



\## 📖 Sobre o Projeto



O \*\*TikTok Uploader\*\* é uma aplicação de linha de comando (CLI) em Python, projetada para automatizar o processo de upload de vídeos para o TikTok. A ferramenta monitora uma pasta local, coleta os vídeos e suas respectivas descrições e os publica na sua conta do TikTok de forma automática.



Este projeto nasceu da necessidade de agilizar a postagem de conteúdo em massa, permitindo que criadores de conteúdo e agências de marketing foquem na criação, e não no processo manual de upload.



\## ✨ Funcionalidades Principais



\-   \*\*Upload Automático:\*\* Envia vídeos para o TikTok sem a necessidade de interação manual.

\-   \*\*Configuração Flexível:\*\* Utilize um arquivo `.env` para gerenciar suas credenciais e configurações de forma segura.

\-   \*\*Metadados Dinâmicos:\*\* Associe um arquivo de texto (`.txt`) a cada vídeo (`.mp4`) para definir a legenda e as hashtags de forma individual.

\-   \*\*Estrutura Simples:\*\* Projeto modular e de fácil entendimento, pronto para ser estendido com novas funcionalidades.

\-   \*\*Validação:\*\* O script verifica se o vídeo já foi publicado para evitar duplicatas.



\## 🚀 Começando



Siga estas instruções para obter uma cópia do projeto em funcionamento na sua máquina local para desenvolvimento e teste.



\### 📋 Pré-requisitos



\-   \[Python 3.9+](https://www.python.org/downloads/)

\-   \[Git](https://git-scm.com/)

\-   Um editor de código de sua preferência (VS Code, PyCharm, etc.)



\### ⚙️ Instalação e Configuração



1\.  \*\*Clone o repositório:\*\*

&nbsp;   ```bash

&nbsp;   git clone \[https://github.com/seu-usuario/tiktok-uploader.git](https://github.com/seu-usuario/tiktok-uploader.git)

&nbsp;   cd tiktok-uploader

&nbsp;   ```



2\.  \*\*Crie e ative um ambiente virtual (Recomendado):\*\*

&nbsp;   ```bash

&nbsp;   # Para Windows

&nbsp;   python -m venv venv

&nbsp;   .\\venv\\Scripts\\activate



&nbsp;   # Para macOS/Linux

&nbsp;   python3 -m venv venv

&nbsp;   source venv/bin/activate

&nbsp;   ```



3\.  \*\*Instale as dependências:\*\*

&nbsp;   ```bash

&nbsp;   pip install -r requirements.txt

&nbsp;   ```



4\.  \*\*Configure suas credenciais:\*\*

&nbsp;   -   Renomeie o arquivo `.env.example` para `.env`.

&nbsp;   -   Abra o arquivo `.env` e preencha a variável `TIKTOK\_SESSION\_ID`.



&nbsp;   ```ini

&nbsp;   # .env

&nbsp;   # Cole aqui o valor do cookie 'sessionid' da sua conta do TikTok

&nbsp;   TIKTOK\_SESSION\_ID="seu\_session\_id\_aqui"

&nbsp;   ```



&nbsp;   > \*\*Como obter o `sessionid`?\*\*

&nbsp;   > 1.  Acesse `https://www.tiktok.com/` no seu navegador e faça login na sua conta.

&nbsp;   > 2.  Abra as Ferramentas de Desenvolvedor (geralmente com a tecla `F12`).

&nbsp;   > 3.  Vá para a aba "Application" (ou "Aplicação").

&nbsp;   > 4.  No menu à esquerda, navegue até `Storage > Cookies > https://www.tiktok.com`.

&nbsp;   > 5.  Encontre o cookie chamado `sessionid` e copie o seu valor.



\## 📁 Estrutura do Projeto



```

tiktok-uploader/

│

├── .env                  # Arquivo de configuração com suas credenciais (não versionar!)

├── .env.example          # Exemplo de arquivo de configuração

├── .gitignore            # Arquivos e pastas a serem ignorados pelo Git

├── COPILOT.md             # Esta documentação

├── main.py               # Ponto de entrada da aplicação

├── requirements.txt      # Lista de dependências Python

│

├── videos\_para\_upload/   # Pasta onde você deve colocar os vídeos e legendas

│   ├── exemplo\_video\_1.mp4

│   └── exemplo\_video\_1.txt

│

└── videos\_publicados/    # Os vídeos são movidos para cá após o upload bem-sucedido

```



\## ▶️ Como Usar



1\.  \*\*Prepare seus vídeos:\*\*

&nbsp;   -   Coloque os arquivos de vídeo (formato `.mp4`) dentro da pasta `videos\_para\_upload/`.

&nbsp;   -   Para cada vídeo, crie um arquivo de texto (`.txt`) com o \*\*mesmo nome\*\*. Por exemplo, para `meu\_video.mp4`, crie `meu\_video.txt`.

&nbsp;   -   O conteúdo do arquivo `.txt` será usado como a legenda (descrição) do seu vídeo no TikTok.



2\.  \*\*Execute a aplicação:\*\*

&nbsp;   Abra seu terminal, certifique-se de que o ambiente virtual está ativado e execute o script principal.



&nbsp;   ```bash

&nbsp;   python main.py

&nbsp;   ```



O script irá varrer a pasta `videos\_para\_upload/`, encontrar os pares de vídeo e texto, realizar o upload de cada um e, em caso de sucesso, mover os arquivos para a pasta `videos\_publicados/` para evitar reenvios.



\## 🛠️ Como Funciona (Lógica Principal)



A lógica do `main.py` segue estes passos:



1\.  \*\*Carregar Configurações\*\*: Lê o `TIKTOK\_SESSION\_ID` do arquivo `.env`.

2\.  \*\*Inicializar API\*\*: Usa uma biblioteca como a `tiktok-uploader` para se autenticar com o `sessionid`.

3\.  \*\*Escanear Pasta\*\*: Procura por arquivos `.mp4` na pasta `videos\_para\_upload/`.

4\.  \*\*Processar Vídeos\*\*: Para cada vídeo encontrado:

&nbsp;   -   Verifica se existe um arquivo `.txt` correspondente.

&nbsp;   -   Lê o conteúdo do `.txt` para obter a legenda.

&nbsp;   -   Chama a função de upload da biblioteca, passando o caminho do vídeo e a legenda.

&nbsp;   -   Se o upload for bem-sucedido, move o `.mp4` e o `.txt` para a pasta `videos\_publicados/`.

&nbsp;   -   Registra o status (sucesso ou falha) em um log no console.

5\.  \*\*Finalizar\*\*: Exibe um resumo da operação.



\## 📝 TODO - Melhorias Futuras



\-   \[ ] Adicionar suporte a agendamento de uploads (`cron` ou `schedule`).

\-   \[ ] Implementar um sistema de log mais robusto (salvando em arquivo).

\-   \[ ] Adicionar suporte a proxies para evitar bloqueios.

\-   \[ ] Criar uma interface gráfica simples (usando `Tkinter` ou `PyQt`).

\-   \[ ] Suporte para obter vídeos de outras fontes (URLs, Google Drive, etc.).



\## 🤝 Contribuições



Contribuições são bem-vindas! Se você tem ideias para melhorar o projeto, sinta-se à vontade para abrir uma \*issue\* ou enviar um \*pull request\*.



\## ⚖️ Licença



Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.



---



\*\*Aviso Legal:\*\* Este projeto é uma ferramenta não oficial e não é afiliado ao TikTok. Use por sua conta e risco. A automação de contas pode violar os Termos de Serviço da plataforma.

