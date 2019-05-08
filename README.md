# 물주 *771

```bash
$ pip freeze > requirements.txt
$ pip install -r requirements.txt
```

## 1) 기술 스택

- python

  - pandas
  - django

- javascript

  - react

- SQLite

- api

  - [카카오 지도](<http://apis.map.daum.net/web/guide/>)
  - 프로토 타이핑 툴



## 2) 데이터 수집

- [용도별 건물정보 서비스](<http://openapi.nsdi.go.kr/nsdi/eios/ServiceDetail.do?svcSe=S&svcId=S029#>)
  - 거주용 / 상업용 건물인지 판별할 수 있음
  - 각 건물의 세부 용도도 파악가능
  - 단, 행정구역코드(법정동코드)를 다 미리 수집해야함.

- [공동주택 가격속성 조회](<http://openapi.nsdi.go.kr/nsdi/eios/OperationSumryDetail.do>)
  - 거주용 건물의 다세대 주택 여부를 판별하기 위한 데이터
  - 면적 / 공시지가도 수집가능



## 3) 요구사항
### 3-1) 메인화면
- 지도+마커 -> 해당정보가 있는 페이지 (모바일도 고려)
  - 마커는 주거용, 상업용이 분류되게끔, 필터를 통해 보고싶은 것만 볼수 있도록

### 3-2) 회원가입
- 회원가입시 이메일 등록 -> 회원가입 완료 표시 및 추가정보 입력권유
- 추가 정보
  - 상호명
  - 건물주소
  - 입주 기간

### 3-3) 상세 페이지

- 평점 - 좋아요(+1), 보통(0), 싫어요(-1)
- 의견, 사진 추가

### 3-4) 게시판

- 공지사항
- Tip 게시판

### 3-5) ERD

- 건물에 대한 것 : 주소(법정동명, 지번), 건물명, 지상층수, 지하층수, 건물용도분류명, 주용도 코드
  - 주용도 코드로 마커 색깔 분류
- 유저 입력 : content, Image, Score / like
- 회원정보 : 상업/거주 분류, 장사기간 / 거주기간, 상호명

<img src = "images/image 003.png">

### 3-6) 지도

- 기본적으로 지도에 마커는 표시 해놓기
  - (호갱노노처럼) 정보가 있는 마커
- 주소 검색이나 건물명 검색으로 건물을 찾아볼 수 있게끔

### A) 메인 페이지 UI

<img src="images/image 001.png">



### B) 페이지 구성

<img src="images/image 002.png">