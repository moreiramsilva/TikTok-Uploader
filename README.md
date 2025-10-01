TikTok Uploader 

Como usar (rápido):

1. Instale dependências: crie e ative um venv e rode `pip install -r requirements.txt`.
2. Copie `.env.example` para `.env` e preencha `TIKTOK_SESSION_ID` se desejar testar um upload real.
3. Coloque arquivos `.mp4` e seus `.txt` correspondentes na pasta `videos_para_upload/`.
4. Rode `python main.py`.

Observação: o upload aqui é simulado. Substitua `mock_upload` em `main.py` por sua implementação real.

Segurança e ação após vazamento de credenciais
-------------------------------------------------

Se você acidentalmente comitou um `sessionid` (ou outro segredo) neste repositório, siga estes passos imediatos:

1. Invalide/rotacione o `sessionid` na sua conta TikTok: faça logout de todas as sessões e altere a senha da conta.
2. Se você já comitou o segredo e precisa removê-lo do histórico remoto, este repositório foi reescrito e um backup foi mantido na branch `backup-before-purge`.
3. Se você colaborou ou clonou este repositório antes da reescrita, instrua seus colaboradores a rodarem:

```bash
# Para sobrescrever o histórico local e sincronizar com o remoto reescrito
git fetch origin
git checkout main
git reset --hard origin/main
```

4. Não compartilhe arquivos `.env` com valores reais. Use `.env.example` (sem valores) e mantenha o `.env` local e em `.gitignore`.

Se quiser, posso adicionar passos automatizados para reescrever o histórico com `git filter-repo`/BFG ou ajudar a invalidar sessões na conta.
