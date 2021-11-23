---
layout:      post
title:       Quarter Two
categories:  school courses food
image:       delft_37_christmas.jpg
---

Hey!
The 2nd quarter is now rolling at full speed, and it's very nice to only take
three courses. Also, one of the courses is the MarsRover project, which is actually
just a bunch of lab sessions, so there's really only two courses that requires preparation
and self-study. Let's discuss the MarsRover project a bit more:

### MarsRover Project
This course gives 5 EC credits, and is the main reason why I choose the Minor in
Electronics for Robotics. The aim of the course is to build a line-following
robot and (potentially) add some extra features and functionalites for it.
It's divided into 14 chapters, where chapter 1-8 aims to give an overview of
VHDL (**V**ery (High Speed Integrated Circuit) **H**ardware **D**escription **L**anguage),
and some basic functions and operations you'd like to perform with it, such as
FSM (**F**inite **S**tate **M**achines), registers etc.
Once the 8 first chapters are completed, we already have a pass for the course
and technically don't need to do anything else. However, during chapters 9-14
we can extend the functionality of the robot a bit. For instance, we can
make it switch between using power from solar panels or from batteries, and I believe
there's some other things as well.
If you don't know what VHDL or FSM is, let me try to explain it:

#### VHDL
VHDL is a type of programming language, that let's you specify *how hardware should look and behave*.
The big difference between VHDL and a normal programming language like Python is that
for a normal programming language, you write some code, and then give it to a computer
that then executes this code, according to some pre-determined rules. This is *not*
the case for VHDL, where we instead specify how the hardware itself should look and
function. One might then ask; How can we execute this code? 

Good question! This can be done by
computer simulations, or programming an FPGA (**F**ield-**P**rogrammable **G**ate **A**rray),
which will then implement the hardware that you described in your VHDL.
This is really cool, because it allows us to *"create"* hardware with code, test it
in simulation and then actually use it with an FPGA. This is probably as close
to creating actual computer hardware that most people will get, because taking
VHDL code to a manufacturer and actually producing silicon chips is very, *very*, **very** expensive.
Perhaps, this could be something that will change in the future, and it might be
as simple and cheap as creating custom PCB's, which you can create yourself for a few
dollars and get them delievered within a week. Another option for the future, would be
to make FPGA's cheaper, so that they can more easily be integrated and used in projects,
and this is starting to show more and more when companies makes new FPGA's, that
in fact are cheaper and cheaper. This is great news for makers! 😃

That was a sidetrack, back to VHDL!

{% include image.html url="vhdl.png" description="Rough overview how VHDL works 😃"%}

During the course, we write the VHDL code in [Xilinx Vivado](https://www.xilinx.com/support/download.html),
which is a pretty nice IDE that is free to download.


#### FSM
Finite State Machines are found everywhere in digital electronics and is an essential block
to understanding how computers operate. Let's break down these words one by one:
- **State**: Let's imagine *state* to be an "abstract" position in time. With abstract,
I mean that it doesn't have to actually be a physical position, but some type of
"position". Position is not the ideal word, *state* is much better, but defining
what state *is* with the word state itself feels a bit silly. I hope you get my point here!
You could see your mood during the day as different *states*, where you might have the following:
  - Happy
  - Angry
  - Sad
  - ...
- **Finite**: There is a *finite* amount of these *states*, so we can only have a fixed
number of them, eg: state **1**, state **2** etc..
- **Machine**: This is just like a "container" that has all these *finite* *states*, and
ensures that you're in the state that you should be in. The machine also handles the
transitions between states, because if we're at state **1**, and we want to go to
state **2**, there has to be some rule, or requirement for this transition to occur.

{% include image.html url="FSM.png" description="Working principle of FSM"%}

In the image above, I illustrate a simple state diagram with only 2 states.
The arrows shows the possible transitions between the states, and the text besides
the arrows shows the requirements for that particular transition to occur.

A natural question might be; Why do we need this?

Good question, again! Let's take our MarsRover as an example:
The robot should be able to follow some lines, and the lines doesn't have to be
completely straight, but can bend and turn. So we need a way for the robot to know
whether it should be driving straight, turn or completely stop. Thus, we could
create an FSM, that has the following states:

{% include image.html url="FSM2.png" description="State diagram example for the MarsRover, excuse my handwriting, hopefully you can read it 😃" %}

This is not exactly how our diagram looks for the actual robot, but it's very similar
and the working principle is identical.

As you now know, *FSM* is a very powerful *machine*, that has a *finite* amount of *states*
that allows you to create logic and build computers! The working principal is
(hopefully) easy and intuitive to understand.

So the knowledge of VHDL and FSM is pretty much all we need for the first 1-8 chapters
of the MarsRover project (obviously I haven't covered any of the details here).
Even though this is really not as cool as I expected the MarsRover project to be,
it's still plenty of fun, and getting better at VHDL is pretty nice as well.
But, I'm simply going to have to build cooler robots on my free time instead, and
if you're wondering hot it's going for [droneh]({% post_url 2021-10-09-droneh_v0.1 %}),
I am making (slow) progress, so I'll probably make a post about it soon! 🦋

---

As I mentioned last time, I've started a Drawing course at [X](https://www.tudelft.nl/en/x),
where we had our first lesson last week. I have to say that it was a lot of fun!
It's divided into a total of 7 lessons, where we're going to explore different
materials and styles of drawing. Hopefully I learn something new here! 🖌️

---

As usual, I'll end the post with some photos! 📷

{% include image.html url="delft_37_christmas.jpg" description="Food-court in the Hague, wiht Christmas decorations!🎅😍" %}
{% include image.html url="delft_38.jpg" description="Beautiful garden in Rotterdam." %}
{% include image.html url="delft_39_baobun.jpg" description="Delicious bao bun with tofu." %}