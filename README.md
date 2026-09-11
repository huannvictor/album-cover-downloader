# Album Cover Downloader

Aplicação Python para buscar a capa de um álbum na API pública do iTunes e
baixá-la em alta resolução.

## O que a aplicação faz

1. Solicita o nome do álbum.
2. Solicita o nome do artista ou da banda.
3. Consulta o iTunes usando os dois valores.
4. Procura um resultado cujo artista e álbum correspondam exatamente aos
	 valores informados, ignorando maiúsculas, minúsculas e espaços nas pontas.
5. Baixa a capa em resolução `1000x1000`.
6. Salva a imagem na pasta atual com o nome do álbum, substituindo espaços por
	 sublinhados, por exemplo `The_Dark_Side_of_the_Moon.jpg`.
7. Tenta abrir o arquivo automaticamente no Windows.

## Requisitos

- Python `3.14` ou superior;
- [uv](https://docs.astral.sh/uv/);
- acesso à internet;
- Windows para a abertura automática da imagem após o download.

A aplicação usa somente a biblioteca padrão do Python e não possui
dependências externas de runtime.

## Instalação

Clone o repositório e entre na pasta do projeto:

```bash
git clone <URL_DO_REPOSITORIO>
cd album-cover-downloader
```

Sincronize o ambiente virtual:

```bash
uv sync
```

O arquivo `.python-version` informa a versão `3.14`. O `uv` pode criar e
atualizar automaticamente o ambiente `.venv` durante a sincronização.

## Uso

Execute o arquivo principal a partir da raiz do projeto:

```bash
uv run python src/main.py
```

Ou, no Windows, use diretamente o Python do ambiente virtual:

```powershell
.\.venv\Scripts\python.exe src\main.py
```

Preencha os prompts exibidos no terminal:

```text
Insira o nome do album: The Dark Side of the Moon
De qual artista/banda: Pink Floyd
```

Quando houver uma correspondência, a capa será salva na pasta em que o
comando foi executado. Para evitar substituir outro arquivo, mova ou renomeie
a imagem depois do download.

## Resultado da busca

Se o iTunes não encontrar uma capa cujo artista e álbum coincidam exatamente,
o programa exibe:

```text
Nenhua capa encontrada correspondente.
```

Confira a grafia do álbum e do artista. O programa não escolhe resultados
aproximados e não solicita confirmação antes de salvar o arquivo.

## Limitações conhecidas

- O resultado precisa corresponder exatamente ao álbum e ao artista
	informados.
- A busca usa a API do iTunes e depende de conexão com a internet.
- O arquivo é salvo na pasta atual, não em um diretório configurável.
- O nome do arquivo é derivado do nome informado para o álbum; caracteres
	especiais e separadores de caminho não são tratados pelo programa.
- Um arquivo com o mesmo nome pode ser substituído.
- A abertura automática usa `os.startfile`, que é específica do Windows.
- Erros de rede, respostas inválidas e outras exceções são apenas exibidos no
	terminal.

## Estrutura do projeto

```text
album-cover-downloader/
├── src/
│   └── main.py          # entrada da aplicação e lógica de download
├── pyproject.toml       # metadados do projeto e configuração do uv
├── uv.lock              # estado resolvido pelo uv
├── .python-version      # versão esperada do Python
└── README.md            # documentação
```

## Solução de problemas

### `uv` não foi encontrado

Instale o `uv` seguindo a [documentação oficial](https://docs.astral.sh/uv/)
e abra um novo terminal. Verifique a instalação com:

```bash
uv --version
```

### O download não acontece

Confirme a conexão com a internet e revise a grafia do álbum e do artista.
O programa só baixa a capa quando encontra uma correspondência exata na
resposta do iTunes.

### A imagem não abre automaticamente

Verifique se o arquivo `.jpg` foi criado na pasta atual e abra-o manualmente.
Esse comportamento automático depende do Windows.

## Desenvolvimento

O código da aplicação está em `src/main.py`. Depois de fazer alterações,
execute novamente o comando da seção **Uso**. Ao adicionar funcionalidades,
considere incluir testes e tratamento específico para falhas de rede e buscas
sem resultados.

## Observação sobre o comando instalado

O `pyproject.toml` declara o comando `album-cover-downloader`, mas a entrada
configurada aponta para `album_cover_downloader:main`, enquanto o código atual
está em `src/main.py`. Por isso, use a execução direta documentada acima até
que essa configuração seja alinhada ao layout do projeto.

## Licença

Este projeto ainda não declara uma licença.
