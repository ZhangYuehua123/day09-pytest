#导包
import json
def read_json(filename):
    filepath  = r"D:/web测试/day09/data/"+filename
    with open(filepath,'r',encoding="utf-8") as f:
        return json.load(f)



if __name__ == '__main__':
    datas = read_json("login.json")
    arr = []
    for data in datas.values():
        arr.append(tuple(data.values()))
    print(arr)
