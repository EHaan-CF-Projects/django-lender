# book nook.

**Author**: Evy Haan
**Version**: 1.0

## Overview
This app allows users to maintain a list of favorite books and monitor availability & checkout status.

## Getting Started
1. Clone the repo.
2. Create a virtual invironment and install the packages in it.
3. Create a .env file that contains the following:
```
# Docker-specific
DB_NAME=postgres
    
# Docker-specific  
DB_USER=postgres
    
# Docker-specific
DB_HOST=db 
    
# This comes from Django when you start the project 
SECRET_KEY= <your secret key>
    
# Turns on development mode and activates the built in debugging tools 
DEBUG=True  
    
# Tells Django while domains can contact the server (whitelist)
ALLOWED_HOSTS=localhost 127.0.0.1 0.0.0.0
```
4. Ensure docker and docker-compose are installed.
5. Launch project for the top directory with `docker-compose up`

## Architecture
**Packages**
- django
- django-registration
- psychopg-binary