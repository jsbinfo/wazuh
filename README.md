Wazuh

Slack Email Documentation Documentation Coverity Twitter YouTube

Como funciona o Wazuh?

O Wazuh é uma solução de segurança cibernética baseada em agentes instalados nos sistemas monitorados, responsáveis por coletar dados críticos de segurança. Esses dados são enviados para um servidor central, que processa, analisa e gera alertas para possíveis ameaças.

A plataforma é totalmente integrada ao Elastic Stack (ELK), oferecendo um poderoso mecanismo de pesquisa e uma interface visual intuitiva. Isso permite que administradores de segurança analisem eventos, detectem padrões suspeitos e tomem decisões informadas de maneira eficiente.

Além disso, o Wazuh é uma plataforma open-source e gratuita, desenvolvida para prevenir, detectar e responder a ameaças em diferentes tipos de ambientes, incluindo infraestruturas locais, virtualizadas, conteinerizadas e em nuvem. Sua flexibilidade e escalabilidade fazem dele uma solução ideal para empresas de todos os portes.
Recursos da Wazuh

Uma breve apresentação de alguns dos casos de uso mais comuns da solução Wazuh.

**Detecção de intrusão

Os agentes da Wazuh examinam os sistemas monitorados em busca de malware, rootkits e anomalias suspeitas. Eles podem detectar arquivos ocultos, processos camuflados ou ouvintes de rede não registrados, bem como inconsistências nas respostas às chamadas do sistema.

Além dos recursos do agente, o componente do servidor usa uma abordagem baseada em assinatura para a detecção de intrusão, utilizando seu mecanismo de expressão regular para analisar os dados de registro coletados e procurar indicadores de comprometimento.

**Análise de dados de registro

Os agentes do Wazuh leem os registros do sistema operacional e dos aplicativos e os encaminham com segurança a um gerenciador central para análise e armazenamento baseados em regras. Quando nenhum agente é implantado, o servidor também pode receber dados via syslog de dispositivos de rede ou aplicativos.

As regras do Wazuh ajudam a alertá-lo sobre erros de aplicativos ou sistemas, configurações incorretas, tentativas e/ou atividades maliciosas bem-sucedidas, violações de políticas e vários outros problemas operacionais e de segurança.

**Monitoramento da integridade dos arquivos

O Wazuh monitora o sistema de arquivos, identificando alterações no conteúdo, nas permissões, na propriedade e nos atributos dos arquivos que você precisa monitorar. Além disso, ele identifica nativamente os usuários e os aplicativos usados para criar ou modificar arquivos.

Os recursos de monitoramento da integridade dos arquivos podem ser usados em conjunto com a inteligência contra ameaças para identificar ameaças ou hosts comprometidos. Além disso, vários padrões de conformidade regulamentar, como o PCI DSS, exigem isso.

**Detecção de vulnerabilidade

Os agentes Wazuh extraem dados de inventário de software e enviam essas informações para o servidor, onde são correlacionadas com bancos de dados CVE (Common Vulnerabilities and Exposure) atualizados continuamente, para identificar software vulnerável conhecido.

    Wazuh Chef

    Wazuh Puppet

    Wazuh Kubernetes

    Wazuh Bosh

    Wazuh Salt

Branches

    main branch contém o código mais recente, esteja ciente de possíveis bugs neste branch.
    A ramificação stable corresponde à última versão estável do Wazuh.

Software e bibliotecas usadas
Software 	Versão 	Autor 	Licença
bzip2 	1.0.8 	Julian Seward 	Licença BSD
cJSON 	1.7.12 	Dave Gamble 	Licença MIT
cPython 	3.10.13 	Guido van Rossum 	Licença Python Software Foundation versão 2
cURL 	8.11.1 	Daniel Stenberg 	Licença MIT
Flatbuffers 	23.5.26 	Google Inc. 	Licença Apache 2.0
GoogleTest 	1.11.0 	Google Inc. 	3-Cláusula "Nova" Licença BSD
jemalloc 	5.2.1 	Jason Evans 	2-Cláusula "Simplificada" Licença BSD
Lua 	5.3.6 	PUC-Rio 	Licença MIT
libarchive 	3.7.2 	Tim Kientzle 	Licença BSD "Nova" de 3 cláusulas
libdb 	18.1.40 	Oracle Corporation 	Affero GPL v3
libffi 	3.2.1 	Anthony Green 	Licença MIT
libpcre2 	10.42.0 	Philip Hazel 	Licença BSD
libplist 	2.2.0 	Aaron Burghardt et al. 	Licença Pública Geral Menor GNU versão 2.1
libYAML 	0.1.7 	Kirill Simonov 	Licença MIT
liblzma 	5.4.2 	Lasse Collin, Jia Tan et al. 	Licença Pública GNU versão 3
Espaço de usuário do Linux Audit 	2.8.4 	Rik Faith 	LGPL (copyleft)
msgpack 	3.1.1 	Sadayuki Furuhashi 	Licença Boost Software versão 1.0
nlohmann 	3.7.3 	Niels Lohmann 	Licença MIT
OpenSSL 	3.0.12 	OpenSSL Software Foundation 	Licença Apache 2.0
pacman 	5.2.2 	Judd Vinet 	Licença Pública GNU versão 2 (copyleft)
popt 	1.16 	Jeff Johnson e Erik Troan 	Licença MIT
procps 	2.8.3 	Brian Edmonds et al. 	LGPL (copyleft)
RocksDB 	8.3.2 	Facebook Inc. 	Licença Apache 2.0
rpm 	4.18.2 	Marc Ewing e Erik Troan 	Licença Pública GNU versão 2 (copyleft)
sqlite 	3.45.0 	D. Richard Hipp 	Domínio Público (sem restrições)
zlib 	1.3.1 	Jean-loup Gailly e Mark Adler 	Licença zlib/libpng

    Pacotes PyPi

Documentação

    Documentação completa
    Guia de instalação do Wazuh

Envolva-se

Faça parte da comunidade do Wazuh para aprender com outros usuários, participar de discussões, conversar com nossos desenvolvedores e contribuir com o projeto.

Se você quiser contribuir com nosso projeto, não hesite em fazer solicitações de pull, enviar problemas ou enviar commits, revisaremos todas as suas perguntas.

Você também pode participar do nosso canal da comunidade Slack e lista de discussão enviando um e-mail para wazuh+subscribe@googlegroups.com, para fazer perguntas e participar de discussões.

Fique por dentro das notícias, lançamentos, artigos de engenharia e muito mais.

    Site Wazuh
    Linkedin
    YouTube
    Twitter
    Blog Wazuh
    Canal de anúncios do Slack

Autores

Direitos autorais Wazuh (C) 2015-2023 Wazuh Inc. (Licença GPLv2)

Baseado no projeto OSSEC iniciado por Daniel Cid.
