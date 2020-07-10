import  pytest
import requests
class WeWork:
    def get_token(self):
        r =requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',params={
            'corpid':'wwe99852284eb00ea5',
                'corpsecret':'8I5vAsm-CGL8h2FmjkZw8JuKIsxybtWxBaJoC_GFE3s'
        })
        return r
        self.token=r.json()['access_token']
    def tag_list(self):
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list', params={
            'access_token': self.token
        })
        return r
    def tag_add(self):
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag', params={
            'access_token': self.token
        },
                          json={
                              "group_id": self.groupid,
                              'tag': [
                                  {
                                      'name': 'demo04'
                                  }
                              ]
                          }
                          )
    def tag_delete(self):
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag')


class TestWeWork:
    def setup(self):
       self = self.WeWork
       return self
    def test_tag_list(self):
        r=self.WeWork.tag_list()
        self.format(r.json())
        assert r.json['errcode'] == 0
    def test_tag_add(self):
       r=self.WeWork.tag_list()
       assert r.json()['errcode'] == 0
    def test_tag_delete(self):
       r=self.WeWork.tag_list()
       assert r.json()['errcode'] == 0
       id = [tag['id'] for group in r.json() ['tag_group'] for tag in group ['tag'] if tag['demo04']]
       print(id)
       r=self.WeWork.tag_delete(id)
       assert r.json()['errcode'] == 0