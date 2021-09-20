<div align="center">
 <h2> 

 🚗 __서울시 도로 열선 시스템 입지 선정__ 🚗  
 </h2>

__공공빅데이터__ 인턴십 실무형 프로젝트<br>
2021.08.02 ~ 2021.08.19 17:00<br>
서울2 38조<br>
__이채훈, 이주천, 정성훈, 임세준, 이상민, 정선경__
<br><br>
<img src="https://github.com/commanderk9826/G-BIG_HACKATHON_4TH/blob/main/IMAGE/%EC%88%98%EB%A3%8C%EC%A6%9D.png" width="300" height="450">

 
  데이터 기반 행정으로 <br> 
  국민의 삶의 질을 개선하라!
  
  <h2>

  G-BIG HACKATHON 4TH<br>**우수상 수상작**
  
  
  <br>
 <h2>

⚒️ **TECH STACK** 
  <br><br>
  <img src="https://github.com/commanderk9826/G-BIG_HACKATHON_4TH/blob/main/IMAGE/TECHSTACK.png" width="450" height="150">
 
<br><br>
</div>
<h2>

📃 **SUMMARY**

<h3>

**1. 주제 선정 배경**
</h3>

**일반 교통 사고 대비 높은 사망률**(일반도로 사고 대비 사망률이 3.2배를 상회)
<br>

**보행 취약계층 관련 사고**
(낙상사고 발생률이 지속적으로 증가
하지만 관련 정책과 사고 예방 방안은 미흡)
<br><br>
<h3> 

**✍ 해결방안으로서의 도로열선**
</h3>

기존 도로 제설제와 비교하였을 때, **도로열선은 매우 친환경적** <br><br>
**성북구, 성동구 시범 설치**를 통해, 효과성 검증후 단계적 확대 예정 <br><br>
설치 기준 문의결과 **정확한 기준이 정해져 있지 않음**
<br> 
<br>
<div align="center">
<h3>

💣 "머신러닝"을 통해 💣<br> **서울시 도로 열선 설치 명확한 기준 제시**
</h3>
</div><br>

<h3> 

**2. 분석 개요**
</h3>

**열선 설치 기준 요인**

위험 구역을 **차량도로/보행도로** 두 가지 관점에서 선정.<br><br>

**🔴 차량 도로 결빙 위험 구역 선정 요인**<br>
제설함 개수, 신호등 개수, 버스정류장 개수, 경사도, 기타 도로 변수
<br><br>
**🔵 보행 도로 결빙 위험 구역 선정 요인**<br>
행정동별 보행취약계층 시설 비율, 행정동별 보행취약계층 인구 비율, 경사도
<br><br>
**👣 보행취약계층 👣**<br>
보행취약계층의 범위를 사고 발생 시 일반인에 비해 사고비율이 높은<br> 
**어린이(12세 이하), 노인(65세 이상~), 장애인** 계층으로 지정

<br>
<h3> 

**3. 분석 과정**
</h3>

**GIS 매칭 및 속성 결합<br>
데이터 전처리(결측치 및 이상치 처리)<br>
LGBM<br>
CLUSTERING(K-MEANS, HIERARCHICAL, DASACN, GMM)**

**🔴 차량도로 분석내용**<br>

👉 실제 열선을 설치한 지역인 성북구, 성동구의 데이터를 기준으로 결빙사고 위험도를 예측하는 모델 개발<br><br>
👉 특정 구를 기반으로 학습된 예측 모델을 바탕으로 서울시 전체 차량 도로에 적용<br><br>
👉 도출한 도로별 결빙사고 위험도 수치를 서울시 전체 행정동에 변환하여 적용 


<br> 

**🔵 보행도로 분석내용**<br><br>
👉 보행취약계층 인구 비율, 보행취약계층 시설 비율, 경사도 데이터를 활용해 클러스터링을 통한 보행취약 위험도 산출<br><br> 
👉 각 모델에서 선정된 행정동을 점수화 한 후, 최종 클러스터 점수 반환<br><br>

<div align="center">

**💣 최종 행정동 선정 💣**<br>
선정된 행정동 내에서<br>
**[차량도로] 결빙사고 위험도 0.8↑**<br>
**[보행도로] 경사도 3↑ & 보행취약계층 시설 교차 지점**
<br>최종 입지 선정
</div>
<br><br>

<h3> 

**4. 분석 결과**
</h3>

**🔴 연희동_차량도로**<br><br>
<img src="https://github.com/commanderk9826/G-BIG_HACKATHON_4TH/blob/main/IMAGE/%EB%B6%84%EC%84%9D%EA%B2%B0%EA%B3%BC1.PNG" width="540" height="300">
<br><br>

