from flask import Flask, render_template, redirect, url_for, request
import numpy as np
import pandas as pd
import stats
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('base_file.html')

#DESCRIPTIVE ANALYTICS
@app.route('/central_tendency/', methods=['GET','POST'])
def central_tendency():
    return render_template('central_tendency.html')

@app.route('/central_upload/', methods=['GET','POST'])
def central_upload():
    #Request method contains all the data
    if request.method == "POST":
        #fetches the file from the request object
        data_file = request.files['data_file']
        #get the data from csv file
        data = pd.read_csv(data_file)
        x = data['x'].values
        x1 = data['x1'].values
        xmean = np.mean(x)
        x1mean = np.mean(x1)
        xmed = np.median(x)
        x1med = np.median(x1)
        x_mode = stats.mode(x)
        x1mode = stats.mode(x1)
        return render_template('central_upload.html', data=data, rows=len(data), xmean=xmean, xmean1=x1mean,
        xmed=xmed, xmed1=x1med, x_mode=x_mode, x1mode=x1mode, xs=sum(x), xs1=sum(x1))

@app.route('/measures_of_variability/', methods=['GET','POST'])
def measures_variability():
    return render_template('measures_of_variability.html')

@app.route('/measures_upload/', methods=['GET','POST'])
def measures_upload():
    #Request method contains all the data
    if request.method == "POST":
        #fetches the file from the request object
        data_file = request.files['data_file']
        #get the data from csv file
        data = pd.read_csv(data_file)
        x = data['x'].values
        x1 = data['x1'].values
        xmin = min(x)
        x1min = min(x1)
        xmax = max(x)
        x1max = max(x1)
        xran = xmax - xmin
        x1ran = x1max - x1min
        xp1 = np.percentile(x, 25)
        xp2 = np.percentile(x, 50)
        xp3 = np.percentile(x, 75)
        x1p1 = np.percentile(x1, 25)
        x1p2 = np.percentile(x1, 50)
        x1p3 = np.percentile(x1, 75)
        return render_template('measures_upload.html', data=data, rows=len(data), xs=sum(x), xs1=sum(x1),
        xran=xran, xran1=x1ran, xmin=xmin, xmin1=x1min, xmax=xmax, xmax1=x1max, xiqr=(xp3-xp1), xiqr1=(x1p3-x1p1),
        xp1=xp1, xp2=xp2, xp3=xp3, x1p1=x1p2, x1p2=x1p2, x1p3=x1p3)

if __name__=='__main__':
    app.run(debug=True)
