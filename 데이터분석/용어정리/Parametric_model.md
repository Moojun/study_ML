> 참고: [An Introduction to Statistical Learning-second edition](https://www.statlearning.com/), [GeeksforGeeks](https://www.geeksforgeeks.org/difference-between-parametric-and-non-parametric-methods/), [유니의 공부 블로그](https://process-mining.tistory.com/131)

## Parametric method vs Non-Parametric method

머신러닝(데이터분석)을 공부하던 중, Parametric/Non-Parametric method, Parametric/Non-Parametric model 과 같은 단어들이 자주 보여서, 이것들을 알아보겠다.

### 정의

**Parametric method**
* The basic idea behind the parametric method is that there is a set of fixed parameters that uses to determine a probability model that is used in Machine Learning as well.
* But in general, fitting a more flexible model requires estimating a greater number of parameters. These more complex models can lead to a phenomenon known as **overfitting** the data.
* 쉽게 정의하면, 파라미터의 수가 정해진 방법이다. 즉, 데이터가 특정한 모델을 따른다고 가정하고, 그것의 고정된 개수의 파라미터들을 학습시켜 튜닝하는 것이다.
* Non-Parametric model에 비해 flexible하지 않다.(flexibility가 낮다)

**Non-Parametric method**
* Non-Parametric methods do not make explicit assumptions about the functional form of *f.*
* Instead, they seek an estimate of *f* that gets as close to the data points as possible without being too rough or wiggly.
* But, since non-parametric approaches do not reduce the problem of estimating *f* to a small number of parameters, a very large number of observation is required in order to obtain an accurate estimation for *f*.
* 쉽게 정의하면, 데이터가 특정 분포를 따른다는 가정이 없으므로 우리가 학습에 따라 튜닝할 파라미터가 명확하게 정해져 있지 않은 것이다. 따라서 이 방법은 data에 대한 사전 지식이 전혀 없을 때 유용하게 사용할 수 있다. 
* parametric method에 비해 더 flexible하다.


**Parametric model**

* Linear regression, Logistic regression, Neural network(CNN, RNN), etc.

**Non-Parametric model**

* Random forest, K-nearest neighbor (k-NN)classifier, etc. 

