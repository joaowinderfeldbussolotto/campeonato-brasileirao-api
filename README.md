# API Campeonato Brasileiro

## Descrição
Este projeto consiste em uma API que fornece informações sobre o Campeonato Brasileiro de Futebol. Os usuários podem consultar a tabela de classificação atualizada, bem como os jogos por rodada. Além disso, há a opção de se cadastrar para receber notificações por e-mail sempre que ocorrer um gol durante as partidas.

## Funcionalidades
- Consulta da tabela de classificação do Campeonato Brasileiro.
- Visualização dos jogos por rodada, incluindo datas, times e resultados.
- Cadastro para receber notificações por e-mail quando um gol acontecer.

## Uso
1. Faça requisições à [API](http://150.136.154.12) para obter dados sobre a classificação e os jogos.
2. Utilize a rota de cadastro para receber notificações por e-mail.

## Documentação
A documentação está disponível aqui: [Documentação](http://150.136.154.12/redoc) 


## Rotas
- `/api/v1/tabela`: Retorna a tabela de classificação.
- `/api/v1/rodada/:rodada`: Fornece informações sobre os jogos de uma rodada específica.
- `/api/v1/inscricao`: Permite o cadastro para receber notificações de gol por e-mail.
- `/api/v1/ao-vivo`: Consultar os jogos acontecendo agora!

## Tecnologias Utilizadas
- Python
- FastAPI
- MongoDB

## Fontes de Dados
Os dados são obtidos de fontes confiáveis, incluindo os sites do Terra, CBF e BBC.

## Deploy
O projeto está implantado no Oracle Cloud.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.
