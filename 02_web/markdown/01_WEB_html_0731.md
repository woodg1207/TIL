# 01_WEB_0731

#단축키 

ctrl + alt 방향키 여러라인 드래그?(들여쓰기 할때 유용)

alt + shift 방향키  라인 복사



백엔드과정

요청과 응답을 처리하도록 만든다.

클라이언트가 요청을 보내는 프로그램 >> 브라우저(크롬)

## HTML(Hyper Text Markup Language)

웹페이지를 작성하기 위한 역할 표시 언어 (프로그래밍 언어가 아니다. 연산을 못함.)

- Hyper Text : 선형적인 텍스트가 아니라 순서가 없는 텍스트  (https : 통신규약)

- Markup : 문서 혹은 데이터의 구조를 명시함 



html(뼈대), css(꾸며주는 역할), javaScript(활기를 불어 넣어줌) : web관련 대표언어 

(javaScript는 프로그래밍 언어이다.)



웹 표준 : 개발을 하나로 표준화함. 

#### IE안쓰는 이유

- 웹표준을 지키지않음
- 모바일대응을하지않음
- 성능개선 X, 느림.. 

모든 사용자가 같은 브라우저를 사용하는게 아니기 때무에 IE에도 어느정도 대응을 해야 함.

-> Cross Browsing 

## html 양식

- 들여쓰기는 공백 2문자.

- 속성값에는 반드시 큰따옴표를 사용

- 태그, 속성, 속성값 등에는 모두 소문자만 사용

- 최상위 html태그에는 lang속성을 주어 문서의 기본 언어를 지정한다.

  (스크린리더는 lang을 통해 언어를 인식하여 자동으로 음서을 변환하거나 해당언어에 적합한 발음을 제공한다. )(접근성을 위함 )

- IE 는 특정 META 태그를 통해 페이지가 특정 버전에 맞게 세팅되도록 지정해 준다.

```html
<meta http-equiv="X-UA-Compatible" content="ie=edge">  
```

- boolean 속성 값은 따로 명시하지 않는다. 

```html
<input type="radio" name="sub" value="egg" checked=true>에그 마요<br>
안좋은 방법
<input type="radio" name="sub" value="egg" checked>에그 마요<br>
좋은방법
```



**시맨틱 태그** : 개발자 및 사용자 뿐만 아니라 검색엔진 등에 의미 있는 정보의 그룹을 태그로 표현하여 단순히 보여주기 위한 것을 넘어서 **의미를 가지는 태그들을 활용하기** 위한 노력

#### 1. semantic.html

```html
<style type="text/css">
  * {
    font-family: 'Source Code Pro', sans-serif;
  }

  nav,
  header,
  section,
  article,
  aside,
  footer {
    margin: 16px;
    padding: 16px;
    border-radius: 4px;
    background-color: skyblue;
    text-align: center;
  }

  nav,
  header,
  footer {
    width: 400px;
  }

  header {
    margin-bottom: 0;
  }

  footer {
    margin-top: 0;
  }

  section {
    display: inline-block;
    width: 216px;
    height: 100px;
    margin-right: 8px;
  }

  aside {
    display: inline-block;
    width: 136px;
    height: 100px;
    margin-left: 0px;
    vertical-align: top;
  }

  article {
    background-color: grey;
  }
</style>
</head>
<body>           여기부터 중요 
<!-- alt B : open in browser 확장프로그램 있으면 크롬으로 열림-->
  <header>&lt;header&gt;</header>    
  <!-- &lt, &gt ->   <> -->
  <nav>&lt;nav&gt;</nav>
  <section>
    section
    <article>
      article
    </article>
  </section>
  <aside>&lt;aside&gt;</aside>
  <footer>&lt;footer&gt;</footer>
</body>
</html>
```



#### 2.index.html

기능

