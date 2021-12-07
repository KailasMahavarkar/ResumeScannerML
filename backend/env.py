import os
import pickle
import pandas as pd
import random

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
ASSET_PATH = os.path.join(ROOT_PATH, 'Atemp')
STORE_PATH = os.path.join(ROOT_PATH, 'Storage')
MODEL_PATH = os.path.join(STORE_PATH, 'MODEL.sav')

def jp(path1, path2):
    return os.path.join(path1, path2)


MODEL = pickle.load(open(MODEL_PATH, 'rb'))

CLEAN_DF = pd.read_csv(jp(STORE_PATH,'cleaned_resumes.csv'), encoding='cp1252')
RESUME_DF = pd.read_csv(jp(STORE_PATH,'linkedin_dataset.csv'), encoding='cp1252')

MODE = 'dev'

FETCH_NUM = 50

ALLOWED_ACCURACY = 25


TESTCASE = '''Use Java technologies to build web applications for client-server environments.
Use expertise in Software Development Life Cycle (SDLC) and core Java technologies to create desktop applications that meet client requirements.
Develop customized, interactive user interfaces using JavaScript, HTML and CSS. I was awarded the Eclipse Award in 2018 for Best Java Application.
Supervise a team of Java Developers, motivate them to meet team goals, collaborate to improve user experiences and provide training to new employees and interns.
Merge my Java-based code and the code created by other Java Developers with applications written in C++ and HTML5.
Use debugging skills to improve the quality of code and improve application performance.Java DeveloperO'Hare ProgrammingAugust 2016
July 2017Responsibilities:
Built, integrated and modified web applications according to client specifications.
Used JavaScript to develop interactive user interfaces (UIs) that provided user experiences that exceeded client expectations and met key performance indicators (KPIs).
Used Enterprise JavaBeans (EJB) to create large applications for key company clients. I received several commendations from the management for my web applications.
Worked in a team of web developers, designers and other IT personnel to meet team goals and improve business outcomes.
Assisted in the onboarding of new web developers.Java Developer intern
Litchfield's Smart Apps
Responsibilities:
Used Java and J2EE technologies to add functionalities to existing applications under supervision.
Learned to use JDBC and write SQL queries.
Used the Hibernate and Spring frameworks to assist senior Java Developers in application development.
Gained practical experience in working with a small team of developers and designers. Learned how to settle conflicts with team members amicably.
Assisted senior colleagues in preparing for client presentations.
'''




REQ = """Any graduate, Should have good verbal and written communication,

· Hands on experience on CMS is mandatory.
· It's a semi technical role.
· Its Work from office hence RTO confirmation is mandate
· CTC: 30000 max
· Location: MDC 2
· CL Level: 12
· Shift: 1:00 PM to 11:00 Pm & can rotate in future

For more details call Priyanka 9538906671

Job Type: Full-time

Salary: ₹25,000.00 - ₹30,000.00 per month

Schedule:
Rotational shift
Education:

Bachelor's (Preferred)
Experience:

CMS: 1 year (Preferred)
HTML5: 1 year (Preferred)
Work Remotely:

Temporarily due to COVID-19"""