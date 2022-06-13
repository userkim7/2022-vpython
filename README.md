# 2022-vpython

## [프로그램 개요]
나는 선형회귀 프로그램을 만들고 싶다.

vpython 에서 처음부터 만들었으나 안타깝게도 web vpython 에서는 Numpy 모듈을 지원해주지 않았다.

따라서 Numpy 모듈에 있는 행렬 사칙연산과 행렬 곱부터 구현하고, 오류값 등을 그래프로 그리고자 한다.

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
