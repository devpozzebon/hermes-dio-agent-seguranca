# Skill: Análise de Vulnerabilidade

## Quando usar
Use esta skill quando o usuário pedir para analisar um código, uma arquitetura ou um cenário em busca de falhas de segurança, ou quando ele fornecer um código e perguntar "está seguro?".

## Como analisar (Roteiro)
Sempre que for analisar, siga este roteiro didático e passo a passo:

1. **Entenda o Contexto:** Antes de apontar falhas, pergunte ao usuário qual é o objetivo do código/sistema e qual a stack tecnológica (linguagem, banco de dados).
2. **Identifique a Falha:** Aponte o trecho exato do código ou o comportamento do sistema que está vulnerável. Dê um nome técnico à falha (ex: "Isso é uma SQL Injection", "Isso é um XSS").
3. **Avalie o Impacto (Tríade CIA):** Explique o que um atacante poderia fazer se explorar isso. Qual pilar da segurança está em risco? (Ex: "Isso quebra a Confidencialidade, pois um atacante pode ler todas as senhas").
4. **Cite o MITRE ATT&CK:** Relacione a falha com uma técnica do MITRE ATT&CK, se aplicável (ex: T1190 - Exploit Public-Facing Application).
5. **Probabilidade e Severidade:** Classifique a vulnerabilidade (Baixa, Média, Alta, Crítica) e explique o porquê.
6. **Oriente a Correção (Sem dar o código pronto):** Explique o conceito da solução. Use boas práticas (ex: "Você precisa usar consultas parametrizadas para separar o comando SQL dos dados"). Não entregue o código corrigido, peça para o aluno tentar aplicar a solução.