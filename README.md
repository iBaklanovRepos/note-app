# Note App

Note App is a note management app written in Python with Flask usage.

## Functionality

User can login or sign up in system.
If the authorization is successful user have access to his notes.
Notes can be removed or added.
Notes are stored in SQLite database.
After first launch the app will create database based on declared model classes in [models.py](website/models.py) 

## Required Libraries

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required libraries from root node.

```bash
pip install -r requirments.txt
```

## Usage

Start the application from root of the project:

```bash
python main.py
```

After start application will be able by followed link
http://127.0.0.1:5000

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
