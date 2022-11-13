### 1.标签属性
```html
字体属性	font-size
文本属性	text-decoration、text-align
首行缩进	text-indent
行高		 line-height
宽高属性	width、height、min-height、max-height
背景属性	background
列表属性	list-style
字体颜色	color

定位属性    position
布局属性	display
浮动属性	float、clear
盒子模型	border、margin、padding
圆角边框	border-radius
阴影		 text-shadow,box-shadow
```

### 2. 选择器

```css
id选择器		     #id
类选择器			.class
关系选择器			div p、div>p、div,p
伪类选择器           hover
结构性伪类选择器      E:after、E:before、E:nth-child()、E:first-child、E:last-child
通用选择器			*
子元素选择器		   > 
```

### 3. 浮动

#### 3.1 CSS浮动的作用

* 浮动会改变块级元素的排列方式，让内容从上下排列变成水平排列，浮动有左浮动和右浮动;
* 浮动元素的外边缘不会超过其父元素的内边缘;
* 浮动元素不会互相重叠, 浮动元素不会上下浮动;
* 任何元素一旦浮动，display 属性将完全失效均；可以设置宽高，并且不会独占一行。
* 父盒子如果不设置高度而由子盒子撑起来，那么如果子盒子开启浮动后就脱离标准文档流，导致父盒子高度塌陷。
 * <font color=red>属性：</font>`float:none/1eft/right`

#### 3.2 CSS清除浮动

* 清除浮动是在使用了浮动之后必不可少的，为了网站布局的效果，清除
  浮动也变得非常麻烦。
* <font color=red>属性：</font>`clear:left/right/both`
* 清除浮动的常用方式：
  1.结尾处div标签加`clear:both`(或在下一个元素上加`clear:both`)
  2.浮动元素的父级div定义 `overflow:hidden`
  3.浮动元素的父元素定宽高

### 4. 定位
#### 4.1 标签定位
| positions 属性值 | 作用 |
| :-----:| :----------:|
| static默认定位 | 始终处于文档流的默认位置，static元素忽略任何top 、bottom、left、right |
|relative 相对定位|相对于自己原来的位置进行定位|
|absolute 绝对定位|如果有父元素且父元素开启相对定位那么就相对于父元素进行定位，如果没有父元素那么就相对于body进行定位，开启绝对定位的元素在页面不会占据位置 , 元素的位置通过top 、bottom、left、right属性进行规定|
|fixed固定定位|相对于浏览器的边框进行定位的，元素的位置通过top 、bottom、left、right属性进行规定|

**绝对定位和固定定位的区别**:
　　当一个元素被定义为绝对定位的时候就脱离了文档流，并且以开启相对定位的父级为基准来进行偏移，如果父元素都没有开启相对定位，那么就一直向上找，直到找到body为止 ，而固定定位是相对于屏幕来进行定位的。

#### 4.2 z-index 

**作用:** 一旦修改了元素的定位方式，则元素可能会发生堆叠
可以使用z-index属性来控制元素框出现的重叠顺序，设置定位属性Z轴的距离(定位元素的显示顺序)

**z-index属性值：**

 	1. 值为数值，数值越大表示堆叠顺序越高，即离用户越近
 	2. 可以设置为负值，表示离用户更远，一般不要设置

*<font color=red>z-index 属性只支持定位属性元素</font>

### 5. display 属性

> 根据CSS规范的规定，每一个网页元素都有一个display属性，用于确定该元素的类型，每一个元素都有默认的display属性值，比如div元素，它的display属性默认值为block，称为[^块级元素]；而span元素的display属性值默认为 inline，称为[^行内元素]。

**块元素与行元素是可以转换的，也就是说display的属性值可以由我们来改变**

| display属性值 |   作用   |
| :-----------: | :------: |
|     *none     | 隐藏对象 |
|*block|指定对象为块元素|
|*inline|指定对象为内联元素|
|inline-block|指定对象为内联块元素|
|table-cell|指定对象作为表格单元格|
|     *flex     |弹性盒|
隐藏属性对应的还有`visibility` 

