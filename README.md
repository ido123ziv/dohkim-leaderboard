# The Dohkim Leader Board Website
## Tech Stack
Front -> Angular      
Back -> Python      
Database -> PostgreSQL      
Running on -> AWS      
Used with Docker      
# prerequisites
Make sure you have:
* `docker`    
* `python3`    
* `npm`    

On `wsl` export the following param name:
```bash
export DB_PASSWORD="shhhhhhh!"
```

## How to run?
first you need to build the project by:
```bash
docker-compose build
```
And then you can start the application by:
```bash
docker compose up
``` 
in order to stop you can either press: `ctrl+c` or `docker compose down`      
after you finish coding, you can rebuild the images.
## clean up the old images
run the following:
```bash
 docker rmi $(docker images -q --filter "dangling=true")
 docker volume prune -f
```