
## 学习中出现的一些问题
[TOC]
### 1、如何解决pdf输出时公式无法显示的问题
 **2023/4/4**
在所编辑的.md文件末尾加上下列代码即可
```markdown

<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });
</script>

```

### 2、<.md>文件中代码渲染出现问题

**问题：**

![80%](picture/渲染问题显示.png)

如图，可以发现代码渲染问题包括：
- 插入图片的代码中中括号渲染问题，一侧方括号为红色，表示没有对应的，但实际上有。
- 标题3中不再出现标题代码的渲染，即'#####'没有出现颜色渲染，且出现了‘()’的渲染

**解决办法：**

目前发现的原因为在该标题前存在latex公式插入符号没有对齐，即如图显示：
![45%](picture/latex公式插入符号对齐对比_1.png)![45%](picture/latex公式插入符号对齐对比_2.png)
如图，在其中用红线圈出的地方出现没有对齐的问题。而在对齐了之后，就发现后面的渲染变成正常的了。

> markdown采用的渲染依据可能与缩进有关，因此需要将代码的层级划分清晰，才可以有清晰的代码渲染。

### 3、加黑加斜体无法同时出现

**问题：**

这是***问题***。

**解决办法：**

实验发现加黑加斜体同时出现时，其前侧后侧都不能是文字才可以（可以是符号），如下：

这不是 ***问题***。
这不是，***问题***。