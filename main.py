import os
from keras.models import load_model
import numpy as np
import cv2

lung_cancer = load_model("lung_cancer_v2")
brain_tumor = load_model("brain_tumor_v1")
breast_cancer = load_model("breast_cancer_v1")
# NLP for Symptom Analysis
#Symptom Matrix
import pickle as pkl
with open("symptoms.pkl","rb") as file:
    symp_dict = pkl.load(file)
symptom = [] #A symptom matrix from the front end questionnaire
#Example of symptom symptoms = set([' skin_rash',' nodal_skin_eruptions','fever',0,0,0,0,0,0,0])

#The medical conditions we can identify as of now
# 'Fungal infection': [],
#  'Allergy': [],
#  'GERD': [],
#  'Chronic cholestasis': [],
#  'Drug Reaction': [],
#  'Peptic ulcer diseae': [],
#  'AIDS': [],
#  'Diabetes ': [],
#  'Gastroenteritis': [],
#  'Bronchial Asthma': [],
#  'Hypertension ': [],
#  'Migraine': [],
#  'Cervical spondylosis': [],
#  'Paralysis (brain hemorrhage)': [],
#  'Jaundice': [],
#  'Malaria': [],
#  'Chicken pox': [],
#  'Dengue': [],
#  'Typhoid': [],
#  'hepatitis A': [],
#  'Hepatitis B': [],
#  'Hepatitis C': [],
#  'Hepatitis D': [],
#  'Hepatitis E': [],
#  'Alcoholic hepatitis': [],
#  'Tuberculosis': [],
#  'Common Cold': [],
#  'Pneumonia': [],
#  'Dimorphic hemmorhoids(piles)': [],
#  'Heart attack': [],
#  'Varicose veins': [],
#  'Hypothyroidism': [],
#  'Hyperthyroidism': [],
#  'Hypoglycemia': [],
#  'Osteoarthristis': [],
#  'Arthritis': [],
#  '(vertigo) Paroymsal  Positional Vertigo': [],
#  'Acne': [],
#  'Urinary tract infection': [],
#  'Psoriasis': [],
#  'Impetigo': []
from nltk.corpus import stopwords
stop_words = list(set(stopwords.words('english')))
remarks = "" #The remark that the user will provide in the UI
from nltk import word_tokenize
tokens = word_tokenize(remarks)
tokens = [token for token in tokens if token.lower() not in stop_words]
symptom.append(tokens)
symptom = set(symptom)
#Calculating the Hessian Matrix to find the similary of our symptom to a medical condition
potential = []
for key in symp_dict.keys():
    chances = []
    for syms in symp_dict[key]:
        syms = set(syms)
        similarity = len(symptom.intersection(syms)) / len(symptom.union(syms))
        if similarity >=0.75: #Highlight a medical condition if 75% match
            chances.append(similarity*100)
    if len(chances) > 0:
        potential.append((key,max(chances)))

#Highlighted Medical Conditions
print(potential)
# AI Models
# U - Net : Lung Cancer and Brain Tumor Detection
# ResNet 50: Early stage breast cancer detection in low risk patients and Breast cancer detection from MRI
path = "" #mongodb path to the image provided by the user
img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
#Loading the vector representation of all the images in various models
Lung_Imgs = np.load("LungsImg_vectors.npy")
Brain_Imgs = np.load("BrainImg_vectors.npy")
Breast_Imgs = np.load("BreastImg_vectors.npy")
from img2vec_pytorch import Img2Vec
vectorizer = Img2Vec(False,model="resnet-18")
type = input() #can be lung, brain, breast scans
if type == "lung":
    img = cv2.resize(img,(460,460))
    vector = vectorizer.get_vec(img)
    label = np.argmax(lung_cancer.predict(img))
    distance = []
    #show related scans
    for vec in Lung_Imgs:
        dis = np.linalg.norm(vector,vec)
        distance.append((vec,dis))
    distance.sort(key=distance[1],reverse=True)
    top_related_imgs = distance[0:5]
    for img in top_related_imgs:
        im = cv2.imshow("Image",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
elif type=="brain":
    img = cv2.resize(img,(260,260))
    vector = vectorizer.get_vec(img)
    label = np.argmax(brain_tumor.predict(img))
    distance = []
    #show related scans using Eculidean distance to find scans that are related to ecah other
    for vec in Brain_Imgs:
        dis = np.linalg.norm(vector,vec)
        distance.append((vec,dis))
    distance.sort(key=distance[1],reverse=True)
    top_related_imgs = distance[0:5]
    for img in top_related_imgs:
        im = cv2.imshow("Image",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

else:
    img = cv2.resize(img,(256,256))
    vector = vectorizer.get_vec(img)
    label = np.argmax(breast_cancer.predict(img))
    distance = []
    #show related Scans
    for vec in Breast_Imgs:
        dis = np.linalg.norm(vector,vec)
        distance.append((vec,dis))
    distance.sort(key=distance[1],reverse=True)
    top_related_imgs = distance[0:5]
    for img in top_related_imgs:
        im = cv2.imshow("Image",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()