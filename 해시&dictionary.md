# 해쉬

> 해쉬는 임의의 크기를 가진 데이터를 고정된 데이터의 크기로 변환시키는 것을 말한다.
>
> 이를 이용해 특정한 배열의 인덱스 위치를 입력하고자 하는 데이터의 값을 이용해 저장하거나 찾을 수 있다.
>
> 기존에 사용했던 자료구조들은 탐색이나 삽입에 선형시간이 걸리기도 했던 것에 비해, 해쉬를 이용하면 즉시 저장하거나 찾고자 하는 위치를 참조할 수 있으므로 더욱 빠른 속도로 처리할 수 있다,



## 1. Direct Addressing Table

Direct Addressing Table 은 KEY_VALUE 쌍의 데이터를 배열에 저장, KEY값을 직접적으로 배열의 인덱스로 사용하는 방법이다

예를 들면 키 값이 400인 데이터가 있다면, 이는 배열의 인덱스가 400인 위치에 키 값을 저장하고 포인터로 데이터를 연결한다. 

똑같은 키 값이 존재하지 않는다고 가정하면, 삽입 시에는 각 키마다 자신의 공간이 존재하므로 그 위치에다가 저장하면 되고,

삭제 시에는 해당 키의 위치에 NULL값을 넣어주면 된다. 탐색시에는 해당 키의 위치를 그냥 찾아가서 참조하면 된다.

찾고자하는 데이터의 key만 알고 있으면 즉시 위치를 찾는것이 가능하므로 탐색, 저장, 삭제, 갱신은 모두 선형시간인 O(1) 로 매우 빠른 속도로 처리가 가능하다

다만 KEY 값의 최대 크기만큼 배열이 할당되기 떄문에, 크기는 매우 큰데 저장하고자 하는데이터가 적다면 공간을 많이 낭비할 수 있다는 단점이 있다.



## 2. dictionary(딕셔너리)

- 딕셔너리 타입은 immutable 한 key와 mutable한 값 value로 매핑되어 있는 순서가 없는 집합

- 일반적인 딕셔너리타입의 모습 : 중괄호가 있고 키와 값이 있다

  ```python
  {"A":1,"B":2}
  
  ```

  - 값은 중복될 수 있지만 키가 중복되면 마지막 값으로 덮어씌워진다

  ```python
    >>> {"a" : 1, "a":2}
    {'a': 2}
  ```

  - 순서가 없기 때문에 인덱스로는 접근할 수 없고, 키로 접근 가능하다

    ```python
      >>> d = {'abc' : 1, 'def' : 2}
      >>> d[0]
      Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
      KeyError: 0
      >>> d['abc']
      1
    ```

  - mutable 한 객체이므로 키로 접근하여 값을 변경할 수 있습니다.

    ```python
      >>> d['abc'] = 5
      >>> d
      {'abc': 5, 'def': 2}
    ```

​         

- 새로운 키와 값을 아래와 같이 추가할 수 있습니다.

  ```
    >>> d['ghi'] = 999
    >>> d
    {'abc': 5, 'def': 2, 'ghi': 999}
  ```

### 2-1.dictionary(딕셔너리) 선언

- 리스트 속에 리스트나 튜플, 튜플속에 리스트나 튜플의 값을 키와 value를 나란히 입력하면, 아래와 같이 dict로 변형할 수 있습니다.

  ```python
    >>> name_and_ages = [['alice', 5], ['Bob', 13]]
    >>> dict(name_and_ages)
    {'alice': 5, 'Bob': 13}
    >>> name_and_ages = [('alice', 5), ('Bob', 13)]
    >>> dict(name_and_ages)
    {'alice': 5, 'Bob': 13}
    >>> name_and_ages = (('alice', 5), ('Bob', 13))
    >>> dict(name_and_ages)
    {'alice': 5, 'Bob': 13}
    >>> name_and_ages = (['alice', 5], ['Bob', 13])
    >>> dict(name_and_ages)
    {'alice': 5, 'Bob': 13}
  ```

