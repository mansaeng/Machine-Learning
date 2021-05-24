{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "main.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyO+r+IXj8Pa+SE13N/e60cx",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/mansaeng/Machine-Learning/blob/main/main.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "dS6PwBs0fsST"
      },
      "source": [
        "# 필요한 모듈 Importing\n",
        "import matplotlib.pyplot as plt\n",
        "import pandas as pd\n",
        "from sklearn import (\n",
        "    ensemble,\n",
        "    preprocessing,\n",
        "    tree,\n",
        ")\n",
        "from sklearn.metrics import (\n",
        "    auc,\n",
        "    confusion_matrix,\n",
        "    roc_auc_score,\n",
        "    roc_curve,\n",
        ")\n",
        "from sklearn.model_selection import (\n",
        "    train_test_split,\n",
        "    StratifiedKFold,\n",
        ")\n",
        "from yellowbrick.classifier import (\n",
        "    ConfusionMatrix,\n",
        "    ROCAUC,\n",
        ")\n",
        "from yellowbrick.model_selection import (\n",
        "    LearningCurve,\n",
        ")\n",
        "\n",
        "# 판다스는 데이터를 가공 처리하는 모듈이다.\n",
        "# 사이킷런은 예측 모델링을 제공한다.\n",
        "# 옐로우브릭은 모델 검증을 위한 시각화 라이브러리이다.\n",
        "\n",
        "\n",
        "# from ~ import ~ 형식으로 Importing 할 때 (\n",
        "#   이렇게,\n",
        "#   Pythonic한 방법을,\n",
        "#   이제 알았다.\n",
        "# )"
      ],
      "execution_count": 17,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "MsTIEOQ5smA5"
      },
      "source": [
        "# *from pandas import **\n",
        "\n",
        "별표를 사용하여 라이브러리를 불러들이면\n",
        "명시적이지 않으므로 코드 이해가 어려워진다.\n",
        "지정해서 불러오는 습관을 들이자."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xGBaq5VFjb9W"
      },
      "source": [
        "# 머신러닝에 필요한 데이터 가져오기\n",
        "url = (\n",
        "    \"https://biostat.app.vumc.org/wiki/pub/Main/DataSets/titanic3.xls\"\n",
        ")\n",
        "df = pd.read_excel(url) # 판다스의 read_excel은 파일 뿐만이 아니라 url의 데이터도 가져올 수 있다.\n",
        "orig_df = df"
      ],
      "execution_count": 14,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "vAaN5WBetaz-"
      },
      "source": [
        "**주어진 데이터 :**\n",
        "> 타이타닉호 탑승객 데이터\n",
        "\n",
        "**목표 :**\n",
        "> 해당 탑승객이 생존했는지 사망했는지 예측(분류)"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Qw0VAOC2uYEp"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}