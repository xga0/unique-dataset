# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 20:14:21 2020

@author: sgaox
"""

from flask import Flask, request, send_file

def uniqueDataset(ID):
    import pandas as pd
    
    house = pd.read_csv('https://raw.githubusercontent.com/xga0/unique-dataset/master/house.csv')
    house_sub = house.sample(n = 100, random_state = ID)
    return house_sub

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def udataset():
    if request.method == "POST":
        ID = int(request.form['ID'])
        df = uniqueDataset(ID)
        df.to_csv('house.csv', index = False)
        return send_file('house.csv',
                     mimetype = 'text/csv',
                     attachment_filename = 'house.csv',
                     as_attachment = True)
    
    return '''
        <html>
            <body>
                <p>Enter Your NJIT ID:</p>
                <form method="post" action=".">
                    <p><input name="ID" /></p>
                    <p><input type="submit" value="Download Your Dataset" /></p>
                </form>
            </body>
        </html>
    '''
    
if __name__ == "__main__":
    app.run(debug = True)
