# revision 32181
# category Package
# catalog-ctan /macros/latex/contrib/reflectgraphics
# catalog-date 2013-11-18 17:49:17 +0100
# catalog-license lppl1.3
# catalog-version 0.2
Name:		texlive-reflectgraphics
Version:	0.2
Release:	5
Summary:	Techniques for reflecting graphics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/reflectgraphics
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/reflectgraphics.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/reflectgraphics.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/reflectgraphics.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a macro for reflecting images, in a number
of different ways, in pursuit of "more striking" graphics in a
document.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/reflectgraphics/reflectgraphics.sty
%doc %{_texmfdistdir}/doc/latex/reflectgraphics/README
%doc %{_texmfdistdir}/doc/latex/reflectgraphics/reflectgraphics.pdf
#- source
%doc %{_texmfdistdir}/source/latex/reflectgraphics/reflectgraphics.dtx
%doc %{_texmfdistdir}/source/latex/reflectgraphics/reflectgraphics.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
