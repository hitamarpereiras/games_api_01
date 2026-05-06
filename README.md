# API de Games (Django + DRF)

API REST para cadastro/consulta de jogos, categorias, requisitos e perfil de player, com autenticação JWT (SimpleJWT) e upload de imagens via Supabase Storage.

## Stack

- Django + Django REST Framework
- JWT: `djangorestframework-simplejwt`
- Filtros: `django-filter`
- Ordenação/pesquisa: DRF `OrderingFilter` / `SearchFilter`
- Upload/resize de imagens: `Pillow` + Supabase Storage
- Banco: PostgreSQL via `dj-database-url` (`DTB_URL`)

## Como rodar (dev)

1) Criar venv e instalar dependências:

```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

2) Configurar variáveis de ambiente (ver seção abaixo).

3) Migrar e subir o servidor:

```bash
python manage.py migrate
python manage.py runserver
```

Base URL (produção): `http://gamesapiv1.vps8317.panel.icontainer.cloud/`

Base URL (local): `http://127.0.0.1:8000/`

Prefixo da API: `/api/`

Admin Django: `/` (o projeto está com `admin.site.urls` mapeado na raiz).

## Variáveis de ambiente

Crie um arquivo `.env` (ou exporte no ambiente) com:

```env
# Banco (obrigatório)
DTB_URL=postgres://USER:PASSWORD@HOST:5432/DBNAME

# Supabase Storage (obrigatório para endpoints com upload de imagem)
SUPABASE_URL=...
SUPABASE_KEY=...
```

Observações:

- Sem `DTB_URL`, o projeto falha ao iniciar (o `dj_database_url.parse(...)` recebe `None`).
- O `core/settings.py` força SSL no banco (`ssl_require=True` / `sslmode=require`).
- `SUPABASE_URL`/`SUPABASE_KEY` são importados em `services/supabase_svc.py`; sem eles a aplicação falha ao iniciar com erro “Supabase não configurado”.

Buckets usados:

- `users_avatars` (avatar do player)
- `covers_games` (capa do jogo)

## Autenticação (JWT)

A API usa `Authorization: Bearer <access_token>`.

- Obter token (login): `POST /api/authentication/token/`
- Verificar token: `POST /api/authentication/token/verify/`

Exemplo (obter token) em PowerShell:

```powershell
curl.exe -X POST "http://gamesapiv1.vps8317.panel.icontainer.cloud/api/authentication/token/" `
  -H "Content-Type: application/json" `
  -d '{"username":"seu_usuario","password":"sua_senha"}'
```

Resposta (exemplo):

```json
{ "refresh": "...", "access": "..." }
```

Observação: o endpoint de *refresh* não está exposto nas `urls.py` (mesmo o SimpleJWT retornando o `refresh` no login).

## Paginação

Listagens usam paginação por número de página (DRF `PageNumberPagination`), com:

- `page` (padrão: 1)
- `page_size` (padrão: 8, máximo: 32)

Formato de resposta padrão do DRF:

```json
{
  "count": 123,
  "next": "http://.../?page=2",
  "previous": null,
  "results": []
}
```

## Filtros e ordenação

Filtros (querystring) via `django-filter`:

- Games: `GET /api/games/`
  - `name__icontains=...`
  - `category__name__icontains=...`
  - `score=...`, `score__gte=...`, `score__lte=...`
  - `release_date=YYYY-MM-DD`, `release_date__gte=...`, `release_date__lte=...`
- Reviews: `GET /api/reviews/?game=<id>`
- Requirements: `GET /api/requirements/?game=<id>`

Ordenação via `OrderingFilter`:

- `?ordering=created_at` (asc) / `?ordering=-created_at` (desc)

## Endpoints

### Authentication

- `POST /api/authentication/token/`
  - Body (JSON): `username`, `password`
  - 200: `{ "refresh": "...", "access": "..." }`
- `POST /api/authentication/token/verify/`
  - Body (JSON): `token`
  - 200: `{}` (token válido) / 401 (inválido/expirado)

### Players

- `POST /api/players/register/` (público)
  - Cria `User` + `Player` (transação atômica).
  - Body (`multipart/form-data` ou JSON):
    - `username` (string), `password` (string)
    - `processor` (string), `memory_ram` (int)
    - `disk` (string), `disk_space` (int)
    - `gpu_name` (string), `gpu_memory` (int)
    - `image` (arquivo, opcional) — máx 1MB, deve ser uma imagem válida
  - 201: `{"message":"Usuário criado com sucesso"}`

