#!/usr/bin/env python
# coding: utf-8

# ## 1. Introduction
# <p><img src="https://assets.datacamp.com/production/project_1197/img/google_play_store.png" alt="Google Play logo"></p>
# <p>Mobile apps are everywhere. They are easy to create and can be very lucrative from the business standpoint. Specifically, Android is expanding as an operating system and has captured more than 74% of the total market<sup><a href="https://www.statista.com/statistics/272698/global-market-share-held-by-mobile-operating-systems-since-2009">[1]</a></sup>. </p>
# <p>The Google Play Store apps data has enormous potential to facilitate data-driven decisions and insights for businesses. In this notebook, we will analyze the Android app market by comparing ~10k apps in Google Play across different categories. We will also use the user reviews to draw a qualitative comparision between the apps.</p>
# <p>The dataset you will use here was scraped from Google Play Store in September 2018 and was published on <a href="https://www.kaggle.com/lava18/google-play-store-apps">Kaggle</a>. Here are the details: <br>
# <br></p>
# <div style="background-color: #efebe4; color: #05192d; text-align:left; vertical-align: middle; padding: 15px 25px 15px 25px; line-height: 1.6;">
#     <div style="font-size:20px"><b>datasets/apps.csv</b></div>
# This file contains all the details of the apps on Google Play. There are 9 features that describe a given app.
# <ul>
#     <li><b>App:</b> Name of the app</li>
#     <li><b>Category:</b> Category of the app. Some examples are: ART_AND_DESIGN, FINANCE, COMICS, BEAUTY etc.</li>
#     <li><b>Rating:</b> The current average rating (out of 5) of the app on Google Play</li>
#     <li><b>Reviews:</b> Number of user reviews given on the app</li>
#     <li><b>Size:</b> Size of the app in MB (megabytes)</li>
#     <li><b>Installs:</b> Number of times the app was downloaded from Google Play</li>
#     <li><b>Type:</b> Whether the app is paid or free</li>
#     <li><b>Price:</b> Price of the app in US$</li>
#     <li><b>Last Updated:</b> Date on which the app was last updated on Google Play </li>
# 
# </ul>
# </div>
# <div style="background-color: #efebe4; color: #05192d; text-align:left; vertical-align: middle; padding: 15px 25px 15px 25px; line-height: 1.6;">
#     <div style="font-size:20px"><b>datasets/user_reviews.csv</b></div>
# This file contains a random sample of 100 <i>[most helpful first](https://www.androidpolice.com/2019/01/21/google-play-stores-redesigned-ratings-and-reviews-section-lets-you-easily-filter-by-star-rating/)</i> user reviews for each app. The text in each review has been pre-processed and passed through a sentiment analyzer.
# <ul>
#     <li><b>App:</b> Name of the app on which the user review was provided. Matches the `App` column of the `apps.csv` file</li>
#     <li><b>Review:</b> The pre-processed user review text</li>
#     <li><b>Sentiment Category:</b> Sentiment category of the user review - Positive, Negative or Neutral</li>
#     <li><b>Sentiment Score:</b> Sentiment score of the user review. It lies between [-1,1]. A higher score denotes a more positive sentiment.</li>
# 
# </ul>
# </div>
# <p>From here on, it will be your task to explore and manipulate the data until you are able to answer the three questions described in the instructions panel.<br></p>

# In[158]:


# Use this cell to begin your analysis, and add as many as you would like!
import pandas as pd
import numpy as np

apps = pd.read_csv("datasets/apps.csv")

apps.head()


# In[159]:


apps["Installs"] = apps["Installs"].apply(lambda x: int(x.replace(",","").replace("+","")))

apps_info = apps[["Category","Rating","Price"]]

app_category_info = apps_info.groupby("Category").mean()

app_category_info


# In[160]:



app_category_info.set_axis(["Average rating", "Average price"],axis = 1)

app_category_info["Number of apps"] = apps["Category"].value_counts()

app_category_info


