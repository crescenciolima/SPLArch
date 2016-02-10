# SPLArch
A **A SPLArch** é uma ferramenta voltada para o gerenciamento dos assets arquiteturais de projetos de Linha de Produto de Software. A ferramenta é desenvolvida utilizando linguagem de programação Python e o framework de desenvolvimento web Django.

**Pacotes Utilizados →** Para realizar a instalação dos pacotes é disponibilizado no arquivo requiremenst.txt, uma vez com o ambiente virtual (aconselhamos o uso do virtualenv) instalado será necessário utilizar o comando " pip install -r /path/to/requirements.txt "

#Versão dos pacotes utilizados<br>
* Python=2.7.3<br>
* Django=1.5.12<br>
* Pillow=3.0.0<br>
* django-admin-bootstrapped==1.6.9<br>
* django-bootstrap3==5.1.1<br>
* html5lib==0.9999999<br>
* pisa==3.0.33<br>
* reportlab==2.6<br>
* django-mptt==0.7.4<br>


#SPLArch - english version

Introduction
------------
Splash is a web application that helps software development documentation, allowing the issuance of personalized documents with different views of software implementation


Requirements
---------------------------

  * Django	1.5
  * Pillow	3.0.0
  * django-bootstrap3	5.1.1
  * django-extensions	1.5.9
  * django-media-tree	0.8.1
  * django-mptt	0.7.4
  * html5lib	0.9999999
  * pisa	3.0.33
  * reportlab	2.6
  * miktex 2.9 (http://miktex.org/download) or texlive (https://www.tug.org/texlive/)

Installation 
---------------------------

Clone the project

        gitclone https://github.com/cretchas/projeto_es_2015_2.git

Install requirements

        pip install -r /path/to/requirements.txt

Create the database

        python /path/to/manage.py syncdb


Run project
---------------------------

        python /path/to/manage.py runserver


Contributors
---------------------------
Crescencio Lima @cretchas, Fagner Santos @fagnerpsantos, Randler @randler


#SPLArch - Previous versions:
**version 1.0** https://github.com/cretchas/projeto_es_2015_1
**version 2.0** https://github.com/cretchas/projeto_es_2015_2
