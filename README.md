# CutIt
## About
CutIt - a useful service to make links shorter.

It is more convenient to use short links. For example, links http://cutit.com/lesson and http://cutit.com/12e07d perceived better than the large one https://www.google.com/url?sa=i&url=%3A%2F%2Fwww.theguardian.com%2Flifeandstyle&source=images.
The CutIt is a link shortening service. Its purpose is to associate a long user link with a short one, which is offered by the user himself or provided by the service.

The API can be viewed in openapi.yml
## How to launch a project
Clone the repository and go to it on the command line:
```
git clone 
```

```
cd cutit
```

Create and activate a virtual environment:

```
python3 -m venv venv
```

* Linux/macOS

    ```
    source venv/bin/activate
    ```

* Windows

    ```
    source venv/scripts/activate
    ```

Install dependencies:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Launch the project:

```
export FLASK_APP=cutit
flask run
```