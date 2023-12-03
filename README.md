### Installing necessary packages:  
* `pip install fastapi`
* `pip install "uvicorn[standard]"`  
* `pip install sqlalchemy`  
* `pip install pymysql`
* `pip install pytest`
* `pip install pytest-mock`
* `pip install httpx`
* `pip install cryptography`
### Run the server:
`uvicorn api.main:app --reload`
### Test API by built-in docs:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Development Setup
- Create new connection in MySQL WorkBench:
  - Connection name & root password must be same as ```api/dependencies/config.py``` so fastapi can access and interact with local MySQL database in your machine (if you have a different password, change the password in config.py to match yours)
  - Test connection to make sure MySQL in your machine is running
- Create a virtualenv and installed all packages above
- Run the server in venv. MySQL database tables should be populated
- run SQL commands in ```mysql_scripts/``` to populate crusts and toppings data

