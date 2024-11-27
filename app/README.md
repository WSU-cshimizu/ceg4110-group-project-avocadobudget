### Ensure you have python3 installed on your device
- If you are on github you know how to do this
  
### Clone repository from github to local directory
- You should know this by now

### Build environment
```python3 -m venv <myenvname>``` (could be venv for example inside)

### Activate virtual environment
- move to working directory where you loaded the virtual environment (CD)
- activate virtual environment - ensure you are in directory that holds directory for environment
   1. ***macOS/Linux*** ```source <myenvname>/bin/activate``` (where .venv was the environment directory I made in build environment)
   2. ***Windows*** ```<myenvname>\Scricts\activate```

### Deactivate virtual environment
```deactivate```

### Install required libraries to virtual environment using requirements.txt

- Move to app directory, in there github should have requirements.txt
- With virtual environment activated use ```pip install -r requirements.txt``` or ```python3 -m pip install -r requirements.txt```

### Run app

- Move to app directory, ensure your enviroment is running and you installed required libraries
- ```python3 app.py```
- This will start the web server

### Pull up website

- On browser navigate to [local webpage for app on port 5000](http://127.0.0.1:5000)
- This will open up local only connection to website and your personal budget app will be available

