
# custom environment variables
import env


def ModelPredictor(text: str) -> list:
    loaded_model = env.MODEL
    return loaded_model.predict_proba([text])


def ProcessData(text):
    category = ['Data Scientist', 'Database Administrator', 'Java Developer', 'Network Administrator',
                'Project Manager', 'Python Developer', 'Security Analyst', 'Software Developer',
                'Systems Administrator', 'Web  Developer']

    model_result = ModelPredictor(text)
    model_result = list(map(list, model_result))[0]

    context = {}
    for i in range(len(model_result)):
        if model_result[i] > 0:
            context.update({category[i]: model_result[i]*100})

    factor1 = sum([x*x for x in context.values()]) / 100
    factor2 = (1 / len(context))*100
    relative_score = (((factor1 / 100) * 70) + ((factor2 / 100) * 30))

    print(relative_score)

    if relative_score < env.ALLOWED_ACCURACY:
        return {
            "score": 0
        }

    return {
        "score": relative_score,
        "context": context
    }


if __name__ == '__main__':
    testcase = """Pranali Raul BSc. Computer Science PROFILE SUMMARY • Seeking an entry -level opportunity with an esteemed organization where I can enhance my skills and enhance learning in the field of work. • Hardworking and capable of mastering technologies. ACADEMIC DETAILS • Pursuing BSc. Computer Science from R.J College of Arts, Science and Commerce. • HSC(Science) from SIES College in 2018 with 72.77% • SSC from Shivaji Vidyalaya High School in 2016 with 85.80% CERTIFICATE National Service Scheme (NSS Volunteer) Actively participated in Volunteering to social activities like Tree Plantation, HEADSUP awareness drives, Cleaning camps, Pulse Polio Immunization etc. MS-CIT (Completed in June 2014) Percentage – 94. Address: Room no.9, Mauli Prasad Society, Kurla Kajupada, Mumbai- 400072. Phone: +91 8108472615 Email: pranaliraul3@gmail.com WORK EXPERIENCE Fresher. PROJECT • Project Name Online Unused Medicine Donation. • Description The project ‘Online Unused Medicine Donation’ is a website created using Angular and Node.js Technical Skills • Database – SQL Server • Coding Language – , Basics of C++ Python, Angular, JavaScript, HTML, Java HOBBIES Acquiring New Technical Knowledge. PERSONAL DETAILS • Date of Birth : 27th June, 2001. • Nationality : Indian. • Marital Status : Single. • Languages Known : English, Hindi & Marathi. """
    testcase2 = """AAKASH PRAJAPATI Phone: +91 9324344591 Email: aakash345.ap@gmail.com Address: Laxmi Bai chawl ghaswala compound pipe line, Room No D-20, Kajupada, Kurla (West), Mumbai - 400072 Portfolio: https://akkytalk.web.app/ Key Skill Area: Frontend developer, Web Designing, Software Development, Digital Marketing OBJECTIVE My aim is to pursue a rewarding career as Frontend developer in React.js and software development where my varied skills can be profitably utilized to achieve corporate objectives and my personal goals. SKILL SET Operating Systems: Windows 7, 8 and 10 IT Skills: React.js, Redux, Firebase, Stripe, Material-UI, C, C++, Java, .NET, DBMS Soft Skills: Communication Skills, Problem Solving, Teamwork EDUCATIONAL QUALIFICATION Degree Board/University Institute Passed Percentage/ CGPA BSc IT Mumbai University K.J Somaiya College of Science and Commerce 2019 62% XII Maharashtra State Board SK Somaiya Vinay Mandir Junior college 2016 60% X Maharashtra State Board Yogiraj Shri Krishana Vidyalaya 2014 87.4% ADDITIONAL WORK ⚫ Project on Online Re-selling Book Store The idea of re-selling books came from the fact that people do not use them once finished while others could not afford one. We thought of buying those finished books and providing them at a cheaper price through our website. The website is designed using Microsoft Visual Studio 2017. ⚫ React Project: 1) amazon-clone with fully e-commerce functionality Link: https://clone-7bbca.web.app/ 2) WhatsApp-clone Link: https://whats-app-clone-568d1.web.app/ 3) Instagram-clone Link: https://instagram-clone-d5dcc.web.app/ • Technologies used in these projects are: React.js, Redux, Material-UI, Firebase for cloud functions and hosting, stripe for payment ⚫ Projects without hosting: YouTube-clone, burger-builder, tik-tok-clone ⚫ Fundamental of Digital Marketing (Google Digital Garage) Learnt various ways to marketing online like SEM marketing, Email marketing, SEO, display advertisement, social media marketing and growing brand. PERSONAL DETAILS Date of Birth: 17th April, 1999 Marital Status: Single Gender: Male Nationality: Indian Languages Known: English, Hindi Hobbies: Reading, Learning, Music, Playing Cricket Aakash Prajapati Mumbai"""
    testcase3 = """Charles K. Sorensen, MTA Python Developer 3689 Parrish Avenue Victoria, TX 77901 830-994-8344 charlesksorensen@gmail.com linkedin.com/in/charlessorensen Summary Motivated PCPP1 and MTA-certified Python developer and professional scrum master with 6+ years of experience. Inclined to bring effectiveness to TechNo’s front-end development. Driven by passion and innovation, designed and introduced a new and IAC-award-worthy feature to the MailSent tool. Highly skilled in Python coding and scripting, Django framework, and communication. Experience Python Developer PyMe, Victoria, TX March 2015-present Handled programming tasks for and maintained 7 internal websites with a high success rate (97%) in product update deployment. Worked on high-impact projects, e.g., content aggregator and expense tracker, delivering solutions with lower than 20% code churn. Developed a marketing lead MySQL database, collecting, categorizing, and filtering leads from various stakeholders, i.e., www, social media channels, or newsletters. Led sprint planning meetings and divided tasks between a 15-person project team. Tutored at three high schools every year, teaching young kids how to code in Python. Key achievement: Designed a new feature for the company’s email marketing tool (MailSent) in 7 Active Days, contributing to the marketing department’s win in the IAC award competition in the Best Email Message Campaign category. Data Scientist PyMe, Victoria, TX April 2012-February 2015 Automated and optimized collecting data using SQL, reaching over a 35% system’s response time boost. Collaborated cross-departmentally on RPA to streamline issue management and migrate the current environments to the cloud, reducing the investment risk by 48%. Education 2011 M.S. in Engineering University of Texas, Austin, TX Skills Python, JavaScript, CSS3, HTML5, SQL ORM libraries Web frameworks: Django MVC and MVT Architecture Design skills Problem-solving skills Communication skills Data visualization Agile frameworks Courses and Certificates PCPP1 – Certified Professional in Python MTA 98-381 – Microsoft Technical Associate PSM II Assessment Certificate – Professional Scrum Master Conferences PyCon, every-year attendee since 2018 DjangoCon, 2020"""
    testcase4 = """Adam Alston San Francisco, CA | (919) 770-0827 | aalston9@gmail.com linkedin.com/in/adam-alston | github.com/adamalston SKILLS Languages: Python, JavaScript, C, Java, TypeScript, C++, SQL, Swift Technologies: AWS, CI/CD, Docker, Jira, Kubernetes, Linux, Node.js, React, Spring, TCP/IP EXPERIENCE Software Engineer | IBM | US Jan 2021 - Present ● IBM Cloud and Cognitive Software DevOps Engineer | Insight | San Francisco, CA | git.io/JUznd Sep 2020 - Dec 2020 ● Engineered Overwatch, an AWS monitoring tool using Docker, Prometheus, and Grafana, that can be set up in minutes to track CI/CD pipelines in the cloud. ● Collaborated on KubeSat, an infrastructure tool that manually deploys Kubernetes to AWS using Terraform and Ansible for more control over the cluster(s). UNC Computer Science | Chapel Hill, NC Cybersecurity Researcher | git.io/JUEKK Jan 2020 - Aug 2020 ● Cross-validated password strength on a 7000-point dataset and discovered that roughly 35% of passwords can be trivially defeated, identifying ineffective password security practices. ● Architected 5 vulnerability exploits in Linux VMs to demonstrate modern attack vectors. ● Explored online privacy in relation to the 120% growth in digital fingerprinting since 2016. Accessibility Researcher | git.io/JUdPP Jan 2019 - Dec 2019 ● Created web apps to help pediatric patients affected by brain injuries. ● Developed Summarizer, a full stack web app and browser extension to consolidate web articles by 75-99% into a digestible summary with one click. ● Created voice-controlled Poker with audio feedback for visually impaired players, and transitioned 4 games to keyboard controls for players with limited mobility. QA Engineer | Self-Employed | Remote Sep 2015 - July 2019 ● Conducted product design reviews for 12 apps during the SDLC and documented 200+ software defects involving program content, functionality, and output using Jira. ● Automated manual testing protocols with Jest and XCTest by writing more than 100 tests. PROJECTS COVID-19 Dashboard | React | git.io/JUEKp April 2020 ● Built a COVID-19 dashboard and map to display real-time statistics on the pandemic. ● Integrated data from 4 sources to create a map with information for 250+ countries. Pokémon Go Map | JavaScript, Python | git.io/JUE6J Sep 2016 ● Collaborated on an app that allowed 10,000+ players to gain a live game visualization. ● Monitored Google Maps API integration and fixed street-level localization errors. EDUCATION B.S. | Computer Science | University of North Carolina - Chapel Hill"""

    print("-------- pranali ------")
    ProcessData(testcase)

    print("-------- akash ------")
    ProcessData(testcase2)

    print('--------- pro python developer -------------')
    ProcessData(testcase3)

    print('--------- IBM software engineer -------------')
    ProcessData(testcase4)

    print('----------spam text 1------------')
    ProcessData('ddssadasd')

    print('----------spam text 2------------')
    ProcessData('Hello World')

    print('----------spam text lorem------------')
    ProcessData("""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum""")

    print('----------spam text article------------')
    ProcessData("""Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.""")

    print('----------spam text 5 -------------')
    ProcessData("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
