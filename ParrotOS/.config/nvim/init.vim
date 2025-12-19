set number
set expandtab
set autoindent
set softtabstop=4
set shiftwidth=2
set tabstop=4
set termguicolors
"Enable mouse click for nvim
set mouse=a
"Fix cursor replacement after closing nvim
set guicursor=
"Shift + Tab does inverse tab
inoremap <S-Tab> <C-d>
syntax enable
"See invisible characters
"set list listchars=tab:>\ ,trail:+,eol:$
syntax on
"wrap to next line when end of line is reached
set whichwrap+=<,>,[,]
hi Normal guibg=NONE ctermbg=NONE
source $HOME/.config/nvim/lotus.vim
source $HOME/.config/nvim/lotusbar.vim


nnoremap ,<space> :CHADopen<CR>
nnoremap <space>x :wq!<CR>



let g:indentLine_color_gui = '#ea4c88'
let g:indentLine_char = '⏽ '

"hi EndOfBuffer guifg=bg guibg=bg
hi LineNr guibg=bg
set foldcolumn=2
hi foldcolumn guibg=bg
hi VertSplit guibg=#302d38 guifg=#302d38
autocmd vimenter * hi Normal guibg=NONE ctermbg=NONE " transparent bg


colorscheme nord
" colorscheme materialbox
syntax on
