from .models import get_predictor


question_text_1 = "I\u2019ve had chronic migraines for four years and they just keep getting worse.  It\u2019s to the point now that I have between 20 and 25 migraines a month. I\u2019ve had a CT scan which came back normal, I\u2019ve been on amitriptyline, topamax, and propranolol to try to prevent the migraines and I\u2019ve used maxalt and sumatriptan to break migraines at onset. I haven\u2019t had consistent relief with any medication, the 3 prophylactics only helped a few of my symptoms and the maxalt/ sumatriptan only succeeded in breaking my migraines about 25% of the time.  I just want to know if anyone can help me figure out what is wrong with me. I\u2019ll list my symptoms below.  -Sharp shooting pain shooting down jawline from mandibular joint and across cheekbones. Usually on only one side of my face but it changes sides randomly.  -Extreme pain in eyes, sensitivity to light and movement. See flashes of light even when eyes are closed.  -sharp pain starting at base of head/top of neck that runs up head and causes pain in eyes.  -Sharp pain in ears usually accompanied by ringing  Dizziness and nausea, occasionally vomiting  Muscle spasms, usually in hands or face  All pain worsens with any change in position; standing, sitting, rolling over while lying down.  Usually I\u2019ll know that I\u2019m going to get a migraine because it starts with the shooting face pain or the eye pain. The 3 prophylactics helped the facial pain but didn\u2019t reduce the number of migraines I had per month and they all gave me pretty bad side effects.  Side effects from medication  Topamax: felt drunk, nauseous, twitchy  Amitriptyline: extreme fatigue even into the next day when taken at night, confusion, balance issues, muscle spasms  Propranolol: nausea, hair loss, fatigue"  #@param {type:"string"}
question_text_2 = "I was running for like an hour, and now I'm feeling pain in my right anckle only"  #@param {type:"string"}


predictor = get_predictor()

search_similarity_by = 'answer'  #@param ['answer', "question"]

number_results_toReturn = 10 #@param {type:"number"}

answer_only = True #@param ["False", "True"] {type:"raw"}

returned_results = predictor.predict( question_text_1 ,
                  search_by=search_similarity_by, topk=number_results_toReturn, answer_only=answer_only)

print(question_text_1)
for jk in range(len(returned_results)):
    print("Result ", jk+1)
    print(returned_results[jk])
    print('')

returned_results = predictor.predict( question_text_2 ,
                  search_by=search_similarity_by, topk=number_results_toReturn, answer_only=answer_only)

print(question_text_1)
for jk in range(len(returned_results)):
    print("Result ", jk+1)
    print(returned_results[jk])
    print('')
