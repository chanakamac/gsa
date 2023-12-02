from flask import Flask, render_template, request
from pusher import Pusher
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
 
app = Flask(__name__)
  

@app.route('/')
def index():
    df = pd.read_csv('data/facebook-fact-check.csv')
  
    dataframe = pd.DataFrame(df)
    
    sharecount = dataframe.groupby(['date_published'])['share_count'].sum().reset_index()
      
    shareL = json.loads(json.dumps(list(sharecount['date_published'])))
    shareC = json.loads(json.dumps(list(sharecount['share_count'])))


    commentcount = dataframe.groupby(['date_published'])['comment_count'].sum().reset_index()
  
    commentL = json.loads(json.dumps(list(commentcount['date_published'])))
    commentC = json.loads(json.dumps(list(commentcount['comment_count'])))


    reactioncount = dataframe.groupby(['date_published'])['reaction_count'].sum().reset_index()
  
    reactionL = json.loads(json.dumps(list(reactioncount['date_published'])))
    reactionC = json.loads(json.dumps(list(reactioncount['reaction_count'])))


     
     
     
    return render_template('index.html', df=df.to_dict(orient='records'), data=shareC, labels=shareL, commentL=commentL, commentC=commentC, reactionL=reactionL, reactionC=reactionC)
 

if __name__ == '__main__':
	app.run(debug=True)
