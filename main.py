import json
import codecs
import os
#This function Intilizalize the File if the File is Empty
def fileIntialize():
    string = '{"data":[]}'
    with open("proccessed.json" , "w") as outfile:
        outfile.write(string)

#Read the File and start processing it
with open("data.json") as json_file:
    data = json.load(json_file)
    form_Responses = data['form_response']
    defentions = form_Responses['definition']
    fields = defentions['fields']
    answers = form_Responses['answers']
    json_object = {}
    json_data = []
    #Loop over the Questions
    for Questions in fields:
        json_object['ID'] = Questions['id']
        json_object['Question'] = Questions['title']
        #Find an id that matches the Question ID in the Answers
        for answer in answers:
            field = answer['field']
            if field['id'] == Questions['id']:
                if answer['type'] == "choices":
                    Answer = []
                    Choices = answer['choices']
                    for choice in Choices['labels']:
                        Answer.append(choice)
                else:
                    Answer = answer[answer['type']]
            json_object['Answer'] = Answer


        #Append the new Question and answer to the File
        with open("proccessed.json",'r+') as outfile:
            if os.path.getsize("proccessed.json") == 0:
                fileIntialize()
            data = json.load(outfile)
            data['data'].append(json_object)
            outfile.seek(0)
            json.dump(data, outfile, indent=4 , ensure_ascii=False)