{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "359afbc1-dfb8-4da6-91dc-aeedc1b55886",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import h5py\n",
    "\n",
    "def load_dataset():\n",
    "    train_dataset = h5py.File('datasets/train_catvnoncat.h5', \"r\")\n",
    "    train_set_x_orig = np.array(train_dataset[\"train_set_x\"][:]) # your train set features\n",
    "    train_set_y_orig = np.array(train_dataset[\"train_set_y\"][:]) # your train set labels\n",
    "\n",
    "    test_dataset = h5py.File('datasets/test_catvnoncat.h5', \"r\")\n",
    "    test_set_x_orig = np.array(test_dataset[\"test_set_x\"][:]) # your test set features\n",
    "    test_set_y_orig = np.array(test_dataset[\"test_set_y\"][:]) # your test set labels\n",
    "\n",
    "    classes = np.array(test_dataset[\"list_classes\"][:]) # the list of classes\n",
    "    \n",
    "    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))\n",
    "    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))\n",
    "    \n",
    "    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "67a01040-f38d-4e2e-a388-290dd26c5ad8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0257147f-e80a-4d6a-8800-e02f278fd4b3",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "998c6de3-e8ea-4f0e-8e63-a749dda42a1b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
