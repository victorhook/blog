---
layout:      post
title:       Introduction to Digital Signal Processing
categories:  signal-processing tech math
image:       delft_17_spectrum.png
---

Tomorrow I'll have my first exam here, in Signal Processing. So I thought it could be nice to have a technical post where I explain what I've learned so far in the course. Note that if you're not interested in tech/math, then you might want to skip this post.
Otherwise, I'll hope that you learn something new, or at least get inspired to!
Also note that I give no proofs, and don't go very deep into anything. This is mainly meant to give an overview.

---

### What is Signal Processing?
Essentially I think it's literally what is says; With the help of **signal processing** (**SP**) we can *process* *signals*. A signal could for instance be an audio signal. When we speak we produce audio signals, which by itself is just vibrations of air, and these audio signals we can capture with a device like a microphone, which turns the **analog** audio signals into a **digital** representation that our computer can understand. This digitalized version of the audio signal we can then **process** in multiple ways. Perhaps we want to filter out background noise, or make our voice sound funny by manipulation the frequencies.
In SP we often refer to analog as *continous* and digital as *discrete*, and this use of words will be more clear later. **D**igital **S**ignal **P**rocessing is referred to as **DSP**.

A signal in the continoues world we often refer to as $$x(t)$$, which is just a function of time $$t$$. So given a specific time instance $$t$$, the signal takes a certain value. This *value* could for instance be the voltage that the microphone picked up when recording audio. When we consider a signal in a computer, the signal must be discrete, and it's therefor convenient to see it as an array of values like $$x[n]$$, where $$n$$ denotes a specific sample from the signal and $$x[n]$$ is the value of the signal at that sample. For instance: $$x[n] = [1, 0, 1, 0]$$

### Unit impulse - Delta pulse $$\delta[n]$$
A delta pulse $$\delta[n]$$ is a function that is 1 only when whatever is inside the brackets $$[]$$ equals $$0$$. So it looks something like this: ![Dirac function]({{ site.static_url }}images/guides/dsp/guide_1.png)
A nice thing with this function is that we can scale it, or shift it, to *"decide where we want the 1 to be"*. We scale it by multiplying it with a scalar and we shift it by adding/subtracting the index $$n$$ with something, eg: ![Dirac function]({{ site.static_url }}images/guides/dsp/guide_2.png)
Note here that $$n-1$$ shifts it to the **right**.
We can also define functions that consists of multiple delta-functions, like this: ![Dirac function]({{ site.static_url }}images/guides/dsp/guide_3.png)

Combining multiple delta-functions as a single function is a very important concept and it is actually what allows us to express a signal, as a sum of (possibly scaled and shifted) delta-functions. We could for instance express a cosine like this: ![Dirac function]({{ site.static_url }}images/guides/dsp/guide_4.png)

Which is just a *"train"* of scaled and shifted delta-pulses. Unit impulse/delta impulse is often referred to as just *impulse*.


### System
A system is something that takes an input and spits out some output. In SP the input can be an audio signal, and the output can be the processed audio signal which contains less noise. For instance, we could have the following system:
![System]({{ site.static_url }}images/guides/dsp/sys1.svg)

### Impulse response
An **impulse response** is the response that a system outputs, given an impulse response. So it's basically the systems *response*, to an *impulse*. This concept is very critical because if we know a systems *impulse response*, we know everything there is to know about the system. This might sound a bit ridiculous, but it's actually true. In DSP lingo, we like the following notations:

| --- | --- |
| Input signal | $$x[n]$$|
| Impulse response | $$h[n]$$ |
| Output signal | $$y[n]$$ |

We can then use the following schematic to express a generic system:
![Generic system]({{ site.static_url }}images/guides/dsp/sys2.svg)

### LTI system
We want all our systems to have certain properties. Why? Well, because that makes calculation **a lot** easier and it allows us to do all sorts of cool manipulations with the signal. The properties we want our systems to have in DSP is:
1. Linearity
2. Time-invariance

#### Linearity
For a system to be **linear** it must fulfill:
1. **Homogeneity**: Scaling the input signal $$x[n]$$ and **then** passing it through the system shall give the same result as **first** passing the signal $$x[n]$$ through the system, and then scaling the result.
2. **Additivity**: Adding two input signals before passing them through the system shall give the same result as first passing the individual systems through the system and then adding the resulting signals.

These two *"rules"* forms the **Superposition principle**.
##### Superposition principle
This is basically a method to check wether a system is linear, by checking if it follows the rules for linearty, **homogeneity** and **additivity**.
The following image illustrates the superposition principle, where the upper and the lower system combinations equals to the same output signal $$y[n]$$.
![Superposition principle]({{ site.static_url }}images/guides/dsp/sys3.svg)

#### Time-invariant
A system is **Time-invariant** if you get the same result from the system, regardless of **when** you give it an input. So the result should **not** change as a function of time.

### Causality
A system is said to be **causal** if it does **not** depend on future samples. So if the impulse response is depending on future values, the system is **not** time-invariant, Eg:
$$h[n] = \delta[n] + \delta[n+1]$$
Remember that $$n+1$$ means a phase shift to the **left**, so it's depending on "future" values.

### Convolutions
I think **convolution** can be seen as applying a filter to a signal. Mathematically what we do is **kind of**  multiplying one vector, eg $$h[n]$$, with every value of another vector. Performing a convultion is denoted as $$*$$, so $$h[x]$$ convolved with $$x[n]$$ is $$h[n]*x[n]$$
Eg: Let $$h[n] = [1, 1]$$ and $$x[n] = [1, 2, 3, 4]$$ the resulting value from the convolution is $$h[n]*x[n] = [1, 3, 5, 7]$$ Note that this is a very rough description!
For small vectors like this, it can be done quite easily by hand, especially with the help of a table, but when the vectors gets bigger, it becomes very tedious and error-prone. Then we instead rely on computational methods, for instance numpy's method $$np.convolve(h, x)$$

