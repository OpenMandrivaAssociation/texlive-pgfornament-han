%global tl_name pgfornament-han
%global tl_revision 72640

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	pgfornament library for Chinese traditional motifs and patterns
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/pgfornament-han
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfornament-han.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfornament-han.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a pgfornament library for Chinese traditional
motifs and patterns. The command \pgfornamenthan takes the same options
as \pgfornament from the pgfornament package, but renders Chinese
traditional motifs instead. The list of supported motifs, as well as
some examples, can be found in the accompanying documentation. This
bundle also provides three beamer themes incorporating these motifs;
sample .tex files for creating beamer presentations and posters are
included. Yi pgfornament Hong Bao De Ji Zhi ,Shi Xian Hui Zhi Yi Feng Tu
Wen . \pgfornamenthan He \pgfornament De Can Shu Shi Yi Yang De ; Bian
Yi De Chu Lai De Dang Ran Shi Yi Feng Wen Yang Liao . Hong Bao Shou Ce
Li You Wan Zheng De Wen Yang Lie Biao Yi Ji Shi Yong Fan Li . Wo Men Ye
Ji Yu Zhe Xie Wen Yang ,Kai Fa Liao San Kuan beamerZhu Ti , Bing Fu
Shang Zhi Zuo beamerHuan Deng Pian He Hai Bao De Shi Fan .texWen Dang .

