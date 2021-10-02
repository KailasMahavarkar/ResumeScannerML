# custom environment variables
import re
from flask.json import jsonify
import env
import time

def requirements(req):
    labels = {}
    idx = env.MODEL.predict_proba([req])[0] 
    for i, item in enumerate(idx):
        if item != 0:
            labels[i] = item
    return labels


def screen(probs: list, reqs: list) -> tuple:
    """
        probs -> probability
        reqs  -> set of requirements
    """
    resume_score = 0
    for item in probs.keys():
        if item in reqs.keys():
            resume_score += probs[item]
        
    if resume_score > 0:
        return True, resume_score
    return False, 0



def RankResume(text):
    resumes = []
    final_resume = []
    for index,row in env.CLEAN_DF.iterrows():
        evaluated = eval(row['Probability Distribution'])
        values = screen(evaluated, reqs=requirements(text))

        if values[0]:
            resumes.append((values[1], int(index), row['Input']))

    
    ranked_resume = sorted(resumes, reverse=True)

    for x in ranked_resume:
        if len(final_resume) <= env.FETCH_NUM:
            final_resume.append({"id": x[1], "rank": x[0], "resumetext": x[2]})

    return final_resume



def singleResume(row):
    category = ['Data Scientist ', 'Database Administrator', 'Java Developer', 'Network Administrator',
                'Project Manager', 'Python Developer', 'Security Analyst', 'Software Developer',
                'Systems Administrator', 'Web Developer']


    if row <= len(env.CLEAN_DF):
        singleDF = env.CLEAN_DF.iloc[[row]].values
        singleDF[0][-1] = eval(singleDF[0][-1])
        id, role, resumetext, roleref, probability =  list(singleDF[0])

        updated_category = {}

        for k, v in probability.items():
            updated_category.update({category[int(k)]: v })

        return {
            "id": id,
            "role": roleref,
            "resumetext": resumetext,
            "probability":  updated_category
        }
    return {}

    


if __name__ == '__main__':
    print(singleResume(800))