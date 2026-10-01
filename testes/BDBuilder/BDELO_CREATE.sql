CREATE TABLE public.canal (
    idelo integer CONSTRAINT canal_idelo_not_null NOT NULL,
    nome character varying(100) NOT NULL,
    descricao text,
    gremio_id integer,
    criador_idelo integer,
    cargo_adm_idelo integer
);

CREATE TABLE public.comunicado (
    idelo integer CONSTRAINT comunicado_idelo_not_null NOT NULL,
    titulo character varying(255) NOT NULL,
    conteudo text NOT NULL,
    data_publicacao timestamp without time zone NOT NULL,
    gremio_id integer,
    autor_idelo integer,
    cargo_adm_idelo integer
);

CREATE TABLE public.enquete (
    idelo integer CONSTRAINT enquete_idelo_not_null NOT NULL,
    titulo character varying(255) NOT NULL,
    descricao text,
    data_criacao timestamp without time zone NOT NULL,
    data_encerramento timestamp without time zone NOT NULL,
    gremio_id integer,
    autor_idelo integer,
    cargo_adm_idelo integer
);

CREATE TABLE public.evento (
    idelo integer CONSTRAINT evento_idelo_not_null NOT NULL,
    nome character varying(255) NOT NULL,
    descricao text,
    data_evento timestamp without time zone NOT NULL,
    local character varying(255) NOT NULL,
    gremio_id integer,
    organizador_idelo integer,
    cargo_adm_idelo integer
);

CREATE TABLE public.mensagem (
    idelo integer CONSTRAINT mensagem_idelo_not_null NOT NULL,
    texto text NOT NULL,
    data_envio timestamp without time zone NOT NULL,
    canal_id integer,
    usuario_id integer
);

CREATE SEQUENCE public.canal_idelo_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

CREATE SEQUENCE public.comunicado_idelo_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

CREATE SEQUENCE public.enquete_idelo_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

CREATE SEQUENCE public.evento_idelo_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

CREATE SEQUENCE public.mensagem_idelo_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER TABLE public.canal OWNER TO "ELO";
ALTER SEQUENCE public.canal_idelo_seq OWNER TO "ELO";
ALTER SEQUENCE public.canal_idelo_seq OWNED BY public.canal.idelo;

ALTER TABLE public.comunicado OWNER TO "ELO";
ALTER SEQUENCE public.comunicado_idelo_seq OWNER TO "ELO";
ALTER SEQUENCE public.comunicado_idelo_seq OWNED BY public.comunicado.idelo;

ALTER TABLE public.enquete OWNER TO "ELO";
ALTER SEQUENCE public.enquete_idelo_seq OWNER TO "ELO";
ALTER SEQUENCE public.enquete_idelo_seq OWNED BY public.enquete.idelo;

ALTER TABLE public.evento OWNER TO "ELO";
ALTER SEQUENCE public.evento_idelo_seq OWNER TO "ELO";
ALTER SEQUENCE public.evento_idelo_seq OWNED BY public.evento.idelo;

ALTER TABLE public.mensagem OWNER TO "ELO";
ALTER SEQUENCE public.mensagem_idelo_seq OWNER TO "ELO";
ALTER SEQUENCE public.mensagem_idelo_seq OWNED BY public.mensagem.idelo;

ALTER TABLE ONLY public.canal ALTER COLUMN idelo SET DEFAULT nextval('public.canal_idelo_seq'::regclass);
ALTER TABLE ONLY public.comunicado ALTER COLUMN idelo SET DEFAULT nextval('public.comunicado_idelo_seq'::regclass);
ALTER TABLE ONLY public.enquete ALTER COLUMN idelo SET DEFAULT nextval('public.enquete_idelo_seq'::regclass);
ALTER TABLE ONLY public.evento ALTER COLUMN idelo SET DEFAULT nextval('public.evento_idelo_seq'::regclass);
ALTER TABLE ONLY public.mensagem ALTER COLUMN idelo SET DEFAULT nextval('public.mensagem_idelo_seq'::regclass);
