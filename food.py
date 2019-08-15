import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "c7920c60-bf7f-11e9-84de-b15b39905d964e7bd86f-1009-4c1e-983a-fb77328f35de"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()
def answer_question():
    question = input(">")
    answer = classify(question)
    answerclass = answer["class_name"]
    confidence = answer["confidence"]
    
    if confidence < 75:
        print("I don't know, please ask me something else!")
        
    elif answerclass == "Vegetables":
        print ("There are a quite a bit of vegetables, though I cannot list all of them. Here is a link to it: https://simple.wikipedia.org/wiki/List_of_vegetables")
               
    elif answerclass == "Meat":
        print ("The meat in my opinion is the best in the world. This meath can only be found in limited restaurants at drastic prices; this is none other than wagyu beef. To find out more please follow this link: https://en.wikipedia.org/wiki/Wagyu")
               
    elif answerclass == "Nutritional_Value":
        print ("The caloric value of the meal you ate today is actually 995, therefore you need to go to the gym now. Higher calorie intake = better healthier body. !).")
               
    elif answerclass == "Taste":
        print ("The taste of the meal altogether is the best meal in my life. This is truly why we got No. 1 in the world." )
        
print ("I will be the waiter attending to your needs this will be a practice before going in the most high class restaurant of the world. You can ask me the amount of veggies/vegetables, How I thought of the meal, the caloric value, and my opinion on the meat. ")
while True:
    answer_question()