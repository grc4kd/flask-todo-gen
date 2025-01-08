version 1
- installation of python3, virtual environment, flask, and SQLAlchemy
- changed GPT output (gpt-py is General Purpose Transformer output, hid-py is Human Interface Device output aka hand-coded)
```gpt-py
db = SQLAlchemy(app)
```

```hid-py
db = sqlalchemy(app)
```
- added to GPT output
```gpt-py
```

```hid-py
import sqlalchemy
```

- create requirements.txt file to document dependencies with a machine-readable format

- copied relevant lines of code from database connection sample
import sqlalchemy

engine = sqlalchemy.create_engine('sqlite://')
connection = engine.connect()

- updated connection variable name to db to match original source code
```gpt-py
connection = engine.connect()
```

```hid-py
db = engine.connect()
```

- updated connection string to use a file-backed database
```gpt-py
engine = sqlalchemy.create_engine('sqlite://')
```

```hid-py
engine = sqlalchemy.create_engine('sqlite://todos.db')
```

- removed call to python module
```gpt-py
db = sqlalchemy(app)
```

```hid-py
```

- changed class definition to include the db object during construction
  db.Model, a Connection object, has no attribute named Model
```gpt-py
class Todo(db.Model):
```

```hid-py
class Todo(db):
```

- added import for String 
```gpt-py
from sqlalchemy import Column, Integer
```

```hid-py
from sqlalchemy import Column, Integer, String
```

- removed last generated code snippet for creating a SQLAlchemy engine object and coded by hand
