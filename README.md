<h1> Self-learning of virtual cars using Neural Networks (Thesis) </h1>

<h2>Introduction</h2>
In this Thesis (TFG in Spanish), We will use the technique of neural networks to give different approaches to car training in a racing video game. It's objective is to improve the results obtained in the
previous thesis, for this we will use new ways to train cars virtual, and then check the performance obtained by going through a set of completely unknown circuits.

<h2>Stages</h2>

The solution to our project is divided into three stages.
<ol>
  <li><strong>Expansion of functionalities</strong>. We will add and improve features to achieve a more complete program. The
  improvements made are: 
  
<ul>
<li>We will make changes in the graphic part to improve its visualization and improvements
  techniques to improve program execution.</li>
<li>We will proceed to improve certain functionalities that were not correctly implemented.</li>
<li>We will add our own particle filter with a series of improvements.</li>
</ul>
</li>
<li>
  <strong>Creation of a training system of Neural Networks</strong>. We will create an automated system that meets a series of requirements, can execute and obtain the results of a set of tests.
</li>
<li>
  <strong>Test case simulator</strong>. It consists in the development of a program that is
able to simulate the behavior of the best car in a given test case. In this case we will have two
case studies, which will have common and specific requirements each.
</li>
</ol>

<h2>Configuration</h2>

In the project we will use Python version 3.6.

The libraries we will use will be the following:

- Pillow 5.4.1
- Numpy 1.16.2
- pip 10.0.1
- pygame 1.9.4
- openpyxl 2.6.1
- setuptools 39.1.0

The last library is about OpenGL with GLUT. We will download these libraries manually from the website:

https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyopengl

In the case of Windows 32, the packages are as follows:
PyOpenGL 3.1.3b2 cp36 cp36m win32.whl
PyOpenGL_accelerate 3.1.3b2 cp36 cp36m win32.whl

In the case of Windows 64, the packages are as follows:
PyOpenGL 3.1.3b2 cp36 cp36m win_amd64.whl
PyOpenGL_accelerate 3.1.3b2 cp36 cp36m win_amd64.whl

For installation on Linux, it will have to be done manually using the apt command:
sudo apt-get install python-opengl

