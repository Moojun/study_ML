# 머신 러닝 공부
* 본 리포지토리는 인프런 [파이썬 머신러닝 완벽 가이드](https://www.inflearn.com/course/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-%EC%99%84%EB%B2%BD%EA%B0%80%EC%9D%B4%EB%93%9C/dashboard) 강의 내용을 기록한 것입니다.
* [참고 코드 출처](https://github.com/chulminkw/PerfectGuide)
* 교재 : '파이썬 머신러닝 완벽 가이드'
* Tip) [마크다운 문서 내부 링크 이동](https://young-cow.tistory.com/21)

| 목차 | 내용 | 
| :------------: | :-------------: |
| **1장** | **파이썬 기반의 머신러닝과 생태계 이해(numpy, pandas)** | 
| Content Cell | Content Cell |
| Content Cell | Content Cell |
| Content Cell | Content Cell |
| 1.4 | 데이터 셀렉션 및 필터링(pandas) : []연산자, iloc, loc, 불린 인덱싱  |
| 1.5 | pandas 그 외 : Aggregation 함수(sum, mean, count, ...), groupby()함수, 결손 데이터 처리, apply lambda식 |
|  **2장** | **사이킷런으로 시작하는 머신러닝**, [요약](#2장-요약) |
| 2.1 | 붓꽃(iris) 품종 예측 |
| Content Cell | Content Cell |
| Content Cell | Content Cell |
| Content Cell | Content Cell |





### 2장 요약
#### 머신 러닝 지도 학습 프로세스
1. 데이터 전처리
   * 데이터 클린징
   * 결손값 처리(Null/NaN 처리)
   * 데이터 인코딩(레이블, 원-핫 인코딩)
   * 데이터 스케일링
   * 이상치 제거
   * Feature 선택, 추출 및 가공
2. 데이터 세트 분리
   * 학습 데이터/테스트 데이터 분리
     * 교차 검증(e.g. 여러번 보는 모의고사), cross_val_score(), GridSearchCV
3. 모델 학습 및 검증 평가
   * 알고리즘 학습
4. 예측 수행
   * 테스트 데이터로 예측 수행
5. 평가
   * 예측 평가
