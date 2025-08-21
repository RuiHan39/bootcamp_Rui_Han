{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "efb529d3-eae1-4590-a6bc-6d4b3feb832f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Imports\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "from sklearn.preprocessing import MinMaxScaler, StandardScaler\n",
    "import missingno as msno"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "48b859de-45d8-4005-8303-d63983735b23",
   "metadata": {},
   "outputs": [],
   "source": [
    "def fill_missing_median(df, columns=None):\n",
    "    df_copy = df.copy()\n",
    "    if columns is None:\n",
    "        columns = df.select_dtypes(include=np.number).columns\n",
    "    for col in columns:\n",
    "        df_copy[col] = df_copy[col].fillna(df_copy[col].median())\n",
    "    return df_copy\n",
    "\n",
    "def drop_missing(df, columns=None, threshold=None):\n",
    "    df_copy = df.copy()\n",
    "    if columns is not None:\n",
    "        return df_copy.dropna(subset=columns)\n",
    "    if threshold is not None:\n",
    "        return df_copy.dropna(thresh=int(threshold*df_copy.shape[1]))\n",
    "    return df_copy.dropna()\n",
    "\n",
    "def normalize_data(df, columns=None, method='minmax'):\n",
    "    df_copy = df.copy()\n",
    "    if columns is None:\n",
    "        columns = df_copy.select_dtypes(include=np.number).columns\n",
    "    if method=='minmax':\n",
    "        scaler = MinMaxScaler()\n",
    "    else:\n",
    "        scaler = StandardScaler()\n",
    "    df_copy[columns] = scaler.fit_transform(df_copy[columns])\n",
    "    return df_copy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "12661743-2993-4dc6-8183-386913e23708",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "bootcamp_env",
   "language": "python",
   "name": "bootcamp_env"
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
   "version": "3.10.18"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