**🔵 연희동 보행도로**<br><br>
<img src="https://github.com/commanderk9826/G-BIG_HACKATHON_4TH/blob/main/IMAGE/%EB%B6%84%EC%84%9D%EA%B2%B0%EA%B3%BC2.PNG" width="540" height="300"><br><br>

<h3> 

**5. 활용 방안**
</h3>

**👉 입지 선정 기준 제시**(기존의 불분명한 도로 열선 입지 선정기준을 순위 최적화 프로세스를 통해 효율적인 입지 선정 기준 제시)<br><br>
**👉 도로 열선 전국 확대 설치**(분석 프로세스를 전국적으로 확대 적용한다면 겨울철 도로 결빙으로 인한 사고율을 낮출 수 있을 것으로 기대)<br><br> 
**👉 선제적인 사고 예방 조치**(도로 열선으로 사전에 제설 작업을 진행하여 결빙으로 인한 사고 발생을 예방)<br><br>
**👉 분석결과 민원 접수**(열선 도로 입지 선정 결과 중 ‘연희동’ 에서 선정된 도로를 분석 내용과 함께 서대문구에 민원 접수)
<br><br>
<img src="https://github.com/commanderk9826/G-BIG_HACKATHON_4TH/blob/main/IMAGE/%ED%99%9C%EC%9A%A9%EB%B0%A9%EC%95%881.PNG" width="450" height="300">



<br><br>
<h3> 

**6. 참고 문헌**
</h3>
[1] 홍현기. (2014). 도로 노면 결빙 사고 원인 분석(국내석사). 서울시립대학교 일반대학원, n.p..<br>
[2] 이상준. (2017). 결빙구간의 교통사고 심각도 영향 요인 연구 (pp. 150-156). 한국안전학회: 한국산업안전학회.<br>
[3] Chang, C., Ho, M., Song, G., Mo, Y.-L., &amp; Li, H. (2009).
A feasibility study of self-heating concrete utilizing carbon nanofiber heating elements. Smart Materials and Structures, 18(12), 127001. 
<br>[4] Lee, D.-H., Jeong, W.-S., Kim, H.-J., Kim, J. (2013). 
Study about the evaluation of Freezing risk Based road surface of solar radiation. Journal of the Korea Institute for Structural Maintenance and Inspection, 17(5), 130–135. 
<br>[5] 정책브리핑. (2019, November 28). 2018 재해연보. 대한민국 정책브리핑.
<br>[6] Lee, H., Jeon, C., Kim, J., Shim, J.; Jeon, I. (2015).
Estimation of service life for Expressway BRIDGE subjected to chloride ingress from DE-ICER. Journal of The Korean Society of Disaster Information, 11(4), 548–555 
<br>[7] 한지은. (2020, December 4). 낙상사고 30% 이상 겨울에 발생..."주머니에 손 넣지 마세요". 연합뉴스
<br>[8] 도로명 및 건물번호 부여 업무처리요령

<br><br><br><br>
<div align="center">
<h2>

⚙️ **PROCESS_VISUALIZATION**
</h2>

<h3>

**🔴 차량도로 열선 설치 입지 선정을 위한 프로세스([Case1.py](https://github.com/commanderk9826/G-BIG_HACKATHON_4TH/blob/main/DATA/CODE/Case1.py))**
<br><br>
<img src="https://github.com/commanderk9826/G-BIG_HACKATHON_4TH/blob/main/IMAGE/PROCESS1.png" width="500" height="300">
<br>
<br>

**🔵 보행도로 열선 설치 입지 선정을 위한 프로세스([Case2.py](https://github.com/commanderk9826/G-BIG_HACKATHON_4TH/blob/main/DATA/CODE/Case2.py))**<br><br>
<img src="https://github.com/commanderk9826/G-BIG_HACKATHON_4TH/blob/main/IMAGE/PROCESS2.png" width="500" height="150">
<br>
<br>

**💣 최종도로 열선 설치 입지 선정을 위한 프로세스**<br><br>
<img src="https://github.com/commanderk9826/G-BIG_HACKATHON_4TH/blob/main/IMAGE/PROCESS3.png" width="500" height="300">
</h3>
<br>
<br>
<h2>

✏️ **OUTPUT & DATA & CODE**
</h2>
<h4> 자세한 분석 내용은 항목별 링크 내 파일들 참고<br><br>

[📕 OUT PUT](https://github.com/commanderk9826/G-BIG_HACKATHON_4TH/tree/main/OUTPUT)
<br>

[📗 DATA](https://github.com/commanderk9826/G-BIG_HACKATHON_4TH/tree/main/DATA/FINAL%20DATA)
<br>


[📘 CODE](https://github.com/commanderk9826/G-BIG_HACKATHON_4TH/tree/main/DATA/CODE)

</h4>





  


