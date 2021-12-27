# 2021 2학기 오픈소스소프트웨어 수업 

<br><br>

## 1주차. git, github, MARKDOWN
### git : 버전 관리 시스템
* commit : 프로젝트 디렉토리의 특정 모습을 하나의 버전으로 남기는 행위 및 결과물
* repository : commit이 저장되는 곳
* git을 GUI(Graphic User Interface) 환경에서 사용하도록 도와주는 프로그램 : sourcetree, tortoisegit ...  

<br>

* the three areas in Git where code lives : working directory, staging area, repository
* 원격 레포지토리 or 리모트(remote) 레포지토리 = github의 레포지토리 
* 로컬 레포지토리 = 내 컴퓨터의 레포지토리 

### Sourcetree
* Stage hunk : it is being added to the staging area, Discard Hunk : remove the change without trace.  
* The conclusion is that Replace the word 'hunk' with 'change' and it becomes pleasurable to follow Git.


<br><br>

### MARKDOWN : A lightweight markup language for formatted documents
* File extension : .md or .markdown
* useful tool : sublime text, Typora ... 
* reference sites : <https://gist.github.com/ihoneymon/652be052a0727ad59601>

<br><br>

## 2주차. Python_01
### Python is an interpreted, high-level, general-purpose programming language.
* What can i do with python? <https://realpython.com/what-can-i-do-with-python/>
* Date types, Operators, Flow control, Function definition, Object-oriented Programming


<br><br>

## 3주차. Python_02
### 2 principles(tips)
> 1. Take advantages of python itself (a.k.a Pythonic)
> 2. Utilize the existing libraries and master them if they are useful  

* Data types(include complex, None) 
* String formatting, trimming, splitting
* Compound data types : list, set, tuple, dict  + (str)
* lambda expression, list comprehension
* Flow control : pass(no action), indent instead of bracket
* Function definition : Keyword argument association
* Object-oriented Programming : inheritance, private member definition
* file input and output
* Exception handling
* Package import

<br><br>
## 4주차. python 03
### standard library
* math : Mathematical Functions
* decimal : Decimal Fixed-point and Floating-point Arithmetic
* random : Pseudo-random Number Generators
* time : Time Access and Conversions
* glob : Unix-style Pathname Pattern Expansion
* fnmatch : Unix-style String Pattern Matching
* csv : CSV File Reading and Writing
* pickle : Python Object Serialization
* tkinter : Python Interface to Tcl/Tk GUI toolkit
* turltle : Turtle Graphics for Programming Education
* Beyond the python standard library
  * pip install package_name

<br><br>
## 5주차. python mathematics : Calculus(미적분학)
* Visualization
   * Matplotlib : A plotting library in python
   * <b>Visualization</b> is very important not only for data but also for programs, systems and society
* Differentitation(미분)
   * Meaning
     * The slope of the tangent line (plane) to the given function
     * The tangent line ~ linear approximation
   * How to get a derivative(도함수)
     * By manual ways using derivative formula(polynomial rule, chain rule, etc)
     * Analytical differentiation using SymPy
     * Numerical differentiation : an algorithm to approximate a derivative value of a function using values of the function

<br><br>
## 6주차. python mathematics : linear algebra(선형대수학)
* Algebra is the study of mathematical objects and their manipulating rules (e.g. arithmetic operations).
* Linear algebra is the mathematical branch on linear equations represented in vector spaces.
   * Linear equation(1차 방정식)
   * Vector space(linear space) : Scalar, Vector, Matrix
   * Matrix : Matrix multiplication, Matrix inverse, etc..
* Numpy library : A matrix library in python 
* Application : LIne and curve fitting(회귀분석)

<br><br>
## 7주차. python mathematics : optimization(최적화)
* Non-linear optimization
   * gradient descent(경사 하강법) : using the 1st-order approximation and the given step size.
   * Newton's method : using the 2nd-order approximation without the step size.
   * use library 'scipy.optimize' for optimization without derivatives. 
* Selecting an objective function is important 
   * e.g. algebraic distance vs geometric distance in line fitting.




