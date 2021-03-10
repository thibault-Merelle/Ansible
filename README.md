
  ![Incubateur Simplon.co : présentation, liste startups, interview](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSSEcKwborrMn9-Q2kmVlfAFLlq3M5DjW5Hlw&usqp=CAU)

this project is part of our courses at simplon school

### Microsoft Cloud Developer

# Flask server with ansible :

Creates an ansible playbook allowing to deploy a simple application on a VM

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

## Building your environment variables : 

- set a .env file in the root directory as follow :

    	    AZ_POSTGRES_HOST="VM-IP-adress"
		    AZ_POSTGRES_USER=user
		    AZ_POSTGRES_PASSWORD=pwd123
		    AZ_POSTGRES_DATABASE=postgres
		    AZ_POSTGRES_PORT=22
		    FLASK_RUN_PORT=3000


- If needed in hosts file set your VM IPaddress :
		

	    [azure-vm]
		13.77.137.96

		[azure-vm:vars]
		dbname=ansible_data
		dbuser=user
		dbpassword=pwd123
		github_user=thibault-Merelle
		AZ_user=azureuser
		app_name=Ansible


## install and run :

1.  Clone this repository.

	    git clone https://github.com/thibault-Merelle/Ansible.git
    
2. Execute ansible on root directory as following :

	    ansible-playbook -i host votre_playbook.yml

## routes:

 - "/"  => welcomming page with input "name"
 
 - "/id" => print page who shows :
		 - number of names stores in database
		 - name of the current user
		 
- "/json" => showing my table with json 

## output port: 
- Flask => 3000
- Postgres => 22



