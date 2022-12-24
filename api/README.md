# Running Locally
Install the dependencies:
```sh
virtualenv api-venv
source api-venv/bin/activate
pip3 install -r api-requirements.txt
```

Running uvicorn:
```sh
uvicorn api:app --reload
```

Sending a request:
```sh
curl 127.0.0.1:8000/classify -F pokemon_img=@classifier/testimages/1.png
```
