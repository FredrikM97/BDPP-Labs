# Lecture 1 - 2020-03-23
* How to process big amount of data.
* Moore's Law . Speed of evolution of components (transistors) or processing power (cpu)

* Existing frameworks?

## Tree topics in the BDPP course
* Apache spark
* Kubernetes
* Nvidia cuda

## Individual project
* Design algorithm, come up with an Idea

## Two kinds of parallelism
* Data parallelism (Same task on different data)
* Task parallelism (Different tawsk on same data)
* Hybrid & pipeline (Lie somewhere is in reality)


## Frameworks
* General-purpose framework (static and streamed massive data) - Spark
* Specialised frameworks (Homogenous clusters) - CUDA

## How to program a pipeline
* MapReduce pattern
    * Functional programming
* Expressive paradigm   
    * Many problams can be phrased this way
    * Results in clean code
    * Easy to implement
* Simple programming model
    * Built-in retry/failure semantics
    * Efficient and portable
    * Easy to distribute across nodes

* Specialised compute-intensivce highly parallel repetitive processing
* Heterogeneous computing
* Matrices/tensors

## Spark
* Process big data in flexible way, arbitrary code
* Built upon ideas from functional programming
* Forbid global state and automate worker management

## CUDA
* Make very repetitive computations on data run very fast
* Only allow simple math operations on tensors/matrices
* Dedicated hardware

## Map-Reduce
* Framework with two steps map and reduce

# Lecture 3  - 2020-03-31

* RDD programming model is complicated and difficult but adaptive?

## Spark sql overview
* Dataset/Dataframe -> Query plan - > Optimized query plan -> RDD
* Dataset -> (Abstraction of user programms) -> RDD
* Transformation between query plan and optimized query plan

## Dataset
* Dataset is represented by user defined object
* Stronly typed, immutable collection of data

## MLLib workfflow
* Featyre transformation
* ML pipeline construction
* Model evaluation / Hyperparameter tuning
* ML persistence (save & load models and pipelines)

## Programming paradigms
* Imperative (Programmer instructs machine how to change state) -> Procedural, object oriented
* Declarative (Programmer declares properties of desired result, not how to do it) -> Functional, Logic, mathematical

# Lecture 4 - 2020-04-02
* Recursive function
* High level function (map, filter, reduce)

## Stream processing

* Discretized streaming processing