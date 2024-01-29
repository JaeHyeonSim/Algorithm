# [Silver III] 놀라운 문자열 - 1972 

[문제 링크](https://www.acmicpc.net/problem/1972) 

### 성능 요약

메모리: 31120 KB, 시간: 76 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 구현, 문자열

### 제출 일자

2024년 1월 30일 01:37:24

### 문제 설명

<p>The D-pairs of a string of letters are the ordered pairs of letters that are distance D from each other. A string is D-unique if all of its D-pairs are different. A string is surprising if it is D-unique for every possible distance D.</p>

<p>Consider the string ZGBG. Its 0-pairs are ZG, GB, and BG. Since these three pairs are all different, ZGBG is 0-unique. Similarly, the 1-pairs of ZGBG are ZB and GG, and since these two pairs are different, ZGBG is 1-unique. Finally, the only 2-pair of ZGBG is ZG, so ZGBG is 2-unique. Thus ZGBG is surprising. (Note that the fact that ZG is both a 0-pair and a 2-pair of ZGBG is irrelevant, because 0 and 2 are different distances.)</p>

### 입력 

 <p>The input consists of one or more nonempty strings of at most 79 uppercase letters, each string on a line by itself, followed by a line containing only an asterisk that signals the end of the input.</p>

<p> </p>

### 출력 

 <p>For each string of letters, output whether or not it is surprising using the exact output format shown below.</p>