- `GET /api/players/` (auth)
  - Retorna apenas o(s) player(s) do usuário autenticado.
- `GET /api/players/{id}/` (auth)
- `PATCH /api/players/{id}/` (auth, `multipart/form-data` recomendado)
  - Campos do perfil e/ou `image` (upload).
  - Nota: no código atual, o `PATCH` assume que a imagem foi enviada (pode exigir ajuste no backend para atualizar sem `image`).
- `DELETE /api/players/{id}/` (auth)

Observação: o endpoint `POST /api/players/` existe por padrão do `ModelViewSet`, mas o fluxo recomendado para criação é `POST /api/players/register/`.

### Categories (auth)

- `GET /api/categories/`
- `POST /api/categories/`
  - Body (JSON): `name`, `description`
- `GET /api/categories/{id}/`
- `PATCH /api/categories/{id}/`
- `DELETE /api/categories/{id}/`

### Games

Leitura é pública; escrita exige autenticação.

- `GET /api/games/` (público)
- `GET /api/games/{id}/` (público)
- `POST /api/games/` (auth)
  - Body (`multipart/form-data` recomendado):
    - `name` (string)
    - `category_ids` (lista de ids — o model é ManyToMany)
    - `description` (string)
    - `release_date` (YYYY-MM-DD, opcional)
    - `score` (float)
    - `image_cover` (arquivo) — máx 1MB
  - 201: `{"message":"Criado com sucesso"}`
- `PATCH /api/games/{id}/` (auth)
  - Nota: no código atual, o `PATCH` com atualização sem `image_cover` pode exigir ajuste no backend.
- `DELETE /api/games/{id}/` (auth)

Observações:

- `cover_url` é preenchida via upload no Supabase.
- Para enviar múltiplas categorias em `multipart`, repita o campo `category_ids` (ex.: `-F "category_ids=1" -F "category_ids=2"`). Em JSON, envie como array (ex.: `"category_ids":[1,2]`).

### Reviews

Leitura é pública; escrita exige autenticação.

- `GET /api/reviews/` (público) — suporta filtro `?game=<id>`
- `GET /api/reviews/{id}/` (público)
- `POST /api/reviews/` (auth)
- `PATCH /api/reviews/{id}/` (auth)
- `DELETE /api/reviews/{id}/` (auth)

Observação: no código atual, `user` e `game` estão como `read_only` no serializer e o ViewSet não sobrescreve `perform_create`; criação/edição pode precisar de ajuste no backend para funcionar.

### Requirements

Leitura é pública; escrita exige autenticação.

- `GET /api/requirements/` (público) — suporta filtro `?game=<id>`
- `GET /api/requirements/{id}/` (público)
- `POST /api/requirements/` (auth)
- `PATCH /api/requirements/{id}/` (auth)
- `DELETE /api/requirements/{id}/` (auth)

Campos (JSON):

- `game` (id)
- `minimum_processor` (string), `minimum_ram` (int), `minimum_gpu` (string), `minimum_gpu_ram` (int)
- `maximum_processor` (string), `maximum_ram` (int), `maximum_gpu` (string), `maximum_gpu_ram` (int)

Observação: o model possui o campo `system`, mas ele não está exposto no serializer atual.

## Exemplos rápidos (curl)

### Criar categoria

```powershell
curl.exe -X POST "http://gamesapiv1.vps8317.panel.icontainer.cloud/api/categories/" `
  -H "Authorization: Bearer <ACCESS_TOKEN>" `
  -H "Content-Type: application/json" `
  -d '{"name":"RPG","description":"Role-playing"}'
```

### Criar jogo com capa (multipart) + múltiplas categorias

```powershell
curl.exe -X POST "http://gamesapiv1.vps8317.panel.icontainer.cloud/api/games/" `
  -H "Authorization: Bearer <ACCESS_TOKEN>" `
  -F "name=Elden Ring" `
  -F "category_ids=1" `
  -F "category_ids=2" `
  -F "description=..." `
  -F "release_date=2022-02-25" `
  -F "score=9.5" `
  -F "image_cover=@capa.jpg"
```