[^块级元素]:具有宽高属性，并且独占一行
[^行内元素]:没有宽高属性，不会独占一行

### 6. 盒子模型

> 盒子模型是CSS中一个重要的概念，理解了盒子模型才能更好的排版。W3C组
> 织建议把网页上元素看成是一个个盒子。盒模型主要定义四个区域：内容(content)、
> 内边距(padding),、边框(border)、外边距(margin)。转换到我们日常生活中，可以
> 拿手机盒来对比，手机=内容，内边距=盒子中的填充物，边框盒子的厚度，外边距
> 两个手机盒之间的距离。

**对象实际宽度 = 左侧外边距 + 左侧边框 + 左侧内边距 + 宽度 + 右侧内边距 + 右侧边框 + 右侧外边距**

#### 6.1 盒子模型-margin(外边距)

* 会在元素外创建额外的空白区域
* 外边距是透明的
* 外间距合并: *<font color=red>(外间距只有上下合并)</font>
  1. 当两个垂直外边距相遇时，他们将形成一个外边距，成为外边距合并
  2. 合并后的外边距的高度等于两个发生合并的外边距的高度中的较大者

|  属性  |  值  |作用|
| :----: | :--: | :--: |
| margin | 像素(px)、%、auto、负值 |1个值：设置上右下左外边距， eg: margin: 10px 20px 10px 10px; 2个值：上下左右；3个值：上左右下；|
|margin-top|像素(px)、%、auto、负值|设置上外边距,  margin-top: -100px;|
|margin-right|像素(px)、%、auto、负值|设置右外边距,  margin-right:  30px;|
|margin-bottom|像素(px)、%、auto、负值|设置下外边距,  margin-bottom:  30px;|
|margin-tleft|像素(px)、%、auto、负值|设置左外边距,  margin-bottom:  30px;|

#### 6.2 盒子模型-border(边框)

**border属性设置一个元素的边框, 它有三个要素：宽度、样式、颜色，统称边框三要素**。

* 统一的写法：

  <font color=red>属性：</font>`border: 3px solid red `

* 单独的写法：

  border-width: ;        不写width会默认有3像素的值

  border-style: ;      	style 为空的情况下，整个边框是不会出现的

  border-color: ;          不写颜色会默认为黑色

| border-style边框常用的样式 | 作用       |
| :--------------------: | :--------: |
|         dotted         | 边框为点状 |
|solid|边框为实线|
|dashed|边框为虚线|
|double|边框为双线|
|none|无边框|

#### 6.3 盒子模型-padding(内边框)

* 内容区域和边框之间的空间

* 会扩大元素边框所占用的区域

* <font color=red>属性：</font> padding: value;

|  属性   |     值      |                             作用                             |
| :-----: | :---------: | :----------------------------------------------------------: |
| padding | 像素(px)、% | padding: 10px 20px 10px 10px; 2个值：上下左右；3个值：上左右下； |
| padding-top |像素(px)、%|设置上内边距,  padding-top: 10px;|
| padding-right |像素(px)、%|设置右内边距,  padding-right: 10px;|
| padding-bottom |像素(px)、%|设置下内边距,  padding-bottom: 10px;|
| padding-left |像素(px)、%|设置左内边距,  padding-left: 10px;|

*<font color=red>盒子模型分两种：一种是符合W3C规范的标准例子模型；另一种是IE的盒
子模型，IE的盒子模型也被叫怪异盒子。</font>IE盒子和标准盒子模型不同的是：IE盒子模型的宽高包含了border和pading。

* **box-sizing** 属性允许你以"W3C的盒模型"或"IE盒模型"来定义元素，以适应区域。
  换句话说，当前元素使用哪种盒模型，可以由box-sizing属性来指定。它有两个值：
  
  * <font color=red>属性：</font> box-sizing：content-box(标准)/border-box(怪异);
    1. **标准模式下的盒模型：**padding和border不被包含在元素的width和height内，元素的实际大小为：【元素本身的宽高 + border + padding】。
    2. **怪异模式下的盒模型：**padding和border被包含在元素的width和height内，元素的实际大小本身包含了border 和padding的宽高。
  
  

