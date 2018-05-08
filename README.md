# Yandex Algorithm 2018 ML track

[Final results: 2nd place](https://contest.yandex.ru/algorithm2018/contest/7914/standings/?lang=en)

To reproduce the second place solution run blend.py script. It will blend predictions from 100 models.

Language and classification model training as well as prediction is in alica_fwd.ipynb file. Backwards model training and prediction (short version based on forward model) is in alica_bkw.ipynb file. 

In order to run the solution install fast.ai library https://github.com/fastai/fastai. Then replace two files (lm_rnn.py and text.py) from fastai folder.
