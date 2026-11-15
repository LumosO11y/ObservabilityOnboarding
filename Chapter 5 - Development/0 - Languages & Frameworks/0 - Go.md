# Go

## Overview

Go is the language most of the cloud-native and observability tooling you've met so far is written in. You won't write much of it on our team, but you'll read it: in the source of the Collector, OBI, and other cloud-native tools we run, in their docs, and in pseudo-code. The goal of this part is to read Go comfortably, not to become a Go developer.

## Goals

**Why Go**

- Where Go is used in the tools you've already worked with

**Reading Go**

- Packages and exported vs. unexported names
- Pointers: the `&` and `*` operators
- Structs, methods, and value vs. pointer receivers
- Interfaces and implicit implementation
- Slices and maps
- Errors as values and `defer`

**Concurrency**

- Goroutines, channels, and `select`
- The `sync` package
- `context` for cancellation and deadlines

**Tests**

- Recognizing and reading Go tests

## Outcome

Write your answers in a markdown file. Short snippets help, and the [Go Playground](https://go.dev/play/) is the quickest way to check that you read a piece of syntax correctly.

1. Name 4 tools you've already worked with in this onboarding that are written in Go. What properties of the language made it a popular choice for this kind of infrastructure software?
2. What are a package and a module in Go? How does Go decide whether a name is visible outside its package?
3. Go has no classes. How do you attach behavior to a type? What is the difference between a value receiver and a pointer receiver?
4. What do the `&` and `*` operators do in Go? Using a struct of your own, explain the difference between `p := Point{X: 1}` and `p := &Point{X: 1}`, and what `*p` means in each place it can appear (a type, an expression, the left side of an assignment).
    - When you pass a struct to a function and the function changes a field, does the caller see the change? What if you pass a pointer to it instead?
    - Why can you write `p.X` on a pointer without dereferencing it first?
5. What is an interface in Go, and how does a type come to implement one? How does that differ from the languages you already know?
6. What is the difference between an array and a slice? When you read from a map with `v, ok := m[key]`, what do the two values mean?
7. How does Go handle errors instead of throwing exceptions? What is the `if err != nil` pattern you'll see everywhere, and how do you add context to an error while keeping the original?
8. What does `defer` do, and in what order do multiple deferred calls run?
9. What does the `go` keyword do? What is a goroutine, and how is it different from an operating-system thread?
10. What is a channel, and what do `ch <- v` and `v := <-ch` do? What is the difference between a buffered and an unbuffered channel?
11. What does `select` do? What would a `select` with a `case <-time.After(time.Second):` branch be for?
12. What are `sync.Mutex` and `sync.WaitGroup` for?
13. What is `context.Context` used for? Why is it passed as the first argument of so many functions in Go libraries?
14. How do you recognize a test in Go? What is a table-driven test, and why is it the common style?
15. Pick a short function from the source of the Collector or OBI (for example, the part of a processor that handles a batch of traces), and explain what it does line by line. Ask your mentor if you need help finding one.

### Links

- [A Tour of Go](https://go.dev/tour/) - start here; it covers most of the language in a few hours
- [Effective Go](https://go.dev/doc/effective_go)
- [Go by Example](https://gobyexample.com/)
- [Go FAQ](https://go.dev/doc/faq) - the designers' reasoning behind many of the language's choices
- [A Tour of Go: Pointers](https://go.dev/tour/moretypes/1) - and the struct pages right after it
- [Go FAQ: Pointers and Allocation](https://go.dev/doc/faq#Pointers)
- [Tutorial: Create a Go module](https://go.dev/doc/tutorial/create-module)
- [Error handling and Go](https://go.dev/blog/error-handling-and-go)
- [Working with Errors in Go 1.13](https://go.dev/blog/go1.13-errors)
- [Go Concurrency Patterns: Context](https://go.dev/blog/context)
- [Package testing](https://pkg.go.dev/testing)
