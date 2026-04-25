-- ==================================================
-- SISTEMA DE GERENCIAMENTO DE TREINAMENTOS
-- ==================================================

-- Tabela: Endereço dos Restaurantes
CREATE TABLE Endereco_Restaurante (
    ID_Endereco INT PRIMARY KEY AUTO_INCREMENT,
    Cep CHAR(9) NOT NULL,
    Estado CHAR(2) NOT NULL,
    Cidade VARCHAR(100) NOT NULL,
    Bairro VARCHAR(100) NOT NULL,
    Rua VARCHAR(200) NOT NULL,
    Numero_Local VARCHAR(10) NOT NULL,
    Complemento_Local VARCHAR(100)
);

-- Tabela: Restaurante
CREATE TABLE Restaurante (
    ID_Restaurante INT PRIMARY KEY AUTO_INCREMENT,
    Nome_Restaurante VARCHAR(100) NOT NULL,
    ID_Endereco INT NOT NULL UNIQUE,
    Atividade BOOLEAN NOT NULL DEFAULT TRUE,
    FOREIGN KEY (ID_Endereco) REFERENCES Endereco_Restaurante(ID_Endereco)
);

-- Tabela: Departamento
CREATE TABLE Departamento (
    ID_Departamento INT PRIMARY KEY AUTO_INCREMENT,
    Nome_Departamento VARCHAR(100) NOT NULL,
    UNIQUE (Nome_Departamento)
);

-- Tabela: Cargo
CREATE TABLE Cargo (
    ID_Cargo INT PRIMARY KEY AUTO_INCREMENT,
    Nome_Cargo VARCHAR(100) NOT NULL,
    ID_Departamento INT NOT NULL, -- Coluna para a chave estrangeira
    FOREIGN KEY (ID_Departamento) REFERENCES Departamento(ID_Departamento),
    INDEX idx_cargo_departamento (ID_Departamento) -- Índice na chave estrangeira
);

-- Tabela: Colaborador/Usuário
CREATE TABLE Colaborador_Usuario (
    ID_Colaborador INT PRIMARY KEY AUTO_INCREMENT,
    Nome_Colaborador VARCHAR(200) NOT NULL,
    Data_Nascimento DATE NOT NULL,
    Email VARCHAR(200) NOT NULL,
    Telefone CHAR(15),  -- Mudado de VARCHAR(20) para CHAR(15) - formato padronizado: +55 11 91234-5678
    Atividade BOOLEAN NOT NULL DEFAULT TRUE,
    Consentimento_LGPD BOOLEAN NOT NULL DEFAULT FALSE,
    Data_Aceite_LGPD DATETIME NULL, -- Pode ser nulo se o consentimento for falso
    ID_Restaurante INT NOT NULL,
    ID_Cargo INT NOT NULL,
    UNIQUE (Email),
    FOREIGN KEY (ID_Restaurante) REFERENCES Restaurante(ID_Restaurante),
    FOREIGN KEY (ID_Cargo) REFERENCES Cargo(ID_Cargo),
    INDEX idx_colaborador_restaurante (ID_Restaurante), -- Índice
    INDEX idx_colaborador_cargo (ID_Cargo) -- Índice
);

-- Tabela: Autenticação do Colaborador
CREATE TABLE Colaborador_Autenticacao (
    ID_Colaborador INT PRIMARY KEY,
    Senha_Hash VARCHAR(255) NOT NULL,  -- Tamanho adequado para bcrypt/argon2
    Data_Ultima_Atualizacao DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    Tentativas_Falhas INT NOT NULL DEFAULT 0,
    Conta_Bloqueada BOOLEAN NOT NULL DEFAULT FALSE,  -- Bloquear após tentativas excessivas
    Data_Bloqueio DATETIME,
    FOREIGN KEY (ID_Colaborador) REFERENCES Colaborador_Usuario(ID_Colaborador),
    CHECK (LENGTH(Senha_Hash) >= 60)  -- Bcrypt gera hashes de 60 caracteres
);

-- Tabela: Perfil de Acesso
CREATE TABLE Perfil (
    ID_Perfil INT PRIMARY KEY AUTO_INCREMENT,
    Nome_Perfil VARCHAR(50) NOT NULL,
    Descricao_perfil VARCHAR(200) NOT NULL
);