# In[161]:


top_10_user_feedback = apps[(apps["Category"] == "FINANCE") & (apps["Type"] == "Free")]

user_reviews = pd.read_csv("datasets/user_reviews.csv")

top_10_user_feedback = pd.merge(user_reviews, top_10_user_feedback, on = "App", how = "inner")

top_10_user_feedback = top_10_user_feedback.groupby("App").mean()

top_10_user_feedback["App"] = top_10_user_feedback.index

top_10_user_feedback = top_10_user_feedback.sort_values(by = "Sentiment Score", ascending = False).head(10)

top_10_user_feedback = top_10_user_feedback["Sentiment Score"]

top_10_user_feedback = pd.DataFrame(top_10_user_feedback)

top_10_user_feedback


# In[162]:


# Importing the pandas module
import pandas as pd

# Read datasets/apps.csv 
apps = pd.read_csv("datasets/apps.csv")

# QUESTION 1
# Data Cleaning
# List of characters to remove
chars_to_remove = ['+', ',']
# Replace each character with an empty string
for char in chars_to_remove:
    apps['Installs'] = apps['Installs'].apply(lambda x: x.replace(char, ''))
# Convert to int
apps['Installs'] = apps['Installs'].astype(int)
    
    
# QUESTION 2
# Group by app category and apply the aggregate functions
app_category_info = apps.groupby('Category').agg({'App': 'count', 'Price': 'mean', 'Rating': 'mean'})

# Rename the columns for easier understanding
app_category_info = app_category_info.rename(columns={"App": "Number of apps", "Price": "Average price", "Rating": "Average rating"})


# QUESTION 3
# Read datasets/user_reviews.csv
reviews = pd.read_csv('datasets/user_reviews.csv')

# Select finance apps
finance_apps = apps[apps['Category'] == 'FINANCE']
# Select free finance apps
free_finance_apps = finance_apps[finance_apps['Type'] == 'Free']
# We can also combine the two conditions in a single line of code using the & operator
# free_finance_apps = apps[(apps['Category'] == 'FINANCE') & (apps['Type'] == 'Free')]

# Join the dataframes
merged_df = pd.merge(finance_apps, reviews, on = "App", how = "inner")
# The default value of "how" argument is "inner", so we can skip specifying it. 
# But it is a good practice to specify the type of your join for better code readability.

# Find the average sentiment score for each app
app_sentiment_score = merged_df.groupby('App').agg({'Sentiment Score' :'mean'})

# Sort the average sentiment score from highest to lowest (ie - in decreasing order)
user_feedback = app_sentiment_score.sort_values(by = 'Sentiment Score', ascending = False)

# select first 10
top_10_user_feedback = user_feedback[:10]
top_10_user_feedback


# In[163]:


