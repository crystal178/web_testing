import requests


# from TestDatas import Common_Datas as cd


class CourseOper:

    def __init__(self, user, passwd):
        url = "https://www.ketangpai.com/UserApi/login"
        data = {"email": user, "password": passwd, "remember": "0"}
        self.s = requests.Session()
        res = self.s.post(url, data)
        print(res.text)

    def add_courser(self, coursename, classname):
        url = "https://www.ketangpai.com/CourseApi/createCourse"
        data = {"coursename": coursename, "relation": 0, "teachClassid": "",
                "neednatureclass": 0, "needgrade": 0,
                "needtrance": 0, "coid": "", "canview": 0,
                "classname": classname, "semester": "2020-2021", "term": 0}
        res = self.s.post(url, data)
        res_json = res.json()
        print(res_json)

        course_id = res_json["data"]["id"]
        course_code = res_json["data"]["code"]
        return course_id, course_code

    def delete_courser(self,course_id, passwd):
        url = "https://www.ketangpai.com/CourseApi/delCourse"
        data = {"courseid":course_id, "password":passwd}
        res = self.s.post(url, data)
        print(res.text)