```html
<body>
  <!-- heading -->
  <!-- h1은 페이지당 1개 -->
  <h1>hi, h1</h1>
  <h2>hi, h2</h2>
  <h3>hi, h3</h3>
  <h4>hi, h4</h4>
  <h5>h5, h5</h5>
  <h6>Hi, h6</h6>

  <!-- bold -->
  <div>
    <b>This is bold.</b>
    <strong>this is strong.(semantic),강조하는 의미가 있다.</strong>
  </div>

  <!-- italic -->
  <div>
    <i>This is italic</i>
    <em>This is em.(semantic) 강조하는 의미 </em>
  </div>

  <!-- highlighted-->
  <h2>This is <mark>Mark</mark>.</h2>

  <!-- del/ ins -->
  <h2>this is <del>del</del></h2>
  <h2>this is <ins>ins</ins></h2>

  <!-- sub/ sup -->
  <h2>this is <sub>sub</sub></h2>
  <h2>this is <sup>sup</sup></h2>

  <!-- p/ br -->
  <p>
    This is p tag.<br>
    This is     p tag.<br>
    This is     p tag.<br>
    This is     p tag.<br>
    this is p tag.
  </p>
  <hr>
  <!-- pre -->
  <pre>
    from flask import flask
    app = Flask(__name__)

    @app.route('/')
    def hello('/'):
      return 'hello world'
  </pre>
  <!-- headline -->
  <hr>
  <!-- q/ blockquote -->
  <p>
    Juno, said <q>Hi there!</q>
  </p>
  <blockquote>
    HI, There! 인용문 쓸때(들여쓰기)
  </blockquote>
  <!-- ol/ ul/ li -->
  <ol>
    <li>first</li>
    <li>second</li>
    <li>third</li>
    <li>fourth</li>
  </ol>
  <ul>
    <li>first</li>
    <li>second</li>
    <li>third</li>
    <li>fourth</li>
  </ul>

</body>
</html>
```



#### 3 markup.html

```html
<body>
  <header>
    <h1>프로그래밍 교육</h1>
    <a href="#python"><img src="images/python.png" alt="python img" style="width:50px; heigth:50px"></a>
    <!-- alt값 반드시 넣어줘야한다.  또는 빈칸은  "#" 을 넣어줘야한다.  -->
    <!-- id값을 접근 -->
    <a href="#web"><img src="images/html5.png" alt="html img" style="width:50px; height:50px"></a>
    <a href="index.html">참고 사이트</a>
    <!-- 내부링크로 이동 -->
  </header>

  <hr>
  <article>
    <a href="https://docs.python.org/3/" target="_blank" id="python">파이썬</a>
    <h3>Number type</h3>
    <p>파이썬에서 숫자형은 아래와 같이 쓸수 있다. </p>
    <ol>
      <li>int</li>
      <li>float</li>
      <li>complex</li>
      <li><del>str</del></li>
    </ol>
    <h2>sequence</h2>
    <p>파이썬에서 시퀀스는 아래와 같이 있다.</p>
    <strong>시퀀스는 for문을 돌릴수 있다!!</strong>
    <ol>
      <!-- w3school or MDN 에서 문서 공부 -->
      <li style="list-style-type: circle">str</li>
      <li style="list-style-type:square">list</li>
      <li style="list-style-type:lower-alpha">tuple</li>
      <li style="list-style-type: lower-roman">range</li>
    </ol>
  </article>
  <hr>
  <header>
    <h2><a href="https://developer.mozilla.org/ko/" id="web">웹</a></h2>
  </header>
  <article>
    <h3>기초</h3>
    <ul>
      <!-- type="circle" -->
      <li style="list-style-type: circle">html</li>
      <li style="list-style-type: circle">CSS</li>
    </ul>
    <a href="mailto:wdj1207@naver.com">메일보내기</a>
  </article>
  <iframe width="914" height="514" src="https://www.youtube.com/embed/ByHNlfmmT-w" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</body>

</html>
```



#### 4.table.html

