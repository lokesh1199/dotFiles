" Remove vi comptability
set nocompatible

if has('syntax')
	filetype on
	syntax on
endif

set number
set relativenumber

" Tab related things
set autoindent
set expandtab
set smarttab
set shiftwidth=4
set tabstop=4

" Filetype
filetype plugin on
filetype indent on

set hidden
set smartcase
set incsearch

" Disable swap and backup files
set nobackup
set noswapfile

" Jump up or down by 10 lines.
noremap <silent> J 10j
noremap <silent> K 10k

" Prohibit certain unsecure VimScript.
set secure
