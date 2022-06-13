# 2022-vpython

### 20220530-github 가입
cpython 포크

tensorflow 포크

repository 추가-지뢰찾기 추가

### 20220603-Linear Regression 추가
알아낸 것-Web VPython 에서 
```python
a=[1,2,3]
print(type(a)) #list
print(type(a)==list) #False
```
따라서 오류 예외 처리로
``` python
run=True
try:
    a.append(0)
    a.remove(0)
except:
    run=False
```    
같은 형식을 써야 한다.
