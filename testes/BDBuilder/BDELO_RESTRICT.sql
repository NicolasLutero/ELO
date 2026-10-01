ALTER TABLE ONLY public.canal
    ADD CONSTRAINT canal_cargo_adm_idelo_key UNIQUE (cargo_adm_idelo);
ALTER TABLE ONLY public.canal
    ADD CONSTRAINT canal_pkey PRIMARY KEY (idelo);
    
ALTER TABLE ONLY public.comunicado
    ADD CONSTRAINT comunicado_cargo_adm_idelo_key UNIQUE (cargo_adm_idelo);
ALTER TABLE ONLY public.comunicado
    ADD CONSTRAINT comunicado_pkey PRIMARY KEY (idelo);

ALTER TABLE ONLY public.enquete
    ADD CONSTRAINT enquete_cargo_adm_idelo_key UNIQUE (cargo_adm_idelo);
ALTER TABLE ONLY public.enquete
    ADD CONSTRAINT enquete_pkey PRIMARY KEY (idelo);

ALTER TABLE ONLY public.evento
    ADD CONSTRAINT evento_cargo_adm_idelo_key UNIQUE (cargo_adm_idelo);
ALTER TABLE ONLY public.evento
    ADD CONSTRAINT evento_pkey PRIMARY KEY (idelo);

ALTER TABLE ONLY public.mensagem
    ADD CONSTRAINT mensagem_pkey PRIMARY KEY (idelo);

ALTER TABLE ONLY public.canal
    ADD CONSTRAINT canal_gremio_id_fkey FOREIGN KEY (gremio_id) REFERENCES public.gremio(idelo) ON DELETE CASCADE;

ALTER TABLE ONLY public.comunicado
    ADD CONSTRAINT comunicado_gremio_id_fkey FOREIGN KEY (gremio_id) REFERENCES public.gremio(idelo) ON DELETE CASCADE;

ALTER TABLE ONLY public.enquete
    ADD CONSTRAINT enquete_gremio_id_fkey FOREIGN KEY (gremio_id) REFERENCES public.gremio(idelo) ON DELETE CASCADE;

ALTER TABLE ONLY public.evento
    ADD CONSTRAINT evento_gremio_id_fkey FOREIGN KEY (gremio_id) REFERENCES public.gremio(idelo) ON DELETE CASCADE;

ALTER TABLE ONLY public.canal
    ADD CONSTRAINT fk_canal_cargo_adm FOREIGN KEY (cargo_adm_idelo) REFERENCES public.cargo(idelo);

ALTER TABLE ONLY public.canal
    ADD CONSTRAINT fk_canal_criador FOREIGN KEY (criador_idelo) REFERENCES public.usuario(idelo);

ALTER TABLE ONLY public.comunicado
    ADD CONSTRAINT fk_comunicado_autor FOREIGN KEY (autor_idelo) REFERENCES public.usuario(idelo);

ALTER TABLE ONLY public.comunicado
    ADD CONSTRAINT fk_comunicado_cargo_adm FOREIGN KEY (cargo_adm_idelo) REFERENCES public.cargo(idelo);

ALTER TABLE ONLY public.enquete
    ADD CONSTRAINT fk_enquete_autor FOREIGN KEY (autor_idelo) REFERENCES public.usuario(idelo);

ALTER TABLE ONLY public.enquete
    ADD CONSTRAINT fk_enquete_cargo_adm FOREIGN KEY (cargo_adm_idelo) REFERENCES public.cargo(idelo);

ALTER TABLE ONLY public.evento
    ADD CONSTRAINT fk_evento_cargo_adm FOREIGN KEY (cargo_adm_idelo) REFERENCES public.cargo(idelo);

ALTER TABLE ONLY public.evento
    ADD CONSTRAINT fk_evento_organizador FOREIGN KEY (organizador_idelo) REFERENCES public.usuario(idelo);

ALTER TABLE ONLY public.mensagem
    ADD CONSTRAINT mensagem_canal_id_fkey FOREIGN KEY (canal_id) REFERENCES public.canal(idelo) ON DELETE CASCADE;

ALTER TABLE ONLY public.mensagem
    ADD CONSTRAINT mensagem_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES public.usuario(idelo) ON DELETE CASCADE;