```html
<body>
  <table border="1px solid black" summary="2019년 7월 마지막 주 월화수 점심메뉴 표입니다.">
    <caption>유성연수원 20주차 점심 메뉴표</caption>
    <thead>
      <tr>
        <!-- table row : 행 -->
        <th></th> <!-- table header : 자동으로 bold로 출력-->
        <th>월</th>
        <th>화</th>
        <th>수</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>A 코스</td> <!-- table data : 열-->
        <td rowspan="2">짬뽕</td>
        <!-- rowspan 행을 2칸 -->
        <td colspan="2">초밥</td>
        <!-- colspan 열을 2칸차지 -->
      </tr>
      <tr>
        <td>B 코스</td>
        <td>김치찍개</td>
        <td>삼계탕</td>
      </tr>
    </tbody>
    <tfoot>    <!-- table 에서 한번만 쓸수 있다. -->
      <tr>
        <td>식수</td>
        <td colspan="3">총 150명 식사</td>
      </tr>
    </tfoot>
  </table>
</body>

</html>
```



#### 5.festival.html

```html
<body>
  <table summary="2019년 공연 타임 테이블입니다. 내부 소극장 외부 잔디마당과 대공연장 총 3곳에서 10시부터 17시까지 공연하는 시간표입니다.">
    <caption><h1>2019 타임테이블</h1></caption>
    <thead>
      <tr>
        <th>TIME</th>
        <th>INDOOR</th>
        <th colspan="2">OUTDOOR</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td></td>
        <td>소극장</td>
        <td>잔디마당</td>
        <td>대공연장</td>
      </tr>
      <tr>
        <td>10:00</td>
        <td rowspan="2">안녕하신가영</td>
        <td></td>
        <td>10CM</td>
      </tr>
      <tr>
        <td>13:00</td>
        <td rowspan="2">선우정아</td>
        <td rowspan="2">참깨와솜사탕</td>
      </tr>
      <tr>
        <td>15:00</td>
        <td></td>
      </tr>
      <tr>
        <td>17:00</td>
        <td>크러쉬</td>
        <td></td>
        <td>폴킴</td>
      </tr>
    </tbody>
  </table>
</body>
</html>
```

#### 6 form.html

```html
<body>
  <form action="#">
    <label for="text">TEXT</label>
    <input type="text" id="text" placeholder="내용을 입력해주세요"><br>
    <label for="number">NUMBER</label>
    <input type="number" id="number"><br>
    PASSWORD: <input type="password"><br>
    EMAIL: <input type="email"><br>
    DATE: <input type="date"><br>
    <input type="radio" name="language" value="1">HTML<br>
    <input type="radio" name="language" value="2">CSS<br>
    <input type="radio" name="language" value="3">JS<br>
    <select name="country">
      <option value="1">한국</option>
      <option value="2">중국</option>
      <option value="3">미국</option>
    </select> <br>
    <input type="checkbox" name="option" value="1"> 1
    <input type="checkbox" name="option" value="2"> 2 <br>

    <input type="submit">
  </form>
</body>

</html>
```



#### 7 subway.html

```html
<body>
  <h1>FORM</h1>
  <form action="#">
    <p> 주문서를 작성하여 주십시오 </p>
    이름: <input type="text" id="text" placeholder="이름을 입력해주세요"><br>
    날짜: <input type="date"><br>
    <h3>1. 샌드위치 선택</h3><br>
    <input type="radio" name="sub" value="egg" checked>에그 마요<br>
    <input type="radio" name="sub" value="bmt">이탈리안 비엠티<br>
    <input type="radio" name="sub" value="bacon">터키베이컨 아보카도
    <hr>
    <h3>2. 사이즈 선택</h3><br>
    <input type="number" min="15" max="30" step="15" >
    <hr>
    <h3>3. 빵</h3>
    <select name="bread" id="">
      <option value="1">허니오트</option>
      <option value="2" disabled>플랫 브레드</option>
      <option value="3">하티 이탈리안</option>
    </select>
    <hr>
    <h3>4. 야채/소스</h3>
    <input type="checkbox" name="" id="">토마토 <br>
    <input type="checkbox" name="" id="">오이<br>
    <input type="checkbox" name="" id="">할라피뇨<br>
    <input type="checkbox" name="" id="">핫 칠리<br>
    <input type="checkbox" name="" id="">바베큐<br>
    <br>
    <input type="submit" value="submit">
  </form>
</body>
</html>
```

