# nvim-nimble

* execute nimble command on neovim

## Installation for dein.vim

```
[[plugins]]
repo = 'honeytrap15/nvim-nimble'
```

## Usage

* Execute command on neovim
  * All arguments are gave to ":Nimble" command

```
:Nimble [task name]
```

## Example

```
:Nimble build
```

```
:Nimble test
```

```
:Nimble test --verbose
```
