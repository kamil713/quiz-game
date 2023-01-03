import connect_to_api
import nanoid
import json

d = dict()


def setting_answers(answers, correct_answer):
    answers_list = []
    for answer in answers:
        d = dict()
        d['answer'] = answer
        d['correct'] = True if answer == correct_answer else False
        answers_list.append(d)
    return answers_list


newData = []
for item in connect_to_api.data['results']:
    d['id'] = nanoid.generate(size=10)
    d['category'] = item['category']
    d['question'] = item['question']
    all_answers = item['incorrect_answers'] + [item['correct_answer']]
    all_answers.sort()
    d['answers'] = setting_answers(all_answers, item['correct_answer'])
    newData.append(d)

# print(type(newData))
# print(newData)

#print(json.dumps(newData, indent=2))