## 4. dictionary(딕셔너리) 복사

- 얕은 복사(shallow copy) 1

  ```python
   >>> a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
   >>> b =a.copy()
   >>> b['alice'].append(5)
   >>> b
   {'alice': [1, 2, 3, 5], 'bob': 20, 'tony': 15, 'suzy': 30}
   >>> a
   {'alice': [1, 2, 3, 5], 'bob': 20, 'tony': 15, 'suzy': 30}
  ```

- 얕은 복사(shallow copy) 2

  ```python
    >>> a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
    >>> b = dict(a)
    >>> a
    {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
    >>> b
    {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
    >>> id(a)
    4334645680
    >>> id(b)
    4334648920
  ```

- 깊은 복사(deep copy)

  ```python
    >>> import copy
    >>> a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
    >>> b = copy.deepcopy(a)
    >>> b['alice'].append(5)
    >>> b
    {'alice': [1, 2, 3, 5], 'bob': 20, 'tony': 15, 'suzy': 30}
    >>> a
    {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
  ```

## 5. dictionary update(딕셔너리 수)

- 단일 수정은 키로 접근하여 값을 할당하면 됩니다.

  ```python
    >>> a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
    >>> a['alice'] = 5
    >>> a
    {'alice': 5, 'bob': 20, 'tony': 15, 'suzy': 30}
  ```

  

- 여러값 수정은 update 메소드를 사용합니다. 키가 없는 값이면 추가됩니다.

  ```python
    >>> a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
    >>> a.update({'bob':99, 'tony':99, 'kim': 30})
    >>> a
    {'alice': [1, 2, 3], 'bob': 99, 'tony': 99, 'suzy': 30, 'kim': 30}
  ```

## 6. dictionary(딕셔너리) for문

- for문을 통해 딕셔너리를 for문을 돌리면 key값이 할당됩니다.

- 순서는 임의적이다.같은 순서를 보장할 수 없다.

  ```python
    >>> a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
    >>> for key in a:
    ...     print(key)
    ... 
    alice
    bob
    tony
    suzy
  ```

- value값으로 for문을 반복하기 위해서는`values()`를 사용해야합니다.

```python
    >>> for val in a.values():
  ...     print(val)
    ... 
    [1, 2, 3]
    20
    15
    30    
```

- key와 value를 한꺼번에 for문을 반복하려면 `items()`를 사용합니다.

  ```python
  >>> for key, val in a.items():
    ...     print("key = {key}, value={value}".format(key=key,value=val))
  ... 
    key = alice, value=[1, 2, 3]
    key = bob, value=20
    key = tony, value=15
    key = suzy, value=30
  ```

## 7. dictionary(딕셔너리) 의 in

- dictionary의 in은 키에 한해서 동작합니다.

  ```python
     >>> 'alice' in a
     True
     >>> 'teacher' in a
     False
     >>> 'teacher' not in a
     True
       
  ```

  ## 8. dictionary(딕셔너리)의 요소 삭제

- list와 마찬가지로 del키워드를 사용합니다.

  ```python
    >>> a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
    >>> del a['alice']
    >>> a
    {'bob': 20, 'tony': 15, 'suzy': 30}
  ```

## 9. dictionary(딕셔너리)를 읽기 쉽게 표현해주는 pprint

- pprint모듈로 dictionary를 찍어보자

  ```python
    >>> from pprint import pprint as pp
    >>> a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30,"dodo": [1,3,5,7], "mario": "pitch"}
    >>> print(a)
    {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30, 'dodo': [1, 3, 5, 7], 'mario': 'pitch'}
    >>> pp(a)
    {'alice': [1, 2, 3],
     'bob': 20,
     'dodo': [1, 3, 5, 7],
     'mario': 'pitch',
     'suzy': 30,
     'tony': 15}
  ```