get_ipython().run_cell_magic('nose', '', '# %%nose needs to be included at the beginning of every @tests cell\n\n# https://instructor-support.datacamp.com/en/articles/4544008-writing-project-tests-guided-and-unguided-r-and-python\n# The @solution should pass the tests\n# The purpose of the tests is to try to catch common errors and\n# to give the student a hint on how to resolve these errors\n\nimport numpy as np\n\ncorrect_apps = pd.read_csv(\'datasets/apps.csv\')\ncorrect_reviews = pd.read_csv(\'datasets/user_reviews.csv\')\n\n# List of characters to remove\nchars_to_remove = [\'+\', \',\']\n# Replace each character with an empty string\nfor char in chars_to_remove:\n    correct_apps[\'Installs\'] = correct_apps[\'Installs\'].apply(lambda x: x.replace(char, \'\'))\n# Convert col to int\ncorrect_apps[\'Installs\'] = correct_apps[\'Installs\'].astype(int)\n   \n\ndef test_pandas_loaded():\n    assert (\'pandas\' in globals() or \'pd\' in globals()), "pandas is not imported."\n\ndef test_installs_plus():\n    assert \'+\' not in apps[\'Installs\'], \\\n    \'The special character "+" has not been removed from Installs column.\' \n    \ndef test_installs_comma():\n    assert \',\' not in apps[\'Installs\'], \\\n    \'The special character "," has not been removed from the Installs column.\'\n    \ndef test_installs_numeric():\n    assert isinstance(apps[\'Installs\'][0], np.int64), \\\n    \'The Installs column is not of numeric data type (int).\'\n    \ndef test_q1_app_category_info_columns():\n    \n    # when DataFrame in MultiIndex\n    if \'BEAUTY\' in app_category_info.index:\n        assert all(x in app_category_info.columns for x in [\'Number of apps\', \'Average price\', \'Average rating\']), \\\n        "Some columns are missing or incorrectly named in your app_category_info DataFrame. Make sure there are 4 columns named: \'Category\', \'Number of apps\', \'Average price\', \'Average rating\'."\n    else:\n        "Some columns are missing or incorrectly named in your app_category_info DataFrame. Make sure there are 4 columns named: \'Category\', \'Number of apps\', \'Average price\', \'Average rating\'."\n\ndef test_q1_app_category_info_app_count():\n    \n    if \'Number of apps\' in app_category_info.reset_index().columns:\n        correct_app_category_info = correct_apps.groupby([\'Category\']).agg({\'App\':\'count\', \'Price\': \'mean\', \'Rating\': \'mean\'}).reset_index()\n        correct_app_category_info = correct_app_category_info.rename(columns={"App": "Number of apps", "Price": "Average price", "Rating": "Average rating"})\n        correct_app_count = correct_app_category_info[\'Number of apps\']\n\n        # convert to single index and compare\n        app_count = app_category_info.reset_index().sort_values(by=\'Category\')[\'Number of apps\']\n        assert correct_app_count.equals(app_count),\\\n        "The aggregate function used to calculate \\"Number of apps\\" is incorrect."\n    \n    else:\n        assert False, "\\"Number of apps\\" column is missing in your app_category_info DataFrame."\n\n    \ndef test_q1_app_category_info_avg_price():\n\n    if \'Average price\' in app_category_info.reset_index().columns:\n        correct_app_category_info = correct_apps.groupby([\'Category\']).agg({\'App\':\'count\', \'Price\': \'mean\', \'Rating\': \'mean\'}).reset_index()\n        correct_app_category_info = correct_app_category_info.rename(columns={"App": "Number of apps", "Price": "Average price", "Rating": "Average rating"})\n        correct_app_count = correct_app_category_info[\'Average price\']\n\n        # convert to single index and compare\n        app_count = app_category_info.reset_index().sort_values(by=\'Category\')[\'Average price\']\n        assert correct_app_count.equals(app_count),\\\n        "The aggregate function used to calculate \\"Average price\\" is incorrect."\n    \n    else:\n        assert False, "\\"Average price\\" column is missing in your app_category_info DataFrame."\n\ndef test_q1_app_category_info_avg_rating():\n    \n    if \'Average rating\' in app_category_info.reset_index().columns:\n        correct_app_category_info = correct_apps.groupby(\'Category\').agg({\'App\':\'count\', \'Price\': \'mean\', \'Rating\': \'mean\'}).reset_index()\n        correct_app_category_info = correct_app_category_info.rename(columns={"App": "Number of apps", "Price": "Average price", "Rating": "Average rating"})\n        correct_app_count = correct_app_category_info[\'Average rating\']\n\n        # convert to single index and compare\n        app_count = app_category_info.reset_index().sort_values(by=\'Category\')[\'Average rating\']\n        assert correct_app_count.equals(app_count),\\\n        "The aggregate function used to calculate \\"Average rating\\" is incorrect."\n    \n    else:\n        assert False, "\\"Average rating\\" column is missing in your app_category_info DataFrame."\n\n# def test_reviews_loaded():\n#     assert (correct_reviews.equals(reviews)), "The dataset was not read correctly into reviews."\n\ndef test_q2_finance_apps():\n    correct_finance_apps = correct_apps[(correct_apps[\'Type\'] == \'Free\') & (correct_apps[\'Category\'] == \'FINANCE\')][\'App\']\n    \n    # if App column is the index\n    if top_10_user_feedback.index.name == \'App\': \n        finance_apps = top_10_user_feedback.index\n        assert(set(finance_apps).issubset(set(correct_finance_apps))),\\\n        "You have not selected the free finance apps correctly. Check your answer again."\n    else:\n        finance_apps = top_10_user_feedback[\'App\']\n        assert(set(finance_apps).issubset(set(correct_finance_apps))),\\\n        "You have not selected the free finance apps correctly. Check your answer again."\n\n\ndef test_q2_top_10():\n    assert(len(top_10_user_feedback) == 10), "You have selected more than 10 apps. Please select only top 10 apps with highest average sentiment score."\n    \n\ndef test_q2_sorted():\n    correct_finance_apps = correct_apps[(correct_apps[\'Type\'] == \'Free\') & (correct_apps[\'Category\'] == \'FINANCE\')]  \n    correct_merged_df = pd.merge(correct_finance_apps, correct_reviews, on = "App", how = "inner")\n    \n    correct_app_sentiment_score = correct_merged_df.groupby(\'App\').agg({\'Sentiment Score\': \'mean\'}).reset_index()\n    correct_sorted_apps = correct_app_sentiment_score.sort_values(by = \'Sentiment Score\', ascending = False)[:10]\n\n    # if App column is the index\n    if top_10_user_feedback.index.name == \'App\': \n        sorted_apps = top_10_user_feedback.index\n        assert(list(sorted_apps) == list(correct_sorted_apps[\'App\'])),\\\n        "You have not sorted top_10_user_feedback correctly. Make sure to sort your DataFrame on Sentiment Score from highest to lowest (ie - in decreasing order)."\n    else: \n        sorted_apps = top_10_user_feedback[\'App\']\n        assert(list(sorted_apps) == list(correct_sorted_apps[\'App\'])),\\\n        "You have not sorted top_10_user_feedback correctly. Make sure to sort your DataFrame on Sentiment Score from highest to lowest (ie - in decreasing order)."\n\n\ndef test_q2():\n    \n    correct_finance_apps = correct_apps[(correct_apps[\'Type\'] == \'Free\') & (correct_apps[\'Category\'] == \'FINANCE\')]  \n    correct_merged_df = pd.merge(correct_finance_apps, correct_reviews, on = "App", how = "inner")\n    \n    correct_app_sentiment_score = correct_merged_df.groupby(\'App\').agg({\'Sentiment Score\': \'mean\'}).reset_index()\n    correct_top_10_user_feedback = correct_app_sentiment_score.sort_values(by = \'Sentiment Score\', ascending = False).reset_index()[:10]\n\n    correct_app_sentiment_score_multiindex = correct_merged_df.groupby(\'App\').agg({\'Sentiment Score\': \'mean\'})\n    correct_top_10_user_feedback_multiindex = correct_app_sentiment_score_multiindex.sort_values(by = \'Sentiment Score\', ascending = False)[:10]\n    \n    # if App column is the index\n    if top_10_user_feedback.index.name == \'App\':\n        assert (correct_top_10_user_feedback_multiindex.equals(top_10_user_feedback)), "You have not computed top_10_user_feedback correctly. Some values are wrong."\n    else:\n        top_10_user_feedback_apps = top_10_user_feedback[\'App\']\n        top_10_user_feedback_sentiment_score = top_10_user_feedback[\'Sentiment Score\']\n        assert (list(top_10_user_feedback_apps) == list(correct_top_10_user_feedback[\'App\']) and\n               list(top_10_user_feedback_sentiment_score) == list(correct_top_10_user_feedback[\'Sentiment Score\'])), "You have not computed top_10_user_feedback correctly. Some values are wrong."')

