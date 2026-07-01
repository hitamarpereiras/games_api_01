# 🎮 API de Gerenciamento de Jogos

Uma API RESTful completa para gerenciamento de jogos, jogadores e requisitos de hardware, desenvolvida com **Django REST Framework**.

---
## Aplicação Web

Acesse a aplicação em:
https://space-games-six.vercel.app/

---

## 📋 Sumário

- [Visão Geral](#visão-geral)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação e Configuração](#instalação-e-configuração)
- [Autenticação](#autenticação)
- [Módulos da API](#módulos-da-api)
- [Endpoints Principais](#endpoints-principais)
- [Serviços Disponíveis](#serviços-disponíveis)
- [Configurações](#configurações)

---


## 👁️ Visão Geral

Este projeto é uma **API REST** que oferece funcionalidades completas para:

✅ **Autenticação** - Login e gerenciamento de usuários  
✅ **Gerenciamento de Jogos** - CRUD de jogos com categorias e requisitos  
✅ **Perfis de Jogadores** - Armazenar especificações de hardware do jogador  
✅ **Avaliações** - Sistema de reviews e pontuação de jogos  
✅ **Requisitos de Sistema** - Definir requisitos mínimos e recomendados  
✅ **Armazenamento em Nuvem** - Upload de imagens via Supabase  
✅ **Filtros e Busca** - Busca avançada de jogos

---

## 🛠️ Tecnologias Utilizadas

```
📦 Core
├── Django 6.0
├── Django REST Framework
├── djangorestframework-simplejwt (JWT Authentication)
└── django-cors-headers (CORS)

📦 Banco de Dados
├── PostgreSQL
└── dj-database-url

📦 Utilitários
├── Pillow (Processamento de Imagens)
├── python-dotenv (Variáveis de Ambiente)
├── django-filter (Filtros avançados)
└── Supabase (Armazenamento em Nuvem)
```

Veja [requirements.txt](requirements.txt) para a lista completa de dependências.

---

## 📁 Estrutura do Projeto

```
api_de_games/
│
├── 🔐 authentication/          # Módulo de autenticação
│   ├── views.py               # Endpoints de auth
│   ├── urls.py                # Rotas de autenticação
│   ├── admin.py               # Admin do Django
│   └── migrations/            # Migrações do banco
│
├── 👾 games/                  # Módulo principal de jogos
│   ├── models.py              # Modelo: Game
│   ├── serializers.py         # Serialização de dados
│   ├── views.py               # ViewSets para jogos
│   ├── urls.py                # Rotas de jogos
│   ├── pagination.py          # Paginação de resultados
│   └── migrations/            # Migrações do banco
│
├── 🎯 categories/             # Categorias de jogos
│   ├── models.py              # Modelo: Category
│   ├── serializers.py         # Serialização
│   ├── views.py               # ViewSets
│   └── urls.py                # Rotas
│
├── 👤 players/                # Perfis de jogadores
│   ├── models.py              # Modelo: Player (hardware specs)
│   ├── serializers.py         # Serialização
│   ├── views.py               # ViewSets
│   └── urls.py                # Rotas
│
├── ⭐ reviews/                # Avaliações de jogos
│   ├── models.py              # Modelo: Review
│   ├── serializers.py         # Serialização
│   ├── views.py               # ViewSets
│   └── urls.py                # Rotas
│
├── 📊 game_requirements/      # Requisitos de sistema
│   ├── models.py              # Modelo: GameRequirement
│   ├── serializers.py         # Serialização
│   ├── views.py               # ViewSets
│   └── urls.py                # Rotas
│
├── 🔧 services/               # Serviços utilitários
│   ├── pillow_svc.py         # Processamento de imagens
│   ├── supabase_svc.py       # Upload em nuvem
│   ├── users_svc.py          # Gerenciamento de usuários
│   └── validators.py         # Validações customizadas
│
├── ⚙️ core/                   # Configurações principais
│   ├── settings.py            # Configurações Django
│   ├── urls.py                # Rotas principais
│   ├── wsgi.py                # WSGI application
│   └── asgi.py                # ASGI application
│
├── 📄 manage.py               # CLI Django
├── 📦 requirements.txt         # Dependências Python
└── 📋 README.md               # Este arquivo

```

---

## 🚀 Instalação e Configuração

### 1️⃣ Pré-requisitos

- Python 3.8+
- PostgreSQL
- Git

### 2️⃣ Clonar o Repositório

```bash
git clone <repository-url>
cd api_de_games
```

### 3️⃣ Criar Ambiente Virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 4️⃣ Instalar Dependências

```bash
pip install -r requirements.txt
```

### 5️⃣ Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
# Banco de Dados
DATABASE_URL=postgresql://usuario:senha@localhost:5432/api_games

# Django
DEBUG=True
SECRET_KEY=sua-chave-secreta-aqui

# Supabase (para upload de imagens)
SUPABASE_URL=https://seu-projeto.supabase.co
SUPABASE_KEY=sua-chave-api-aqui
SUPABASE_BUCKET=seu-bucket-aqui

# JWT
JWT_SECRET=sua-chave-jwt-aqui
```

### 6️⃣ Migrar o Banco de Dados

```bash
python manage.py migrate
```

### 7️⃣ Criar Superusuário

```bash
python manage.py createsuperuser
```

### 8️⃣ Executar o Servidor

```bash
python manage.py runserver
```

O servidor estará disponível em: `http://127.0.0.1:8000/`

---

## 🔐 Autenticação

### Tipos de Autenticação

A API utiliza **JWT (JSON Web Token)** para autenticação segura.

### Fluxo de Autenticação

```
1. Usuário faz login com credenciais
   ↓
2. API retorna Access Token e Refresh Token
   ↓
3. Incluir Access Token no header: Authorization: Bearer <token>
   ↓
4. Quando expirar, usar Refresh Token para obter novo Access Token
```

### Headers Necessários

```http
Authorization: Bearer <seu-access-token>
Content-Type: application/json
```

### Endpoints de Autenticação

```
POST   /api/auth/login          # Fazer login
POST   /api/auth/register       # Criar nova conta
POST   /api/token/refresh       # Renovar token
POST   /api/token/blacklist     # Fazer logout
```

---

## 🎮 Módulos da API

### 1. 👾 **GAMES** - Gerenciamento de Jogos

#### Modelo: Game

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `name` | String | Nome único do jogo |
| `description` | Text | Descrição detalhada |
| `category` | ManyToMany | Categorias do jogo |
| `release_date` | Date | Data de lançamento |
| `cover_url` | URL | URL da capa do jogo |
| `cover_path` | String | Caminho local da imagem |
| `score` | Float | Pontuação (0.0 - 10.0) |
| `user` | FK | Usuário que adicionou |
| `created_at` | DateTime | Data de criação |

#### Endpoints Principais

```
GET    /api/games/                      # Listar todos os jogos
POST   /api/games/                      # Criar novo jogo
GET    /api/games/{id}/                 # Obter detalhes do jogo
PUT    /api/games/{id}/                 # Atualizar jogo
DELETE /api/games/{id}/                 # Deletar jogo
```

#### Filtros e Busca

```
GET /api/games/?search=mario            # Buscar por nome
GET /api/games/?category=Ação           # Filtrar por categoria
GET /api/games/?score__gte=8.0          # Jogos com score >= 8.0
GET /api/games/?ordering=-created_at    # Ordenar por data (descendente)
```

---

### 2. 🎯 **CATEGORIES** - Categorias

#### Modelo: Category

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `name` | String | Nome único da categoria |
| `description` | Text | Descrição da categoria |
| `created_at` | DateTime | Data de criação |
| `updated_at` | DateTime | Última atualização |

#### Endpoints

```
GET    /api/categories/                 # Listar todas as categorias
POST   /api/categories/                 # Criar categoria
GET    /api/categories/{id}/            # Obter detalhes
PUT    /api/categories/{id}/            # Atualizar
DELETE /api/categories/{id}/            # Deletar
```

---

### 3. 👤 **PLAYERS** - Perfis de Jogadores

#### Modelo: Player (Especificações de Hardware)

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `user` | OneToOne | Usuário associado |
| `processor` | String | CPU do jogador |
| `memory_ram` | Integer | RAM em GB |
| `disk` | String | Tipo: SSD/HDD |
| `disk_space` | Integer | Espaço disponível |
| `unit` | String | Unidade (GB/TB) |
| `gpu_name` | String | Placa de vídeo |
| `gpu_memory` | Integer | VRAM em GB |
| `avatar_url` | URL | URL do avatar |
| `avatar_path` | String | Caminho da imagem |

#### Endpoints

```
GET    /api/players/                    # Listar jogadores
POST   /api/players/                    # Criar perfil
GET    /api/players/{id}/               # Obter perfil
PUT    /api/players/{id}/               # Atualizar specs
DELETE /api/players/{id}/               # Deletar
```

---

### 4. ⭐ **REVIEWS** - Avaliações

#### Modelo: Review

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `game` | FK | Jogo avaliado |
| `username` | String | Nome do avaliador |
| `rating` | Integer | Nota (1-5) |
| `comment` | Text | Comentário |
| `created_at` | DateTime | Data de criação |

#### Endpoints

```
GET    /api/reviews/                    # Listar avaliações
POST   /api/reviews/                    # Criar review
GET    /api/reviews/{id}/               # Obter review
PUT    /api/reviews/{id}/               # Atualizar
DELETE /api/reviews/{id}/               # Deletar
```

---

### 5. 📊 **GAME_REQUIREMENTS** - Requisitos de Sistema

#### Modelo: GameRequirement

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `game` | FK | Jogo relacionado |
| `system` | String | Sistema operacional |
| `minimum_processor` | String | Processador mínimo |
| `minimum_ram` | Integer | Memória RAM mínima (GB) |
| `minimum_gpu` | String | GPU mínima |
| `minimum_gpu_ram` | Integer | Memória de GPU mínima (GB) |
| `maximum_processor` | String | Processador recomendado/máximo |
| `maximum_ram` | Integer | Memória RAM máxima/recomendada (GB) |
| `maximum_gpu` | String | GPU máxima/recomendada |
| `maximum_gpu_ram` | Integer | Memória de GPU máxima/recomendada (GB) |
| `storage` | Integer | Espaço de armazenamento necessário (GB) |
| `released_by` | String | Origem ou fornecedor do requisito |
| `created_at` | DateTime | Data de criação |
| `updated_at` | DateTime | Data de atualização |

#### Permissões

- `GET /api/requirements/` e `GET /api/requirements/{id}/` são públicos.
- `POST`, `PUT` e `DELETE` exigem autenticação.

#### Endpoints

```
GET    /api/requirements/                # Listar requisitos
POST   /api/requirements/                # Criar requisito
GET    /api/requirements/{id}/           # Obter requisito
PUT    /api/requirements/{id}/           # Atualizar requisito
DELETE /api/requirements/{id}/           # Deletar requisito
```

---

## 📡 Endpoints Principais

### Estrutura das Respostas

#### ✅ Sucesso (200 OK)

```json
{
  "id": 1,
  "name": "The Witcher 3",
  "description": "Um épico RPG...",
  "score": 9.5,
  "category": [1, 2],
  "release_date": "2015-05-19",
  "cover_url": "https://...",
  "created_at": "2024-01-15T10:30:00Z"
}
```

#### ❌ Erro (400/401/404)

```json
{
  "error": "Descrição do erro",
  "status": 400,
  "detail": "Detalhes adicionais"
}
```

### Exemplo de Requisição

```bash
# GET - Listar jogos com filtros
curl -X GET "http://localhost:8000/api/games/?search=mario&category=Ação" \
  -H "Authorization: Bearer seu_token"

# POST - Criar novo jogo
curl -X POST "http://localhost:8000/api/games/" \
  -H "Authorization: Bearer seu_token" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "The Witcher 3",
    "description": "Um épico RPG",
    "score": 9.5,
    "category": [1, 2]
  }'

# PUT - Atualizar jogo
curl -X PUT "http://localhost:8000/api/games/1/" \
  -H "Authorization: Bearer seu_token" \
  -H "Content-Type: application/json" \
  -d '{"score": 9.8}'

# DELETE - Deletar jogo
curl -X DELETE "http://localhost:8000/api/games/1/" \
  -H "Authorization: Bearer seu_token"
```

---

## 🔧 Serviços Disponíveis

### 1. 🖼️ **Pillow Service** (`services/pillow_svc.py`)

Processamento e otimização de imagens.

**Funcionalidades:**
- ✅ Redimensionamento automático
- ✅ Otimização de qualidade
- ✅ Suporte a múltiplos formatos (JPG, PNG, WebP)

**Uso:**
```python
from services.pillow_svc import process_image

processed = process_image(
    image_file,
    max_width=1024,
    max_height=1024,
    quality=85
)
```

---

### 2. ☁️ **Supabase Service** (`services/supabase_svc.py`)

Gerenciamento de armazenamento em nuvem.

**Funcionalidades:**
- ✅ Upload seguro de imagens
- ✅ Exclusão de arquivos
- ✅ Geração de URLs públicas

**Uso:**
```python
from services.supabase_svc import upload_image, delete_image

# Upload
url = upload_image(file, bucket='covers')

# Delete
delete_image(file_path, bucket='covers')
```

---

### 3. 👥 **Users Service** (`services/users_svc.py`)

Gerenciamento de usuários.

**Funcionalidades:**
- ✅ Criar usuário
- ✅ Atualizar perfil
- ✅ Validar permissões

---

### 4. ✔️ **Validators** (`services/validators.py`)

Validações customizadas.

**Funcionalidades:**
- ✅ Validação de imagens
- ✅ Validação de campos
- ✅ Validação de dados do jogo

**Uso:**
```python
from services.validators import validate_image

validate_image(file)  # Lança exceção se inválido
```

---

## ⚙️ Configurações

### 1. CORS

```python
# core/settings.py
CORS_ALLOW_ALL_ORIGINS = True  # Desenvolvimento

# Produção (restritivo):
CORS_ALLOWED_ORIGINS = [
    "https://seu-frontend.com",
    "https://www.seu-frontend.com",
]
```

### 2. Hosts Permitidos

```python
ALLOWED_HOSTS = [
    "gamesearch-nine.vercel.app",
    "spacegames.vps8317.panel.icontainer.cloud",
    "127.0.0.1",
    "216.22.27.187",
]
```

### 3. Aplicações Instaladas

```python
INSTALLED_APPS = [
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'django_filters',
    
    'authentication',
    'players',
    'categories',
    'games',
    'reviews',
    'game_requirements',
]
```

### 4. Filtros REST Framework

```python
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
    'DEFAULT_PAGINATION_CLASS': 'games.pagination.GamePagination',
    'PAGE_SIZE': 20,
}
```

---

## 🌐 URLs Principais

| Caminho | Descrição |
|---------|-----------|
| `/` | Home da API |
| `/admin/` | Painel administrativo |
| `/api/auth/` | Endpoints de autenticação |
| `/api/games/` | Endpoints de jogos |
| `/api/categories/` | Endpoints de categorias |
| `/api/players/` | Endpoints de jogadores |
| `/api/reviews/` | Endpoints de reviews |
| `/api/requirements/` | Endpoints de requisitos |

---

## 📊 Modelo de Dados (ER Diagram)

```
User (Django Auth)
├── Player (1-1)
│   ├── processor
│   ├── memory_ram
│   ├── gpu_name
│   └── avatar_url
│
└── Game (1-N)
    ├── name
    ├── description
    ├── score
    ├── category (M-N) ──→ Category
    ├── reviews (1-N) ──→ Review
    └── requirements (1-1) ──→ GameRequirement

Category
├── name
├── description
└── games (M-N) ──→ Game

Review
├── game (FK)
├── username
├── rating
└── comment

GameRequirement
├── game (1-1)
├── minimum_*
└── recommended_*
```

---

## 🚨 Tratamento de Erros

### Códigos de Status HTTP

| Status | Significado |
|--------|------------|
| `200` | OK - Requisição bem-sucedida |
| `201` | Created - Recurso criado |
| `400` | Bad Request - Dados inválidos |
| `401` | Unauthorized - Token inválido/expirado |
| `403` | Forbidden - Sem permissão |
| `404` | Not Found - Recurso não existe |
| `500` | Server Error - Erro interno |

### Exemplo de Erro

```json
{
  "detail": "Token inválido ou expirado",
  "code": "token_not_valid"
}
```

---

## 📦 Dependências Principais

```txt
Django==6.0
djangorestframework==3.14.0
djangorestframework-simplejwt==5.3.2
django-cors-headers==4.3.0
django-filter==23.4
Pillow==10.0.0
python-dotenv==1.0.0
dj-database-url==2.1.0
psycopg2-binary==2.9.9
```

---

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

---

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

---

## 👨‍💻 Suporte

Para dúvidas ou sugestões, abra uma issue no repositório.

**Desenvolvido com ❤️**
