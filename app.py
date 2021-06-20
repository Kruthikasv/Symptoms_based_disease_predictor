import numpy as np
from flask import Flask, render_template, request
import pickle  # Initialize the flask App

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('symptoms.html')


# To use the predict button in our web-app
@app.route('/predict', methods=['POST'])
def predict():
    # For rendering results on HTML GUI
    form_values = request.form.listvalues()
    user_symptoms = list(form_values)[0]

    new_user_list = []
    newString = ''
    for each in user_symptoms:
        newString = each.lower()
        new_user_list.append(newString.replace(" ", "_"))
    print(new_user_list)

    inp_symptoms = [0 for x in range(132)]
    symptoms = "itching skin_rash nodal_skin_eruptions continuous_sneezing shivering chills joint_pain stomach_pain acidity ulcers_on_tongue muscle_wasting vomiting burning_micturition spotting urination fatigue weight_gain anxiety cold_hands_and_feets mood_swings weight_loss restlessness lethargy patches_in_throat irregular_sugar_level cough high_fever sunken_eyes breathlessness sweating dehydration indigestion headache yellowish_skin dark_urine nausea loss_of_appetite pain_behind_the_eyes back_pain constipation abdominal_pain diarrhoea mild_fever yellow_urine yellowing_of_eyes acute_liver_failure fluid_overload swelling_of_stomach swelled_lymph_nodes malaise blurred_and_distorted_vision phlegm throat_irritation redness_of_eyes sinus_pressure runny_nose congestion chest_pain weakness_in_limbs fast_heart_rate pain_during_bowel_movements pain_in_anal_region bloody_stool irritation_in_anus neck_pain dizziness cramps bruising obesity swollen_legs swollen_blood_vessels puffy_face_and_eyes enlarged_thyroid brittle_nails swollen_extremeties excessive_hunger extra_marital_contacts drying_and_tingling_lips slurred_speech knee_pain hip_joint_pain muscle_weakness stiff_neck swelling_joints movement_stiffness spinning_movements loss_of_balance unsteadiness weakness_of_one_body_side loss_of_smell bladder_discomfort foul_smell_of urine continuous_feel_of_urine passage_of_gases internal_itching toxic_look_(typhos) depression irritability muscle_pain altered_sensorium red_spots_over_body belly_pain abnormal_menstruation dischromic_patches watering_from_eyes increased_appetite polyuria family_history mucoid_sputum rusty_sputum lack_of_concentration visual_disturbances receiving_blood_transfusion receiving_unsterile_injections	coma stomach_bleeding distention_of_abdomen	history_of_alcohol_consumption fluid_overload blood_in_sputum prominent_veins_on_calf palpitations painful_walking pus_filled_pimples blackheads scurring skin_peeling silver_like_dusting small_dents_in_nails inflammatory_nails blister red_sore_around_nose yellow_crust_ooze"
    symptomsList = [i for i in symptoms.split()]
    for i in new_user_list:
        for j in symptomsList:
            if j == i:
                inp_symptoms[symptomsList.index(j)-1] = 1
    final_symptoms = np.array(inp_symptoms)
    final_symptoms = final_symptoms.reshape((-1,1)).transpose()
    #print(final_symptoms)

    prediction = model.predict(final_symptoms)
    output = (prediction[0])
    print(output)

    desc_dict = {}
    
    treat_dict={}
    specialist_dict={}

    
    treat_dict.update({'hepatitis A':'''The condition clears up on its own in one or two months. Rest and adequate hydration can help. Avoid alcohol as it may be harmful and aggregate certain conditions.''',

    'Hepatitis B':'''The condition often clears up on its own. Chronic cases require medication and possibly a liver transplant.Avoid alcohol as it may be harmful and aggregate certain conditions.''',

    'Hepatitis C':'''The condition often clears up on its own. Chronic cases require medication and possibly a liver transplant.Avoid alcohol as it may be harmful and aggregate certain conditions.''',
    'Hepatitis D':'''There are few treatments specifically for hepatitis D, although different regimes may be tried. Management also focuses on supportive care. Avoid alcohol as it may be harmful and aggregate certain conditions.''',
    'Hepatitis E':'''Hepatitis E usually resolves on its own within four to six weeks. Treatment focuses on supportive care, rehydration and rest. Avoid alcohol as it may be harmful and aggregate certain conditions.''',
    'Alcoholic hepatitis':'''Treatment involves hydration, nutritional care and stopping alcohol use. Steroid drugs can help reduce liver inflammation.''',

    'Tuberculosis':'''Treatment isn't always required for those without symptoms. Patients with active symptoms will require a long course of treatment involving multiple antibiotics.''',
    'Pneumonia':'''Treatment: Antibiotics can treat many forms of pneumonia. Some forms of pneumonia can be prevented by vaccines. ''',
    'Dimorphic hemmorhoids(piles)':''' A high-fibre diet can be effective, along with stool softeners. In some cases, a medical procedure to remove the haemorrhoid may be needed to provide relief.''',

    'Heart attack':'''Treatment ranges from lifestyle changes and cardiac rehabilitation to medication, stents and bypass surgery.
    ''',
    'Fungal infection':'''Treatments for fungal infection include antifungal medication.''',
    'Allergy':'''Avoiding harsh soaps and detergents, perfumed soaps, lotions and known allergy triggers may help to soothe irritated skin. Using an antihistamine or steroid cream may also help.
    ''',
    'GERD':'''Relief from lifestyle changes and over-the-counter medication is usually temporary. Stronger medication may be required.Elevate head of bed-reduces the likelihood of acid reflux or developing a pneumonia from saliva entering the airways.''',
    'Chronic cholestatic':'''The first step to treating cholestasis is to treat the underlying cause. For example, if it’s determined that medication is causing the condition, your doctor may recommend a different drug. If an obstruction like gallstones or a tumor is causing the backup of bile, your doctor may recommend surgery. In most cases, obstetric cholestasis resolves after delivery. Women who develop obstetric cholestasis should be monitored post-pregnancy.''',
     'Gastroenteritis':'''The first step to treating cholestasis is to treat the underlying cause. For example, if it’s determined that medication is causing the condition, your doctor may recommend a different drug. If an obstruction like gallstones or a tumor is causing the backup of bile, your doctor may recommend surgery.In most cases, obstetric cholestasis resolves after delivery. Women who develop obstetric cholestasis should be monitored post-pregnancy.''',
    'Drug Reaction':''' With a severe allergic reaction to a drug, you’ll likely need to avoid the drug entirely. Your doctor will probably try to replace the drug with a different one that you’re not allergic to.If you have a mild allergic reaction to a drug, your doctor may still prescribe it for you. But they may also prescribe another medication to help control your reaction. Certain medications can help block the immune response and reduce symptoms.''',
    'Peptic ulcer disease':''' Treatment usually includes medication to decrease stomach acid production. If it is caused by bacteria, antibiotics may be required.''',
    'AIDS':'''No cure exists for AIDS, but strict adherence to antiretroviral regimens (ARVs) can dramatically slow the disease's progress as well as prevent secondary infections and complications.''',
    'Diabetes':'''Controlling blood sugar through diet, oral medication or insulin is the main treatment.   Regular screening for complications is also required.''',
    'Gastroentritis':'''Avoiding contaminated food and water and washing hands can often help prevent infection. Rest and rehydration are the mainstays of treatment.''',
    '(vertigo)_paroymsal_positional_vertigo': '''Treatment consists of procedures. Treatment includes a series of head movements that shift particles in the ears.''',
    'Acne':'''Treatments include over-the-counter creams and cleanser, as well as prescription antibiotics.''',
    'Urinary tract infection':''' Common treatment is with antibiotics. In most cases, the cause is bacteria. UTIs caused by bacteria are treated with antibiotics.In some cases, viruses or fungi are the causes. Viral UTIs are treated with medications called antivirals. Often, the antiviral cidofovir is the choice to treat viral UTIs. Fungal UTIs are treated with medications called antifungals.''',
    'Psoriasis':'''Treatment aims to remove scales and stop skin cells from growing so quickly. Topical ointments, light therapy and medication can offer relief.
    ''',
   'Impetigo':'''Antibiotics shorten the infection and can help prevent spread to others.''',
   'Typhoid':'''Typhoid fever is treated with antibiotics which kill the Salmonella bacteria. Prior to the use of antibiotics, the fatality rate was 20%. With antibiotics and supportive care, mortality has been reduced to 1%-2%. With appropriate antibiotic therapy, there is usually improvement within one to two days and recovery within seven to 10 days. Several antibiotics are effective for the treatment of typhoid fever. Chloramphenicol was the original drug of choice for many years. Because of rare serious side effects, chloramphenicol has been replaced by other effective antibiotics. The choice of antibiotics is guided by identifying the geographic region where the infection was contracted (certain strains from South America show a significant resistance to some antibiotics.) If relapses occur, patients are retreated with antibiotics.''',
  'Arthritis':'''Treatment consists of self care and therapy
   Medication, physiotherapy or sometimes surgery helps reduce symptoms and improve quality of life.''','Bronchial Asthma':'''Asthma can usually be managed with rescue inhalers to treat symptoms (salbutamol) and controller inhalers that prevent symptoms (steroids). Severe cases may require longer-acting inhalers that keep the airways open (formoterol, salmeterol, tiotropium), as well as inhalant steroids.''',
'Hypertension':'''Eating a healthier diet with less salt, exercising regularly and taking medication can help lower blood pressure.''',
'Migraine':'''Preventive and pain-relieving medication can help manage migraine headaches.
''',
'Cervical spondylosis':'''In many cases, no specific treatment is required. If symptoms occur, treatments include medication, corticosteroid injections, physiotherapy and sometimes surgery.
''',
'Paralysis(brain hemorrhage)':'''Treatment usually includes medication to decrease stomach acid production. If it is caused by bacteria, antibiotics may be required.
''',
'Jaundice':'''Jaundice must always be evaluated by a doctor. See a doctor immediately if you. Notice any yellow tint to the skin or eyes of an infant, child or adult. Have dark coloured urine and abdominal swelling or expansion
''',
'Malaria':'''People travelling to areas where malaria is common typically take protective drugs before, during and after their trip. Treatment includes antimalarial drugs.
''',
'Chicken pox':'''Chickenpox can be prevented by a vaccine. Treatment usually involves relieving symptoms, although high-risk groups may receive antiviral medication.
''',
'Dengue':'''Treatment consists of pain medications and fluids. Treatment includes fluids and pain relievers. Severe cases require hospital care.
''',
'Common cold':'''Most people recover on their own within two weeks. Over-the-counter products and home remedies can help control symptoms.
''',
'Hypothyroidism':'''Treatment consists of hormones. Treatment consists of thyroid hormone replacement.
''',
'Hyperthyroidism':'''Treatment consists of anti-thyroid medications.Treatments include radioactive iodine, medication and sometimes surgery.
''',
'Hypoglycemia':'''Treatment consists of diet modifications. Consuming high-sugar foods or drinks, such as orange juice or regular fizzy drinks, can treat this condition. Alternatively, medication can be used to raise blood sugar levels. It's also important that a doctor identifies and treats the underlying cause.''',
'Osteoarthritis':'''Treatment consists of self care and therapy.Medication, physiotherapy and sometimes surgery can help reduce pain and maintain joint movement.
'''
})


   

    desc_dict.update({'hepatitis A':'''A highly contagious liver infection caused by the hepatitis A virus. Hepatitis A is preventable by vaccine. It spreads from contaminated food or water or contact with someone who is infected.Symptoms include fatigue, nausea, abdominal pain, loss of appetite and low-grade fever.The condition clears up on its own in one or two months. Rest and adequate hydration can help.\n
    ''',

'Hepatitis B':'''A serious liver infection caused by the hepatitis B virus that's easily preventable by a vaccine.This disease is most commonly spread by exposure to infected bodily fluids.Symptoms are variable and include yellowing of the eyes, abdominal pain and dark urine. Some people, particularly children, don't experience any symptoms. In chronic cases, liver failure, cancer or scarring can occur.The condition often clears up on its own. Chronic cases require medication and possibly a liver transplant.

''',

'Hepatitis C':'''A serious liver infection caused by the hepatitis B virus that's easily preventable by a vaccine.This disease is most commonly spread by exposure to infected bodily fluids.Symptoms are variable and include yellowing of the eyes, abdominal pain and dark urine. Some people, particularly children, don't experience any symptoms. In chronic cases, liver failure, cancer or scarring can occur.The condition often clears up on its own. Chronic cases require medication and possibly a liver transplant.

''',
'Hepatitis D':'''A serious liver disease caused by infection with the hepatitis D virus.Hepatitis D only occurs amongst people who are infected with the Hepatitis B virus. Transmission requires contact with infectious blood. At-risk populations include intravenous drug abusers and men who have sex with men.Symptoms include abdominal pain, nausea and fatigue.There are few treatments specifically for hepatitis D, although different regimes may be tried. Management also focuses on supportive care.

''',
'Hepatitis E':'''A liver disease caused by the hepatitis E virus. The hepatitis E virus is mainly transmitted through drinking water contaminated with faecal matter. Symptoms include jaundice, lack of appetite and nausea. In rare cases, it may progress to acute liver failure. Hepatitis E usually resolves on its own within four to six weeks. Treatment focuses on supportive care, rehydration and rest.

''','Alcoholic hepatitis':'''Liver inflammation caused by drinking too much alcohol.Alcoholic hepatitis can occur in people who drink heavily for many years.Symptoms include yellow skin and eyes along with increasing stomach size due to fluid accumulation. Treatment involves hydration, nutritional care and stopping alcohol use. Steroid drugs can help reduce liver inflammation.
''',

'Tuberculosis':'''A potentially serious infectious bacterial disease that mainly affects the lungs.The bacteria that cause TB are spread when an infected person coughs or sneezes.Most people infected with the bacteria that cause tuberculosis don't have symptoms. When symptoms do occur, they usually include a cough (sometimes blood-tinged), weight loss, night sweats and fever.Treatment isn't always required for those without symptoms. Patients with active symptoms will require a long course of treatment involving multiple antibiotics.
''',
'Pneumonia':'''Infection that inflames air sacs in one or both lungs, which may fill with fluid.With pneumonia, the air sacs may fill with fluid or pus. The infection can be life-threatening to anyone, but particularly to infants, children and people over 65.Symptoms include a cough with phlegm or pus, fever, chills and difficulty breathing.Antibiotics can treat many forms of pneumonia. Some forms of pneumonia can be prevented by vaccines.

''',
'Dimorphic hemmorhoids(piles)':'''Swollen and inflamed veins in the rectum and anus that cause discomfort and bleeding.Haemorrhoids are usually caused by straining during bowel movements, obesity or pregnancy.Discomfort is a common symptom, especially during bowel movements or when sitting. Other symptoms include itching and bleeding.A high-fibre diet can be effective, along with stool softeners. In some cases, a medical procedure to remove the haemorrhoid may be needed to provide relief.
''',

'Heart attack':'''A blockage of blood flow to the heart muscle.A heart attack is a medical emergency. A heart attack usually occurs when a blood clot blocks blood flow to the heart. Without blood, tissue loses oxygen and dies.

''',
'Fungal infection':'''Any disease caused by a fungus.A fungus that invades the tissue can cause a disease that's confined to the skin, spreads into tissue, bones and organs or affects the whole body.Symptoms depend on the area affected, but can include skin rash or vaginal infection resulting in abnormal discharge.Treatments include antifungal medication.
''',
'Allergy':'''An allergy is an immune system response to a foreign substance that's not typically harmful to your body.They can include certain foods, pollen, or pet dander. Your immune system's job is to keep you healthy by fighting harmful pathogens.

''',
'GERD':'''A digestive disease in which stomach acid or bile irritates the food pipe lining.This is a chronic disease that occurs when stomach acid or bile flows into the food pipe and irritates the lining. Acid reflux and heartburn more than twice a week may indicate GERD.Symptoms include burning pain in the chest that usually occurs after eating and worsens when lying down.Relief from lifestyle changes and over-the-counter medication is usually temporary. Stronger medication may be required.
''',
'Chronic cholestatic':'''Chronic cholestatic diseases, whether occurring in infancy, childhood or adulthood, are characterized by defective bile acid transport from the liver to the intestine, which is caused by primary damage to the biliary epithelium in most cases. 
''',
'Gastroenteritis':'''An intestinal infection marked by diarrhoea, cramps, nausea, vomiting and fever.Stomach flu is typically spread by contact with an infected person or through contaminated food or water.Diarrhoea, cramps, nausea, vomiting and low-grade fever are common symptoms.Avoiding contaminated food and water and washing hands can often help prevent infection. Rest and rehydration are the mainstays of treatment.
''',
'Drug Reaction':'''This is basically  an allergic reaction to a medication. With an allergic reaction, your immune system, which fights infection and disease, reacts to the drug. This reaction can cause symptoms such as rash, fever, and trouble breathing.
''',
'Peptic ulcer disease':'''A sore that develops on the lining of the oesophagus, stomach or small intestine.Ulcers occur when stomach acid damages the lining of the digestive tract. Common causes include the bacteria H. Pylori and anti-inflammatory pain relievers including aspirin.Upper abdominal pain is a common symptom.
''',
'AIDS':'''HIV causes AIDS and interferes with the body's ability to fight infections.The virus can be transmitted through contact with infected blood, semen or vaginal fluids.Within a few weeks of HIV infection, flu-like symptoms such as fever, sore throat and fatigue can occur. Then the disease is usually asymptomatic until it progresses to AIDS. AIDS symptoms include weight loss, fever or night sweats, fatigue and recurrent infections.No cure exists for AIDS, but strict adherence to antiretroviral regimens (ARVs) can dramatically slow the disease's progress as well as prevent secondary infections and complications.
''',
'Diabetes':'''Diabetes is the condition in which the body does not properly process food for use as energy.The pancreas, an organ that lies near the stomach, makes a hormone called insulin to help glucose get into the cells of our bodies. When you have diabetes, your body either doesn't make enough insulin or can't use its own insulin as well as it should. This causes sugars to build up in your blood. This is why many people refer to diabetes as “sugar.” 
.''',
'Gastroentritis':'''Stomach flu is typically spread by contact with an infected person or through contaminated food or water.
''',
'Bronchial Asthma':'''A condition in which a person's airways become inflamed, narrow and swell and produce extra mucus, which makes it difficult to breathe.Asthma can be minor or it can interfere with daily activities. In some cases, it may lead to a life-threatening attack. Asthma may cause difficulty breathing, chest pain, cough and wheezing. The symptoms may sometimes flare up.''',
'Hypertension':'''A condition in which the force of the blood against the artery walls is too high. Usually hypertension is defined as blood pressure above 140/90, and is considered severe if the pressure is above 180/120.High blood pressure often has no symptoms. Over time, if untreated, it can cause health conditions, such as heart disease and stroke.Eating a healthier diet with less salt, exercising regularly and taking medication can help lower blood pressure.''',
'Migrane':'''A headache of varying intensity, often accompanied by nausea and sensitivity to light and sound.Migraine headaches are sometimes preceded by warning symptoms. Triggers include hormonal changes, certain food and drink, stress and exercise.''',
'Cervical spondylosis':'''A general term for age-related wear and tear of the spinal discs. Spondylosis is common and worsens with age. This condition is often used to describe degenerative arthritis (osteoarthritis) of the spine. Most people don't have symptoms, but some may experience pain or muscle spasms. In many cases, no specific treatment is required. If symptoms occur, treatments include medication, corticosteroid injections, physiotherapy and sometimes surgery.''',
'Paralysis(brain hemorrhage)':'''Intracerebral hemorrhage (ICH) is when blood suddenly bursts into brain tissue, causing damage to your brain. Symptoms usually appear suddenly during ICH. They include headache, weakness, confusion, and paralysis, particularly on one side of your body.''',

'Jaundice':'''Yellow skin caused by the build-up of bilirubin in the blood.
Jaundice may occur if the liver can't efficiently process red blood cells as they break down. It's normal in healthy newborns and usually clears on its own. At other ages, it may signal infection or liver disease.''',
'Malaria':'''A disease caused by a plasmodium parasite, transmitted by the bite of infected mosquitoes.
The severity of malaria varies based on the species of plasmodium.''',
'Chicken pox':'''A highly contagious viral infection which causes an itchy, blister-like rash on the skin.
Chickenpox is highly contagious to those who haven't had the disease or been vaccinated against it.
The most characteristic symptom is an itchy, blister-like rash on the skin.
Chickenpox can be prevented by a vaccine. Treatment usually involves relieving symptoms, although high-risk groups may receive antiviral medication.''',
'Dengue':'''A mosquito-borne viral disease occurring in tropical and subtropical areas.
Those who become infected with the virus a second time are at a significantly greater risk of developing severe disease.
Symptoms include high fever, headache, rash and muscle and joint pain. In severe cases there is serious bleeding and shock, which can be life threatening.''',
'Common cold':'''A common viral infection of the nose and throat.
In contrast to the flu, a common cold can be caused by many different types of viruses. The condition is generally harmless and symptoms usually resolve within two weeks.''',
'Hypothyroidism':'''A condition in which the thyroid gland doesn't produce enough thyroid hormone.
Hypothyroidism's deficiency of thyroid hormones can disrupt such things as heart rate, body temperature and all aspects of metabolism. Hypothyroidism is most prevalent in older women.''',
'Hyperthyroidism':'''The overproduction of a hormone by the butterfly-shaped gland in the neck (thyroid).
Hyperthyroidism is the production of too much thyroxine hormone. It can increase metabolism.''',
'Hypoglycemia':'''Low blood sugar, the body's main source of energy.
Diabetes treatment and other conditions can cause hypoglycaemia.
Confusion, heart palpitations, shakiness and anxiety are symptoms.
Consuming high-sugar foods or drinks, such as orange juice or regular fizzy drinks, can treat this condition. Alternatively, medication can be used to raise blood sugar levels. It's also important that a doctor identifies and treats the underlying cause.''',
'Osteoarthritis':'''A type of arthritis that occurs when flexible tissue at the ends of bones wears down.
The wearing down of the protective tissue at the ends of bones (cartilage) occurs gradually and worsens over time.''',
'Arthritis':'''Inflammation of one or more joints, causing pain and stiffness that can worsen with age.
Different types of arthritis exist, each with different causes including wear and tear, infections and underlying diseases.''',
'Typhoid':'''Typhoid fever is an infection that spreads through contaminated food and water.
Vaccines are recommended in areas where typhoid fever is common.
''',
'Impetigo':'''A condition in which skin cells build up and form scales and itchy, dry patches. Psoriasis is thought to be an immune system problem. Triggers include infections, stress and cold. The most common symptom is a rash on the skin, but sometimes the rash involves the nails or joints. Treatment aims to remove scales and stop skin cells from growing so quickly. Topical ointments, light therapy and medication can offer relief.''',
'Psoriasis':'''A condition in which skin cells build up and form scales and itchy, dry patches. Psoriasis is thought to be an immune system problem. Triggers include infections, stress and cold. The most common symptom is a rash on the skin, but sometimes the rash involves the nails or joints. Treatment aims to remove scales and stop skin cells from growing so quickly. Topical ointments, light therapy and medication can offer relief.''',
'Urinary tract infection':'''
 An infection in any part of the urinary system, the kidneys, bladder or urethra. Urinary tract infections are more common in women. They usually occur in the bladder or urethra, but more serious infections involve the kidney. A bladder infection may cause pelvic pain, increased urge to urinate, pain with urination and blood in the urine. A kidney infection may cause back pain, nausea, vomiting and fever. Common treatment is with antibiotics.''',
 'Acne':'''A skin condition that occurs when hair follicles plug with oil and dead skin cells. Acne is most common in teenagers and young adults.''',
 '(vertigo) Paroymsal  Positional Vertigo':'''Episodes of dizziness and a sensation of spinning with certain head movements. Benign paroxysmal positional vertigo (BPPV) is triggered by certain changes in head position, such as tipping the head up or down. It's rarely serious unless it increases the risk of falling. People can experience dizziness, a spinning sensation (vertigo), lightheadedness, unsteadiness, loss of balance and nausea. Treatment includes a series of head movements that shift particles in the ears.'''

})

    specialist_dict.update({'Fungal Infection': 'Dermatologist', 'Allergy': ' Allergist / Dermatologist', 'GERD': ' Gastroenterologist', 'Chronic cholestasis': ' Hepatologist', 'Drug Reaction': ' Allergist', 'Peptic ulcer diseae': ' Gastroenterologist', 'AIDS': ' Internist / Family Physician', 'Diabetes': ' Physician / Endocrinologist', 'Gastroenteritis': ' Gastroenterologist', 'Bronchial Asthma': ' Pulmonologist (Lung Specialist)', 'Hypertension': ' Cardiologist', 'Migraine': ' Neurologist', 'Cervical spondylosis': ' Orthopaedic', 'Paralysis (brain hemorrhage)': ' Neurologist', 'Jaundice': ' Gastroenterologist', 'Malaria': ' Infectious disease specialist', 'Chicken pox': ' Paediatrician', 'Dengue': ' Infectious disease specialist', 'Typhoid': ' Infectious disease specialist', 'Common Cold': ' Otolaryngologist(ENT)', 'Hepatitis A': ' Hepatologist / Gastroenterologists', 'Hepatitis B': ' Hepatologist / Gastroenterologists', 'Hepatitis C': ' Hepatologist / Gastroenterologists', 'Hepatitis D': ' Hepatologist / Gastroenterologists', 'Hepatitis E': ' Hepatologist / Gastroenterologists', 'Alcoholic hepatitis': ' Hepatologist / Gastroenterologists', 'Tuberculosis': ' Pulmonologist (Lung Specialist)', 'Pneumonia': ' Pulmonologist (Lung Specialist)', 'Dimorphic hemmorhoids(piles)': ' Proctologist / General Physician', 'Heart attack': 'Cardiologist', 'Varicose veins': ' phebologist/ dermatologist / dermatology surgeon', 'Hypothyroidism': ' Thyroidologists', 'Hyperthyroidism': ' Thyroidologists', 'Hypoglycemia': ' pcp / critical care', 'Osteoarthristis': ' Rheumatologists', 'Arthritis': ' Rheumatologists', '(vertigo) Paroymsal Positional Vertigo': ' Neurologists / Otolaryngologists', 'Acne': ' Dermatologists', 'Urinary tract infection': ' PCP/ Urologists / Nephrologists', 'Psoriasis': ' Dermatologists/ Rheumatologists', 'Impetigo': ' Dermatologists/ PCP/ Paediatricians'})
    treatment=treat_dict[output]
    desc = desc_dict[output]
    specialist=specialist_dict[output]
    #print(desc)

    file1 = open("prognosis.txt","a+")
    file1.write(format(output))
    file1.write("\n")

    return render_template('predict.html',prediction_text='{}'.format(output),description_text=desc,treatment_text=treatment,spec_text=specialist)

    # return render_template('predict.html', prediction_text='There are chances that you may have: {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)