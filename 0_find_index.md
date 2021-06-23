# Find Index from List

> 리스트에서 특정 값의 모든 인덱스를 찾는 방법

<br/>

#### 1) filter

```python
a = [100, 200, 300, 100, 200, 300, 100, 200, 300]
target = 200

print(list(filter(lambda x : a[x] == target, range(len(a)))))

결과 :
[1, 4, 7]
```

<br/>

<br/>

#### 2) enumerate

```python
a = [100, 200, 300, 100, 200, 300, 100, 200, 300]
target = 200

print([i for i, x in enumerate(a) if x == target])

결과 :
[1, 4, 7]
```

<br/>

<br/>

* 존재 하지 않는 경우

```python
a = [100, 200, 300, 100, 200, 300, 100, 200, 300]
target = 400

print(list(filter(lambda x : a[x] == target, range(len(a)))))
print([i for i, x in enumerate(a) if x == target])

결과 :
[]
[]
```

<br/>

<br/>

* 여러 개의 값의 인덱스를 찾는 경우

```python
a = [100, 200, 300, 100, 200, 300, 100, 200, 300]
target = [100, 300]

print(list(filter(lambda x : a[x] in target, range(len(a)))))
print([i for i, x in enumerate(a) if x in target])

결과 :
[0, 2, 3, 5, 6, 8]
[0, 2, 3, 5, 6, 8]
```

