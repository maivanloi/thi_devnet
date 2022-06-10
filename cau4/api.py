import requests
import json

base_url = 'https://api.meraki.com/api/v1'
key = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'


# Hàm lấy tất cả organizationsID
def get_org():
    url = base_url + '/organizations'

    header = {
        'X-Cisco-Meraki-API-Key': key
    }

    response = requests.get(url, headers=header)
    data = response.json()
    # print(data)
    # print(json.dumps(data, indent = 4))
    # num = len(data)
    # print(num)
    # In tất cả các organizationID
    # for i in range(num):
    #     id_org = data[i]['id']
    #     print(id_org)

    # In id đầu tiên
    id_1 = data[0]['id']
    # print(id_1)
    return id_1


# Hàm lấy organization inventory với ID đã lấy ở trên
def get_org_inventory():
    url = base_url + f'/organizations/{get_org()}/inventory/devices'
    header = {
        'X-Cisco-Meraki-API-Key': key
    }
    response = requests.get(url, headers=header)
    data = response.json()
    # print(data)
    # print(json.dumps(data, indent=4))
    num = len(data)
    # print(num)
    # In tat ca cac networkId
    count = 0
    for i in range(num):
        id_net = data[i]['networkId']
        # print(id_net)
        # print danh sach networkId = null
        if (id_net == None):
            count += 1
            result = data[i]
            print(json.dumps(result, indent=4))
    print('So luong thiet bi networkId null la: ', count)


if __name__ == "__main__":
    get_org_inventory()