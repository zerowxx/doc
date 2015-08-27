set tabstop=4
set expandtab
set softtabstop=4  
set shiftwidth=4  
set noautoindent
set nosmartindent
set nocindent
autocmd FileType python setlocal completeopt-=preview

"显示行号
set nu!
"显示光标坐标
set ruler
"搜索字符高亮
set incsearch
set helplang=cn
set encoding=utf-8

set nocompatible               " be iMproved
 filetype off                   " required!

 set rtp+=~/.vim/bundle/vundle/
 call vundle#rc()

 " let Vundle manage Vundle
 " required! 
 Bundle 'gmarik/vundle'

 " My Bundles here:
 "
 " original repos on github
 
 "git比较内容 :Gdiff
 Bundle 'tpope/vim-fugitive'
 "快速跳转
 Bundle 'Lokaltog/vim-easymotion'
 "python代码补全
 Bundle 'davidhalter/jedi-vim'
 "显示tag
 Bundle 'majutsushi/tagbar'
 "nmap <Leader>tb :TagbarToggle<CR>     "快捷键设置
 let g:tagbar_ctags_bin='ctags'         "ctags程序的路径
 let g:tagbar_width=30                  "窗口宽度的设置
 map <F8> :Tagbar<CR>
 "autocmd BufReadPost *.cpp,*.c,*.h,*.hpp,*.cc,*.cxx call tagbar#autoopen()
 "如果是c语言的程序的话，tagbar自动开启
 
 "浏览文件,资源管理器
 Bundle 'scrooloose/nerdtree'
 let NERDTreeWinPos='right'
 let NERDTreeWinSize=30
 map <F6> :NERDTree<CR>

 "多文件编辑
 Bundle 'fholgado/minibufexpl.vim'
 let g:miniBufExplMapWindowNavVim = 1   
 let g:miniBufExplMapWindowNavArrows = 1   
 let g:miniBufExplMapCTabSwitchBufs = 1   
 let g:miniBufExplModSelTarget = 1  
 let g:miniBufExplMoreThanOne=0
 map <F11> :MBEbp<CR>
 map <F12> :MBEbn<CR>



 " vim-scripts repos
 "" Bundle 'L9'
 "" Bundle 'FuzzyFinder'
 " non github repos
 ""Bundle 'git://git.wincent.com/command-t.git'
 " git repos on your local machine (ie. when working on your own plugin)
 ""Bundle 'file:///Users/gmarik/path/to/plugin'
 " ...

 filetype plugin indent on     " required!
 "
 " Brief help
 " :BundleList          - list configured bundles
 " :BundleInstall(!)    - install(update) bundles
 " :BundleSearch(!) foo - search(or refresh cache first) for foo
 " :BundleClean(!)      - confirm(or auto-approve) removal of unused bundles
 "
 " see :h vundle for more details or wiki for FAQ
 " NOTE: comments after Bundle command are not allowed..
