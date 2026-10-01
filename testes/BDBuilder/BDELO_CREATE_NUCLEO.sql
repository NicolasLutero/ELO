CREATE TABLE public.cargo (
    idelo integer CONSTRAINT cargo_idelo_not_null NOT NULL,
    nome character varying(100) NOT NULL,
    descricao text,
    vagas integer NOT NULL,
    gremio_id integer
);

CREATE TABLE public.cargo_concede_permissao (
    cargo_idelo integer NOT NULL,
    permissao_idelo integer NOT NULL
);

CREATE TABLE public.gremio (
    idelo integer CONSTRAINT gremio_idelo_not_null NOT NULL,
    nome character varying(255) NOT NULL,
    instituicao_id integer,
    etapa_ensino character varying(100) NOT NULL,
    legitimado boolean DEFAULT false,
    cargo_adm_idelo integer,
    fundador_idelo integer
);

CREATE TABLE public.instituicao (
    idelo integer CONSTRAINT instituicao_idelo_not_null NOT NULL,
    nome character varying(255) NOT NULL,
    endereco character varying(255) NOT NULL
);

CREATE TABLE public.ocupa (
    usuario_idelo integer NOT NULL,
    cargo_idelo integer NOT NULL
);

CREATE TABLE public.permissao (
    idelo integer CONSTRAINT permissao_idelo_not_null NOT NULL,
    nome character varying(100) NOT NULL,
    descricao text
);

CREATE TABLE public.usuario (
    idelo integer CONSTRAINT usuario_idelo_not_null NOT NULL,
    nome character varying(255) NOT NULL,
    cpf character varying(14) NOT NULL,
    email character varying(255) NOT NULL,
    ra character varying(50) NOT NULL,
    senha character varying(255) NOT NULL,
    gremio_id integer
);

CREATE TABLE public.validade (
    idelo integer CONSTRAINT validade_idelo_not_null NOT NULL,
    data_inicio date NOT NULL,
    data_fim date NOT NULL,
    cargo_id integer
);

CREATE SEQUENCE public.cargo_idelo_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

CREATE SEQUENCE public.gremio_idelo_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

CREATE SEQUENCE public.instituicao_idelo_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

CREATE SEQUENCE public.permissao_idelo_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

CREATE SEQUENCE public.usuario_idelo_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

CREATE SEQUENCE public.validade_idelo_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER TABLE public.cargo OWNER TO "ELO";
ALTER SEQUENCE public.cargo_idelo_seq OWNER TO "ELO";
ALTER SEQUENCE public.cargo_idelo_seq OWNED BY public.cargo.idelo;

ALTER TABLE public.cargo_concede_permissao OWNER TO "ELO";

ALTER TABLE public.gremio OWNER TO "ELO";
ALTER SEQUENCE public.gremio_idelo_seq OWNER TO "ELO";
ALTER SEQUENCE public.gremio_idelo_seq OWNED BY public.gremio.idelo;

ALTER TABLE public.instituicao OWNER TO "ELO";
ALTER SEQUENCE public.instituicao_idelo_seq OWNER TO "ELO";
ALTER SEQUENCE public.instituicao_idelo_seq OWNED BY public.instituicao.idelo;

ALTER TABLE public.ocupa OWNER TO "ELO";

ALTER TABLE public.permissao OWNER TO "ELO";
ALTER SEQUENCE public.permissao_idelo_seq OWNER TO "ELO";
ALTER SEQUENCE public.permissao_idelo_seq OWNED BY public.permissao.idelo;

ALTER TABLE public.usuario OWNER TO "ELO";
ALTER SEQUENCE public.usuario_idelo_seq OWNER TO "ELO";
ALTER SEQUENCE public.usuario_idelo_seq OWNED BY public.usuario.idelo;

ALTER TABLE public.validade OWNER TO "ELO";
ALTER SEQUENCE public.validade_idelo_seq OWNER TO "ELO";
ALTER SEQUENCE public.validade_idelo_seq OWNED BY public.validade.idelo;


ALTER TABLE ONLY public.cargo ALTER COLUMN idelo SET DEFAULT nextval('public.cargo_idelo_seq'::regclass);
ALTER TABLE ONLY public.gremio ALTER COLUMN idelo SET DEFAULT nextval('public.gremio_idelo_seq'::regclass);
ALTER TABLE ONLY public.instituicao ALTER COLUMN idelo SET DEFAULT nextval('public.instituicao_idelo_seq'::regclass);
ALTER TABLE ONLY public.permissao ALTER COLUMN idelo SET DEFAULT nextval('public.permissao_idelo_seq'::regclass);
ALTER TABLE ONLY public.usuario ALTER COLUMN idelo SET DEFAULT nextval('public.usuario_idelo_seq'::regclass);
ALTER TABLE ONLY public.validade ALTER COLUMN idelo SET DEFAULT nextval('public.validade_idelo_seq'::regclass);
