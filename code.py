import requests
token=""
headers={
    "Authorization":f"Bearer {token}"
}
response=requests.get("https://hulms.instructure.com/api/v1/users/self/enrollments",headers=headers)

json=response.json()
dict={}
for i in json:
    dict[i['course_id']]=i['grades']['current_score']
scores={}

for id in dict:
    course_response=requests.get(f"https://hulms.instructure.com/api/v1/courses/{id}",headers=headers)
    course_response=course_response.json()
    scores[course_response["name"]]=dict[id]
    
for i in scores:
    if scores[i]!=None:
        print(f"Your grade in {i} is {scores[i]}%")
