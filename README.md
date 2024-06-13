**Activate the virtual environment for mac**
```
source tus-env/bin/activate
```

**Activate the virtual environment for windows**
```
tus-winenv/Scripts/activate 
``` 

**Install all packages**
```
pip3 install -r requirements.txt
```

**Run the tests**
Make sure to activate the virtual environment

```
python3 -m pytest backend/tests
```

**You to create a .env file**
```
PROJ_NAME=
ASTRADB_KEYSPACE=
ASTRA_DB_CLIENT_ID=
ASTRA_DB_CLIENT_SECRET=
ASTRADB_TOKEN=
SECRET_KEY=
```