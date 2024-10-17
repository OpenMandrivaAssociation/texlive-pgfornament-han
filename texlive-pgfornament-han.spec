Name:		texlive-pgfornament-han
Version:	68704
Release:	1
Summary:	pgfornament library for Chinese traditional motifs and patterns
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pgfornament-han
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfornament-han.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfornament-han.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a pgfornament library for Chinese
traditional motifs and patterns. The command \pgfornamenthan
takes the same options as \pgfornament from the pgfornament
package, but renders Chinese traditional motifs instead. The
list of supported motifs, as well as some examples, can be
found in the accompanying documentation. Yi pgfornament Hong
Bao De Ji Zhi ,Shi Xian Hui Zhi Yi Feng Tu Wen .
\pgfornamenthan He \pgfornament De Can Shu Shi Yi Yang De ;Bian
Yi De Chu Lai De Dang Ran Shi Yi Feng Wen Yang Liao . Hong Bao
Shou Ce Li You Wan Zheng De Wen Yang Lie Biao Yi Ji Shi Yong
Fan Li .

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/pgfornament-han
%doc %{_texmfdistdir}/doc/latex/pgfornament-han

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
