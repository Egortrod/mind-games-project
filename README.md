### Сodeclimate:
<a href="https://codeclimate.com/github/Egortrod/mind-games-project/maintainability"><img src="https://api.codeclimate.com/v1/badges/3ed57a1dde9b2423eaab/maintainability" /></a>

### Discription:
The Brain Games project consists of 5 mini-games that run from the console. Each task is logic-based and run with the following commands:

   ### 1.Calculate
Correctly solve the provided expression, which can only contain addition subtraction and multiplication operations

### Asciinema of calculate game features:
https://asciinema.org/a/rUkRkLl7vlf88jhHxMevWrE8i

2. arithmetic progression: put the correct number\nin the missing place, using the laws of arithmetic progression
3. geometric progression: put the correct number\nin the missing place, using the laws of geometric progression
4. divisor: determine the greatest common divisor of two numbers 
5. prime number: determine whether a given number is prime or not

### Installation (ssh):
```
git clone git@github.com:Egortrod/mind-games-project.git
cd mind-games-project
make install
make package-install
```

### Problems:
1. There are no difficulties in games 2-5;
2. There is no victory counter;
3. There is no configured pyproject;
4. Not everywhere there are alerts for incorrect conclusions;
5. There is no customized README file; 
6. Need to refactor all scripts in /games (dup blocks).

