# p-strace
p-strace is a simple python script for you to monitor output of a specific process on linux. So you don't have to stare at the display impatiently waiting.

##usage
Say you have a very complex task running (might be some machine learning stuff), and it keep printing 'iteration 71/1000'  and others.
```
Iteration 1 / 1000
  Content 1 loss: 332424.57665
  Style 1 loss: 654754.64645
  ...
Iteration 2 / 1000
  Content 1 loss: 331984.5786
  Style 1 loss: 865775.64675
  ...
  ...
Iteration 71 / 1000
  Content 1 loss: 343253534.3242
  Style 1 loss: 432432.432423423
  ...

```
Now, when the iteration achieves 100 you want to get a notification. So you should:

```
mcfatealan@mcfatealan-desktop: ~$ sudo python p-strace.py
input pid: [PID]
input sensitive word:  Iteration 100 / 1000
```


When the process outputs that line, you will get a `Retard Alert` with some beeps. You will get one when the process exits.

Enjoy your coffee.
