# onedimheateq

## Introduction

This repository contains Python code to simulate the one-dimensional heat equation in its finite difference form with Dirichlet Boundary Conditions for temperature on both ends.

## One-Dimensional Heat Equation

The one-dimensional heat equation is given by

$$\frac{\partial u}{\partial t} = c^2 \frac{\partial^2 u}{\partial x^2}$$

It is discretized as:

$$\frac{\partial u}{\partial t} = \frac{u_{i, j + 1} - u_{i, j}}{\Delta t}$$

and

$$\frac{\partial^2 u}{\partial x^2} = \frac{u_{i - 1, j} - 2u_{i, j} + u_{i + 1, j}}{(\Delta x)^2}$$

where $i$ is along $x$ and $j$ is along time. Therefore,

$$u_{i, j + 1} = \frac{c^2 \Delta t}{(\Delta x)^2} [u_{i - 1, j} - 2u_{i, j} + u_{i + 1, j}] $$

## References

- Chapter 33, Grewal B. S., "Higher Engineering Mathematics", 42nd ed. Jun 2012, ISBN: 978-81-7409-195-5
