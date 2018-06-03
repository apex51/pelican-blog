Title: Notes on Basic Support Vector Machines
Date: 2014-08-08 11:50:43
Modified: 2014-08-08 11:50:43
Category: math
Tags: math
Authors: tester, mult1vac
Summary: Notes on Basic Support Vector Machines
Status: published


Support vector classifier (or regressor) is one of the "*off-the-shelf*" machine learning tools often used in daily tasks. Its theory is highly developed now and quite interesting to study. 

I wrote this after I did some revision on notes I took in my graduate's time. I found that beginners like me tend to skip the basis of SVM right to the more sophisticated part. This article focuses on ***"what a basic support vector machine is"*** question, whose answer may come in three parts: ***hypothesis, optimization goal and training algorithm***.

<!--more-->

## Hypothesis

A basic support vector machine is a linear classifier for binary classification problems. Consider a set of linear separable training samples below. From these samples SVM trains a hyperplane $${w^T}x + b = 0$$ as the decision boundary, and the decision function can be written as:

$${h_{w,b} }(x) =  \left \{ {\begin{array}{c} { 1, {w^T}x + b \ge 0} \\ { - 1,{w^T}x + b < 0} \end{array}}\right.$$


<div  align="center">
{% img center {filename}/images/2014-08-08/1.png decision boundary %}
</div>

Notice that the dicision function is quite different from ***logit regression***. Instead of predicting the probability of being $$1$$ as the intermediate step in logit regression, SVM directly jump to the result of $$1$$ or $$-1$$.



## Optimization Goal



#### A Confident Decision

Check the two points $$A$$ and $$B$$ below. $$A$$ is farther from the hyperplane. When making decisions, it's intuitive that predicting $$A$$ as $$1$$ is more confident than predicting $$B$$ as $$1$$. $$B$$ is a more difficult point because a slight tilt of the hyperplane may cause it to be on the negative side. This draws out the basic idea behind SVM: finding a separating hyperplane which can ***make the most confident decision for the most difficult points***.

<div  align="center">
{% img center {filename}/images/2014-08-08/2.png confident split %}
</div>

#### Two Kinds of Margin

We start by defining the ***functional margin*** with respect to the training sample $$({x^{(i)} },{y^{(i)} })$$:

$${ {\hat \gamma }^{(i)} } = {y^{(i)} }({w^T} {x^{(i)} } + b)$$

Given a training set $$S = \{ ({x^{(i)} },{y^{(i)} }),i = 1,...,m\} $$, the functional margin with respect to $$S$$ is:

$$\hat \gamma  = \mathop {min}\limits_{i = 1,...,m} { { \hat \gamma }^{(i)} }$$

Notice that the functional margin is not a good measure of confidence. We can multiply a number to both $$w$$ and $$b$$ without changing $$h_{w,b}(x)$$, while at the same time the functional margin was changed by the same magnitude. This can a little bit help us later.

We also define the ***geometric margin*** with respect to training sample $$(x^{(i)},y^{(i)})$$ as the distance from $$(x^{(i)},y^{(i)})$$ to the hyperplane. 

<div  align="center">
{% img center {filename}/images/2014-08-08/3.png geometric margin %}
</div>

From figure above, we assume that point $$A$$'s coordinate is $$x^{(i)}$$ with its label $$y^{(i)}=1$$. Line segment $$AB$$ is orthogonal to the hyperplane. We know that $$w$$ is orthogonal to $${w^T}{x^{(i)} } + b=0$$. Assume $$w$$ points to the positive direction and $${\gamma ^{(i)} }$$ is the distance of $$AB$$. Then $$B$$'s coordinate can be represented as $${x^{(i)} } - {\gamma ^{(i)} } \cdot w / \left\vert w \right\vert$$. Putting $$B$$ into $${w^T} {x^{(i)} } + b=0$$ and solving for $${\gamma ^{(i)} }$$, we get the geometric margin:

$${\gamma ^{(i)} } = {y^{(i)} }(\frac{ { {w^T} } } { {\left\| w \right\|} } \cdot x^{(i)} + \frac{b} { {\left\| w \right\|} })$$

*We made some assumptions on $$y^{(i)}=1$$ and $$w$$'s direction. If we assume them differently, we can also get the same result.*

The geometric margin of training set $$S = \{ ({x^{(i)} },{y^{(i)} }),i = 1,...,m\} $$ is:

$$\gamma  = \mathop {min}\limits_{i = 1,...,m} {\gamma ^{(i)} }$$

The relationship between the funcitonal margin and geometric margin is as follows. When $${\left \vert w \right \vert}=1$$ the functional margin equals the geometric margin. 

$${\gamma ^{(i)} } = \frac{ { { {\hat \gamma }^{(i)} } } } { {\left\| w \right\|} }$$

$$\gamma  = \frac{ {\hat \gamma } } { {\left\| w \right\|} }$$




#### Linear Separable Case

Given a training set that is linear seperable, SVM finds a hyperplane that seperates the positive and negative samples with the maximun "gap". As we've talked above, this equals maximizing the geometric margin:

$$\mathop {max}\limits_{w,b} \gamma $$

$$s.t.\;{y^{(i)} }(\frac{ { {w^T} } } { {\left\| w \right\|} } \cdot {x^{(i)} } + \frac{b} { {\left\| w \right\|} }) \ge \gamma ,\ \ i = 1,...,m$$

Since $$\gamma  = { {\hat \gamma } }/{ {\left\vert w \right\vert} }$$, this problem can be derived as:

$$\mathop {max}\limits_{w,b} \frac{ {\hat \gamma } } { {\left\| w \right\|} }$$

$$s.t.\;{y^{(i)} }({w^T}x + b) \ge \hat \gamma ,\ \ i = 1,...,m$$

We can add constraints on $$w$$ and $$b$$ to make the functional margin $${\hat \gamma}=1$$. As we've talked above, this wouldn't change anything to the hyperplane. Maximizing $${1}/{ {\left\vert w \right\vert} }$$ is the same as minimizaing $${\left\vert w \right\vert}^2$$. The final optimization goal is:

$$\mathop {min}\limits_{w,b} \frac{1} {2}||w|{|^2}$$

$$s.t. \ {y^{(i)} }({w^T} {x^{(i)} } + b) \ge 1,i = 1,...,m$$

#### Non-linear Separable Case and Soft Margin

Problem above is based on linear separable training set. In the real world we often tackle on problems like: 

* **Non-linear separable training set**
* **Training set with outliers**

These problems can be solved by introducing ***$$l1$$ regularization*** to the optimization formula:

$$\mathop {min}\limits_{w,b} \frac{1} {2}||w|{|^2} + C\sum\limits_{i = 1}^m { {\xi _i} } $$

$$s.t.\;{y^{(i)} }({w^T} {x^{(i)} } + b) \ge 1 - {\xi _i},\;\ \ i = 1,...,m$$

$${\xi _i} \ge 0,\ \ i = 1,...,m$$

This allows training samples with margin less than 1 by placing a penalty $$C{\xi}$$ to the optimization formula. $$C$$ controls the balance between $${\left\vert w \right\vert}^2$$ and the penalty.

#### Hinge Loss

SVM can also be viewed as an optimization of the function:

$$\sum\limits_{i = 1}^m { { {[1 - {y^{(i)} }({w^T} {x^{(i)} } + b)]}_ + } + \lambda { {\left\| w \right\|}^2} } $$

The first part is SVM's empirical loss function, which is called the ***hinge loss***. The second part is $$w$$'s $$L_2$$ regularization with $$\lambda$$ coefficient. Hinge loss works as:

$$L = {[1 - {y^{(i)} }({w^T} {x^{(i)} } + b)]_ + } = \left\{ \begin{array} {l}1 - {y^{(i)} }({w^T} {x^{(i)} } + b),\ \ {y^{(i)} }({w^T} {x^{(i)} } + b) < 1\\0,\ \ {y^{(i)} }({w^T} {x^{(i)} } + b) \ge 1\end{array} \right.$$

<div  align="center">
{% img center {filename}/images/2014-08-08/4.png hinge loss %}
</div>

Above figure is clipped from ***[ESLII][1]*** Figure 12.4 . We only focus on hinge loss here (red line in the figure). We can see that only if the point is correctly classified and the margin is no less than 1, the loss will be zero. Otherwise the loss will be $$1 - {y^{(i)} }({w^T} {x^{(i)} } + b)$$. The penalty is linear on the wrong side, which is thought to be a robust loss function.

We can prove that hinge loss with L2 regularization can be transformed to the soft margin optimization (*[ESLII][1] Exercise 12.1*).

Set $${[1 - {y^{(i)} }({w^T} {x^{(i)} } + b)]_ + } = {\xi _i}$$, then we get $${\xi _i} \ge 0$$.

* If $${y^{(i)} }({w^T}x + b) \ge 1$$, then $${\xi _i} = 0$$. So $${y^{(i)} }({w^T} {x^{(i)} } + b) \ge 1 - {\xi _i}$$ stands.
* If $${y^{(i)} }({w^T}x + b) < 1$$, then $${y^{(i)} }({w^T} {x^{(i)} } + b) = 1 - {\xi _i}$$.

So soft margin optimization's constraints are all satisfied. Hinge loss with L2 regularization can be written as:

$$\mathop {min}\limits_{w,b} \sum\limits_{i = 1}^m { {\xi _i} }  + \lambda {\left\| w \right\|^2}$$

If we set $$\lambda  = 1/2C$$, above formula can be written as follows, which equals to the soft margin optimization.

$$\mathop {min}\limits_{w,b} \frac{1} {C}(\frac{1} {2} {\left\| w \right\|^2} + C\sum\limits_{i = 1}^m { {\xi _i} } )$$

The soft margin optimization can be transformed to hinge loss with L2 regularization vice versa.

## Training Algorithm

From above we've transformed the largest margin problem into an optimization of a convex quadratic objective with linear constraints. It's a convex QP (quadratic programming) problem, which can be efficiently solved using commercial QP codes.

## Conclusion

So a basic support vector machine consists of three parts:

* **Hypothesis:** $${w^T}x + b = 0$$ as separating hyperplane and $${h_{w,b} }(x)$$ as decision function
* **Optimization Goal:** Maximizing the soft margin
* **Training Algorithm:** Convex QP

We can call a stop here since the basic SVM problem has been solved. I know beginners like me may want to explore something more and there's truly a lot more since the theory has been long developed. We can start by studying SVM's dual form, which will yield:

* **Kernel tricks**, which makes SVM possible to work in high dimensions and non-linear cases.
* **SMO** (Squential Minimal Optimization), a more efficient training algorithm 

For dual form and kernel tricks, one can learn from **[Standford CS229 Lecture Notes][2]** to get a basic understand. For SMO algorithm, one can refer to:

* Platt, John (1998), **[Sequential Minimal Optimization: A Fast Algorithm for Training Support Vector Machines][3]**
* **[Nice guide on SMO with C++ implementation][4]**
* I wrote a toy SMO in python, code can be found **[here][5]** in my GitHub
* I wrote a note on SVM and SMO, which may help a little bit. Notes can be found **[here][6]** in Jupyter Notebooks

## Reference

* *[CS229 Lecture Notes, Part V, Support Vector Machines][2]*
* *[The Elements of Statistical Learning, 12.3.2, the SVM as a Penalty Method][1]*

[1]: http://statweb.stanford.edu/~tibs/ElemStatLearn/
[2]: http://cs229.stanford.edu/
[3]: http://research.microsoft.com/apps/pubs/default.aspx?id=69644
[4]: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.24.7001
[5]: https://github.com/apex51/SVM
[6]: http://nbviewer.ipython.org/github/apex51/SVM/blob/master/note/SVM%20and%20SMO.ipynb

<!-- conclusion

further reading
- dual form
	- kernel trick
	- smo
		- original smo, paper, code guide, my code
		- more developed smo
- primal form
	- pegasos (which I have not read yet) -->