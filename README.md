# p-strace
p-strace is simply a wrapper of linux `strace` command, and gives notifications(sound, screen flicker and printed log) when specific output is detected. So you needn't stare at the display impatiently waiting any more.

##simple usage
```
sudo python p-strace.py [PID] '[Sensitive String]'
```

##a common scenario
Say you have a very complex task running (might be some machine learning stuff, pid:2345), and it keep printing 'iteration 71/1000'  and others.
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
mcfatealan@mcfatealan-desktop: ~$ sudo python p-strace.py 2345 'Iteration 100 / 1000'
```

When the process outputs that line, you will get:
* a `Retard Alert`:
```
************************RETARD ALERT************************
write(1, "Iteration 100 / 1000\n", 21)                     = 21
```
* six short beeps
* screen flicker

You will also get alerts when the process exits.

##related system command
`strace`
`xrandr`

tested on Ubuntu.

##future
Maybe later I will add more complex functions like:
  * more advanced judge rules: regex and condition.
  * better notification: colorful display and animation (local), or even email (remote)
  
Enjoy your coffee.