### Complex number refresh
Do we really need complex numbers? Yes, sorry, we do, we really do.

Remember that $$i = \sqrt{-1}$$. In most engineering disciplines (especially Electrical Engineering), we use the letter $$j$$ instead of $$i$$ ($$i$$ is used for *current*), so we'll always use $$j$$ to denote $$\sqrt{-1}$$ here.

A complex number $$z$$:

$$\begin{equation}
z = a + bj
\end{equation}$$

is made up of a **real** part $$a = Re{z}$$ part and an **imaginary** part $$b = Im{z}$$. 
The complex conjugate of $$a+bj$$ is $$a-bj$$, so the imaginary part "flips" sign.

A complex number can be plotted on the **complex plane** where the real part is what we usually refer to as x-axis, and the imaginary part on the y-axis. The number can also be written as a **phazor**. We then only need the numbers **magnitude** $$A$$ and it angle from the real axis. This angle, we like to call the **phase** $$\phi$$ and these can be achieved by:
$$A = \sqrt{a^2 + b^2}$$ and $$\phi = arctan{\frac{b}{a}}$$
We can then write the phazor as: $$z = A\angle{\phi}$$

Another way to express the complex number is by using its polar form where $$z = r(cos \theta + j\cdot sin \theta)$$ where $$r$$ is the same as $$A$$ in phazor, and $$\theta$$ is the same as $$\phi$$ in phazor. We can also express this as a complex exponential with the help of Eulers identity like $$z = e^{j\theta}$$. This expression is the foundation for the understanding the **Fourier Series**

$$\begin{equation}
z = e^{j\theta}
\end{equation}$$

### Fourier Series
Let's start with the following:

*We can represent any signal as a sum of cosines.*

This is kind of the essence of the Fourier Series, and I think it's important to think about this statement and try to appreciate it. The "goal" of the Fourier Series is to represent any kind of signal as a sum of (perhaps infinitely) many individual sinosoidal signals.

To describe this with math, we need the following relationship:

$$\begin{equation}
cos (x) = \frac{e^{jx}+e^{-jx}}{2}
\end{equation}$$

Which easily can be proven by some manipulations. This equation allows us to describe a cosine wave as a sum of two complex numbers, where the numbers are complex conjugated. These complex numbers are (as you can see) in complex exponential form.

We can then describe a signal as a sum of *complex exponentials*. For instance, take the signal $$x(t) = cos(x) + cos(2x)$$, which we can plot like:
![cosx+cos2x]({{ site.static_url }}images/guides/dsp/guide_5.png)

This signal is made up of two cosines, $$cos(x)$$ and $$cos(2x)$$. The sum of these cosines forms the resulting signal from the plot above. Here we can all of the signals, both the indivudal cosines, and the sum of them:
![sum of cosines]({{ site.static_url }}images/guides/dsp/guide_6.png)

If we use the complex exponential notation to describe the signals instead, we can write is as:
$$x(t) = \frac{1}{2}(e^{jx} + e^{-jx}) + \frac{1}{2}(e^{j2x} + e^{-j2x})$$

If we use the complex exponential notation to describe the signals instead, we can write is as:
$$x(t) = \frac{1}{2}(e^{jx} + e^{-jx}) + \frac{1}{2}(e^{j2x} + e^{-j2x})$$

In this example, it's quite easy, because we already know how the signal looks, and it's just a sum of two different cosines. However, if I asked you to find me the sum of complex exponentials that describe this signal, you might have an issue:
![hard signal to estimate]({{ site.static_url }}images/guides/dsp/guide_7.png)

In this case we need to perform some fourier analysis, which I will have to cover in more depth later, but to give you a small teaser:

$$\begin{equation}
x(t) = \sum_{k=-\infty}^{\infty} a_k e^{j\omega_{fund}kt}
\end{equation}$$

Woah! That's a nasty equation! Well not really, if we investigate it furher. This is actually just what we just discussed, a *sum of cosines*, where each cosine is scaled and shifted by the compelx coefficient $$a_k$$. You might wonder why we have negative frequencies here, and that's something I'll save for next time!

If we plot the complex coefficients as phasors in the complex plane, and rotate
them with their respective frequency (multiple of $$f_{fund}$$), and then draw
a line at the tip of the "final" phasor, we actually get the resulting signal
along the imaginary axis. Here's an animation for $$x(t) = cos(2t) + 0.5cos(3t) + 0.3cos(4t)$$
Notice how the complex conjugate ensures that the "final" tip always stays
on the real axis.

{% include fourier_phasor.html %}


You might also wonder how we calculate the coefficients $$a_k$$. This is done with this formula:


$$\begin{equation}
x_k = \frac{1}{T_{fund}} \int_{0}^{T_{fund}} x(t) e^{-j\omega_{fund}kt} dt
\end{equation}$$

- $$T_{fund}$$ - The fundamental period of the signal. This is $$\frac{1}{f_{fund}}$$ which is the fundamental frequency (highest common divisor between the cosines).
- $$\omega_{fund}$$ - Fundamental radial frequency, same as $$2\pi f_{fund}$$
- $$k$$ - A multiple of the fundamental frequency, eg $$0, 1, 2$$.


With this knowledge we are ready to tackle one of the most
profound ideas in this field, which is the **Fourier Transform**, but that
will definetely have to wait for another time.

I hope you learned something new!
