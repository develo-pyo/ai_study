#!/usr/bin/env python
# coding: utf-8

# ## 모듈
#     : 함수나 변수 또는 클래스를 모아놓은 소스 파일

# In[4]:


def add(a,b):
    c = a + b
    return c
def multiply(a,b):
    c = a * b
    return c



# if __name__ == '__main__':
print(__name__)
ret = add(10, 20)
print(ret)
ret = multiply(10, 20)
print(ret)


# In[ ]:




