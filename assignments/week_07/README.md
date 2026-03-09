# Week 7: Numerical Linear Algebra

**Due:** March 13, 2026

This week, you will practice using the linear algebra tools built into `numpy` to perform compute inertia tensors and perform coordinate transformations. You will learn how to use matrix operations to rotate and translate coordinates, as well as how to compute the inertia tensor of a system of particles. By the end of this week, you should be able to apply these techniques to analyze the structure and dynamics of systems in three-dimensional space.

## Context

Spiral galaxies are roughly disk-shaped systems of stars, gas, and dark matter that rotate around a common center. 
If we imagine our galaxy as a plate, a 'face-on' view would show us the full disk, while an 'edge-on' view would show us the thin profile of the disk.
But the orientation of a galaxy in space is generally random, so when we observe galaxies, they can be tilted at any angle. However, for analysis purposes we typically want to align the galaxy so that we are looking at it face-on, which allows us to study its structure and dynamics more easily. To do this, we can use coordinate transformations to rotate the galaxy's coordinates so that the plane of the disk is aligned with our line of sight. This involves computing the inertia tensor of the galaxy to determine its principal axes and then applying a rotation to align those axes with our desired orientation.

In this exercise, we will compute the inertia tensor of a mock barred spiral galaxy, determine its principal axes, and then perform a coordinate transformation to align the galaxy face-on. This will demonstrate how linear algebra can be used to analyze and manipulate the structure of complex systems in three-dimensional space.

There are a multitude of other applications of numerical linear algebra in physics and engineering, including solving systems of linear equations, performing eigenvalue decompositions, and computing singular value decompositions. These techniques are fundamental tools for analyzing and understanding complex systems in a wide range of fields. As part of this week's exercise, I am also asking you to find an example of a linear algebra problem you have seen before (either in this course or in another context) and solve it again using `numpy`'s linear algebra tools. This should help you get more practice with these techniques and see how they can be applied in different contexts.



## Resources

- [NumPy Linear Algebra documentation](https://numpy.org/doc/stable/reference/routines.linalg.html)
- [Linear Algebra with Python Github repository](https://github.com/weijie-chen/Linear-Algebra-With-Python)
- [Eigenvectors and Eigenvalues — 3Blue1Brown (video)](https://www.youtube.com/watch?v=PFDu9oVAE-g)
- [Galaxies and the Universe — University of Alabama astronomy course notes](http://www.astr.ua.edu/keel/galaxies/)
- [IllustrisTNG: About the Simulations](https://www.tng-project.org/about/)