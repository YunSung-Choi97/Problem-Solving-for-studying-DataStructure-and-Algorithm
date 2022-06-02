# 11 정렬

|문제 번호|문제 제목|문제 풀이|
|:---:|---|:---:|
[2750](https://www.acmicpc.net/problem/2750)|수 정렬하기|[python](2750.py)
[2751](https://www.acmicpc.net/problem/2751)|수 정렬하기 2|[python](2751.py)
[10989](https://www.acmicpc.net/problem/10989)|수 정렬하기 3|[python](10989.py)
[2108](https://www.acmicpc.net/problem/2108)|통계학|[python](2108.py)
[1427](https://www.acmicpc.net/problem/1427)|소트인사이드|[python](1427.py)
[11650](https://www.acmicpc.net/problem/11650)|좌표 정렬하기|[python](11650.py)
[11651](https://www.acmicpc.net/problem/11651)|좌표 정렬하기 2|[python](11651.py)
[1181](https://www.acmicpc.net/problem/1181)|단어 정렬|[python](1181.py)
[10814](https://www.acmicpc.net/problem/10814)|나이순 정렬|[python](10814.py)
[18870](https://www.acmicpc.net/problem/18870)|좌표 압축|[python](18870.py)

---

## Summary

### 딕셔너리

- .keys() / .values() / .items()

 > 딕셔너리의 모든 key값과 value값에 대한 정보를 얻을 수 있다.<br>
 keys() : 딕셔너리의 모든 key값을 객체 dict_keys로 반환한다.<br>
 values() : 딕셔너리의 모든 value값을 객체 dict_values로 반환한다.<br>
 items() : 딕셔너리의 모든 key와 value 쌍을 객체 dict_items로 반환한다.

- .get()

 > key값이 입력 파라미터인 value를 반환한다. 존재하지 않으면 None을 반환한다.<br>
 .get(value1, value2) : val1을 key값으로 하는 value를 반환하고, 존재하지 않는다면 val2를 반환한다.

- .update() / .setdefault()

 > 딕셔너리에 key-value를 추가하는 함수<br>
 update(*key*=*value*) : 입력받은 key에 대응하는 value값을 수정하고, key가 없다면 key-value 쌍을 추가한다. 또한, 여러 개를 동시에 추가할 수 있다.<br>
 setdefault(*key*, *value*) : 입력받은 key-value 쌍을 추가한다. 입력 파라미터가 하나인 경우 key로 처리되고 value로 None이 저장된다.

- .pop() / .popitem()

 > 딕셔너리에 key-value를 제거하는 함수<br>
 pop() : 입력받은 key에 대응하는 value값을 반환하고, 딕셔너리에서 key-value를 제거한다. 입력 파라미터가 두개인 경우 key가 딕셔너리 내에 없을 때 두번째 파라미터가 반환값이 된다.<br>
 popitem() : 마지막 key, value 쌍을 반환하고, 딕셔너리에서 제거한다.

- .clear()

 > 딕셔너리의 모든 key, value를 삭제.

- .copy()

 > 딕셔너리를 복사하여 반환하는 함수.<br>
 같은 객체가 되지 않으며 복사할 때 사용된다.

<br>

### 함수

- enumerate()

> 순서가 있는 자료형을 입력받고, 인덱스와 값을 함께 enumerate 객체로 반환한다.<br>
일반적으로 for문과 함께 자주 사용된다.<br>
list, tuple, dict, string 등을 입력받아 인덱스와 값을 리턴하고, 입력값이 dict형인 경우 인덱스와 key-value를 함께 리턴한다.