-- Tabela: Permissões do Sistema
CREATE TABLE Permissao (
    ID_Permissao INT PRIMARY KEY AUTO_INCREMENT,
    Nome_Permissao VARCHAR(100) NOT NULL,
    Descricao_Permissao VARCHAR(200) NOT NULL
);

-- Tabela: Relacionamento Perfil-Permissões
CREATE TABLE Perfil_Permissoes (
    ID_Perfil INT NOT NULL,
    ID_Permissao INT NOT NULL,
    PRIMARY KEY (ID_Perfil, ID_Permissao),
    FOREIGN KEY (ID_Perfil) REFERENCES Perfil(ID_Perfil) ON DELETE CASCADE, -- Se um perfil for deletado, suas permissões associadas também são.
    FOREIGN KEY (ID_Permissao) REFERENCES Permissao(ID_Permissao) ON DELETE CASCADE,
    INDEX idx_perfilperm_permissao (ID_Permissao) -- Índice
);

-- Tabela: Relacionamento Colaborador-Perfil
CREATE TABLE Colaborador_Perfil (
    ID_Perfil INT NOT NULL,
    ID_Colaborador INT NOT NULL,
    PRIMARY KEY (ID_Perfil, ID_Colaborador),
    FOREIGN KEY (ID_Perfil) REFERENCES Perfil(ID_Perfil) ON DELETE CASCADE,
    FOREIGN KEY (ID_Colaborador) REFERENCES Colaborador_Usuario(ID_Colaborador) ON DELETE CASCADE,
    INDEX idx_colabperfil_colaborador (ID_Colaborador) -- Índice
);

-- Tabela: Conteúdo Teórico
CREATE TABLE Conteudo_Teorico (
    ID_Conteudo INT PRIMARY KEY AUTO_INCREMENT,
    Conteudo TEXT NOT NULL,
    Data_criacao DATE NOT NULL DEFAULT (CURRENT_DATE)
);

-- Tabela: Trilha de Treinamento
CREATE TABLE Trilha_Treinamento (
    ID_Trilha INT PRIMARY KEY AUTO_INCREMENT,
    Nome_Trilha VARCHAR(100) NOT NULL,
    ID_Conteudo INT NOT NULL,
    FOREIGN KEY (ID_Conteudo) REFERENCES Conteudo_Teorico(ID_Conteudo)
);

-- Tabela: Categoria de Treinamento
CREATE TABLE Categoria_Treinamento (
    ID_Categoria INT PRIMARY KEY AUTO_INCREMENT,
    Nome_Categoria VARCHAR(100) NOT NULL,
    Obrigatoriedade BOOLEAN NOT NULL DEFAULT FALSE,
    UNIQUE (Nome_Categoria)
);

-- Tabela: Treinamento
CREATE TABLE Treinamento (
    ID_Treinamento INT PRIMARY KEY AUTO_INCREMENT,
    Nome_Treinamento VARCHAR(150) NOT NULL,
    Descricao VARCHAR(500),
    ID_Trilha INT NOT NULL,
    ID_Categoria INT NOT NULL,
    FOREIGN KEY (ID_Trilha) REFERENCES Trilha_Treinamento(ID_Trilha),
    FOREIGN KEY (ID_Categoria) REFERENCES Categoria_Treinamento(ID_Categoria),
    INDEX idx_treinamento_trilha (ID_Trilha),
    INDEX idx_treinamento_categoria (ID_Categoria)
);

-- Tabela: Tipo de Local
CREATE TABLE Local_Tipo (
    ID_Local INT PRIMARY KEY AUTO_INCREMENT,
    Nome_Local VARCHAR(100) NOT NULL,
    Descricao VARCHAR(200),
    UNIQUE (Nome_Local)
);

-- Tabela: Sessão em Equipe
CREATE TABLE Sessao_Equipe (
    ID_Sessao INT PRIMARY KEY AUTO_INCREMENT,
    ID_Treinamento INT NOT NULL,
    Data_treinamento DATE NOT NULL,
    Hora_treinamento TIME NOT NULL,
    ID_Criador INT NOT NULL,
    Data_Criacao DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    ID_Local INT,
    FOREIGN KEY (ID_Treinamento) REFERENCES Treinamento(ID_Treinamento),
    FOREIGN KEY (ID_Criador) REFERENCES Colaborador_Usuario(ID_Colaborador),
    FOREIGN KEY (ID_Local) REFERENCES Local_Tipo(ID_Local),
    INDEX idx_sessao_treinamento (ID_Treinamento),
    INDEX idx_sessao_local (ID_Local)
);

