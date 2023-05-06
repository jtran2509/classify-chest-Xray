# -*- coding: utf-8 -*-
"""Chest X-ray.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bVCzjYIgUi71TZOPyvJrrdIu9jNAvtxS
"""

!pip install -Uqq fastbook
import fastbook
fastbook.setup_book()

from fastbook import *

from fastai.vision import *
import numpy as np

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
import nibabel as nib
from ipywidgets import interact, interactive, IntSlider, ToggleButtons
import os
import seaborn as sns
sns.set_style('darkgrid')

from google.colab import drive
drive.mount('/content/drive')

tfms = aug_transforms(do_flip=False)
path = '/content/drive/My Drive/fastai'
data = ImageDataLoaders.from_folder(path, train = 'train', valid = 'test',
                                    item_tfms = Resize(224), seed = 42,
                                    num_workers = 3, bs = 64, valid_pct=0.2)

data.show_batch()

my_trained_mod = cnn_learner(data, models.resnet34, metrics=error_rate)
my_trained_mod.fit_one_cycle(5)

# Check the learning rate
my_trained_mod.lr_find()
plt.plot(my_trained_mod.recorder.lrs, my_trained_mod.recorder.losses)

interp = ClassificationInterpretation.from_learner(my_trained_mod)
interp.plot_confusion_matrix()

interp = ClassificationInterpretation.from_learner(my_trained_mod)
upp, low = interp.confusion_matrix()
tn, fp = upp[0], upp[1]
fn, tp = low[0], low[1]
specificity = tn/(fp + tn)

specificity

precision = tp/(tp+fp)
recall = tp/(tp+fn)
print(recall)
print(precision)

interp.plot_top_losses(3, nrows=1, figsize = (25,5))

my_trained_mod.fit_one_cycle(3, lr_max=slice(1e-6,1e-1))

my_trained_mod.export()

path = Path ('/content/drive/My Drive/fastai')
path.ls(file_exts= '.pkl')

learn_inf = load_learner('/content/drive/My Drive/fastai/export.pkl')

# normal X-ray
learn_inf.predict('/content/drive/MyDrive/fastai/test/NORMAL/IM-0005-0001.jpeg')

learn_inf.predict('/content/drive/MyDrive/fastai/test/PNEUMONIA/person44_virus_94.jpeg')

learn_inf.predict('/content/drive/MyDrive/fastai/test/NORMAL/IM-0109-0001.jpeg')

learn_inf.predict('/content/drive/MyDrive/fastai/test/PNEUMONIA/person101_bacteria_484.jpeg')

import os
!pip install -q streamlit

import streamlit as st


def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)
    return os.path.join(folder_path, selected_filename)


if __name__ == '__main__':
    # Select a file
    if st.checkbox('Select a file in current directory'):
        folder_path = '.'
        if st.checkbox('Change directory'):
            folder_path = st.text_input('Enter folder path', '.')
        filename = file_selector(folder_path=folder_path)
        st.write('You selected `%s`' % filename)

