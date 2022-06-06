## 아나콘다로 tensorflow 설치하기(windows)
<hr>

* tensorflow version 2.x를 설치하는 것 : 구글링으로 쉽게 설치할 수 있음. 하지만  인공지능 수업에서 1.x 버전을 사용하기 때문에 1.x 버전을 설치하려함.
* tensorflow version 2.x , 1.x verison은 문법에서 일부 차이가 있다. 


* conda 가상환경 명령어 모음 (anaconda prompt를 관리자 권한으로 실행)
  * 현재 가상환경 목록 확인 : conda info --envs
  * 가상환경 삭제 : conda remove -n 가상환경이름 --all 
  * 가상환경 생성 : conda create --name 가상환경이름 python=3.7 
  * 가상 환경에 진입(활성화) : conda activate 가상환경이름
  

### tensorflow version 1.15 설치 
#### 1. gpu 환경 x, Anaconda prompt (base)에 tensorflow 설치
매우 간단하다.  
pip install tensorflow==1.15 입력 후 jupyter notebook을 실행하면 바로 실행되는 것을 확인할 수 있다.  
'> pip freeze를 통해 tensorflow 및 그 외 라이브러리 버전 확인 가능   
'> pip uninstall tensorflow : 삭제


#### 2. gpu 환경 파이참에 anaconda 연동해서 tensorflow 실행

  1. 새로운 가상환경 만들기 : conda create --name tensorflow1.x python=3.7
  2. 생성된 가상환경 확인 : conda info --envs
  3. 가상 환경에 진입(활성화) : conda activate tensorflow1.x
  4. tensorflow 1.15버전 설치 : conda install tensorflow==1.15
  5. 텐서플로(TensorFlow)의 설치가 완료되면, 파이썬(Python)을 실행해서 설치된 텐서플로(TensorFlow)의 버전을 확인한다.  
     1. '> python(파이썬 실행)
     2. '>>>> import tensorflow as tf
     3. '>>>> tf.__version__
     4. '>>>> exit()
  6. 이후 필요한 라이브러리들 추가로 설치
     1. conda install pandas
     2. conda install seaborn
     3. conda install keras
     4. etc..
     
  7. 가상환경 비활성화 : conda deactivate
  8. 파이참에 anaconda 연동해서 tensorflow 실행
     1. (base)에서 conda info --envs 명령어를 통해 가상환경 폴더의 위치 확인  <br><br>
     ![image](https://user-images.githubusercontent.com/80478750/149560059-71d13927-d52b-4ad2-8bd4-c797e1a50687.png)

     2. New Project를 통해 Create Project 화면으로 들어간 뒤, Previously configured interpreter를 선택 후, 맨 오른쪽에 '...'선택  <br><br>
     ![image](https://user-images.githubusercontent.com/80478750/149560247-42cca848-3304-4423-9577-e4186bb574a3.png)
     
     3. Conda Environment 선택, conda info --env 명령으로 확인한 경로에서 python.exe를 찾아 연결한다. <br><br>
     ![image](https://user-images.githubusercontent.com/80478750/149560609-e356b751-e729-4595-bc21-543c3a67842b.png)

     4. 연결된 것을 확인후, 생성한다. <br><br>
        ![image](https://user-images.githubusercontent.com/80478750/149560706-1f17900f-af92-4afb-ada0-087835add27d.png)
       
     5. 정상적으로 실행됨을 확인. <br><br>
     ![image](https://user-images.githubusercontent.com/80478750/149560989-d4535890-9bd9-42a9-ac08-9aadd9a58be9.png)
     

