# Go

## Overview

In this part, you'll learn **Go**, the language most of the cloud-native and observability tooling you've met so far is written in. Since you already know how to program, the focus is on what Go does differently, not on programming basics.

## Goals

**Why Go**

- Where Go is used in the tools you've already worked with
- What Go deliberately leaves out of the language, and why

**Language Fundamentals**

- Packages, modules, and exported vs. unexported names
- Pointers: the `&` and `*` operators
- Structs, methods, and value vs. pointer receivers
- Interfaces and implicit implementation
- Slices and maps
- Errors as values, `defer`, `panic` and `recover`
- Generics

**Concurrency**

- Goroutines
- Channels and `select`
- The `sync` package
- `context` for cancellation and deadlines

**Tooling**

- The `go` command: `build`, `run`, `test`, `vet`, `mod`
- `gofmt`
- Testing and benchmarking
- Static binaries and cross-compilation

## Outcome

Write your answers in a markdown file, with short code snippets where they help. Run every snippet yourself; don't paste code you haven't executed.

1. Name 4 tools you've already worked with in this onboarding that are written in Go. What properties of the language made it a popular choice for this kind of infrastructure software?
2. Go's designers left out several features common in other languages. Pick 3 of them, and for each one explain what Go offers instead.
3. What is the difference between a package and a module in Go? What are `go.mod` and `go.sum` each for?
4. How does Go decide whether a name is visible outside its package?
5. Go has no classes. How do you attach behavior to a type?
6. What do the `&` and `*` operators do in Go? Using a struct of your own, explain the difference between `p := Point{X: 1}` and `p := &Point{X: 1}`, and what `*p` means in each place it can appear (a type, an expression, the left side of an assignment).
    - When you pass a struct to a function and the function changes a field, does the caller see the change? What if you pass a pointer to it instead? Write a snippet that shows both.
    - Why can you write `p.X` on a pointer without dereferencing it first? What does Go do for you there?
    - What is the zero value of a pointer, and what happens when you access a field through it?
    - Can you take the address of a local variable and return it from a function? Where does that variable live after the function returns?
7. What is the difference between a value receiver and a pointer receiver? Write an example where choosing the wrong one causes a bug that still compiles.
8. What is an interface in Go, and how does a type come to implement one? How does that differ from the languages you already know, and what does it make easier?
9. What is the empty interface (`any`), and when is using it a code smell?
10. What is the difference between an array and a slice? What happens to a slice's underlying array when you `append` past its capacity, and how can two slices end up unexpectedly sharing data?
11. What happens when you read a key that doesn't exist in a map? How do you tell a missing key apart from a key that holds the zero value?
12. How does Go handle errors, and why did its designers choose this over exceptions? How do you add context to an error while keeping the original, and how do you check for a specific error further up the call stack?
13. What does `defer` do? In what order do multiple deferred calls run, and when are their arguments evaluated?
14. When is it appropriate to `panic` instead of returning an error? What does `recover` do?
15. What are generics in Go, and what problem did they solve when they were added? Give an example of a function that is better written generically.
16. What is a goroutine, and how is it different from an operating-system thread?
17. What is a channel? What is the difference between a buffered and an unbuffered channel, and what happens when you send on a channel nobody reads from?
18. What does `select` do? Write a snippet that waits for a result from a channel but gives up after one second.
19. When would you use a `sync.Mutex` instead of a channel? What are `sync.RWMutex` and `sync.WaitGroup` for?
20. What is a data race? How do you detect one with the Go toolchain? Write a small program that has one, catch it, and fix it.
21. What is `context.Context` used for? Why is it passed as the first argument of so many functions in Go libraries?
22. What is a goroutine leak? Show a simple example and how you'd fix it.
23. How do you write and run a unit test in Go? What is a table-driven test, and why is it the common style?
24. How do you write a benchmark, and how do you read its output?
25. What do `gofmt` and `go vet` each do? Why does the Go community treat `gofmt` output as non-negotiable?
26. Go builds a single static binary. How does that affect the Docker images you build for Go apps, compared to the Python image from the Dockerfile Exercise? Write a multi-stage Dockerfile for a hello-world HTTP server and compare the final image size to the Python one.

### Links

- [A Tour of Go](https://go.dev/tour/) - start here; it covers most of the language in a few hours
- [Effective Go](https://go.dev/doc/effective_go)
- [Go by Example](https://gobyexample.com/)
- [Go FAQ](https://go.dev/doc/faq) - the designers' reasoning behind many of the language's choices
- [A Tour of Go: Pointers](https://go.dev/tour/moretypes/1) - and the struct pages right after it
- [Go FAQ: Pointers and Allocation](https://go.dev/doc/faq#Pointers)
- [Tutorial: Create a Go module](https://go.dev/doc/tutorial/create-module)
- [Go Modules Reference](https://go.dev/ref/mod)
- [Error handling and Go](https://go.dev/blog/error-handling-and-go)
- [Working with Errors in Go 1.13](https://go.dev/blog/go1.13-errors)
- [Tutorial: Getting started with generics](https://go.dev/doc/tutorial/generics)
- [Go Concurrency Patterns: Pipelines and cancellation](https://go.dev/blog/pipelines)
- [Go Concurrency Patterns: Context](https://go.dev/blog/context)
- [Data Race Detector](https://go.dev/doc/articles/race_detector)
- [Add a test](https://go.dev/doc/tutorial/add-a-test)
- [Package testing](https://pkg.go.dev/testing)
- [Go Code Review Comments](https://go.dev/wiki/CodeReviewComments)
