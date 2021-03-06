--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: employee; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE employee (
    "ID" character varying(10) NOT NULL,
    "First Name" text,
    "Last Name" text,
    jefe text
);


ALTER TABLE public.employee OWNER TO postgres;

--
-- Name: employee_department; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE employee_department (
    "ID" character varying(10),
    "Name" text,
    "Description" text
);


ALTER TABLE public.employee_department OWNER TO postgres;

--
-- Name: employee_hobby; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE employee_hobby (
    "ID" character varying(10) NOT NULL,
    name text NOT NULL,
    description text
);


ALTER TABLE public.employee_hobby OWNER TO postgres;

--
-- Data for Name: employee; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO employee VALUES ('09835FJSCS', 'Carolina', 'Linares', 'Francisco Linares');
INSERT INTO employee VALUES ('23839FHSNR', 'Rogger', 'Pérez', 'Francisco Linares');
INSERT INTO employee VALUES ('03945JFSCC', 'Hermes', 'Nuñes', 'Daniel Romero');
INSERT INTO employee VALUES ('18238FVDSF', 'Carlos', 'Rangel', 'Francisco Linares');


--
-- Data for Name: employee_department; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO employee_department VALUES ('09835FJSCS', 'Dto. de Servicio Social', 'Control de los chicos del Servicio Social y Recidencias');
INSERT INTO employee_department VALUES ('23839FHSNR', 'Dto. de Escolares', 'Control del chicos del servicio');
INSERT INTO employee_department VALUES ('03945JFSCC', 'Dto. de Mantenimiento', 'Se encuarga de mantener en buen estado las instalaciones');
INSERT INTO employee_department VALUES ('18238FVDSF', 'Dto. de Calidad', 'Auditorias, Minutas, Oficios');
INSERT INTO employee_department VALUES (NULL, 'Dto. de Sistemas', 'Control de los Sistemas de Computo');
INSERT INTO employee_department VALUES (NULL, 'Dto. de Recursos Financieros', 'Se encarga de Administrar el dinero');


--
-- Data for Name: employee_hobby; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO employee_hobby VALUES ('09835FJSCS', 'Ejercicio', 'Personas que les gusta ejercitar su cuerpo');
INSERT INTO employee_hobby VALUES ('09835FJSCS', 'Jugar Video-Juegos', 'Personas que se distraen por ratos largos en los video juegos ');
INSERT INTO employee_hobby VALUES ('23839FHSNR', 'Escuchar Musica', 'Personas que les gusta escuchar musica para relajarse');
INSERT INTO employee_hobby VALUES ('23839FHSNR', 'Ejercicio', 'Personas que les gusta ejercitar su cuerpo');
INSERT INTO employee_hobby VALUES ('03945JFSCC', 'Jugar Video-Juegos', 'Personas que se distraen por ratos largos en los video juegos');
INSERT INTO employee_hobby VALUES ('03945JFSCC', 'Escuchar Musica', 'Personas que les gusta escuchar musica para relajarse');
INSERT INTO employee_hobby VALUES ('18238FVDSF', 'Ejercicio', 'Personas que les gusta ejercitar su cuerpo');
INSERT INTO employee_hobby VALUES ('18238FVDSF', 'Jugar Video-Juegos', 'Personas que se distraen por ratos largos en los video juegos');


--
-- Name: employee_department_ID_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY employee_department
    ADD CONSTRAINT "employee_department_ID_key" UNIQUE ("ID");


--
-- Name: employee_employee_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY employee
    ADD CONSTRAINT employee_employee_pkey PRIMARY KEY ("ID");


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