-- Tabela: Tipo de Resultado
CREATE TABLE Resultado_Tipo (
    ID_Resultado INT PRIMARY KEY AUTO_INCREMENT,
    Nome_Resultado VARCHAR(50) NOT NULL,
    Aprovacao BOOLEAN NOT NULL,
    UNIQUE (Nome_Resultado)
);

-- Tabela: Desempenho na Sessão
CREATE TABLE Desempenho_Sessao (
    ID_Desempenho INT PRIMARY KEY AUTO_INCREMENT,
    Progresso DECIMAL(5,2) NOT NULL,  -- Mudado de FLOAT para DECIMAL(5,2) para maior precisão
    Feedback_Treinador VARCHAR(500),
    Feedback_Colaborador VARCHAR(500),
    ID_Sessao_Equipe INT NOT NULL,
    ID_Colaborador INT NOT NULL,
    Nota_Avaliacao DECIMAL(4,2),  -- Mudado de FLOAT para DECIMAL(4,2) para maior precisão
    ID_Resultado INT NOT NULL,
    CHECK (Progresso BETWEEN 0 AND 100),
    FOREIGN KEY (ID_Sessao_Equipe) REFERENCES Sessao_Equipe(ID_Sessao),
    FOREIGN KEY (ID_Colaborador) REFERENCES Colaborador_Usuario(ID_Colaborador),
    FOREIGN KEY (ID_Resultado) REFERENCES Resultado_Tipo(ID_Resultado),
    INDEX idx_desempenho_sessao (ID_Sessao_Equipe),
    INDEX idx_desempenho_colaborador (ID_Colaborador)
);

-- Tabela: Relacionamento Colaborador-Treinamento
CREATE TABLE Colaborador_Treinamento (
    ID_Colaborador_Usuario INT NOT NULL,
    ID_Treinamento INT NOT NULL,
    PRIMARY KEY (ID_Colaborador_Usuario, ID_Treinamento),
    FOREIGN KEY (ID_Colaborador_Usuario) REFERENCES Colaborador_Usuario(ID_Colaborador),
    FOREIGN KEY (ID_Treinamento) REFERENCES Treinamento(ID_Treinamento),
    INDEX idx_colabtrein_treinamento (ID_Treinamento)
);

-- Tabela: Presença na Sessão
CREATE TABLE Presenca_Sessao (
    ID_Sessao INT NOT NULL,
    ID_Colaborador INT NOT NULL,
    PRIMARY KEY (ID_Sessao, ID_Colaborador),
    FOREIGN KEY (ID_Sessao) REFERENCES Sessao_Equipe(ID_Sessao),
    FOREIGN KEY (ID_Colaborador) REFERENCES Colaborador_Usuario(ID_Colaborador),
    INDEX idx_presenca_colaborador (ID_Colaborador)
);

-- Tabela: Treinador da Sessão
CREATE TABLE Treinador_Sessao (
    ID_Sessao_Equipe INT NOT NULL,
    ID_Colaborador_Treinador INT NOT NULL,
    PRIMARY KEY (ID_Sessao_Equipe, ID_Colaborador_Treinador),
    FOREIGN KEY (ID_Sessao_Equipe) REFERENCES Sessao_Equipe(ID_Sessao),
    FOREIGN KEY (ID_Colaborador_Treinador) REFERENCES Colaborador_Usuario(ID_Colaborador),
    INDEX idx_treinador_colaborador (ID_Colaborador_Treinador)
);

-- Tabela: Log de Auditoria
CREATE TABLE Log_Auditoria (
    ID_Log INT PRIMARY KEY AUTO_INCREMENT,
    Data_Hora_Transacao DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    ID_Usuario_Responsavel INT NOT NULL,
    Tabela_Afetada VARCHAR(100) NOT NULL,
    ID_Registro_Afetado INT NOT NULL,
    Acao VARCHAR(50) NOT NULL,
    Detalhes_Alteracao JSON,
    FOREIGN KEY (ID_Usuario_Responsavel) REFERENCES Colaborador_Usuario(ID_Colaborador)
);