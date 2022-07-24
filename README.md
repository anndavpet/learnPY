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
https://github.com/anndavpet/learnPY/blob/main/7_11_3.py
    <hr>
    
