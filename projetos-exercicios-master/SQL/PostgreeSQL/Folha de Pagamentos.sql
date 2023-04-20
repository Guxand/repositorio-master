create table Empresa(
	id_empresa serial not null,
	nome_empresa varchar(100) not null,
	cidade varchar(100) not null,
	CONSTRAINT pk_empresa primary key (id_empresa)
);

create table Funcionario(
	id_funcionario serial not null,
	nome_funcionario varchar(100) not null,
	cpf varchar(11) not null,
	pis_pasep varchar(11) not null,
	CONSTRAINT pk_funcionario primary key (id_funcionario)
);

CREATE table emprego (
	id_emprego serial not null,
	salario numeric(7,2) not null,
	id_empresa serial not null,
	id_funcionario INTEGER not null,
	CONSTRAINT pk_emprego primary key (id_emprego),
	CONSTRAINT fk_emprego_empresa foreign key (id_empresa) REFERENCES empresa (id_empresa),
	constraint fk_emprego_funcionario FOREIGN key (id_funcionario) references funcionario (id_funcionario)	
);


--drop table emprego

select * from funcionario
SELECT * from empresa
select * from emprego

insert into empresa
(nome_empresa, cidade) values('ADR Design', 'Ivoti')
(nome_empresa, cidade) values('Agência de Marketing Propagar Agora', 'Dois Irmãos')

insert into funcionario
(id_funcionario, nome_funcionario, cpf, salario, pis_pasep)
VALUES (1, 'Ígor Douglas Ramos da Silva', '04141538043', 1646, '20768934103')
(id_funcionario, nome_funcionario, cpf, pis_pasep)
VALUES (1, 'Ígor Douglas Ramos da Silva', '04141538043', '20768934103')

insert into emprego
(id_emprego, salario, id_empresa, id_funcionario) values ('1', 1646, '1', '1');
(id_emprego, salario, id_empresa, id_funcionario) values ('2', 1500, '2', '1')

select f.nome_funcionario, e.nome_empresa, emprego.salario
from funcionario f
inner join emprego on emprego.id_funcionario = f.id_funcionario
inner join empresa e on emprego.id_empresa = e.id_empresa

select nome_funcionario, salario
from funcionario f
inner join emprego on f.id_funcionario = emprego.id_funcionario
group by nome_funcionario, salario
having salario > 1500

select f.nome_funcionario, avg(emprego.salario), sum(emprego.salario)
from funcionario f
inner join emprego on f.id_funcionario = emprego.id_funcionario
group by f.nome_funcionario
