
  ![Incubateur Simplon.co : présentation, liste startups, interview](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSSEcKwborrMn9-Q2kmVlfAFLlq3M5DjW5Hlw&usqp=CAU)

this project is part of our courses at simplon school

### Microsoft Cloud Developer

# Flask server with ansible :

Creates an ansible playbook allowing to deploy a simple Flask application on a VM (with PostgreSQL db localy)

# Specifications:

-  Build a flask application
- Build a posgres database
- Connect thm with ansible files


## Build with:

-  HTML
-  CSS
- Python
- Flask
- jinja2

## install and run :

 1. Be sure to have ansible install on your machine:
 
	 https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html

 2.  Clone this repository.

	    git clone https://github.com/thibault-Merelle/Ansible.git
    
 3. Execute ansible on root directory as following :

	    ansible-playbook -i host playbook.yml

 4. finally, in your browser, go to the following address (where your need to call your own VM-IP) 
	

		 http://13.77.137.96:3000



## Architecture:

    |- app.py
    |- db.py
    |- .env
    |- playbook.yml
    |- hosts
    |- logger.py
    |- static:
	       |- css:
		       |- style.css
    |- templates:
		    |- id.html
		    |- index.html

 - app.py : main script in flask
 - db.py : class DB used to store query functions
 - .env : store your environnement variables
 - playbook.yml : orchestration script to build your VM
 - hosts : store your ansible environnement variables
 - logger.py : set decoration loggers
 - statics && templates : resources for flask

## Building your environment variables : 

- set a .env file in the root directory as follow :

    	    AZ_POSTGRES_HOST="VM-IP-adress"
		    AZ_POSTGRES_USER=your_user
		    AZ_POSTGRES_PASSWORD=your_password
		    AZ_POSTGRES_DATABASE=postgres
		    AZ_POSTGRES_PORT=22
		    FLASK_RUN_PORT=3000


- If needed in hosts file set your VM IPaddress like :
		

	    [azure-vm]
		13.77.137.96


## output port: 
- Flask => 3000
- Postgres => 22


## routes:

 - "/"  => welcomming page with input "name"
 
 
 - "/id" => print page who shows :
		 - number of names stores in database
		 - name of the current user
		 
- "/json" => showing my table with json 


