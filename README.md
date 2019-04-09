# 물주 *771

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