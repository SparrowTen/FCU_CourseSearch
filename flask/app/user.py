import requests
import time
import base64
import hmac

class User:
    def __init__(self, std_id, pwd):
        self.key = 'poyu39AdminGeneralKey'
        self.std_id = std_id
        self.pwd = pwd
    
    def __init__(self, std_id):
        self.key = 'poyu39AdminGeneralKey'
        self.std_id = std_id
    
    # def is_active(self):
    #     return self._active
    
    def generate_token(self, expire = 3600):
        key = self.key
        ts_str = str(time.time() + expire)
        ts_byte = ts_str.encode("utf-8")
        sha1_tshexstr  = hmac.new(key.encode("utf-8"),ts_byte,'sha1').hexdigest() 
        token = ts_str + ':' + sha1_tshexstr
        b64_token = base64.urlsafe_b64encode(token.encode("utf-8"))
        
        # r = requests.post('http://localhost:5000/API/setToken', data = {'token': b64_token.decode("utf-8")})
        # print(f"gen token: {r.text}")
        
        return b64_token.decode("utf-8")
        
    def certify_token(self, token):
        key = self.key
        token_str = base64.urlsafe_b64decode(token).decode('utf-8')
        token_list = token_str.split(':')
        
        if len(token_list) != 2:
            return False
        ts_str = token_list[0]
        
        if float(ts_str) < time.time():
            # token 過期
            return False
        
        known_sha1_tsstr = token_list[1]
        sha1 = hmac.new(key.encode("utf-8"),ts_str.encode('utf-8'),'sha1')
        calc_sha1_tsstr = sha1.hexdigest()
        
        if calc_sha1_tsstr != known_sha1_tsstr:
            # token 驗證錯誤
            return False 
        # token 驗證成功
        return True