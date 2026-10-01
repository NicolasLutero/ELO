ALTER TABLE ONLY public.cargo
    ADD CONSTRAINT cargo_pkey PRIMARY KEY (idelo);

ALTER TABLE ONLY public.gremio
    ADD CONSTRAINT gremio_cargo_adm_idelo_key UNIQUE (cargo_adm_idelo);
ALTER TABLE ONLY public.gremio
    ADD CONSTRAINT gremio_pkey PRIMARY KEY (idelo);

ALTER TABLE ONLY public.instituicao
    ADD CONSTRAINT instituicao_pkey PRIMARY KEY (idelo);

ALTER TABLE ONLY public.permissao
    ADD CONSTRAINT permissao_pkey PRIMARY KEY (idelo);

ALTER TABLE ONLY public.cargo_concede_permissao
    ADD CONSTRAINT uq_cargo_concede_permissao UNIQUE (cargo_idelo, permissao_idelo);

ALTER TABLE ONLY public.ocupa
    ADD CONSTRAINT uq_ocupa UNIQUE (usuario_idelo, cargo_idelo);

ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_cpf_key UNIQUE (cpf);
ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_email_key UNIQUE (email);
ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_pkey PRIMARY KEY (idelo);
ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_ra_key UNIQUE (ra);

ALTER TABLE ONLY public.validade
    ADD CONSTRAINT validade_pkey PRIMARY KEY (idelo);

ALTER TABLE ONLY public.cargo
    ADD CONSTRAINT cargo_gremio_id_fkey FOREIGN KEY (gremio_id) REFERENCES public.gremio(idelo) ON DELETE CASCADE;

ALTER TABLE ONLY public.cargo_concede_permissao
    ADD CONSTRAINT fk_cargo_concede_permissao_cargo FOREIGN KEY (cargo_idelo) REFERENCES public.cargo(idelo);

ALTER TABLE ONLY public.cargo_concede_permissao
    ADD CONSTRAINT fk_cargo_concede_permissao_permissao FOREIGN KEY (permissao_idelo) REFERENCES public.permissao(idelo);

ALTER TABLE ONLY public.gremio
    ADD CONSTRAINT fk_gremio_cargo_adm FOREIGN KEY (cargo_adm_idelo) REFERENCES public.cargo(idelo);

ALTER TABLE ONLY public.gremio
    ADD CONSTRAINT fk_gremio_fundador FOREIGN KEY (fundador_idelo) REFERENCES public.usuario(idelo);

ALTER TABLE ONLY public.ocupa
    ADD CONSTRAINT fk_ocupa_cargo FOREIGN KEY (cargo_idelo) REFERENCES public.cargo(idelo);

ALTER TABLE ONLY public.ocupa
    ADD CONSTRAINT fk_ocupa_usuario FOREIGN KEY (usuario_idelo) REFERENCES public.usuario(idelo);

ALTER TABLE ONLY public.gremio
    ADD CONSTRAINT gremio_instituicao_id_fkey FOREIGN KEY (instituicao_id) REFERENCES public.instituicao(idelo) ON DELETE CASCADE;

ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_gremio_id_fkey FOREIGN KEY (gremio_id) REFERENCES public.gremio(idelo) ON DELETE SET NULL;

ALTER TABLE ONLY public.validade
    ADD CONSTRAINT validade_cargo_id_fkey FOREIGN KEY (cargo_id) REFERENCES public.cargo(idelo) ON DELETE CASCADE;
