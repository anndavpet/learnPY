<h1>Here I solved all sorts of exercises from Sergey Balakirev</h1>

<div class="step-inner page-fragment">
    <div id="ember2978" class="html-content rich-text-viewer ember-view" data-processed=""><!----><span><p><strong>7_11_0.py</strong> Объявите функцию с именем get_sq, которая вычисляет площадь прямоугольника по двум параметрам: width и height - ширина и высота прямоугольника. И возвращает результат (сама ничего на экран не выводит). То есть, функция имеет сигнатуру:</p>

<p>def get_sq(width, height): ...</p>

<p>Определите декоратор func_show для этой функции, который отображает результат на экране в виде строки (без кавычек):</p>

<p>"Площадь прямоугольника: &lt;значение&gt;"</p>

<p>Вызывать функцию и декоратор не нужно, только объявить. Применять декоратор к функции также не нужно.</p></span></div>

<div class="step-text-wrapper">
          <p class="step-text__limit-title">
            <strong>Sample Input<!---->:</strong>
          </p>
          <pre class="step-text__limit-value">8 11</pre>
          <p class="step-text__limit-title">
            <strong>Sample Output<!---->:</strong>
          </p>
          <pre class="step-text__limit-value">Площадь прямоугольника: 88</pre>

<!---->      </div>


https://github.com/anndavpet/learnPY/blob/main/7_11_0.py




<hr> 
<div class="step-inner page-fragment">
    <div id="ember2997" class="html-content rich-text-viewer ember-view" data-processed=""><!----><span><p><strong>7_11_1.py </strong>На вход программы поступает строка с названиями пунктов меню, записанные в одну строчку через пробел. Необходимо задать функцию с именем get_menu, которая преобразует эту строку в список из слов и возвращает этот список. Сигнатура функции, следующая:</p>

<p>def get_menu(s): ...</p>

<p>Определите декоратор для этой функции с именем show_menu, который отображает список на экран в формате:<br>
1. Пункт_1<br>
2. Пункт_1<br>
...<br>
N. Пункт_N</p>

<p>Примените декоратор show_menu к функции get_menu, используя оператор @. Более ничего в программе делать не нужно. Сами функции не вызывать.</p></span></div>

<div class="step-text-wrapper">
          <p class="step-text__limit-title">
            <strong>Sample Input<!---->:</strong>
          </p>
          <pre class="step-text__limit-value">Главная Добавить Удалить Выйти</pre>
          <p class="step-text__limit-title">
            <strong>Sample Output<!---->:</strong>
          </p>
          <pre class="step-text__limit-value">1. Главная
2. Добавить
3. Удалить
4. Выйти</pre>

<!---->      </div>
https://github.com/anndavpet/learnPY/blob/main/7_11_1.py
<hr>
<div id="ember3422" class="html-content rich-text-viewer ember-view" data-processed=""><!----><span><p><strong>7_11_2.py. </strong> На вход программы поступает строка из целых чисел, записанных через пробел. Напишите функцию get_list, которая преобразовывает эту строку в список из целых чисел и возвращает его. Определите декоратор для этой функции, который сортирует список чисел по возрастанию. Результат сортировки должен возвращаться при вызове декоратора.</p>

<p>Вызовите декорированную функцию get_list и отобразите полученный отсортированный список lst командой:</p>
    

<p><code>print(*lst)</code></p></span></div>
    <div class="step-text-wrapper">
          <p class="step-text__limit-title">
            <strong>Sample Input<!---->:</strong>
          </p>
          <pre class="step-text__limit-value">8 11 -5 4 3 10
</pre>
          <p class="step-text__limit-title">
            <strong>Sample Output<!---->:</strong>
          </p>
          <pre class="step-text__limit-value">-5 3 4 8 10 11</pre>

<!---->      </div>
https://github.com/anndavpet/learnPY/blob/main/7_11_2.py
    <hr>
    
<div class="step-inner page-fragment">
    <div id="ember3864" class="html-content rich-text-viewer ember-view" data-processed=""><!----><span><p><strong>7_11_3.py .</strong> Вводятся две строки из слов (слова записаны через пробел). Объявите функцию, которая преобразовывает эти две строки в два списка слов и возвращает эти списки.</p>

<p>Определите декоратор для этой функции, который из двух списков формирует словарь, в котором ключами являются слова из первого списка, а значениями - соответствующие элементы из второго списка. Полученный словарь должен возвращаться при вызове декоратора.</p>

<p>Примените декоратор к первой функции и вызовите ее для введенных строк. Результат (словарь d) отобразите на экране командой:</p>

<p>print(*sorted(d.items()))</p></span></div>

<div class="step-text-wrapper">
          <p class="step-text__limit-title">
            <strong>Sample Input<!---->:</strong>
          </p>
          <pre class="step-text__limit-value">house river tree car
дом река дерево машина</pre>
          <p class="step-text__limit-title">
            <strong>Sample Output<!---->:</strong>
          </p>
          <pre class="step-text__limit-value">('car', 'машина') ('house', 'дом') ('river', 'река') ('tree', 'дерево')</pre>

<!---->      </div>
https://github.com/anndavpet/learnPY/blob/main/7_11_3.py
    <hr>
    <div class="step-inner page-fragment">
    <div id="ember4209" class="html-content rich-text-viewer ember-view" data-processed=""><!----><span><p><strong>7_11_4.py </strong>Объявите функцию, которая принимает строку на кириллице и преобразовывает ее в латиницу, используя следующий словарь для замены русских букв на соответствующее латинское написание:</p>

