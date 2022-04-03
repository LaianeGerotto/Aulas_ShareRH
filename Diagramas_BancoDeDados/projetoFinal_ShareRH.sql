
CREATE DATABASE "projeto_final_ShareRh2";


CREATE TABLE public.clientes (
    id integer NOT NULL,
    nome character varying NOT NULL,
    doc_identificacao character varying NOT NULL,
    tipo_pessoa character varying NOT NULL,
    telefone character varying NOT NULL,
    endereco character varying NOT NULL,
    email character varying
);


ALTER TABLE public.clientes ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.clientes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);

CREATE TABLE public.contratos (
    id integer NOT NULL,
    inicio_contrato date NOT NULL,
    termino_contrato date NOT NULL,
    id_corretor integer NOT NULL,
    id_cliente integer NOT NULL,
    id_imovel integer NOT NULL
);

ALTER TABLE public.contratos ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.contratos_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);

CREATE TABLE public.corretores (
    id integer NOT NULL,
    nome character varying NOT NULL,
    telefone character varying NOT NULL,
    email character varying NOT NULL
);


ALTER TABLE public.corretores ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.corretores_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);

CREATE TABLE public.imoveis (
    id integer NOT NULL,
    endereco character varying NOT NULL,
    id_proprietario integer NOT NULL,
    tipo_de_imovel character varying NOT NULL,
    descricao_imovel character varying NOT NULL
);

CREATE TABLE public.proprietarios (
    id integer NOT NULL,
    nome character varying NOT NULL,
    doc_identificacao character varying NOT NULL,
    tipo_pessoa character varying NOT NULL,
    telefone character varying NOT NULL,
    endereco character varying NOT NULL,
    email character varying
);


ALTER TABLE public.clientes
    ADD CONSTRAINT clientes_pkey PRIMARY KEY (id);


ALTER TABLE public.contratos
    ADD CONSTRAINT contratos_pkey PRIMARY KEY (id);


ALTER TABLE public.corretores
    ADD CONSTRAINT corretores_pkey PRIMARY KEY (id);


ALTER TABLE public.imoveis
    ADD CONSTRAINT imoveis_pkey PRIMARY KEY (id);


ALTER TABLE public.proprietarios
    ADD CONSTRAINT proprietarios_pkey PRIMARY KEY (id);

ALTER TABLE public.contratos
    ADD CONSTRAINT contratos_id_cliente_clientes FOREIGN KEY (id_cliente) REFERENCES public.clientes(id);

ALTER TABLE public.contratos
    ADD CONSTRAINT contratos_id_corretor_corretores FOREIGN KEY (id_corretor) REFERENCES public.corretores(id);


ALTER TABLE public.contratos
    ADD CONSTRAINT contratos_id_imovel_imoveis FOREIGN KEY (id_imovel) REFERENCES public.imoveis(id) NOT VALID;

ALTER TABLE public.imoveis
    ADD CONSTRAINT imoveis_id_proprietario_proprietarios FOREIGN KEY (id_proprietario) REFERENCES public.proprietarios(id) NOT VALID;

