---
publish: true
review-frequency: normal
---
2021-12-29-We
Type:: #idea
Tags:: [[C]], [[3D rendering]], [[math]], [[matrices]]

# How does Donut 3D rendering work

# Projection
We are viewing the object being projected onto a screen.

The object is $z$ distance away from viewer, and the screen is $z'$ distance away from the viewer.
To render a 3D object onto a 2D screen, we project each point $(x,y,z)$ in 3D-space onto a plane located $z’$ units away from the viewer, so that the corresponding 2D position is $(x’,y’)$.

![[perspective.png]]

Let $K_1 = z'$ since $z'$ is a fixed constant.

We can scale a coordinate by the screen distance _z’_.

Where our projection equation becomes
$(x', y') = ( {K_1 x\over z}, {K_1 y\over z})$

# Z-buffer
Since we are plotting a 3D object onto a 2D plane, there will be different points from the object get mapped to same $(x', y')$ point 2D plane. Therefore to fix this issue, we need to maintain a [z-buffer](https://en.wikipedia.org/wiki/Z-buffering) that stores the Z coordinate of every 2D point we draw. When plotting a new point on 2D plane, we first check if there is already a point plotted in front of the new point.

A simple optimization for Z-buffer is to store Z coordinate as $z^{-1} = {1 \over z}$ because:
- $z^{-1} = 0$ corresponds to infinite depth, so we can pre-initialize our z-buffer to 0 and have the background be infinitely far away
- we can re-use $z^{-1}$ when computing $x’$ and $y’$ dividing once and multiplying by $z^{-1}$ twice is cheaper than dividing by $z$ twice.

# Drawing a donut/torus
![[torusxsec.png]]

Let $R_1$ be radius of thickness of the torus round pipe.

Let $R_2$ be radius of thickness of torus' overall width.

So we have a circle of radius $R_1$ centered at point $(R_2,0,0)$, drawn on the $xy$-plane. 
$(x,y,z) = (R_2, 0, 0) + (R_1 \cos \theta, R_1 \sin \theta, 0)$

Where $\theta = [0,2\pi]$

To make 3D torus, we take the circle that is only on $xy$-plane and rotate it around $y$ axis by another angle, $\phi$. The standard method to rotate 3D point around a cardinal axes is to use the [rotation matrix](https://en.wikipedia.org/wiki/Rotation_matrix). 

$$
(R_2 + R_1 \cos \theta, R_1 \sin \theta, 0)  \cdot \begin{pmatrix} \cos\phi & 0 & \sin\phi \\ 0 & 1 & 0 \\ -\sin\phi & 0 & \cos\phi \end{pmatrix}
$$
$$
= ((R_2 + R_1 \cos \theta) \cos\phi , R_1 \sin \theta,-(R_2 + R_1 \cos \theta)\sin \phi)
$$

The final look require the torus spin around on at least 2 more axes for animation, which is multiplying above with two more rotation matrix.

For example if were to rotate the torus on x-axis by `A` degree and z-axis by `B`.
$$
(R_2 + R_1 \cos \theta, R_1 \sin \theta, 0)  
\cdot 
\begin{pmatrix} \cos\phi & 0 & \sin\phi \\ 0 & 1 & 0 \\ -\sin\phi & 0 & \cos\phi \end{pmatrix}
\cdot 
\begin{pmatrix} 1 & 0 & 0 \\ 0 & \cos A & \sin A \\ 0 & -\sin A & \cos A \end{pmatrix}
\cdot 
\begin{pmatrix} \cos B & \sin B & 0 \\ -\sin B & \cos B & 0 \\ 0 & 0 & 1 \end{pmatrix}
$$

# Distance of donut to the viewer
A new constant $K_2$ for the distance of the donut from the viewer.

$(x', y') = ( {K_1 x\over K_2 + z}, {K_1 y\over K_2 + z})$

# Shade
We have figured out where to draw each points for the donut, but we still need to know how bright each point is. We need to know the surface normal, the direction perpendicular to the surface at each point.

With the surface normal value we can take the dot product of it with direction of the light. If dot product > 0, the surface is facing the light, else it is not and should be black. Higher the dot product value, higher the brightness of the point.

Since is the just a donut, and the cross section being a circle. The surface normal is just the same point on a unit circle centered at the origin $(\cos \theta, \sin \theta, 0)$. Applying the _XYZ_ same rotation to it:
$$
(N_x, N_y, N_z) =
(\cos \theta, \sin \theta, 0)  
\cdot 
\begin{pmatrix} \cos\phi & 0 & \sin\phi \\ 0 & 1 & 0 \\ -\sin\phi & 0 & \cos\phi \end{pmatrix}
\cdot 
\begin{pmatrix} 1 & 0 & 0 \\ 0 & \cos A & \sin A \\ 0 & -\sin A & \cos A \end{pmatrix}
\cdot 
\begin{pmatrix} \cos B & \sin B & 0 \\ -\sin B & \cos B & 0 \\ 0 & 0 & 1 \end{pmatrix}
$$

Dot product of that with a light direction vector get brightness level of any point on the donut.
$$
L = (N_x, N_y, N_z) \cdot (0, 1, -1)
$$

And with that we have all the pieces to render the donut.

# Source code
```c
             k;double sin()
         ,cos();main(){float A=
       0,B=0,i,j,z[1760];char b[
     1760];printf("\x1b[2J");for(;;
  ){memset(b,32,1760);memset(z,0,7040)
  ;for(j=0;6.28>j;j+=0.07)for(i=0;6.28
 >i;i+=0.02){float c=sin(i),d=cos(j),e=
 sin(A),f=sin(j),g=cos(A),h=d+2,D=1/(c*
 h*e+f*g+5),l=cos      (i),m=cos(B),n=s\
in(B),t=c*h*g-f*        e;int x=40+30*D*
(l*h*m-t*n),y=            12+15*D*(l*h*n
+t*m),o=x+80*y,          N=8*((f*e-c*d*g
 )*m-c*d*e-f*g-l        *d*n);if(22>y&&
 y>0&&x>0&&80>x&&D>z[o]){z[o]=D;;;b[o]=
 ".,-~:;=!*#$@"[N>0?N:0];}}/*#****!!-*/
  printf("\x1b[H");for(k=0;1761>k;k++)
   putchar(k%80?b[k]:10);A+=0.04;B+=
     0.02;}}/*****####*******!!=;:~
       ~::==!!!**********!!!==::-
         .,~~;;;========;;;:~-.
             ..,--------,*/
```

---
# References
https://www.a1k0n.net/2011/07/20/donut-math.html