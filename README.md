# Refractor (for Customer Churn Prediction)

This is the CML port of the Refractor prototype which is part of the [Interpretability
report from Cloudera Fast Forward Labs](https://clients.fastforwardlabs.com/ff06/report).

## Setup:  
Admin->Engine  
Engine Profile: 2 CPU / 8GB Memory (Add)  

A custom Docker engine has been created (see utils/Dockerfile and utils/build-engine.sh) to simplify this demo.  
Admin->Engine->Engine Images  
Description: TKO Demo  
Repository:Tag: docker.io/cdsw/engine:11-cml1.4-tko  
Edit->New Editor
Name: RStudio  
Command: /usr/sbin/rstudio-server start  
New Editor
Name: Jupyter Notebook	 
Command: /usr/local/bin/jupyter-notebook --no-browser --ip=127.0.0.1 --port=${CDSW_APP_PORT} --NotebookApp.token= --NotebookApp.allow_remote_access=True --log-level=ERROR  

Start a Python3 Session (at least 8gb memory) and run **utils/setup.py**  
This will setup the project for Models and Experiments to build and also (in case you are not using a custom engine) install all requirements for the code below. 


## CML Applications: Train and inspect a new model locally

This project uses the Applications feature of CML (>=1.2) and CDSW (>=1.7) to instantiate a UI frontend for visual interpretability and decision management.  

### Train a predictor model
A model has been pre-trained and placed in the models directory.  
Start a Python 3 Session with at least 8GB of memory and __run the utils/setup.py code__.  This will create the minimum setup to use existing, pretrained models.  

If you want to retrain the model start a Python 3 Session and run the 3_DS_train.py code to train a new model.  

The model artifact will be saved in the models directory named after the datestamp, dataset and algorithm (ie. 20191120T161757_ibm_linear). The default settings will create a linear regression model against the ibm telco dataset. However, the code is vary modular and can train multiple model types against essentially any tabular dataset (see below for details).  

### Deploy Predictor and Explainer models
Go to the **Models** section and create a new predictor model.   The sample features below should predict a 3.9% churn probability.
* **Name**: Predictor
* **Description**: Predict customer churn
* **File**: deploy_model.py
* **Function**: predict
* **Input**: 
`{"StreamingTV":"No","MonthlyCharges":70.35,"PhoneService":"No","PaperlessBilling":"No","Partner":"No","OnlineBackup":"No","gender":"Female","Contract":"Month-to-month","TotalCharges":1397.475,"StreamingMovies":"No","DeviceProtection":"No","PaymentMethod":"Bank transfer (automatic)","tenure":29,"Dependents":"No","OnlineSecurity":"No","MultipleLines":"No","InternetService":"DSL","SeniorCitizen":"No","TechSupport":"No"}`  
* **Kernel**: Python 3

If you created your own model (see above)
* Click on "Set Environment Variables" and add:
  * **Name**: MODEL_NAME
  * **Value**: 20191120T161757_ibm_linear  **your model name from above**
  Click "Add" and "Deploy Model"

Create a new Explainer model.

* **Name**: Explainer
* **Description**: Explain churn prediction
* **File**: deploy_model.py
* **Function**: explain
* **Input**: `{"StreamingTV":"No","MonthlyCharges":70.35,"PhoneService":"No","PaperlessBilling":"No","Partner":"No","OnlineBackup":"No","gender":"Female","Contract":"Month-to-month","TotalCharges":1397.475,"StreamingMovies":"No","DeviceProtection":"No","PaymentMethod":"Bank transfer (automatic)","tenure":29,"Dependents":"No","OnlineSecurity":"No","MultipleLines":"No","InternetService":"DSL","SeniorCitizen":"No","TechSupport":"No"}`
* **Kernel**: Python 3

If you created your own model (see above)
* Click on "Set Environment Variables" and add:
  * **Name**: MODEL_NAME
  * **Value**: 20191120T161757_ibm_linear  **your model name from above**
  Click "Add" and "Deploy Model"

In the deployed Explainer model -> Settings note (copy) the "Access Key" (ie. mukd9sit7tacnfq2phhn3whc4unq1f38)


### Instatiate the flask UI application
From the Project level click on "Open Workbench" (note you don't actually have to Launch a session) in order to edit a file.
Select the flask/single_view.html file and **paste the Access Key from your Explainer model in at line 19**. 
Save and go back to the Project.  

Go to the **Applications** section and select "New Application" with the following:
* **Name**: Visual Churn Analysis
* **Subdomain**: churn-prediction
* **Script**: flask_app.py
* **Kernel**: Python 3
* **Engine Profile**: 1vCPU / 2 GiB Memory  

If you created your own model (see above)
* Add Environment Variables:  
  * **Name**: MODEL_NAME  
  * **Value**: 20191120T161757_ibm_linear  **your model name from above**  
  Click "Add" and "Deploy Model"  
  
  
After the Application deploys, click on the blue-arrow next to the name.  The initial view is a table of rows selected at  random from the dataset.  This shows a global view of which features are most important for the prediction made.  

Clicking on any single row will show a "local" interpretabilty of a particular instance.  Here you 
can see how adjusting any one of the features will change the instance's prediction.  

## Additional options
By default this code trains a linear regression model for the ibm telco dataset.  
There are other datasets and other model types as well.  Look at run_experiment.py for examples or set the Project environment variables to try other datasets and models:  
Name              Value  
DATASET     ibm (default) | breastcancer | iris  
MODEL_TYPE  linear (default) | gb | nonlinear | voting  


**NOTE** that not all of these options have been fully tested so your mileage may vary.
