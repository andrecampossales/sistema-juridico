# Modelo de dados: Processo
| Campo | Tipo | Obrigatório | Regras |
|---|---|---|---|
| id | uuid | sim | gerado pelo sistema |
| numero_cnj | texto | sim | formato NNNNNNN-DD.AAAA.J.TR.OOOO, dígito verificador válido, único |
| valor_causa | decimal | sim | maior ou igual a zero |
| data_distribuicao | data | sim |  |
| escritorio_representa | enum(REQUERENTE, REQUERIDO) | sim |  |
| status | enum(ATIVO, ARQUIVADO, EXTINTO, SUSPENSO) | sim |  |
| segredo_justica | booleano | sim |  |
| criado_em | data_hora | sim | gerado pelo sistema |
| atualizado_em | data_hora | sim | gerado pelo sistema |
| assunto | texto | nao |  |
| juiz | texto | nao |  |
| referencia_interna | texto | nao |  |
| area | enum(CIVEL, CRIMINAL, TRABALHISTA, TRIBUTARIO, PREVIDENCIARIO, FAMILIA, CONSUMIDOR, BANCARIO) | nao |  |
| vara | texto | nao |  |
| foro | texto | nao |  |
| classe | texto | nao |  |

## Entidades futuras
### Parte
Pessoa física ou jurídica que integra o processo. Um processo pode ter várias partes.
- nome
- cpf_cnpj
- polo (ATIVO, PASSIVO, TERCEIRO)

### Movimentação
São as movimentações do processo que pode conter data, horário e o texto explicativo de cada ato processual.

### Arquivos
Responsável por armazenar arquivos importantes. Por exemplo, contrato social, procuração, substabelecimento, e peças processuais, como sentença, petição inicial etc.

### Processo relacionado
São relacionados com o principal, por exemplo, cumprimento de sentença etc.

### Vara
Corresponde ao número do juízo onde o processo está tramitando, por exemplo "6ª Vara da Família e Sucessões"

### Foro
Corresponde à competência territorial do processo, por exemplo "Foro Central Cível".