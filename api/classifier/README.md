# Classifier
Used Model: [https://jovian.ai/gitrohitjain/pokemon-classification](https://jovian.ai/gitrohitjain/pokemon-classification)

Used Dataset: 
[https://www.kaggle.com/lantian773030/pokemonclassification](https://www.kaggle.com/lantian773030/pokemonclassification)

# Running classifier
Install the dependencies:
```sh
virtualenv classify-venv
source classify-venv/bin/activate
pip3 install -r classify-requirements.txt
```

Then, use the following code to run the classifier and print the classified pokemon and its confidence:
```python3
import torch
from classify import classify_image

model = torch.load("model.pth")
model.eval()

print(classify_image("img.png", model))
```


# Training model by yourself
First download the [dataset](https://www.kaggle.com/lantian773030/pokemonclassification) and save it to the `classifier` directory as `PokemonData`.  

Next install the dependencies:

```sh
virtualenv model-venv
source model-venv/bin/activate
pip3 install -r model-requirements.txt
```

Run `python3 model.py` to train the model and generate a `.pth` file for the model, or run the [Notebook](https://jovian.ai/gitrohitjain/pokemon-classification) and add the lines to save the model as done in `model.py`.  

This may take a couple of hours, depending on your GPU.
