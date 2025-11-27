# CapVideo Bot 🤖

Um bot do Telegram desenvolvido em Python que processa e responde a mensagens de vídeo, foto e texto em tempo real.

## 📋 Tabela de Conteúdos

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Uso](#uso)
- [Arquitetura](#arquitetura)
- [Deploy](#deploy)
- [Desenvolvimento](#desenvolvimento)
- [Contribuindo](#contribuindo)
- [Licença](#licença)
- [Suporte](#suporte)

## Sobre o Projeto

O **CapVideo Bot** é um bot do Telegram construído com a biblioteca `pyTelegramBotAPI` que monitora mensagens em um canal específico e responde automaticamente ao conteúdo enviado, processando vídeos, fotos e texto.

## Funcionalidades

- ✅ **Processamento de Vídeos**: Captura e responde com legendas de vídeos
- ✅ **Processamento de Fotos**: Monitora e responde a imagens enviadas
- ✅ **Processamento de Texto**: Responde a mensagens de texto
- ✅ **Monitoramento de Canal**: Funciona especificamente em um canal configurado
- ✅ **Logging Integrado**: Sistema de logs estruturado para debug e monitoramento
- ✅ **Containerização Docker**: Suporte nativo para deployment em containers

## Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Token do bot do Telegram (obtenha em [@BotFather](https://t.me/botfather))
- (Opcional) Docker e Docker Compose para containerização

## Instalação

### Método 1: Instalação Local

1. **Clone o repositório**
```bash
git clone https://github.com/luizchaos/capvideo-bot.git
cd capvideo-bot
```

2. **Crie um ambiente virtual** (recomendado)
```bash
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

### Método 2: Usando Docker

1. **Clone o repositório**
```bash
git clone https://github.com/luizchaos/capvideo-bot.git
cd capvideo-bot
```

2. **Construa a imagem Docker**
```bash
docker build -t capvideo-bot .
```

## Configuração

### 1. Configure o Token do Bot

Abra o arquivo `bot.py` e configure seu token do Telegram:

```python
BOT_TOKEN = "seu_token_aqui"
```

**⚠️ Importante**: Nunca faça commit do token no repositório. Use variáveis de ambiente em produção:

```python
import os
BOT_TOKEN = os.getenv("BOT_TOKEN")
```

### 2. Configure o ID do Canal

O bot está configurado para responder apenas em um canal específico. Edite o ID do canal em `bot.py`:

```python
if message.chat.id == -4799576555:  # Substitua pelo seu ID de canal
```

Para encontrar o ID do seu canal, envie uma mensagem nele e verifique os logs.

## Uso

### Execução Local

```bash
python bot.py
```

O bot iniciará com polling infinito e começará a monitorar mensagens.

### Execução com Docker

```bash
docker run -e BOT_TOKEN="seu_token_aqui" capvideo-bot
```

Ou com Docker Compose:

```bash
docker-compose up
```

### Exemplo de Uso

1. Adicione o bot ao seu canal
2. Envie um vídeo com legenda
3. O bot responderá com a legenda
4. Envie uma mensagem de texto
5. O bot responderá com o mesmo texto

## Arquitetura

### Estrutura do Projeto

```
capvideo-bot/
├── bot.py              # Código principal do bot
├── requirements.txt    # Dependências do projeto
├── Dockerfile          # Configuração para containerização
├── README.md          # Este arquivo
└── .gitignore         # Arquivos a ignorar no Git
```

### Fluxo de Execução

```
Iniciação
    ↓
Configuração de Logging
    ↓
Inicialização do Bot com Token
    ↓
Registro de Handler de Mensagens
    ↓
Polling Infinito (aguardando mensagens)
    ↓
Processamento de Conteúdo (vídeo, foto, texto)
    ↓
Resposta ao Usuário
```

### Dependências Principais

| Pacote | Versão | Descrição |
|--------|--------|-----------|
| pyTelegramBotAPI | 4.12.0 | SDK oficial para bots do Telegram |
| requests | 2.31.0 | Requisições HTTP |
| aiohttp | 3.8.4 | Cliente HTTP assíncrono |
| aiosignal | 1.3.1 | Sinais assíncronos |

## Deploy

### Deploy em Servidor Linux

1. **SSH no servidor**
```bash
ssh usuario@seu_servidor.com
```

2. **Clone o repositório**
```bash
git clone https://github.com/luizchaos/capvideo-bot.git
cd capvideo-bot
```

3. **Configure variáveis de ambiente**
```bash
export BOT_TOKEN="seu_token_aqui"
```

4. **Execute com nohup** (para rodar em background)
```bash
nohup python bot.py > bot.log 2>&1 &
```

### Deploy com Systemd (Recomendado)

Crie um arquivo `/etc/systemd/system/capvideo-bot.service`:

```ini
[Unit]
Description=CapVideo Bot
After=network.target

[Service]
Type=simple
User=seu_usuario
WorkingDirectory=/home/seu_usuario/capvideo-bot
Environment="BOT_TOKEN=seu_token_aqui"
ExecStart=/usr/bin/python3 /home/seu_usuario/capvideo-bot/bot.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Ative o serviço:
```bash
sudo systemctl enable capvideo-bot
sudo systemctl start capvideo-bot
```

### Deploy em Kubernetes

Crie um arquivo `deployment.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: capvideo-bot
spec:
  replicas: 1
  selector:
    matchLabels:
      app: capvideo-bot
  template:
    metadata:
      labels:
        app: capvideo-bot
    spec:
      containers:
      - name: bot
        image: capvideo-bot:latest
        env:
        - name: BOT_TOKEN
          valueFrom:
            secretKeyRef:
              name: bot-secret
              key: token
```

## Desenvolvimento

### Estrutura de Requisitos

Para desenvolvimento, instale dependências adicionais:

```bash
pip install -r requirements.txt
pip install pytest black flake8 pylint
```

### Executar Testes

```bash
pytest tests/
```

### Verificar Qualidade do Código

```bash
flake8 bot.py
pylint bot.py
black bot.py --check
```

### Formatar Código

```bash
black bot.py
```

### Debugging

Habilite logs detalhados modificando o nível de logging:

```python
logging.basicConfig(level=logging.DEBUG)
```

### Estrutura Recomendada para Expansão

Se precisar expandir o projeto:

```
capvideo-bot/
├── src/
│   ├── __init__.py
│   ├── bot.py              # Instância do bot
│   ├── handlers.py         # Handlers de mensagens
│   ├── processors.py       # Processadores de conteúdo
│   └── utils.py            # Funções utilitárias
├── tests/
│   ├── test_handlers.py
│   └── test_processors.py
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Troubleshooting

### O bot não responde

- ✓ Verifique se o token está correto
- ✓ Confirme que o bot foi adicionado ao canal
- ✓ Verifique se o ID do canal está correto
- ✓ Consulte os logs: `tail -f bot.log`

### Erro de conexão

```
ConnectionError: [Errno -2] Name or service not known
```

Verifique sua conexão com a internet e certifique-se de que o bot pode acessar a API do Telegram.

### Erro de autenticação

```
ApiException: UNAUTHORIZED - bot token is invalid
```

Confirme que o token está correto e não expirou.

### Uso excessivo de CPU

Reduza a frequência de polling:

```python
bot.infinity_polling(timeout=10, long_polling_timeout=5)
```

## Contribuindo

Contribuições são bem-vindas! Por favor:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

### Diretrizes

- Mantenha o código legível e bem comentado
- Adicione testes para novas funcionalidades
- Atualize a documentação conforme necessário
- Siga o [PEP 8](https://www.python.org/dev/peps/pep-0008/)

## Roadmap 🗺️

- [ ] Suporte a processamento de audio
- [ ] Sistema de fila de mensagens
- [ ] Dashboard de monitoramento
- [ ] Suporte a múltiplos canais
- [ ] Cache de respostas
- [ ] Integração com banco de dados
- [ ] Testes automatizados

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Autor

- **Luiz Chaos** - [GitHub](https://github.com/luizchaos)

## Suporte

Encontrou um problema? Abra uma [issue](https://github.com/luizchaos/capvideo-bot/issues) ou entre em contato.

### Recursos Úteis

- 📚 [Documentação pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
- 🔗 [API do Telegram](https://core.telegram.org/bots/api)
- 🐳 [Documentação Docker](https://docs.docker.com/)
- 🐍 [Documentação Python](https://docs.python.org/3/)

---

**Última atualização**: Novembro de 2025

