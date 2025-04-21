#导包
import yaml
def read_yaml(filename):
    filepath  = r"D:/web测试/day09_pytest/data/"+filename
    with open(filepath,'r',encoding="utf-8") as f:
        return yaml.safe_load(f)



if __name__ == '__main__':
    datas = read_yaml("login1.yaml")
    arr = []
    for data in datas.values():
        arr.append(tuple(data.values()))
    print(arr)