<pre><code class="hljs ebnf"><span class="hljs-attribute">t</span> = {<span class="hljs-string">'ё'</span>: <span class="hljs-string">'yo'</span>, <span class="hljs-string">'а'</span>: <span class="hljs-string">'a'</span>, <span class="hljs-string">'б'</span>: <span class="hljs-string">'b'</span>, <span class="hljs-string">'в'</span>: <span class="hljs-string">'v'</span>, <span class="hljs-string">'г'</span>: <span class="hljs-string">'g'</span>, <span class="hljs-string">'д'</span>: <span class="hljs-string">'d'</span>, <span class="hljs-string">'е'</span>: <span class="hljs-string">'e'</span>, <span class="hljs-string">'ж'</span>: <span class="hljs-string">'zh'</span>,
&nbsp; &nbsp; &nbsp;<span class="hljs-string">'з'</span>: <span class="hljs-string">'z'</span>, <span class="hljs-string">'и'</span>: <span class="hljs-string">'i'</span>, <span class="hljs-string">'й'</span>: <span class="hljs-string">'y'</span>, <span class="hljs-string">'к'</span>: <span class="hljs-string">'k'</span>, <span class="hljs-string">'л'</span>: <span class="hljs-string">'l'</span>, <span class="hljs-string">'м'</span>: <span class="hljs-string">'m'</span>, <span class="hljs-string">'н'</span>: <span class="hljs-string">'n'</span>, <span class="hljs-string">'о'</span>: <span class="hljs-string">'o'</span>, <span class="hljs-string">'п'</span>: <span class="hljs-string">'p'</span>,
&nbsp; &nbsp; &nbsp;<span class="hljs-string">'р'</span>: <span class="hljs-string">'r'</span>, <span class="hljs-string">'с'</span>: <span class="hljs-string">'s'</span>, <span class="hljs-string">'т'</span>: <span class="hljs-string">'t'</span>, <span class="hljs-string">'у'</span>: <span class="hljs-string">'u'</span>, <span class="hljs-string">'ф'</span>: <span class="hljs-string">'f'</span>, <span class="hljs-string">'х'</span>: <span class="hljs-string">'h'</span>, <span class="hljs-string">'ц'</span>: <span class="hljs-string">'c'</span>, <span class="hljs-string">'ч'</span>: <span class="hljs-string">'ch'</span>, <span class="hljs-string">'ш'</span>: <span class="hljs-string">'sh'</span>,
&nbsp; &nbsp; &nbsp;<span class="hljs-string">'щ'</span>: <span class="hljs-string">'shch'</span>, <span class="hljs-string">'ъ'</span>: <span class="hljs-string">''</span>, <span class="hljs-string">'ы'</span>: <span class="hljs-string">'y'</span>, <span class="hljs-string">'ь'</span>: <span class="hljs-string">''</span>, <span class="hljs-string">'э'</span>: <span class="hljs-string">'e'</span>, <span class="hljs-string">'ю'</span>: <span class="hljs-string">'yu'</span>, <span class="hljs-string">'я'</span>: <span class="hljs-string">'ya'</span>}</code></pre>

<p>Функция должна возвращать преобразованную строку. Замены делать без учета регистра (исходную строку перевести в нижний регистр - малые буквы). Все небуквенные символы ": ;.,_" превращать в символ '-' (дефиса).</p>

<p>Определите декоратор для этой функции, который несколько подряд идущих дефисов, превращает в один дефис. Полученная строка должна возвращаться при вызове декоратора. (Сам декоратор на экран ничего выводить не должен).</p>

<p>Примените декоратор к первой функции и вызовите ее для введенной строки s на кириллице:</p>

<p><code>s = input()</code></p>

<p>Результат работы декорированной функции отобразите на экране.</p></span></div>

<div class="step-text-wrapper">
          <p class="step-text__limit-title">
            <strong>Sample Input<!---->:</strong>
          </p>
          <pre class="step-text__limit-value">Python - это круто!</pre>
          <p class="step-text__limit-title">
            <strong>Sample Output<!---->:</strong>
          </p>
          <pre class="step-text__limit-value">python-eto-kruto!</pre>

<!---->      </div>
https://github.com/anndavpet/learnPY/blob/main/7_11_4.py
    <hr>
<div id="ember2049" class="html-content rich-text-viewer ember-view" data-processed=""><!----><span><p><strong>Подвиг 6. </strong>В программе задана функция filter_lst (см. программу ниже), которая отбирает элементы, переданного ей итерируемого объекта и возвращает сформированный кортеж значений.</p>

<p>На вход программы поступает список целых чисел, записанных в одну строчку через пробел. Вызовите функцию filter_lst для формирования:</p>

<p>- кортежа из всех значений входного списка (передается в параметр it);<br>
- кортежа только из отрицательных чисел;<br>
- кортежа только из неотрицательных чисел (то есть, включая и 0);<br>
- кортежа из чисел в диапазоне [3; 5]</p>

<p>Каждый результат работы функции следует отображать с новой строки командой:</p>

<p><code>print(*lst)</code></p>

<p>где lst - список на возвращенный функцией&nbsp;filter_lst. Для отбора нужных значений формальному параметру key следует передавать соответствующие определения анонимной функции.<br>
&nbsp;</p></span></div>

<div class="step-text-wrapper">
          <p class="step-text__limit-title">
            <strong>Sample Input<!---->:</strong>
          </p>
          <pre class="step-text__limit-value">5 4 -3 4 5 -24 -6 9 0</pre>
          <p class="step-text__limit-title">
            <strong>Sample Output<!---->:</strong>
          </p>
          <pre class="step-text__limit-value">5 4 -3 4 5 -24 -6 9 0
-3 -24 -6
5 4 4 5 9 0
5 4 4 5</pre>

<!---->      </div>
https://github.com/anndavpet/learnPY/blob/main/7_8_4.py
