## FETAL HEALTH TRACK USING DJANGO AND CRYPTOGRAPHY
#### PROBLEM DEFINITION
Health complications during the gestation period have evolved as a global issue. These complications sometimes result in the mortality of the fetus, which is more prevalent in developing and underdeveloped countries. The origin of machine learning (ML) algorithms in the healthcare domain have brought remarkable progress in disease diagnosis, treatment, and prognosis. This project assesses the influence of various factors measured through CTG to predict the health of the fetus through various machine learning algorithms. Many statistical techniques like regression , correlation etc. will be carried out to reveal the influence of the attributes on the fetal health. 

Designed and Developed a Web portal using a Django Web frame work along with various machine learning algorithms and Cryptographic algorithms.
#### PROJECT WORK FLOW
#### 1. Data Collection
* Kaggle : https://www.kaggle.com/datasets/andrewmvd/fetal-health-classification
* No. of Records: 2126
* No. of Attributes: 21
#### 2. Data Pre Processing
* Deleting redundant columns.
* Renaming the columns.
* Dropping duplicates.
* Cleaning individual columns.
* Remove the NaN values from the dataset
* Some Transformations
#### 3. Tools and Technologies used
*	FRONT END : HTML, CSS, JAVASCRIPT
*	WEB FRAME WORK : DJANGO
*	BACKEND: DJANGO MODELS
*	CRYPTOGRAPHY ALGORITHMS: MD5, AES
*	MACHINE LEARNING ALGORITHMS: RANDOM FOREST CLASSIFIERS
*	LANGUAGE: PYTHON
#### WORK FLOW DIAGRAM
![image](https://github.com/PRIYADHARSHINI-star/FETAL_PROJECT/assets/72924709/e0129f14-df11-4a2c-9558-be7280db7ebf)

#### WORKING OF DJANGO
Django is a Python framework that makes it easier to create web sites using Python. Django emphasizes reusability of components, also referred to as DRY (Don't Repeat Yourself), and comes with ready-to-use features like login system, database connection and CRUD operations (Create Read Update Delete).
Django follows the MVT design pattern (Model View Template).
* Model - The data you want to present, usually data from a database.
* View - A request handler that returns the relevant template and content - based on the request from the user.
* Template - A text file (like an HTML file) containing the layout of the web page, with logic on how to display the data.
#### 1. Django Models
The model provides data from the database. In Django, the data is delivered as an Object Relational Mapping (ORM), which is a technique designed to make it easier to work with databases. The most common way to extract data from a database is SQL. One problem with SQL is that you have to have a pretty good understanding of the database structure to be able to work with it. Django, with ORM, makes it easier to communicate with the database
without having to write complex SQL statements. The models are usually located in a file called models.py.
#### 2. Views
A view is a function or method that takes http requests as arguments, imports the relevant model(s), and finds out what data to send to the template, and returns the final result. The views are usually located in a file called views.py.
#### 3. Template
A template is a file where you describe how the result should be represented. Templates are often .html files, with HTML code describing the layout of a web page, but it can also be in other file formats to present other result.
#### 4. URLS
Django also provides a way to navigate around the different pages in a website. When a user requests a URL, Django decides which view it will send it to. This is done in a file called urls.py.
#### About Dataset
* No. of Dependent Variable : 1
*	No. of Independent Variable : 21
*	No. of Classes: 3
*	Classes : NORMAL SUSPECT , PATHOLOGICAL
*	Machine learning model : RANDOM FOREST CLASSIFIER

#### Feature Selection
![image](https://github.com/PRIYADHARSHINI-star/FETAL_PROJECT/assets/72924709/3f044cdb-9868-48a2-9361-ce97af84219c)

#### WEB PORTAL SCREENSHOTS
#### 1. Home Page
![image](https://github.com/PRIYADHARSHINI-star/FETAL_PROJECT/assets/72924709/5ed179d0-3e40-4cdd-a68b-3a6e15da4677)
![image](https://github.com/PRIYADHARSHINI-star/FETAL_PROJECT/assets/72924709/22bc440c-0520-40b4-9dc5-7a731f635659)
![image](https://github.com/PRIYADHARSHINI-star/FETAL_PROJECT/assets/72924709/6cffa6c9-fe96-4dd6-af77-7c4620494366)

#### 2. About Us Page
![image](https://github.com/PRIYADHARSHINI-star/FETAL_PROJECT/assets/72924709/746a86c4-f1c0-4911-98d0-5a2d21e2a3f6)
#### 3. Login and Register Page
![image](https://github.com/PRIYADHARSHINI-star/FETAL_PROJECT/assets/72924709/7f38f99d-8a73-43e7-8f20-640568fdb90c)
![image](https://github.com/PRIYADHARSHINI-star/FETAL_PROJECT/assets/72924709/c0427603-8907-4662-8c41-799343ce1a0c)
#### 4. Prediction Page
![image](https://github.com/PRIYADHARSHINI-star/FETAL_PROJECT/assets/72924709/67d12361-ffe9-4827-8c22-8f478c0d1e5f)
![image](https://github.com/PRIYADHARSHINI-star/FETAL_PROJECT/assets/72924709/a8330f6d-ef35-4157-908e-78121cfbd8c8)
![image](https://github.com/PRIYADHARSHINI-star/FETAL_PROJECT/assets/72924709/df0596f3-c7db-4766-8687-07ab44733c13)
#### 5. Contact Us Page
![image](https://github.com/PRIYADHARSHINI-star/FETAL_PROJECT/assets/72924709/e4085ad6-2b5f-4a42-9db0-7531a7d20e40)
#### 6. Models
![image](https://github.com/PRIYADHARSHINI-star/FETAL_PROJECT/assets/72924709/1ecc342d-b7b2-452a-8a1e-1ec8558c87d0)
![image](https://github.com/PRIYADHARSHINI-star/FETAL_PROJECT/assets/72924709/b2db908a-b6c9-44ce-88dd-a250a78891cb)
#### 7. Encrypted Data: AES ALGORITHM
![image](https://github.com/PRIYADHARSHINI-star/FETAL_PROJECT/assets/72924709/d319bf39-1e19-42c7-9a06-b180dd0f8692)
#### 8. LOGIN PAGE: MD5 ALGORITHM
![image](https://github.com/PRIYADHARSHINI-star/FETAL_PROJECT/assets/72924709/12b5b211-04ca-4f90-b475-05709191002f)
#### 9. Encryted Dataset
![image](https://github.com/PRIYADHARSHINI-star/FETAL_PROJECT/assets/72924709/d3f4c013-103a-464f-94d0-de8776a783d4)
#### 10. Model Performance
![image](https://github.com/PRIYADHARSHINI-star/FETAL_PROJECT/assets/72924709/46e954f1-14c8-4553-a54a-61559377f6cf)












